import pandas as pd, numpy as np, re, logging
from functools import reduce
from operator import concat

class rules():
    ## Array in an Array not handled
    def __init__(self, data=None, columns=None, scripterCall=False):
        self.data = data

        if scripterCall:
            pass
        else:
            self.columns = list(columns)
            self.column_sequence = ['Source','Logic','Canonical']
            # Check if the columns in the incoming file matches the preferred column sequence
            for item in self.column_sequence:
                if item in self.columns:
                    pass
                else:
                    logging.error("The 'Header' in the file is not having one or more of the mandatory columns : ['Source','Logic','Canonical']")
                    exit()
            
            if ((list(self.data['Source'])[-1].lower().startswith('<<')) or (list(self.data['Canonical'])[-1].lower().startswith('<<'))):
                logging.error("The last line on the file should not belong to any collection. Please put a normal root-level mapping.")
                exit()

            self.dataSanity()
            self.tcheck()
            self.checkl()
            self.matchCollection()

    def dataSanity(self):
        # STATIC REGEX TEMPLATE - Valid data should only start with <<, ++, letters & other combinations
        first_word_re = r"[a-zA-Z][\w']*"
        c1 = r"^<<object:(\w+)$"     # eg - <<objectInsideArray
        c2 = r"^<<(\w+)"            # eg - <<normalFieldInsideCollection
        c3 = r"^<<<<(\w+)"          # eg - <<<<fieldInsideObjectn1
        c4 = r"^(\w+)"              # eg - field
        c5 = r"^object:(\w+)"       # eg - object:{name}
        c6 = r"^array:(\w+)"        # eg - array:{name}

        ## Data Sanity check on 'Source' column
        check_source = []
        for loc in range(0,len(self.data['Source'])):
            root = self.data['Source'][loc]
            if(not(pd.isna(root))):
                if re.search(c1,root.strip().lower()):
                    check_source.append(root)
                elif re.search(c2,root.strip().lower()):
                    check_source.append(root)
                elif re.search(c3,root.strip().lower()):
                    check_source.append(root)
                elif (root.strip().lower()[0:2] == "++"):
                    check_source.append(root)                   
                elif re.search(c5,root.strip().lower()):
                    check_source.append(root)
                elif re.search(c6,root.strip().lower()):
                    check_source.append(root)
                elif re.search(c4,root.strip().lower()):
                    if (':' in root):
                        pass
                    else:
                        check_source.append(root) 
                else:
                    pass
            else:
                check_source.append('')

        ## Data Sanity check on 'Canonical' column
        check_canoni = []
        for loc in range(0,len(self.data['Canonical'])):
            root = self.data['Canonical'][loc]
            if(not(pd.isna(root))):
                if re.search(c1,root.strip().lower()):
                    check_canoni.append(root)
                elif re.search(c2,root.strip().lower()):
                    check_canoni.append(root)
                elif re.search(c3,root.strip().lower()):
                    check_canoni.append(root)
                elif (root.strip().lower()[0:2] == "++"):
                    logging.error("Any element on the 'Canonical' column should not start with '++'.")
                    exit()
                elif re.search(c5,root.strip().lower()):
                    check_canoni.append(root)
                elif re.search(c6,root.strip().lower()):
                    check_canoni.append(root)
                elif re.search(c4,root.strip().lower()):
                    if (':' in root):
                        pass
                    else:
                        check_canoni.append(root)
                else:
                    pass
            else:
                check_canoni.append('')
        
        z1 = []
        for l in range(0,len(self.data['Source'])):
            root = self.data['Source'][l]
            if(not(pd.isna(root))):
                z1.append(root)
            else:
                root2 = self.data['Canonical'][l]
                if(not(pd.isna(root2))):
                    word_1 = ((re.search(first_word_re,root2.lower())).group(0))
                    if word_1 == "object":
                        z1.append('dummy')
                    elif word_1 == "array":
                        logging.error("On 'Canonical' for row : " + str(l) + ", there is 'Array' but null on 'Source'. Cannot map.")
                        exit()
                    
        z2 = [x for x in list(self.data['Canonical']) if pd.isna(x) == False]
        
        if len(z1) != len(z2):
            logging.error("The number of elements on both the columns 'Source' & 'Canonical' should match")
            exit()
        if len(z1) != len(check_source):
            logging.error("The valid syntax for 'Source' are : <<object:nameInsideArray, normalField, <<normalFieldInsideCollection, <<<<fieldInsideObjectInsideArray, ++fieldFromRootUnderCollection, object:{name}, array:{name}")
            exit()
        if len(z2) != len(check_canoni):
            logging.error("The valid syntax for 'Canonical' are : <<object:nameInsideArray, normalField, <<normalFieldInsideCollection, <<<<fieldInsideObjectInsideArray, object:{name}, array:{name}")
            exit()

    def checkl(self):
        # STATIC REGEX CHECK
        first_word_re = r"[a-zA-Z][\w']*"

        ## CAPTURE THE COLLETION SIGNATURES
        ## Capture collections on 'Source' column
        collec_name_source = {}
        collec_vals_source = {}

        for loc in range(1,len(self.data['Source'])):
            if (not (pd.isna(self.data['Source'][loc]))):
                root = (self.data['Source'][loc]).lower()
                if ((root.startswith('array') or root.startswith('object'))):
                    word_1 = ((re.search(first_word_re,(self.data['Source'][loc]).lower())).group(0))
                    if (((word_1 == "array") or (word_1 == "object"))):
                        collec_name_source[loc] = (self.data['Source'][loc])
                # Capture orphan collections on 'Source' column
                elif (not (pd.isna(self.data['Source'][loc-1]))):
                    if (root.startswith('<<') or root.startswith('++') or root.startswith('<<object')):
                        root = (self.data['Source'][loc]).lower()
                        prev_root = (self.data['Source'][loc-1]).lower()
                        frst_char = prev_root[0:2]
                        word_1 = ((re.search(first_word_re,prev_root)).group(0))
                        if ((frst_char not in ['<<','++']) and (word_1 not in ['array','object'])): 
                            collec_name_source[loc-1] = ''
            else:
                if (len(self.data['Source']) > loc+1):
                    root = (self.data['Source'][loc+1]).lower()
                    if ((root.startswith('<<') or root.startswith('++'))):
                        collec_name_source[loc] = ''

        for i in list(collec_name_source.keys()):
            collec_temp  = []
            for x in range(i+1,len(self.data['Source'])):
                if (not(pd.isna((self.data['Source'][x])))):
                    root = (self.data['Source'][x]).lower()
                    if (root.startswith('<<') or root.startswith('++') or root.startswith('<<object')):
                        collec_temp.append((self.data['Source'][x])) 
                    else:
                        collec_vals_source[i] = collec_temp
                        break
                else:
                    collec_vals_source[i] = collec_temp
                    break
            collec_vals_source[i] = collec_temp

        ## Capture collections on 'Canonical' column
        collec_name_canoni = {}
        collec_vals_canoni = {}

        for loc in range(1,len(self.data['Canonical'])):
            if (not (pd.isna(self.data['Canonical'][loc]))):
                root = (self.data['Canonical'][loc]).lower()
                if ((root.startswith('array') or root.startswith('object'))):
                    word_1 = ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))
                    if (((word_1 == "array") or (word_1 == "object"))):
                        collec_name_canoni[loc] = (self.data['Canonical'][loc])
                # Capture orphan collections on 'Canonical' column
                elif (not (pd.isna(self.data['Canonical'][loc-1]))):
                    if (root.startswith('<<') or root.startswith('++') or root.startswith('<<object')):
                        root = (self.data['Canonical'][loc]).lower()
                        prev_root = (self.data['Canonical'][loc-1]).lower()
                        frst_char = prev_root[0:2]
                        word_1 = ((re.search(first_word_re,prev_root)).group(0))
                        if ((frst_char not in ['<<','++']) and (word_1 not in ['array','object'])): 
                            collec_name_canoni[loc-1] = ''
            else:
                if (len(self.data['Canonical']) > loc+1):
                    root = (self.data['Canonical'][loc+1]).lower()
                    if ((root.startswith('<<') or (root.startswith('++')))):
                        collec_name_canoni[loc] = ''

        for i in list(collec_name_canoni.keys()):
            collec_temp  = []
            for x in range(i+1,len(self.data['Canonical'])):
                if (not(pd.isna((self.data['Canonical'][x])))):
                    root = (self.data['Canonical'][x]).lower()
                    if (root.startswith('<<') or root.startswith('++') or root.startswith('<<object')):
                        collec_temp.append((self.data['Canonical'][x])) 
                    else:
                        collec_vals_canoni[i] = collec_temp
                        break
                else:
                    collec_vals_canoni[i] = collec_temp
                    break
            collec_vals_canoni[i] = collec_temp

        ## Store the field names on the 'Source' column
        valid_source_fields = []
        
        for name in (self.data['Source'].values):
            if (not (pd.isna(name))):
                word_1 = ((re.search(first_word_re,name.lower())).group(0))
                if (name.lower().startswith('array') or name.lower().startswith('object')):
                    # Check if the word is exactly matching to 'array'/'object' in this 'if'
                    # If not, then throw an error
                    if ((word_1 == "array") or (word_1 == "object")):
                        pass
                    else:
                        x = self.data[self.data['Source'] == name].index.tolist()
                        logging.error("Please check the row on 'Source' column : " + str(x))
                        exit()
                else:
                    valid_source_fields.append(word_1)

        # REGEX TEMPLATES FOR COLLECTION SANITY CHECK
        c1 = r"^<<(\w+)"            # eg - <<normalFieldInsideCollection
        c2 = r"^<<object:(\w+)$"    # eg - <<objectInsideArray
        c3 = r"^<<<<(\w+)"          # eg - <<<<fieldInsideObjectn1

        ## Array/Object check for 'Source'
        if (not (pd.isna(self.data['Source'][0]))):
            root = (self.data['Source'][0]).lower()
            if (root.startswith('array') or root.startswith('object')):
                logging.error("The 'Source' column should not start with 'Array'/'Object'.")
                exit()
            elif (root[0:2] in ['<<','++']):
                logging.error("The 'Source' column should not start with '++'/'<<'.")
                exit()
        else:
            logging.error("The 'Source' column should not start with null.")
            exit()

        loop_count = 0
        temp_obj = []
        temp_obj_child = []

        for ls in (list(collec_vals_source.values())):
            loop_count+=1
            key = list(collec_vals_source.keys())[loop_count-1]
            if (len(ls) > 0):
                find_true = list(pd.Series(ls).apply(lambda x: (x.lower().startswith('++'))).values)
                a = (np.array(np.where(np.array(find_true)==True))[0]).tolist()
                b = list(range(0,len(a)))
                if (a != b):
                    logging.error("The '++' should come first always if present in a collection. Check row : " + str(key) + " in 'Source' column.")
                    exit()
                if re.search(c2,(ls[-1]).strip().lower()):
                    logging.error("The collection on row : " + str(key) + " on 'Source' column has no child.")
                    exit()
                else:
                    for val in ls:
                        if (len(temp_obj) == 0): 
                            if re.search(c2,val.strip().lower()):
                                temp_obj_child = []
                                temp_obj.append(val)
                                pass
                            elif re.search(c1,val.strip().lower()):
                                temp_obj_child = []
                                pass
                            elif re.search(c3,val.strip().lower()):
                                if (len(temp_obj_child) == 0):
                                    logging.error("The collection on row : " + str(key) + " on 'Source' has an element starting with '<<<<' without having a parent 'Object'.")
                                    exit()
                                else:
                                    pass
                        else:
                            if re.search(c1,val.strip().lower()):
                                logging.error("The collection on row : " + str(key) + " on 'Source' has no child elements to an internal 'Object'.")
                                exit()
                            elif re.search(c2,val.strip().lower()):
                                logging.error("The collection on row : " + str(key) + " on 'Source' has 2 internal 'Object's one after other.")
                                exit()
                            if re.search(c3,val.strip().lower()):
                                temp_obj_child.append(val)
                                temp_obj.pop()
                                pass
            else:
                logging.error("The collection on row : " + str(key) + " on 'Source' is empty which is not good. Please check.")
                exit()

        loop_count = 0
        for ls in (list(collec_name_source.values())):
            loop_count+=1
            key = list(collec_name_source.keys())[loop_count-1]
            if (ls != ""):
                find_grp = ls.lower().split(":")
                if find_grp[0] in ['array','object']:
                    pass
                elif (find_grp[0] == ""):
                    logging.error("Cannot find valid collection type. Check row : " + str(key) + " on 'Source' column.")
                    exit()
                else:
                    logging.error("Valid collections are : Array/Object. Check row : " + str(key) + " on 'Canonical' column. Please check.")
                    exit()
                if (find_grp[1] == ""):
                    logging.error("Cannot find valid collection name. Check row : " + str(key) + " on 'Source' column.")
                    exit()
                elif (find_grp[1] != ""):
                    pass
                else:
                    logging.error("Something is wrong. Check row : " + str(key) + " on 'Canonical' column.")
                    exit()                 
            else:
                logging.error("The collection on row : " + str(key) + " on 'Source' is not having any collection type. Please check.")
                exit()

        ## Array/Object check for 'Canonical'
        if (not (pd.isna(self.data['Canonical'][0]))):
            root = (self.data['Canonical'][0]).lower()
            if (root.startswith('array') or root.startswith('object')):
                logging.error("The 'Canonical' column should not start with 'Array'/'Object'.")
                exit()
            elif (root[0:2] in ['<<']):
                logging.error("The 'Canonical' column should not start with '<<'.")
                exit()
            elif (root[0:2] in ['++']):
                logging.error("The 'Canonical' column should not have any member starting with '++'.")
                exit()
        else:
            logging.error("The 'Canonical' column should not start with null.")
            exit()

        loop_count = 0
        temp_obj = []
        temp_obj_child = []
        for ls in (list(collec_vals_canoni.values())):
            loop_count+=1
            key = list(collec_vals_canoni.keys())[loop_count-1]
            if (len(ls) > 0):
                find_true = list(pd.Series(ls).apply(lambda x: (x.lower().startswith('++'))).values)
                if (True in find_true):
                    logging.error("There should not be any row starting with '++' in 'Canonical'. Check row : " + str(key))
                    exit()
                if re.search(c2,(ls[-1]).strip().lower()):
                    logging.error("The collection on row : " + str(key) + " in 'Canonical' column has no child.")
                    exit()
                else:
                    for val in ls:
                        if (len(temp_obj) == 0): 
                            if re.search(c2,val.strip().lower()):
                                temp_obj_child = []
                                temp_obj.append(val)
                                pass
                            elif re.search(c1,val.strip().lower()):
                                temp_obj_child = []
                                pass
                            elif re.search(c3,val.strip().lower()):
                                if (len(temp_obj_child) == 0):
                                    logging.error("The collection on row : " + str(key) + " on 'Canonical' has an element starting with '<<<<' without having a parent 'Object'.")
                                    exit()
                                else:
                                    pass
                        else:
                            if re.search(c1,val.strip().lower()):
                                logging.error("The collection on row : " + str(key) + " on 'Canonical' has no child elements to an internal 'Object'.")
                                exit()
                            elif re.search(c2,val.strip().lower()):
                                logging.error("The collection on row : " + str(key) + " on 'Canonical' had 2 internal 'Object's one after other.")
                                exit()
                            if re.search(c3,val.strip().lower()):
                                temp_obj_child.append(val)
                                temp_obj.pop()
                                pass
            else:
                logging.error("The collection on row : " + str(key) + " on 'Canonical' is empty which is not good. Please check.")
                exit()

        loop_count = 0
        for ls in (list(collec_name_canoni.values())):
            loop_count+=1
            key = list(collec_name_canoni.keys())[loop_count-1]
            if (ls != ""):
                find_grp = ls.lower().split(":")
                if find_grp[0] in ['array','object']:
                    pass
                elif (find_grp[0] == ""):
                    logging.error("Cannot find valid collection type. Check row : " + str(key) + " on 'Canonical' column.")
                    exit()
                else:
                    logging.error("Valid collections are : Array/Object. Check row : " + str(key) + " on 'Canonical' column.")
                    exit()  
                if (find_grp[1] == ""):
                    logging.error("Cannot find valid collection name. Check row : " + str(key) + " on 'Canonical' column.")
                elif (find_grp[1] != ""):
                    pass
                else:
                    logging.error("Something is wrong. Check row : " + str(key) + " on 'Canonical' column. Please check.")
                    exit()                    
            else:
                logging.error("The collection on row : " + str(key) + " on 'Canonical' is not having any collection type. Please check.")
                exit()

        ## ARRAY/OBJECT CHECK
        # Check # of rows marked with 'Array'/'Object' in the Source column
        source_collec_loca = []
        for loc in range(0,len(self.data['Source'])):
            if ((not (pd.isna(self.data['Source'][loc])))):
                word_1 = ((re.search(first_word_re,(self.data['Source'][loc]).lower())).group(0))
                # Check if the row starts with "Array"/"Object"
                if ((self.data['Source'][loc]).lower().startswith('array') or (self.data['Source'][loc]).lower().startswith('object')):
                    # Check if the row's first word is 'array'/'object'. This is to ensure that the words 'array'/'object' are not misspelled
                    if ((word_1 == "array") or (word_1 == "object")):
                        # Store the row # of 'Array'/'Object' on the Source column
                        source_collec_loca.append(loc)
                    else:
                        logging.error("The valid collection names are 'Array'/'Object'.")
                        exit()
                elif ((not (pd.isna(self.data['Canonical'][loc])))):
                    if ((':' in (self.data['Canonical'][loc]).lower())):
                        word_2 = ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))
                        if (':' in (self.data['Source'][loc]).lower()):
                            if ((word_1 == "array") and (word_2 == "array")):
                                pass
                            elif ((word_1 == "array") and (word_2 == "object")):
                                logging.error("The row at " + str(loc) + " has 'Array' on 'Source' but 'Object' on 'Canonical'. This mapping is not possible.")
                                exit()
                            elif ((word_1 == "object") and (word_2 == "array")):
                                logging.error("The row at " + str(loc) + " has 'Object' on 'Source' but 'Array' on 'Canonical'. This mapping is not possible.")
                                exit()
                            elif ((word_1 == "object") and (word_2 == "object")):
                                pass
                            else:
                                logging.error("The row at " + str(loc) + " has a ':' but is not preceed with 'Array' or 'Object'. Please check.")
                                exit()
                        elif (not(':' in (self.data['Source'][loc]).lower())):
                            if (word_2 in ['array','object']):
                                logging.error("The row at " + str(loc) + " has a collection on 'Canonical' but a normal field on 'Source'. This mapping is not possible.")
                                exit()
                    else:
                        pass
            else:
                if (not(pd.isna(self.data['Canonical'][loc]))):
                    word_1 = ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))
                    if (word_1 == 'array'):
                        logging.error("The collection on 'Canonical' for row : " + str(loc) + " is 'Array'. An array can be mapped to only an array.")
                        exit()
                    elif (word_1 == 'object'):
                        pass
                else:
                    logging.info("There is a blank on the 'Source' column on row " + str(loc))

        ## Check for the captured row numbers & see if they have the collection name
        for loc in source_collec_loca:
            if (not (pd.isna(self.data['Canonical'][loc]))):
                if ':' not in self.data['Source'][loc]:
                    logging.error("There is no 'Array'/'Object' name for the row : " + str(loc) + " on the 'Source' column")
                    exit()
                elif ':' not in self.data['Canonical'][loc]:
                    logging.error("There is no 'Array'/'Object' name for the row : " + str(loc) + " on the 'Canonical' column")
                    exit()
                else:
                    pass
                # Check if the collection types are matching
                if (((re.search(first_word_re,(self.data['Source'][loc]).lower())).group(0)) != ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))):
                    logging.error("The collection types needs to be same for both the columns. Check row : " + str(loc))
                    exit()
            else:
                logging.info("There is a blank on the 'Canonical' column on row " + str(loc))

        ## Checks for the Logic column
        adjusted_logic = []
        source_field_on_logic = []

        for logic in self.data['Logic']:
            if not (pd.isna(logic)):
                if '\n' in logic:
                    adjusted_logic.append(logic.split('\n'))
                else:
                    adjusted_logic.append([logic])

        ## Checks:
        # 1. # of else statements in each logic
        # 2. The logic should always start with if/else for each line
        # 3. There should not be more than 1 'if' in a single line but there should be minimum of 1 'if' per logic
        # 4. There should not be exactly 1 'else' per logic
        count_else = 0
        count_if = 0
        count_use = 0
        
        for item in adjusted_logic:
            run_else = 0
            run_if = 0
            run_use = 0
            if ((((re.search(first_word_re,item[0].lower())).group(0)) == "use") and (len(item) > 1)):
                logging.error("There should not be more than one statements while having 'USE' in the logic cell.")
                exit()
            for logic in item:
                if(len((logic.lower().split('if'))[1:]) > 1):
                    logging.error("There should not be more than 1 'IF' statement in a single line in a logic cell. Please break into multiple lines.")
                    exit()
                elif (('if' in logic.lower()) and ('else' in logic.lower())):
                    logging.error("'IF' & 'ELSE' cannot co-exist in a single line in a logic cell. Please break into multiple lines.")
                    exit()
                elif (len((logic.lower().split('else'))[1:]) > 1):
                    logging.error("There should not be more than 1 'ELSE' statement in a single line in a logic cell.")
                    exit()
                elif (len((logic.lower().split('use'))[1:]) > 1):
                    logging.error("There should not be more than 1 'USE' statement in a single line in a logic cell.")
                    exit()
                else:
                    if not (pd.isna(logic)):
                        if (((re.search(first_word_re,logic.lower())).group(0)) == "else"):
                            if (run_else < 1):
                                run_else += 1
                                count_else += 1
                            else:
                                logging.error("There should not be more than 1 'ELSE' statement in a logic cell.")
                                exit()
                        elif (((re.search(first_word_re,logic.lower())).group(0)) == "if"):
                            if (run_if < 1):
                                run_if += 1
                                count_if += 1
                            continue
                        elif (((re.search(first_word_re,logic.lower())).group(0)) == "use"):
                            if (run_use > 1):
                                logging.error("There should not be more than one statements while having 'USE' in a logic cell.")
                                exit()
                            else:
                                if (len(logic.lower().strip().split(' ')) > 2):
                                    logging.error("The allowed template for 'USE' is -> use {value}")
                                    exit()
                                else:
                                    count_use += 1
                                    continue
                        else:
                            logging.error("A logic can only start with 'IF'/'ELSE'/'USE'.")
                            exit()

        if (len(adjusted_logic) - count_use) != (count_if):
            logging.error("There should be atleast 1 'IF' per logic statement in logic cell which is not starting with 'USE'.")
            exit()
        if (len(adjusted_logic) - count_use) != (count_else):
            logging.error("There should be atleast 1 'ELSE' per logic statement in logic cell which is starting with 'IF'.")
            exit()
       
        flat_logic_list = reduce(concat, adjusted_logic)

        ## Check for assigment operator in a logic
        for item in flat_logic_list:
            if (((re.search(first_word_re,item.lower())).group(0)) == "if"):
                if '=' in item:
                    source_field_on_logic.append(((item.split('=')[0]).split(' ')[1]).strip())
                else:
                    logging.error("A valid 'IF' statement should have an '=' operator in it.")
                    exit()

        for name in source_field_on_logic:
            if (name.lower()) not in valid_source_fields:
                logging.error("The logic should be written pertinent to fields available in the 'Source' column.")
                exit()

        ## Logic string template check
        if_template = re.compile(r'^if (\w+)=(\w+);send (\w+)')
        else_template = re.compile(r'^else (\w+)')
        use_template = re.compile(r'^use (\w+)$')

        if_accept_list = [item for item in flat_logic_list if if_template.match(item.strip().lower())]
        else_accept_list = [item for item in flat_logic_list if else_template.match(item.strip().lower())]
        use_accept_list = [item for item in flat_logic_list if use_template.match(item.strip().lower())]

        final_captured_length = len(if_accept_list) + len(else_accept_list) + len(use_accept_list)

        if len(flat_logic_list) != (final_captured_length):
            logging.error("The logic string should either match : 1. if {source field}={value};send {value} \n else {value} \n 2. use {value}")
            exit()

    def collectionSignature(self):
        ## STATIC REGEX CHECK
        first_word_re = r"[a-zA-Z][\w']*"
        c1 = r"^<<(\w+)"            # eg - <<normalFieldInsideCollection
        c2 = r"^<<object:(\w+)$"    # eg - <<objectInsideArray
        c3 = r"^<<<<(\w+)"          # eg - <<<<fieldInsideObjectn1

        ## Capture collections on 'Canonical'
        canonical_coll = {}
        detect = False
        coll_type = ""
        position = []

        for loc in range(0, len(self.data['Canonical'])):
            if (not (pd.isna(self.data['Canonical'][loc]))):
                root = (self.data['Canonical'][loc]).lower()
                if ((root.startswith('array') or root.startswith('object'))):
                    word_1 = ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))
                    if (((word_1 == "array") or (word_1 == "object"))):
                        if (len(position) > 0):
                            canonical_coll[coll_type] = position
                            position = []
                        position.append(loc)
                        detect = True
                        coll_type = word_1 + ':' + str(loc)
                elif detect:
                    a = re.search(c1,root.strip())
                    b = re.search(c2,root.strip())
                    c = re.search(c3,root.strip())
                    if b: 
                        position.append('object:' + str(loc))
                    elif a or c:
                        position.append(loc)
                    else:
                        detect = False
                        canonical_coll[coll_type] = position
                        position = []
                else:
                    detect = False
                    position = []
                    pass

        ## Capture collections on 'Source'
        source_coll = {}
        detect = False
        coll_type = ""
        position = []

        for loc in range(0, len(self.data['Source'])):
            if (not (pd.isna(self.data['Source'][loc]))):
                root = (self.data['Source'][loc]).lower()
                if ((root.startswith('array') or root.startswith('object'))):
                    word_1 = ((re.search(first_word_re,(self.data['Source'][loc]).lower())).group(0))
                    if (((word_1 == "array") or (word_1 == "object"))):
                        if (len(position) > 0):
                            source_coll[coll_type] = position
                            position = []
                        position.append(loc)
                        detect = True
                        coll_type = word_1 + ':' + str(loc)
                elif detect:
                    a = re.search(c1,root.strip())
                    b = re.search(c2,root.strip())
                    c = re.search(c3,root.strip())
                    if b:
                        position.append('object:' + str(loc))
                    elif a or c:
                        position.append(loc)
                    elif (root.strip().startswith('++')):
                        position.append(loc)
                    else:
                        detect = False
                        source_coll[coll_type] = position
                        position = []
                else:
                    detect = False
                    position = []
                    pass
            else:
                if (not (pd.isna(self.data['Canonical'][loc]))):
                    word_2 = ((re.search(first_word_re,(self.data['Canonical'][loc]).lower())).group(0))
                    if ((word_2 == "object")):
                        source_coll[('source-map:' + str(loc))] = ['na']

        return (canonical_coll,source_coll)

    def matchCollection(self):
        ## STATIC REGEX CHECK
        c1 = r"^<<(\w+)"            # eg - <<normalFieldInsideCollection
        c2 = r"^<<object:(\w+)$"    # eg - <<objectInsideArray
        c3 = r"^<<<<(\w+)"          # eg - <<<<fieldInsideObjectn1
        c4 = r"^array:(\w+)$"       # eg - array:name
        c5 = r"^object:(\w+)$"      # eg - object:name

        cap_temp = (self.collectionSignature())

        canonical = cap_temp[0]
        source = cap_temp[1]
        
        if(len(canonical.values()) == len(source.values())):
            for i,j in zip(canonical.values(),source.values()):
                if (j[0] == "na"):
                    pass
                elif (len(i) == len(j)):
                    for a,b in zip(i,j):
                        if ((":" in str(a)) or (":" in str(b))):
                            da = int(a.split(":")[1]); db = int(b.split(":")[1])
                            a = da ; b = db

                        if ((not (pd.isna(self.data['Canonical'][a]))) and (not (pd.isna(self.data['Source'][b])))):
                            a = (self.data['Canonical'][a]).lower()
                            b = (self.data['Source'][b]).lower()
                            q = (re.search(c1,a.strip())) and (re.search(c1,b.strip()))
                            w = (re.search(c2,a.strip())) and (re.search(c2,b.strip()))
                            e = (re.search(c3,a.strip())) and (re.search(c3,b.strip()))
                            r = (re.search(c4,a.strip())) and (re.search(c4,b.strip()))
                            t = (re.search(c5,a.strip())) and (re.search(c5,b.strip()))
                            y = (b.strip().startswith('++'))
                            if q or w or e or r or t or y:
                                pass
                            else:
                                logging.error("There is a mismatch in signatures found between the elements in the one/more collection. Please check.")
                                exit()
                else:
                    logging.error("There is a mismatch found in the # of elements for one/more collections. Please check.")
                    exit()
        else:
            logging.error("The number of collections should match. Please check.")
            exit()

    def tcheck(self):
        ## STATIC REGEX CHECK
        c1 = r"^(\w+)"              # eg - normalField
        c2 = r"^<<object:(\w+)$"    # eg - <<objectInsideArray
        c3 = r"^<<<<(\w+)"          # eg - <<<<fieldInsideObjectn1

        for i in range(0,len(self.data['Source'])-1):
            if (not(pd.isna(self.data['Source'][i]))):
                if (re.search(c3,(self.data['Source'][i]).strip())):
                    if ((re.search(c3,(self.data['Source'][i+1]).strip())) or 
                        (re.search(c2,(self.data['Source'][i+1]).lower().strip())) or
                        (re.search(c1,(self.data['Source'][i+1]).strip()))):
                        pass
                    else:
                        logging.error("There is an object within an array that has normal elements (within the array) succeeding it. Please check.")
                        exit()