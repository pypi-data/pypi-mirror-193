import pandas as pd, logging, re, warnings, numpy as np
from dwscripter import rulesets
from collections import ChainMap
from functools import reduce
from operator import concat
warnings.filterwarnings("ignore")

class script():
    def __init__(self, data=None):
        self.data = data

    def _final(self):
        _d1 = self.mapper1()
        _d2 = self.mapper2()
        result = {**_d1, **_d2}
        formatRes = self.formatJSON(result)
        return(formatRes)

    def formatJSON(self, data=None):
        y={}; y1={}
        for k,v in data.items():
            if isinstance(v,list):
                t1 = []; t2 = {}
                for x in v:
                    if isinstance(x,dict):
                        for k1,v1 in x.items():
                            if isinstance(v1,list):
                                t2[k1]=dict(ChainMap(*v1))
                                t1.append(t2)
                            else:
                                t1.append(x)
                        y[k]=t1
                    else:
                        y[k] = dict(ChainMap(*v))
            else:
                y[k]=v
    
        for k,v in y.items():
            if isinstance(v,list):
                y1[k] = dict(ChainMap(*v))
            else:
                y1[k] = v

        return(y1)

    def extract(self):
        response = rulesets.rules(data=self.data, scripterCall=True).collectionSignature()
        canonical = (response)[0]
        source = (response)[1]
        f2 = []

        for i,j in zip(canonical.values(),source.values()):
            if (j[0] == "na"):
                pass
            else:
                if (list(i) == list(j)):
                    temp_i = map(str, i); temp_j = map(str, j)
                    i = list(pd.Series(temp_i).apply(lambda x: ((x.split(":"))[1]) if (':' in x) else (x)))
                    j = list(pd.Series(temp_j).apply(lambda x: ((x.split(":"))[1]) if (':' in x) else (x)))
                    temp_i = list(map(int, i)); temp_j = list(map(int, j))
                    if temp_i != temp_j:
                        logging.error("Unknown data issue (1.1) : mismatch in one/more collections. Please check.")
                        exit()
                    else:
                        f2.append(temp_i)
                else:
                    logging.error("Unknown data issue (1.2) : mismatch in one/more collections. Please check.")
                    exit()

        final = reduce(concat, f2)

        return(final)

    def mapper1(self):
        # STATIC REGEX CHECK
        first_word_re = r"[a-zA-Z][\w']*"

        final = self.extract()

        newCanonical = self.data['Canonical'].drop(final)
        newSource = self.data['Source'].drop(final)
        newLogic = self.data['Logic'].drop(final)

        captureColl = pd.Series(list(self.data['Source'])).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['object','array']) if (not(pd.isna(x))) else (False))
        collLoc =  ((np.where(np.array(list(captureColl)) == True))[0]).tolist()

        mapper1 = {}; mapOb = False

        canonical = list(newCanonical); source = list(newSource); logic_ = list(newLogic)

        for loc in range(0,len(canonical)):
            logix = []
            if (not(pd.isna(canonical[loc]))):
                word_1 = ((re.search(first_word_re,(canonical[loc]).lower())).group(0))
                if (not(pd.isna(logic_[loc]))):
                    logic = logic_[loc]
                    a0 = logic.split('\n')
                    for i in a0:
                        a1 = i.split(' ')                                                       # Split 'i' using " "
                        a2 = i.split(';')                                                       # Capture 'if' & 'send'
                        a3 = a2[0].split('=')                                                   # Capture the groups before & after '=' in the 'if'
                        a4 = a3[0].lower().split('if')                                          # Cature the group before '=' & after 'if' in the 'if'
                        a5 = (a2[1].split('send')) if ('send' in i.lower()) else ('')           # Capture the group after 'send' in 'else'        

                        if (len(a4) > 1):
                            captureA4 = pd.Series(list(self.data['Source'])).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) == a4[1].strip().lower()) if ((not(pd.isna(x)))) else (False))
                            a4loc_t = ((np.where(np.array(list(captureA4)) == True))[0]).tolist()
                            a4Loc = list(captureA4).index(True)

                            if (self.data['Source'][a4Loc].startswith("<<<<")):
                                logging.error("Writing a logic for a field at root level while referring to a field in a collection within collection is not recommended.")
                                exit()
                            else:
                                if (len(a4loc_t) == 1):
                                    if (self.data['Source'][a4Loc].startswith("<<")):
                                        _r = list(pd.Series(collLoc).apply(lambda x : a4Loc - x))
                                        _r1 = [x for x in _r if x > -1]
                                        if (len(_r1) > 0):
                                            _x = _r1.index(min(_r1))
                                            _x1 = collLoc[_x]
                                            verb = self.data['Source'][_x1]
                                        else:
                                            verb = pd.isna

                                        if (((re.search(first_word_re,(verb).lower())).group(0)) == "array"):
                                            logging.error("Writing a logic for a field at root level while referring to a field in an array is not recommended.")
                                            exit()
                                        else:
                                            if ":" in verb:
                                                verbiage = "payload." + str((verb.split(":"))[1].strip()) + "."
                                            else:
                                                logging.error("Invalid object name found. Please check.")
                                                exit()                                        
                                    else:
                                        verbiage = "payload."
                                else:
                                    verbiage = "payload."

                        if (a1[0].strip().lower() == 'use'):
                            l1 = "('" + a1[1].strip() + "')"
                            logix.append(l1)
                        elif (a1[0].strip().lower() == 'else'):
                            l1 = " else '" + a1[1].strip() + "'"
                            logix.append(l1)
                        elif ((a3[1].strip().lower() == 'null') or (a3[1].strip().lower() == 'empty')):
                            if (len(logix) == 0):
                                l1 = "if (isEmpty(" + verbiage + a4[1].strip() + ")) ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if (isEmpty(" + verbiage + a4[1].strip() + ")) ('" + a5[1].strip() + "')"
                            logix.append(l1)
                        elif ((a3[1].strip().lower() == 'not_null') or (a3[1].strip().lower() == 'not_empty')):
                            if (len(logix) == 0):
                                l1 = "if !(isEmpty(" + verbiage + a4[1].strip() + ")) ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if !(isEmpty(" + verbiage + a4[1].strip() + ")) ('" + a5[1].strip() + "')"
                            logix.append(l1)
                        else:                          
                            if (len(logix) == 0):
                                l1 = "if (" + verbiage + a4[1].strip() + " == '" + a3[1].strip() + "') ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if (" + verbiage + a4[1].strip() + " == '" + a3[1].strip() + "') ('" + a5[1].strip() + "')"
                            logix.append(l1)
                    logic = reduce(concat, logix)
                else:
                    logic = ""

                if (len(logic) > 0): capture_map = (logic)
                elif (not(pd.isna(source[loc]))): capture_map = ("payload." + source[loc])
                else: capture_map = ("")

                if ((word_1 == "object") and (":" in canonical[loc])):
                    mapOb = True
                    obName = (canonical[loc].split(":"))[1]
                    mapper1[obName] = ([])
                    source[loc] = 'dummy'
                elif (("++" in canonical[loc]) and mapOb and (len(obName)>0)):
                    mapper1[obName].append({canonical[loc][2:] : ("payload." + source[loc][2:])})
                elif (("<<" in canonical[loc]) and mapOb and (len(obName)>0)):
                    mapper1[obName].append({canonical[loc][2:] : capture_map})
                else:
                    mapper1[canonical[loc]] = (capture_map)

        return(mapper1)

    def mapper2(self):
        # STATIC REGEX CHECK
        first_word_re = r"[a-zA-Z][\w']*"

        final = list(self.extract())

        newCanonical = self.data['Canonical'][final]
        newSource = self.data['Source'][final]
        newLogic = self.data['Logic'][final]
        source_ = self.data['Source'].drop(final)

        canonical = list(newCanonical); source = list(newSource); logic_ = list(newLogic)

        mapper2 = {}; cap = {}; mapOb = False; mapAr = False
        mapObInAr = False; cap_collection = []; mapper_t = {}

        for loc in range(0,len(canonical)):
            logix = []
            if(not(pd.isna(canonical[loc]))):
                word_1 = ((re.search(first_word_re,(canonical[loc]).lower())).group(0))
                if ((word_1 in ['array','object']) and (not(canonical[loc].lower().startswith("<<")))):
                    cap[loc] = [[loc]]
                    cap_collection.append(word_1)

                elif (canonical[loc].lower().startswith("<<object")):
                    _temp = list(cap.keys())[-1]
                    cap[_temp].append([loc])

                if (not(pd.isna(logic_[loc]))):
                    logic = logic_[loc]
                    a0 = logic.split('\n')
                    for i in a0:
                        logix_temp = []
                        a1 = i.split(' ')                                                       # Split 'i' using " "
                        a2 = i.split(';')                                                       # Capture 'if' & 'send'
                        a3 = a2[0].split('=')                                                   # Capture the groups before & after '=' in the 'if'
                        a4 = a3[0].lower().split('if')                                          # Cature the group before '=' & after 'if' in the 'if'
                        a5 = (a2[1].split('send')) if ('send' in i.lower()) else ('')           # Capture the group after 'send' in 'else'

                        if (len(a4) > 1):
                            _a = []; _b = []
                            # Check if the column that is mentioned before '=' & after 'if' in the 'if' statement belongs to the collection (_a) / at root level (_b)
                            _a = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) == (a4[1]).lower().strip()) if (not(pd.isna(x))) else (False))
                            _b = pd.Series(list(source_)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) == (a4[1]).lower().strip()) if (not(pd.isna(x))) else (False))

                            if (True in list(_a)):
                                _cap = reduce(concat, (list(cap.values())[-1] if len(cap) > 0 else []))
                                _tempa = pd.Series(list(source)[_cap[-1]:]).apply(lambda x : ("allowed") if (x.startswith('<<<<')) else ("stop"))
                                _subcol = list(range(_cap[-1], (_cap[-1] + list(_tempa).index('stop',1)) )) if('stop' in (list(_tempa)[1:])) else (list(range(_cap[-1], (_cap[-1] + len(list(_tempa)) ) )))
                                _col = _subcol[1:]

                                _ind = list(_a).index(True)
                                _fin_t = pd.Series(_cap).apply(lambda x : (_ind-x))
                                _fin = [x for x in list(_fin_t) if (x > 0)]

                                if (len(list(_fin)) > 0):
                                    if (_ind in _col):
                                        _locind = list(_fin).index(min(_fin))
                                        _collection = source[_cap[_locind]]
                                        if (':' in _collection):
                                            _fn1 = (re.search(first_word_re,(_collection.split(':')[1]))).group(0)
                                        else:
                                            logging.error("Data issue (2.0) : The collection " + str(_collection) + " does not have a name (usually mentioned after ':'). Please check.")
                                            exit()
                                        _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                        _field = _fn1 + "." + _fn2
                                        _l = "item." + _field

                                    elif (_ind in list(range(_cap[0], _cap[-1]))):
                                        if ((_ind < _cap[-1]) and (_ind not in (list(range(_cap[0], _cap[1]))))):
                                            _f1 = pd.Series(list(_cap)).apply(lambda x : (_ind - x))
                                            _ft = [x for x in list(_f1) if (x > 0)]
                                            _collection = source[_cap[_ft.index(min(_ft))]]
                                            if (':' in _collection):
                                                _fn1 = (re.search(first_word_re,(_collection.split(':')[1]))).group(0)
                                            else:
                                                logging.error("Data issue (2.0) : The collection " + str(_collection) + " does not have a name (usually mentioned after ':'). Please check.")
                                                exit()
                                            _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                            _field = _fn1 + "." + _fn2
                                            _l = "item." + _field
                                            
                                        elif (_ind in (list(range(_cap[0], _cap[1])))):
                                            _fn1 = (re.search(first_word_re,(a4[1]))).group(0)
                                            _l = "item." + _fn1
                                        else:
                                            _fn = (source[_ind])
                                            _field = (re.search(first_word_re,(_fn).lower())).group(0)
                                            _l = "item." + _field
                                    else:
                                        if ((_ind > _cap[0]) and (len((_col)) == 0)):
                                            _c1 = pd.Series(list(source)[(_cap[0]):]).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['object','array']) if (not(pd.isna(x))) else (False))
                                            _c2 = pd.Series(list(source)[(_cap[0]):]).apply(lambda x : (((re.search(first_word_re,(x).lower().strip())).group(0)) == a4[1].lower().strip()) if (not(pd.isna(x))) else (False))
                                            _c1t = ((np.where(np.array(list(_c1)) == True))[0]).tolist()
                                            _c2t = list(_c2).index(True)

                                            _ft1 = list(pd.Series(list(_c1t)).apply(lambda x : _c2t - x))
                                            _updated_ft1 = [x for x in _ft1 if (x > 0)]

                                            _ft1t = _updated_ft1.index(min(_updated_ft1))
                                            _fn = (list(source)[(_cap[0]):])[list(_c1t)[_ft1t]]

                                            _u1 = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['object','array']) if (not(pd.isna(x))) else (False))
                                            _u2 = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower().strip())).group(0)) == a4[1].lower().strip()) if (not(pd.isna(x))) else (False))
                                            _u1t = ((np.where(np.array(list(_u1)) == True))[0]).tolist()
                                            _u2t = list(_u2).index(True)

                                            _u3 = list(pd.Series(list(_u1t)).apply(lambda x : _u2t - x))
                                            _u3t = [x for x in _u3 if (x > 0)][-1]

                                            if ((list((source)[(_cap[0]):])[_c2t]).startswith("++")):
                                                _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                _l = "payload." + _fn2
                                            else:
                                                if (':' in _fn):
                                                    _fn1 = (re.search(first_word_re,(_fn.split(':')[0]))).group(0)
                                                    _fn1t = (re.search(first_word_re,(_fn.split(':')[1]))).group(0)
                                                else:
                                                    logging.error("Data issue (2.0.0) : The collection " + str(_fn) + " does not have a name (usually mentioned after ':'). Please check.")
                                                    exit()
                                                if _fn1.lower() == "array":
                                                    _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                    _l = "item" + "." + _fn2
                                                elif ((((list(source))[_u3t]).lower().split(":")[0] == "object") and (_fn.lower().split(":")[0] == "array")):
                                                    logging.error("Data issue (2.0.1) : Collection : " + str(_fn) + ". Not recommended to write logic pertnent to a field / a field in an object which is placed inside an array. Please check.")
                                                    exit()
                                                else:
                                                    _fn = (source[_ind])
                                                    _field = (re.search(first_word_re,(_fn).lower())).group(0)
                                                    _l = "item." + _fn1t + "." + a4[1].strip()

                                        elif (_ind > _cap[1]):
                                            _capture = pd.Series(list(source)[(_col[-1]+1):]).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['object']) if (not(pd.isna(x))) else (False))
                                            _ftemp = list(_capture).index(True)
                                            _fture = (_col[-1]+1) + _ftemp
                                            _fn = (source[_fture])
                                            if (':' in _fn):
                                                _fn1 = (re.search(first_word_re,(_fn.split(':')[1]))).group(0)
                                            else:
                                                logging.error("Data issue (2.0.2) : The collection " + str(_fn) + " does not have a name (usually mentioned after ':'). Please check.")
                                                exit()

                                            if (_fn.lower().startswith("<<")):
                                                _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                _l = "item." + _fn1 + "." + _fn2
                                            else:
                                                _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                _l = "payload." + _fn1 + "." + _fn2                                                
                                        else:
                                            logging.error("Data issue (2.0.3) : The field mentioned in 'if' statement is not present within the same collection in the Array. Please check.")
                                            exit()                                        
                                else:
                                    # position of the occurances of the mentioned field in the 'if' statement
                                    log_key = (re.search(first_word_re,a4[1].lower())).group(0)
                                    _fin = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) == log_key) if (not(pd.isna(x))) else (False))
                                    _ft = ((np.where(np.array(list(_fin)) == True))[0]).tolist()
                                    # capture the locations of the collections in the 'source' column
                                    _c1 = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['object','array']) if (not(pd.isna(x))) else (False))
                                    _c1t = ((np.where(np.array(list(_c1)) == True))[0]).tolist()

                                    _p = list(pd.Series(list(_c1t)).apply(lambda x : x - _ft[0]))
                                    _p1 = [x for x in _p if (x < 0)]
                                    _p = _c1t[_p1.index(max(_p1))]

                                    if (len(_fin) > 0):
                                        _coll = source[_p]
                                        if (":" in _coll):
                                            word_x = ((re.search(first_word_re,(_coll.split(":")[0]).lower())).group(0))
                                            if (not(_coll.split(":")[0].startswith("<<"))) and (word_x != "array"):
                                                _fn1 = (re.search(first_word_re,_coll.split(":")[1])).group(0)
                                                _fn2 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                _l = "payload." + _fn1 + "." + _fn2
                                            elif (list(source)[_ft[0]].startswith("++")):
                                                _fn1 = (re.search(first_word_re,(a4[1]).lower())).group(0)
                                                _l = "payload." + _fn1
                                            else:
                                                logging.error("Data issue (2.1.x.1) : Some issue with the field mentioned in one of the 'if' statements. Please check.")
                                                exit()
                                        else:
                                            logging.error("Data issue (2.1.x.2) : Some issue with the field mentioned in one of the 'if' statements. Please check.")
                                            exit()
                                    else:
                                        logging.error("Data issue (2.1.x.3) : Some issue with the field mentioned in one of the 'if' statements. Please check.")
                                        exit()

                            elif (True in list(_b)):
                                _fn = (list(source_)[list(_b).index(True)])
                                _field = (re.search(first_word_re,(_fn).lower())).group(0)
                                _l = "payload." + _field
                            else:
                                logging.error("Data issue (2.2) : The field in row : " + str(loc) + " mentioned in 'if' statement is not present at root level. Please check.")
                                exit()
                            
                            logix_temp.append(_l)

                        # Check for 'Object' Logic
                        if (len(cap_collection) > 0):
                            if (cap_collection[-1] == "object"):
                                logix_temp = list(pd.Series(logix_temp).apply(lambda x:(x.replace('item','payload')) if ('item' in x) else (x)))
                        if (a1[0].strip().lower() == 'use'):
                            l1 = "('" + a1[1].strip() + "')"
                            logix.append(l1)
                        elif (a1[0].strip().lower() == 'else'):
                            l1 = " else '" + a1[1].strip() + "'"
                            logix.append(l1)
                        elif ((a3[1].strip().lower() == 'null')):
                            if (len(logix) == 0):
                                l1 = "if (isEmpty(" + logix_temp[0].strip() + ")) ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if (isEmpty(" + logix_temp[0].strip() + ")) ('" + a5[1].strip() + "')"
                            logix.append(l1)
                        elif (a3[1].strip().lower() == 'not_null'):
                            if (len(logix) == 0):
                                l1 = "if !(isEmpty(" + logix_temp[0].strip() + ")) ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if !(isEmpty(" + logix_temp[0].strip() + ")) ('" + a5[1].strip() + "')"
                            logix.append(l1)
                        else:
                            if (len(logix) == 0):
                                l1 = "if (" + logix_temp[0].strip() + " == '" + a3[1].strip() + "') ('" + a5[1].strip() + "')"
                            else:
                                l1 = " else if (" + logix_temp[0].strip() + " == '" + a3[1].strip() + "') ('" + a5[1].strip() + "')"
                            logix.append(l1)
                    logic = reduce(concat, logix)
                else:
                    logic = ""
                
                _a = pd.Series(list(source)).apply(lambda x : (((re.search(first_word_re,(x).lower())).group(0)) in ['array','object']) if (not(pd.isna(x))) else (False))
                _a_true = ((np.where(np.array(list(_a)) == True))[0]).tolist()

                # Find the nearest collection to the current element
                _a_con = pd.Series(list(_a_true)).apply(lambda x : loc-x)
                _a_flt = [x for x in list(_a_con) if (x > -1)]
                _c_name = list(source)[(_a_true)[_a_flt.index(min(_a_flt))]]
                _c_n = re.search(first_word_re,((_c_name.split(":"))[1])).group(0)

                _x1 = re.search(first_word_re,(canonical[loc])).group(0)
                _x2 = re.search(first_word_re,(source[loc])).group(0)

                if ((word_1 == "object") and (canonical[loc].lower().startswith("<<object")) and (mapAr)):
                    try:
                        if ((len(cap_obInAr) > 0) and (len(cap_currOb) > 0)):
                            mapper_t[cap_currOb] = cap_obInAr
                            mapper2[store_cap_currOb_2].append(mapper_t)
                            mapper_t = {}
                            cap_obInAr = []
                    except:
                        cap_obInAr = []
                        mapper_t = {}
                    
                    cap_currOb = re.search(first_word_re,(canonical[loc].split(":")[1])).group(0)
                    mapOb = False; mapObInAr = True

                elif ((word_1 == "object") and (":" in canonical[loc])):
                    mapOb = True; mapAr = False; mapObInAr = False
                    cap_currOb_1 = re.search(first_word_re,(canonical[loc].split(":")[1])).group(0)
                    mapper2[cap_currOb_1] = []
                
                elif ((word_1 == "array") and (":" in canonical[loc]) and (":" in source[loc])):
                    mapOb = False; mapAr = True; mapObInAr = False
                    cap_currOb_2 = re.search(first_word_re,(canonical[loc].split(":")[1])).group(0)
                    mapper2[cap_currOb_2] = [{"__header_script": "payload." + (source[loc].split(":")[1]) + " map ((item, index) -> {})"}]

                elif (mapOb):
                    if ((source[loc]).strip().startswith('++')):
                        mapping = ({_x1: ("payload." + _x2)}) if (len(logic)==0) else ({_x1 : logic})
                    else:
                        mapping = ({_x1: ("payload." + _c_n + "." + _x2)}) if (len(logic)==0) else ({_x1 : logic})
                    mapper2[cap_currOb_1].append(mapping)

                elif ((mapAr) and (not(mapObInAr))):
                    if ((source[loc]).strip().startswith('++')):
                        mapping = ({_x1: ("payload." + _x2)}) if (len(logic)==0) else ({_x1 : logic})
                    else:
                        mapping = ({_x1: ("item." + _x2)}) if (len(logic)==0) else ({_x1 : logic})
                    mapper2[cap_currOb_2].append(mapping)

                elif ((mapAr) and (mapObInAr)):
                    store_cap_currOb_2 = cap_currOb_2
                    if (len(logic)==0):
                        if ((_x2).lower() == "payload"):
                            if (len(source[loc].split(">")) == 2):
                                mapping = ({_x1: ("payload." + str(source[loc].split(">")[1]))})
                            else:
                                logging.error("Syntax to refer to a field from root within an object in an array - <<<<Payload>{field}. Check row - " + str(loc))
                                exit()
                        elif ((_x2).lower() == "root"):
                            if (len(source[loc].split(">")) == 2):
                                mapping = ({_x1: ("item." + str(source[loc].split(">")[1]))})
                            else:
                                logging.error("Syntax to refer to a field from inside the array within an object in that array - <<<<Root>{field}. Check row - " + str(loc))
                                exit()
                        else:
                            mapping = ({_x1: ("item." + _c_n + "." + _x2)}) 
                    else:
                        mapping = ({_x1 : logic})
                    cap_obInAr.append(mapping)

        try:
            if ((len(cap_obInAr) > 0) and (len(cap_currOb) > 0)):
                mapper_t[cap_currOb] = cap_obInAr
                mapper2[store_cap_currOb_2].append(mapper_t)
                mapper_t = {}
                cap_obInAr = []
        except:
            cap_obInAr = []

        return(mapper2)