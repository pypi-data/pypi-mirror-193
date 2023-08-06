# logcheckerrdm 
## 1. Log_Checker
```python
from logcheckerrdm import Log_Checker
# 1st param : Log file path we want to analysis 
# 2nd param ：Project top word rank list
# 3rd param : top_rank_num, default is 50
# 4th param : Log of the 1st parameter to check whether it contains elements of key_word_list
# 5th param : log repetitions greater than line_num_threshold will be detected
Log_Checker("uart_log.txt", "top_50.txt", top_rank_num, key_word_list, line_num_threshold)
```
### A simple example
```python
path = "D:/2022task/Log_Checker_Code/test/log/log"
line_num_threshold = 20
key_word_list = [" e ","fail","error","exception"]
top_rank_num = 50
result_path = path + "/log_check.png"

lc = Log_Checker("uart_log.txt", "top.txt", top_rank_num, key_word_list, line_num_threshold)
lc.do_check()
lc.find_elog_at_boot(path+'/boot_log.txt', path)
uart_log_path= path + '/uart_log.txt'
lc.check_log_format(uart_log_path,path)
lc.gen_result(result_path)
if (os.path.exists(path)):
    lc.check_duration_warn_log(path, path)
    lc.check_log_times(path, float('inf'), int(line_num_threshold), path, ['main', 'adas', 'cluster', 'kernel'])
```

## 2. Log_Checker
```python
from logcheckerrdm import ReadCSV
```

## 3. CommomAutoRDM
```python
from logcheckerrdm import CommomAutoRDM
# default_requst_info = {
#     'host'         : 'http://172.28.133.217:8080',
#     'login_url'    : '/user/login.wbs',
#     'bug_url'      : '/startbug',
#     'get_user_url' : '/user/get.wbs',
#     'user_name'    : 'QAAuto',
#     'password'     : 'zxcv!1234',
#     'default_account' : 'ATC0274',
#     'public_account'  : 'ci_build' 
# }
rdm = CommonAutoRDM(default_requst_info)
#input  : issues 
#output : issues_result[bug_num, bug_id, module, pic]
#   issues:{
#         'image_path':,   
#         'log_path':, 
#         'summary': ,     # eg,unit test fail
#         'issue_type': ,  # Unit Test
#         'project':       # AC8025SW
#         'pic':,
#         'details':       # eg:watermarkwrapper.cpp line34 failed
#         'module':        # only for yourself, could be ""
#   }
rdm.create_bug(issues)
```
### A simple example
```python
path = "D:/2022task/Log_Checker_Code/test/log/log"
keywords_list=['log_wrong_format', 'boot_errorlog', 'log_times']
common_info = {
    'image_path' : "\\172.28.133.21\Release\Sync\AC8025\Cockpit\cockpit-trunk-s.linux.ac8025\cockpit_s_linux_ac8025\minibuild\cockpit-trunk-s.linux.ac8025-AB-2023-02-17-02-00_cypress",
    'log_path' : '\\atcfs02\Release\AtcAutomatedTest\cockpit_s_linux_ac8025\integrationtest\cockpit_s_linux_ac8025-2023-02-17-11-46-59',
    'project': "AC8025SW",
    'issue_type' :'Unit Test',
    'module' : 'watermark'
}
rc = ReadCSV(path, 60)
rc.do_prepare(keywords_list, common_info)

rdm = CommomAutoRDM()
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
```


