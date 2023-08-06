import time, json, threading, os, logging, pandas as pd, time, calendar
from dwscripter import scripter,rulesets
from tabulate import tabulate

class bridgeClass():
    def map_gen(self):
        try:
            input_directory = input("\nEnter directory (folder location where the file resides) : ")
        except:
            logging.error("Invalid file path. Please try again.")
            exit()
        try:
            available_files = os.listdir(input_directory.strip())
        except:
            logging.error("Invalid file path. Please try again.")
            exit()

        possible_files = []

        for file in available_files:
            extension = file.split(".")[-1]
            if extension == 'csv':
                possible_files.append(file)
        
        possible_files_dict = {}
        possible_files_dict['Available files'] = possible_files
        print(tabulate(pd.DataFrame(possible_files_dict), headers='keys', tablefmt='psql'))

        try:
            input_file_number = input("\nEnter File Number from the above list : ")
        except:
            logging.error("Invalid file number provided. Please try again.")
            exit()

        _l = len(list(possible_files_dict.values())[0])
        if int(input_file_number) not in list(range(0,_l)):
            logging.error("Invalid option selected. Please try again.")
            exit()

        file_loc = input_directory.strip() + "\\" + possible_files_dict['Available files'][int(input_file_number)]

        try:
            read = pd.read_csv(file_loc)
        except:
            logging.error("Empty file. Please use a valid file.")
            exit()

        cols = list(read.columns)
        rulesets.rules(data=read, columns = cols)
        final_mapping = self.performMapping(data=read)

        current_GMT = time.gmtime()
        ts = calendar.timegm(current_GMT)
        print(f'\n\nTrying to write the file in the directory from where the input CSV file was read... \n')
        time.sleep(2)
        try:
            with open(os.path.join(input_directory,'mapping-'+ str(ts) +'.json'), "w") as f:
                f.write(final_mapping)
        except:
            logging.error("Problem occured while writing the file. Printing the mapping below...")
            print(final_mapping)
            exit()

    def performMapping(self, data=None):
        global stop_threads
        self.data = data
        stop_threads = False
        t1 = threading.Thread(target = self.animate)
        t1.daemon = True
        t1.start()
        res_t = json.dumps(scripter.script(data = data)._final())
        res_d = json.loads(res_t)
        res = json.dumps(res_d, indent=2)
        time.sleep(4)
        stop_threads = True
        return res

    def animate(self):  
        bar = []
        print('\n')
        for i in range(-1,31):
            x = (["||"] * (1+i) + ["|"] + ["  "] * (30-i))
            bar.append("Loading : [" + "".join(x) + "]")

        i = 0
        while True:
            print(bar[i % len(bar)], end="\r")
            time.sleep(.2)
            i+=1
            global stop_threads
            if stop_threads:
                break