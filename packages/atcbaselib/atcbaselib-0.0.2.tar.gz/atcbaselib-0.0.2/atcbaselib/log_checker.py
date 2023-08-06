# -*- coding: utf-8 -*-
import os
import re
import numpy as np
import logging
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import re
from fuzzywuzzy import fuzz
import pdb

'''
    Log_Checker will find out below unsuitable behaviors in output logs:
        a) includes the error key words, such as '[E]', 'failed', 'err', etc
        b) some debug log output with un-acceptable frequence
        c) the log file lines exceed the system tolerance
        d) any other we want to filter out

        For item c), a simplfy method I used is sorting the top10 word.
           1) for normal log file, top10 word might fixed words, only 7~9 maybe unfixed.
           2) if a word suddenly rush into the rank, it will be a major suspector (assuming ranked into threhold top 5)
           3) if resonable after reviewing, we update the top10 histroy list we saved before

        Also, if we have a model that can get the characteristic of a sentence, for example we ignore some non-critical info of one sentence, we can find out the abnormal lines.
          Such as:
            "This is the testing log - 2021-7-8-22-12" and "This is the testing log - 2021-7-8-22-13", we can inference two sentences are dupulicated.
        I think it is more smart, accuratly, but it's diffcult for me to implement. So we can award the guys who implement this. :-)
'''

class Log_Time_Info():
    def __init__(self, _path = '', _log = ''):
        self.times = 0
        self.list_time = []
        self.freq = 0
        self.path = _path
        self.log = _log

    def set_last_time(self, time):
        self.list_time.append(time)
        self.times += 1
        if (self.times > 0 and (time - self.list_time[0]).seconds > 0):
            self.freq = self.times / (time - self.list_time[0]).seconds
        

