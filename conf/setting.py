import os

'''
    配置文件,定义相关变量
'''

# 根路径，上上一级目录的绝对路径
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
# 接口的地址
BASE_URL = 'http://118.24.3.40'
# 日志的文件名
LOG_NAME = 'utp.log'

# 邮件相关参数
MAIL_HOST = 'smtp.163.com'
MAIL_USER = 'uitestp4p@163.com'
MAIL_PASSWRD = 'houyafan123'
TO = [
    '511402865@qq.com',
]
# 日志级别
LEVEL = 'debug'

LOG_PATH = os.path.join(BASE_PATH, 'logs')                  # 存放日志的路径
CASE_PATH = os.path.join(BASE_PATH, 'cases')                # 存放用例的路径
YAML_PATH = os.path.join(BASE_PATH, 'case_data')            # 存放yaml文件的路径
CASE_TEMPLATE = os.path.join(BASE_PATH, 'conf', 'base.txt') # 用例模板的路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')             # 存放报告的目录


