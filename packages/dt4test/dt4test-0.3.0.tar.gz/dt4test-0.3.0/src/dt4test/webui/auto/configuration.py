# -*- coding: utf-8 -*-

__author__ = "mawentao119@gmail.com"

import shutil
import sys

"""
Init the App
init Admin and DemoProject
"""

import os
import getpass
from utils.dbclass import TestDB
from utils.mylogger import getlogger

from utils.time_server.scheduler_data import TimeServerData
from utils.time_server.checkrules import CheckRules
from utils.time_server.serviceinterface import ServiceProxy

log = getlogger(__name__)

class Config:

    SSL_REDIRECT = False

    SECRET_KEY = 'QWERTYUIOPASDFGHJ'
    SHOW_DIR_DETAIL = False

    APP_DIR = os.path.abspath(os.environ["PROJECT_DIR"])   # Should be ${PROJECT_DIR} dir
    COMMON_DIR = os.path.join(APP_DIR, "common")
    OUTPUT_DIR = os.path.join(APP_DIR, "output")
    #WEBUI_DIR = os.path.join(COMMON_DIR, "webui")
    WEBUI_DIR = os.path.join(os.path.abspath(__file__), '../../../webui')


    AUTO_HOME = os.path.join(APP_DIR, "output/.works")
    DB_DIR    = os.path.join(AUTO_HOME, "DBs")
    SPACE_DIR = os.path.join(AUTO_HOME, "workspace")
    AUTO_TEMP = os.path.join(AUTO_HOME, "runtime")
    API_RUN_DIR = OUTPUT_DIR                             # api 执行输出目录

    USER_NAME = getpass.getuser()

    CASE_TEMPLATE_DIR = os.path.join(WEBUI_DIR, 'auto/www/templates/case_template')

    os.makedirs(AUTO_HOME) if not os.path.exists(AUTO_HOME) else None
    os.mkdir(DB_DIR) if not os.path.exists(DB_DIR) else None
    os.mkdir(SPACE_DIR) if not os.path.exists(SPACE_DIR) else None
    os.mkdir(AUTO_TEMP) if not os.path.exists(AUTO_TEMP) else None
    os.mkdir(API_RUN_DIR) if not os.path.exists(API_RUN_DIR) else None

    #os.environ["PROJECT_DIR"] = APP_DIR      # ** 这个可以和外面的 ${PROJECT_DIR} 一致
    os.environ["AUTO_HOME"] = AUTO_HOME
    os.environ["SPACE_DIR"] = SPACE_DIR
    os.environ["AUTO_TEMP"] = AUTO_TEMP
    os.environ["API_RUN_DIR"] = API_RUN_DIR
    os.environ["OUTPUT_DIR"] = OUTPUT_DIR
    os.environ["USER_NAME"] = USER_NAME
    os.environ["CASE_TEMPLATE_DIR"] = CASE_TEMPLATE_DIR

    PROJECT_DIR = APP_DIR
    PROJECT_NAME = os.path.basename(APP_DIR)
    os.environ["ROBOT_DIR"] = PROJECT_DIR
    # os.environ["PROJECT_DIR"] = PROJECT_DIR
    os.environ["PROJECT_NAME"] = PROJECT_NAME

    log.info("初始化数据库...")
    DB = TestDB(AUTO_HOME)

    os.environ["DB_FILE"] = DB.get_dbfile()

    os.environ["BF_RESOURCE"]  = os.path.join(APP_DIR, 'utils/case_resource')
    os.environ["BF_RESOURCES"] = os.path.join(APP_DIR, 'utils/case_resource')
    os.environ["PY_TEMPLATE"]  = os.path.join(APP_DIR, 'utils/case_template')
    os.environ["PY_TEMPLATES"] = os.path.join(APP_DIR, 'utils/case_template')
    os.environ["CS_TEMPLATES"] = os.path.join(APP_DIR, 'auto/www/templates/case_template')

    log.info("设置环境变量：")
    log.info("PROJECT_DIR:{}\nAUTO_HOME:{}".format(PROJECT_DIR, AUTO_HOME))

    sys.path.append(os.path.join(APP_DIR, 'utils/case_resource'))

    ############################ Added for CIA system ###########################################
    TOPOLOGY = {}
    COMMANDS = {}
    SUBCOMMANDS = {}
    COMMAND_TYPES = ["cmd", "ufile", "cfile", "dfile", "dfile_c", "dfile_a", "ufile_c","ufile_a", "getlog"]
    AGENT_INTERVAL = 3
    #############################################################################################

    ############################ Added for Scheduler system #####################################
    log.info("创建 Scheduler Data 对象：SD")
    SD = TimeServerData()    # SD short for Scheduler Data
    log.info("创建 Check Rules 对象：CR")
    CR = CheckRules(SD)    # CR Short for Check Rules
    log.info("创建 Service Porxy 对象: SV")
    SV = ServiceProxy(SD)
    #############################################################################################

    AUTO_ROBOT = [] # Process list of running tasks, only for hand running ,not for schceduled jobs. MAX: setting:MAX_PROCS

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_TIMEZONE = "Asia/Shanghai"

    SCHEDULER_API_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # 发送服务启动初始化时错误信息给管理员： Send Error info to Admin
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()

        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' AutoLine Startup Error',
            credentials=credentials,
            secure=secure)

        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