class Log_Checker():
    def __init__(self, _log_path = "", _result_path = "", _uart_log_path = "uart_log.txt", _boot_log_path = "boot_log.txt", _top_word_path = "top.txt", _top_rank_num = 50, _log_total_num_thres = 1000, _log_num_thres_one_second = 20, _key_word_list = [" e ","fail","error","exception"]):
        logging.info("============Log_Check Init====================")
        self.log_path         = _log_path           # Log file path we want to analysis
        self.boot_log_path    = _boot_log_path      # boot log path
        self.uart_log_path    = _uart_log_path      # uart log path
        self.top_word_path    = _top_word_path      # Project top word rank list
        self.result_path      = _result_path
        self.log_line_num     = 0                   # Total lines number
        self.log_total_num_thres   = _log_total_num_thres 
        self.log_num_thres_one_second = _log_num_thres_one_second
        self.top_rank_num     = _top_rank_num
        self.key_word_list    = _key_word_list

        self.pattern_dic      = {}                  # Save lines which including the pattern world
        self.word_dic         = {}                  # Save the files words count
        self.cur_top_rank     = {}                  # Current log file top rank
        self.rushman_dic      = {}
        self.all_log_path = {}

        if os.path.exists("top_rank.npy"):
            self.ori_top_rank = np.load("top_rank.npy", allow_pickle=True).item()  # Original top rank
        else:
            self.ori_top_rank = None

        logging.debug('top_rank: {}'.format(self.ori_top_rank))
        for w in self.key_word_list:
            self.pattern_dic[w] = []                # Init the pattern dic

        logging.info("Dump reg info:")
        logging.info(self.pattern_dic)                     # Dump debug information

    def find_rushman(self):
        logging.info("============Find_rushman======================")
        rushman = []

        if self.ori_top_rank is None:
            logging.info('No rank! exit')
            return

        i = 0
        logging.debug(self.ori_top_rank.keys())
        for m in self.cur_top_rank.keys():
            if m not in self.ori_top_rank.keys():
                rushman.append( m )
                i = i + 1

        if len(rushman) == 0:
            logging.info("All Acquaintance!!!!!")
        else:
            logging.info("Catch the rushman :" + str(rushman))

            for n in rushman:
                i = 0
                self.rushman_dic.setdefault(n, 0)
                for l in self.cur_top_rank.keys():
                    if n == l:
                        break
                    i = i + 1
                self.rushman_dic[n] = i
        return

    def cal_similarity(self, log_dict, log):
        ratio = 0
        for key in log_dict:
            words_ori = key.split(' ')
            words_current = log.split(' ')
            ratio = fuzz.ratio(words_ori[1:], words_current[1:])
            if ratio > 85:
                return key, ratio
        return '', ratio

    def find_log_path(self, root, pattern):
        dirs = []
        for x in os.listdir(root):
            nd = os.path.join(root, x)
            if os.path.isdir(nd):
                dirs.append(nd)
            elif os.path.isfile(nd) and 'uart' in pattern and 'uart_log.txt' in nd:
                    self.all_log_path.setdefault('uart',[]).append(nd)
            elif os.path.isfile(nd) and "adas" in root:
                if 'adas' in pattern and 'syslog' in nd:
                    self.all_log_path.setdefault('adas',[]).append(nd)
            elif os.path.isfile(nd) and "cluster" in root:
                if 'cluster' in pattern and 'syslog' in nd:
                    self.all_log_path.setdefault('cluster',[]).append(nd) 
            elif os.path.isfile(nd) and 'ivi' in root:
                if 'main' in pattern and 'main' in nd:
                    self.all_log_path.setdefault('main',[]).append(nd)
                elif 'kernel' in pattern and 'kernel' in nd:
                    self.all_log_path.setdefault('kernel',[]).append(nd)
        for dir in dirs:
            self.find_log_path(root=dir, pattern=pattern)

    # input log_line
    # output log_time, module_name, main_log
    def parse_log(self, log_line, pattern):
        if "adas" in pattern or "cluster" in pattern or "uart" in pattern:
            res = re.findall('\[[A-Z]\]', log_line)
            if res:
                log_level = res[0]
            else:
                return None, None, None
            start = log_line.find(log_level) + 3
            main_log = log_line[start:].strip()
            start_iter = re.search('\[[a-zA-Z]', main_log)#eg:[151][151][[AVMViewManager]] -> [AVMViewManager]
            module = re.findall('\[.*\]', main_log[start_iter.span()[0]:] if start_iter else main_log[0:])
            module_name = ""
            if len(module) >= 1:
                module_name = re.sub('\[|\]','', module[0])
            try:
                if "uart" in pattern:
                    log_time = datetime.strptime(str(log_line[1:20]), "%Y-%m-%d-%H-%M-%S")
                else:
                    tmp = log_line.split('  ')
                    timestamp = tmp[0] + " " + " ".join(tmp[1].split(' ')[0:2])
                    log_time = datetime.strptime(timestamp.split(".")[0], "%b %d %H:%M:%S")
            except Exception as a:
                return None, None, None
            return log_time, module_name, main_log

        elif "main" in pattern:
            res = re.findall('[A-Z]+', log_line)
            if res:
                log_level = res[0]
            else:
                return None, None, None
            try:
                start = log_line.find(log_level) + 1
                main_log = log_line[start:].strip()
                start_iter = re.search('\[[A-Z]', main_log)#eg:[151][151][[AVMViewManager]] -> AVMViewManager
                module = re.findall('\[.*\]', main_log[start_iter.span()[0]:] if start_iter else main_log.split(":")[0])
                module_name = ""
                if len(module) >= 1:
                    module_name = re.sub('\[|\]','', module[0])
                if module_name == "":
                    module_name = main_log.split(':')[0]
                log_time = datetime.strptime(str(log_line[0:14]), "%m-%d %H:%M:%S")
            except Exception as a:
                return None, None, None
            return log_time, module_name, main_log

        elif "kernel" in pattern:
            start = log_line.rfind(']') + 1
            main_log = log_line[start:].strip()
            try:
                start_iter = re.search('\[[A-Z]', main_log)#eg:[151][151][[AVMViewManager]] -> AVMViewManager
                module = re.findall('\[.*\]', main_log[start_iter.span()[0]:] if start_iter else main_log.split(":")[0])
                module_name = ""
                if len(module) >= 1:
                    module_name = re.sub('\[|\]','', module[0])
                if module_name == "":
                    module_name = main_log.split(':')[0]
                log_time = datetime.strptime(str(log_line[0:14]), "%m-%d %H:%M:%S")
            except Exception as a:
                return None, None, None
            return log_time, module_name, main_log

        return None, None, None

    def check_log_times(self, patterns = ['main', 'adas', 'cluster', 'kernel']):
        for pattern in patterns:
            result_log_info = {}
            last_log = ""
            base_log = ""
            result_file_name = self.result_path + '/' + pattern + '_log_times.csv'
            logging.info("============check_" + str(pattern)+ "_log_times====================")
            logging.info("log path : " + self.log_path)
            self.find_log_path(self.log_path, pattern)
            logging.info(self.all_log_path[pattern])

            for path in self.all_log_path[pattern]:
                try:
                    with open(path, "r", encoding='ISO-8859-1') as f:
                        print(path)
                        all_log = f.readlines()
                except Exception as a:
                    print(a)
                    continue
                for log_line in all_log:
                    #find the log level and log module name
                    log_time, module_name, main_log = self.parse_log(log_line, pattern)
                    if not log_time and not module_name and not main_log:
                        continue

                    key = path + main_log
                    if module_name in result_log_info:
                        if key in result_log_info[module_name]:
                            if last_log == key:
                                result_log_info[module_name][base_log].set_last_time(log_time)
                            else:
                                result_log_info[module_name][key].set_last_time(log_time)
                        else:
                            key_log, radio=self.cal_similarity(result_log_info[module_name], main_log)
                            if radio > 85 and result_log_info[module_name][key_log].path == path:
                                result_log_info[module_name][key_log].set_last_time(log_time)
                                last_log = key
                                base_log = key_log
                            else:
                                info = Log_Time_Info(path, main_log)
                                info.set_last_time(log_time)
                                result_log_info[module_name][key] = info
                    else:
                        result_log_info[module_name] = {}
                        info = Log_Time_Info(path, main_log)
                        info.set_last_time(log_time)
                        result_log_info[module_name][key] = info
            self.write_times_check_result(result_log_info, result_file_name)

    def write_times_check_result(self, log_dict, result_file):
        with open(result_file, 'w', newline='') as csvfile:
            fieldnames = ['log', 'path', 'times', 'freq', 'max_time', 'max_times_one_second']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for module_name in log_dict:
                for info in log_dict[module_name]:
                    max_time = max(log_dict[module_name][info].list_time, key=log_dict[module_name][info].list_time.count)
                    max_times_one_second = log_dict[module_name][info].list_time.count(max_time)
                    if log_dict[module_name][info].times > int(self.log_total_num_thres) or max_times_one_second > int(self.log_num_thres_one_second):
                        writer.writerow({'log': log_dict[module_name][info].log, 'path': log_dict[module_name][info].path.replace('log_for_check',''),
                                        'times': log_dict[module_name][info].times, 'freq': log_dict[module_name][info].freq,
                                        'max_time': max_time, 'max_times_one_second': max_times_one_second})
        csvfile.close()

    def check_log_format(self):
        logging.info("============Check_Log_Format====================")
        LIST_FILE_SUFFIX = [".cpp", ".java", ".c"]
        LIST_LOG_LEVEL = ["[E]"]

        containsAny = lambda seq, aset: True if any(i in seq for i in aset) else False

        wrong_format_log = []
        with open(self.uart_log_path, "r") as f:
            all_log = f.readlines()

        for log_line in all_log:
            if containsAny(log_line, LIST_LOG_LEVEL) and not containsAny(log_line, LIST_FILE_SUFFIX):
                wrong_format_log.append(log_line.strip())

        with open(self.result_path + '/log_wrong_format.csv', 'w', newline='') as csvfile:
            fieldnames = ['log']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for log in wrong_format_log:
                writer.writerow({'log': log})
            csvfile.close()

    def find_elog_at_boot(self):
        logging.info("============find_E_log====================")
        with open(self.boot_log_path, "r") as f:
            all_log = f.readlines()

        elog = [x.strip() for x in all_log if '[E]' in x]

        if len(elog) == 0:
            logging.info("not E log at boot")
            return

        with open(self.result_path + '/boot_errorlog.csv', 'w', newline='') as csvfile:
            fieldnames = ['log']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for log in elog:
                writer.writerow({'log': log})
            csvfile.close()

    def check_duration_warn_log(self):
        logging.info("============Check_duration_warn_Log====================")
        duration_warn_log = []
        self.find_log_path(self.log_path, 'kernel')
        print(self.all_log_path['kernel'])

        for path in self.all_log_path['kernel']:
            with open(path, "r", encoding='ISO-8859-1') as f:
                print(path)
                try:
                    all_log = f.readlines()
                except Exception as a:
                    print(a)
                    continue

            for log_line in all_log:
                if 'DURATION WARN' in log_line:
                    info = Log_Time_Info(path, log_line.strip())
                    duration_warn_log.append(info)

        if len(duration_warn_log) == 0:
            logging.info("not duration warn log")
            return

        with open(self.result_path + '/duration_warn_log.csv', 'w', newline='') as csvfile:
            fieldnames = ['log', 'path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for warn_log in duration_warn_log:
                writer.writerow({'log': warn_log.log, 'path': warn_log.path.replace('log_for_check','')})
            csvfile.close()

    def do_top_rank(self):
        logging.info("============Find_suspector====================")
        if os.path.exists(self.top_word_path):
            with open(self.top_word_path, 'r') as lf:
                text = lf.read()
                temp_words = re.split('[^a-zA-Z]', text)      # Split the words from the line
                words = list(filter(None, temp_words))        # Give up all None string

                for word in words:
                    self.word_dic.setdefault(word, 0)
                    self.word_dic[word] = self.word_dic[word] + 1  # Calculate the specail word's count
                lf.close()
        else:
            logging.info("top rank file not exited")
            return

        # Sort the dic from big to small by the dic value
        sorted_list = (sorted(self.word_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))

        for i in range(self.top_rank_num):
            # Save the top N words  0:(word, count)
            self.cur_top_rank[sorted_list[i][0]] = sorted_list[i][1]

        #np.save("top_rank.npy", self.cur_top_rank)

    def find_abnormal_sentences(self):
        logging.info("============Find_abnormal_sentences and total line number===========")
        if os.path.exists(self.log_path):
            with open(self.uart_log_path, 'r') as lf:
                while True:
                    line = lf.readline()
                    for w in self.key_word_list:
                        if w in line.lower():
                            self.pattern_dic[w].append(line)
                    self.log_line_num = self.log_line_num + 1
                    if line == '':
                        break

                lf.close()

    def do_check(self):
        logging.info("Do log check")
        self.find_abnormal_sentences()
        self.do_top_rank()
        self.find_rushman()

    def gen_result(self, result_filename):
        x_data = []
        y_data = []
        logging.info(self.result_path + result_filename)
        for m in self.pattern_dic:
            logging.info(str(m) + ": " + str(len(self.pattern_dic[m])))
            y_data.append(len(self.pattern_dic[m]))
            x_data.append(m)

        fig = plt.figure(figsize=(10,10))

        data_cnt = len(self.pattern_dic)
        color = ['#A9A9A9','#006699', '#006400', '#999933','#CC9966', '#FFFFCC']
        plt.bar(x_data, y_data, width=0.5, color = color[1])
        for a,b in zip(x_data, y_data):
            plt.text(a,b,
                     b,
                     ha='center', 
                     va='bottom',
                    )
        ax = plt.gca()
        ax.set_xticks(range(data_cnt))
        ax.set_xticklabels(x_data, rotation = 45)
        ax.set_yticks([0,512,3072,3584,4096])
        ax.set_xlabel("key word")
        ax.set_ylabel("The number of key word")
        ax.set_title("log_check") 
        plt.savefig(self.result_path + result_filename)
        #plt.show()

    def report(self):
        # Generate the report file
        logging.info("============Report result================")
        #logging.debug("============All sentence need to be reviewed:")
        #for m in self.pattern_dic:
        #    logging.debug(str(m) + ": \n")
        #    for n in self.pattern_dic[m]:
        #        logging.debug("\t" + n)

        # print top rank on screen
        logging.info("============Top rank status:")
        logging.info("\t" + str(self.cur_top_rank))

        #
        logging.info("============Total line number: ")
        logging.info("\tlog line number: " + str(self.log_line_num))
        logging.info("\tline number threshold: " + str(self.line_num_thres))

        #
        logging.info("============High Risk words: ")
        logging.info("\t" + str(self.rushman_dic))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(message)s -----%(filename)s(line:%(lineno)d):%(asctime)s')
    path = "D:/2022task/Log_Checker_Code/test/log/log"
    line_num_threshold = input("每秒输出最大次数")
    print(line_num_threshold)
    key_word_list = [" e ","fail","error","exception"]
    top_rank_num = 50

    lc = Log_Checker(path, path, key_word_list, path + "/uart_log.txt", path + "/boot_log.txt", "top.txt", 50, 1000, line_num_threshold)
    lc.do_check()
    lc.find_elog_at_boot()
    lc.check_log_format()
    lc.gen_result("result.png")
    if (os.path.exists(path)):
        lc.check_duration_warn_log()
        lc.check_log_times(['main', 'adas', 'cluster', 'kernel'])

