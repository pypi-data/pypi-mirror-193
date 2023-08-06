# read csv,then info -> rdm
import os
import re
import logging
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import configparser
from fuzzywuzzy import fuzz

class CSVToRdmInfo():
    def __init__(self, _path = '', _module2pic_config_path = './atcbaselib/logconfig.ini', _log_num_threshold_second = 60):
        self.path = _path
        self.module2pic_config_path = _module2pic_config_path #module2pic comfig path
        self.csv_path = [] #所有以.csv结尾的绝对路径
        self.log_times = {}   #{pic:log}
        self.boot_error_log = {}   #{pic:log}
        self.log_wrong_format = {} #{pic:log}
        self.log_num_threshold_second = _log_num_threshold_second
        self.log_times_rdm_info = {}
        self.boot_error_log_rdm_info = {}
        self.log_wrong_format_rdm_info = {}

    def find_csv(self):
        #遍历文件夹，找到.csv结尾的文件，存入self.csv_path
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if str(file).endswith('.csv'):
                    csv_path = os.path.join(root, file)
                    self.csv_path.append(csv_path)

    def cal_similarity(self, log_dict, log):
        ratio = 0
        for key in log_dict:
            words_ori = key.split(' ')
            words_current = log.split(' ')
            ratio = fuzz.ratio(words_ori[1:], words_current[1:])
            if ratio > 85:
                return key, ratio
        return '', ratio

    def read_csv(self, keywords_list):
        self.find_csv()
        print(self.csv_path)
        all_csv = list(filter(lambda text: any([word in text for word in keywords_list]), self.csv_path))
        #是否将每个 csv的寻找pic过程变成异步线程？
        last_log = ""
        base_log = ""
        for csv_file in all_csv:
            csv_reader = csv.DictReader(open(csv_file))
            if "log_times" in csv_file:
                for row in csv_reader:
                    log = row['log']
                    pic = self.find_pic(log)
                    if pic == " ":
                        continue
                    if int(row['max_times_one_second']) < self.log_num_threshold_second:
                        continue
                    if pic in self.log_times:
                        key_log, radio = self.cal_similarity(self.log_times[pic], log)
                        if radio > 85:
                            last_log = row
                            base_log = key_log
                            continue
                        else:
                            self.log_times[pic].append(log)
                        # todo 检测log相似度，无论path，只看log
                    else:
                        self.log_times.setdefault(pic,[]).append(log)

            elif "log_wrong_format" in csv_file:
                for row in csv_reader:
                    log = row['log']
                    pic = self.find_pic(log)
                    if pic == " ":
                        continue
                    if pic in self.log_wrong_format:
                        key_log, radio = self.cal_similarity(self.log_wrong_format[pic], log)
                        if radio > 85:
                            last_log = row
                            base_log = key_log
                            continue
                        else:
                            self.log_wrong_format[pic].append(log)
                        #todo 检查log相似度，无论path，只看log
                    else:
                        self.log_wrong_format.setdefault(pic,[]).append(log)

            elif "boot_errorlog" in csv_file:
                for row in csv_reader:
                    log = row['log']
                    pic = self.find_pic(log)
                    if pic == " ":
                        continue
                    if pic in self.boot_error_log:
                        self.boot_error_log[pic].append(log)
                    else:
                        self.boot_error_log.setdefault(pic,[]).append(log)

            else:
                continue

    def find_pic(self, log):
        #logconfig.ini中，一级模块和二级模块是由空格进行分割的
        read_ini = configparser.ConfigParser()
        read_ini.read(self.module2pic_config_path, encoding='utf-8')
        logmodule2result = eval(read_ini['AC8025S-LogModule2PIC']['LOGMODULE2PIC'])
        for subteam in logmodule2result:
            for item in logmodule2result[subteam]:
                module_name_list = item.split(' ')
                if len(module_name_list) > 1:
                    first_module_name = item.split(' ')[0]
                    sub_module_name = item.split(' ')[1]
                    index = re.search(first_module_name + '.*' + sub_module_name, log)
                    if index == None:
                        continue
                    else:
                        return logmodule2result[subteam][item]
                else:
                    first_module_name = item.split(' ')[0]
                    index = re.search(first_module_name, log)
                    if index == None:
                        continue
                    else:
                        return logmodule2result[subteam][item]
        return ' '
        
    #传入common_info，组合成rdm的issues传出
    #common_info 包含的Key为  image_path、log_path、project、issue_type
    def prepareInfo(self, common_info):
        for item in self.log_times:
            self.log_times_rdm_info.setdefault(item,{})
            self.log_times_rdm_info[item]['image_path'] = common_info['image_path']
            self.log_times_rdm_info[item]['log_path'] = common_info['log_path']
            self.log_times_rdm_info[item]['summary'] = "[log check] max_times_one_second > 60"
            self.log_times_rdm_info[item]['issue_type'] = common_info['issue_type']
            self.log_times_rdm_info[item]['project'] = common_info['project']
            self.log_times_rdm_info[item]['pic'] = item
            self.log_times_rdm_info[item]['details'] = '<b>1. log_path: </b>' + common_info['log_path'] + ';</br>' \
                                                       '<b>2. Log check结果详情</b>: log_path/log_check_result/main_log_times.csv 或 kernel_log_times.csv;</br>' \
                                                        "<b>3. 部分具体logs: </b>"+ "</br>".join(self.log_times[item])
            self.log_times_rdm_info[item]['module'] = common_info['module']
        for item in self.boot_error_log:
            self.boot_error_log_rdm_info.setdefault(item,{})
            self.boot_error_log_rdm_info[item]['image_path'] = common_info['image_path']
            self.boot_error_log_rdm_info[item]['log_path'] = common_info['log_path']
            self.boot_error_log_rdm_info[item]['summary'] = "[log check] Error log appears at boot stage"
            self.boot_error_log_rdm_info[item]['issue_type'] = common_info['issue_type']
            self.boot_error_log_rdm_info[item]['project'] = common_info['project']
            self.boot_error_log_rdm_info[item]['pic'] = item
            self.boot_error_log_rdm_info[item]['details'] = '<b>1. log_path: </b>' + common_info['log_path'] + ';</br>' \
                                                            '<b>2. Log check结果详情</b>: log_path/log_check_result/boot_errorlog.csv;</br>' \
                                                            "<b>3. 部分具体logs:</b> "+ "</br>\t".join(self.boot_error_log[item])
            self.boot_error_log_rdm_info[item]['module'] = common_info['module']
        for item in self.log_wrong_format:
            self.log_wrong_format_rdm_info.setdefault(item,{})
            self.log_wrong_format_rdm_info[item]['image_path'] = common_info['image_path']
            self.log_wrong_format_rdm_info[item]['log_path'] = common_info['log_path']
            self.log_wrong_format_rdm_info[item]['summary'] = "[log check] Error log or warning log format error "
            self.log_wrong_format_rdm_info[item]['issue_type'] = common_info['issue_type']
            self.log_wrong_format_rdm_info[item]['project'] = common_info['project']
            self.log_wrong_format_rdm_info[item]['pic'] = item
            self.log_wrong_format_rdm_info[item]['details'] = '<b>1. log_path: </b>' + common_info['log_path'] + ';</br>' \
                                                              '<b>2. Log check结果详情</b>: log_path/log_check_result/log_wrong_format.csv;</br>' \
                                                              "<b>3. 部分具体logs: </b>"+ "</br>".join(self.log_wrong_format[item])
            self.log_wrong_format_rdm_info[item]['module'] = common_info['module']
    
    def do_prepare(self, common_info, keywords_list = ['log_times', 'log_wrong_format', 'boot_error_log']):
        logging.info('do prepare rdm info=======================')
        try:
            self.read_csv(keywords_list)
            self.prepareInfo(common_info)
        except Exception as a:
            print("prepare rdm info exception")
        


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(message)s -----%(filename)s(line:%(lineno)d):%(asctime)s')
    path = "D:/2022task/Log_Checker_Code/test/log/log"
    keywords_list=['log_wrong_format', 'boot_errorlog']
    common_info = {
        'image_path' : "\\172.28.133.21\Release\Sync\AC8025\Cockpit\cockpit-trunk-s.linux.ac8025\cockpit_s_linux_ac8025\minibuild\cockpit-trunk-s.linux.ac8025-AB-2023-02-17-02-00_cypress",
        'log_path' : '\\atcfs02\Release\AtcAutomatedTest\cockpit_s_linux_ac8025\integrationtest\cockpit_s_linux_ac8025-2023-02-17-11-46-59',
        'project': "AC8025SW",
        'issue_type' :'Unit Test',
        'module' : 'watermark'
    }
    rc = CSVToRdmInfo(path, 60)
    rc.do_prepare(keywords_list, common_info)
    print(rc.log_wrong_format_rdm_info)
    print(rc.log_times_rdm_info)
    print(rc.boot_error_log_rdm_info)

    rdm = CommomAutoRDM(host = "http://rdm.autochips.inc:8080")
    if rc.log_wrong_format_rdm_info:
        issues_result = rdm.create_bug(rc.log_wrong_format_rdm_info)
        for result in issues_result:
            print(result)
    if rc.log_times_rdm_info:
        issues_result = rdm.create_bug(rc.log_times_rdm_info)
        for result in issues_result:
            print(result)
    if rc.boot_error_log_rdm_info:
        issues_result = rdm.create_bug(rc.boot_error_log_rdm_info)
        for result in issues_result:
            print(result)

        

    


