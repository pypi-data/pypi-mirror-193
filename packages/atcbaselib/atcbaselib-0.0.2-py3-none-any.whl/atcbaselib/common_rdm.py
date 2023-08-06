import logging
import requests
import pdb

#host = 'http://172.28.133.217:8080'  # test server
#host = 'http://rdm.autochips.inc:8080'
default_requst_info = {
    'login_url'    : '/user/login.wbs',
    'bug_url'      : '/startbug',
    'get_user_url' : '/user/get.wbs',
    'user_name'    : 'QAAuto',
    'password'     : 'zxcv!1234',
    'public_account'  : 'ci_build' 
}
class CommomAutoRDM():
    def __init__(self, request_info = default_requst_info, host = "http://172.28.133.217:8080", default_account = 'ATC0274'):
        self.host            = host
        self.default_account = default_account
        self.login_url       = request_info['login_url']
        self.bug_url         = request_info['bug_url']
        self.get_user_url    = request_info['get_user_url']
        self.user_name       = request_info['user_name']
        self.password        = request_info['password']
        self.public_account  = request_info['public_account']
        self.token = self.get_access_token()
        self.all_user_info = self.get_all_users_info()

    def get_all_users_info(self):
        url = "{}{}?token={}".format(self.host,  self.get_user_url, self.token)
        r = requests.request('GET', url)

        if 'error' in r.text:
            logging.error("get all users info fail : " + str(r.text))
            return None
        else:
            json_data = r.json()
            return json_data['User']

    def get_user_code_by_name(self, name):
        if self.all_user_info is not None:
            for info in self.all_user_info:
                if name.lower() in info["Email"].lower():
                    return info['Num']
        return self.default_account

    def get_access_token(self):
        url = "{}{}?userName={}&password={}".format(self.host, self.login_url, self.user_name, self.password)
        r = requests.request('GET', url)
        return r.text.rstrip()

    def get_project_key(self, project):
        if 'r.ac8015' in project:
            return 'AC8015R'
        elif 'p.ac8015' in project:
            return 'AC8015P'
        else:
            return 'AC8025SW'

    #input  : info包含的Key为 common_info 和 issues 
    #output : bug_num, bug_id, module和pic
    #   issues:{
    #         'image_path':,   
    #         'log_path':, 
    #         'summary': ,     # eg,unit test fail
    #         'issue_type': ,  # Unit Test
    #         'project':       # AC8025SW
    #         'pic':,
    #         'details':
    #         'module':
    #   }
    #
    #  description:
    #              log_path : test_log_path
    #              details  : issue['detail'] eg:watermarkwrapper.cpp line34 failed
    def create_bug(self, issues):
        logging.info('create rdm bug=======================')
        url = "{}{}".format(self.host, self.bug_url)
        issues_results = []

        for item in issues:
            body ={
                "token": self.token,
                "entity": {
                    "CreateCode": self.public_account,  # 创建人工号，必填
                    "OwnerCode": self.get_user_code_by_name(issues[item]['pic']),  # 责任人工号，必填
                    "ProjectCode": issues[item]['project'],  # 项目编号，必填
                    "Summary": issues[item]['summary'],
                    "IssueType": issues[item]['issue_type'],
                    "Platform": "Demo",
                    "Source": "RD",
                    "Project_Model": issues[item]['project'],
                    "Priority": "Medium",
                    "Severity": "Normal",
                    "Repeat_Steps": "No Repeat Steps",
                    "PICCode": self.get_user_code_by_name(issues[item]['pic']),
                    "SW_Version": issues[item]['image_path'],
                    "Expected_Due_Date": "",
                    "Description": issues[item]['details'],
                    "Repeat_Ratio": "Always",
                    "Bug_Category": "None"
                }
            }
            r = requests.request(method='post', url=url, json=body)
            logging.info('pic:' + issues[item]['pic'] +" rdm json:" + str(r.json()))
            if ('OK' in r.json()['Msg']):
                issue_msg = r.json()['BugCode']
                issue_id = r.json()['ObjectId']
            else:
                issue_msg = r.json()['Msg']
                issue_id = r.json()['ObjectId']
            result = {}
            result['pic'] = issues[item]['pic']
            result['bug_number'] = issue_msg
            result['bug_id'] = issue_id
            issues_results.append(result)
        return issues_results