# -*- utf-8 -*-
import sqlite3 as db
import os
import shutil
from datetime import datetime, date

# TODO DELETE from robot.api import TestData
from robot.api import TestSuiteBuilder
from robot.errors import DataError
from utils.mylogger import getlogger

log = getlogger(__name__)

class DBcli():
    def __init__(self, dbfile):
        self.DBcon = db.connect(
            dbfile, isolation_level=None, check_same_thread=False)
        self.DBcor = self.DBcon.cursor()

    def runsql(self, sql):
        log.info("DBCLI:"+sql)
        try:
            res = self.DBcor.execute(sql)
            self.DBcon.commit()
        except Exception as e:
            log.error("异常:{}".format(e))
            return None
        return res

    def insert_loginfo(self, user, target, action, key, result=''):
        sql = ''' INSERT INTO loginfo(user,target,action,key,result) 
                  VALUES('{}','{}','{}','{}','{}');'''.format(user, target, action, key, result)

        return self.runsql(sql)

    def insert_monitor(self,task_no, ip, monitor_item, time_now, value, info):
        sql = ''' INSERT INTO monitor(task_no, ip, monitor_item, time_now, value, info) 
                          VALUES('{}','{}','{}','{}','{}','{}');'''.format(task_no, ip, monitor_item, time_now, value, info)
        return self.runsql(sql)

    def get_casestatus(self, info_key, info_name):
        """
        duplictate function of TestDB
        :param info_key:
        :param info_name:
        :return:
        """
        sql = "select run_status,info_name from testcase where info_key='{}' and info_name ='{}'; ".format(
            info_key, info_name)
        res = self.runsql(sql)
        if not res:
            return 'unknown'
        (status, name) = res.fetchone()
        return status

class TestDB():
    def __init__(self, confdir):
        # Init system TestDBID with file TestCaseDB.id if exists, Create new if not exists.

        self.DBID = '0'
        self.DBcon = None
        self.DBcor = None

        self.confdir = confdir
        self.dbpath = os.path.join(self.confdir, 'DBs')
        self.refresh_interval = 180  # seconds
        self.refresh_time = self.get_timenow()
        self.DBIDFileName = 'TestCaseDB.id'
        self.DBIDFile = os.path.join(self.dbpath, self.DBIDFileName)
        self.DBFileName = ''
        self.IsNewDBID = False

        self.project_dir = ""
        self.project_name = ""

        log.info("检查项目信息是否完备 ...")
        self.check_project_info(self.confdir)
        log.info("将项目的模版拷贝到平台 ...")
        self.copy_project_templates()

        log.info("初始化数据库，系统目录：{}".format(confdir))
        log.info("检查DBID文件是否存在:" + self.DBIDFile)
        if os.path.exists(self.DBIDFile):
            with open(self.DBIDFile, 'r') as f:
                self.DBID = f.readline().strip()
                log.info("读取 DBID from " + self.DBIDFile + ": "+self.DBID)
        else:
            self.DBID = self.get_timenow()
            self.IsNewDBID = True
            with open(self.DBIDFile, 'w') as f:
                f.write(self.DBID)
                log.info("创建新 ID: " + self.DBID)

        self.DBFileName = os.path.join(self.dbpath, self.DBID+'.db')

        if not os.path.exists(self.DBFileName):
            log.warning("ID文件:" + self.DBIDFile +
                        " with DBID:" + self.DBID + " 找不到.db文件!")
            log.warning("创建新到 DB file ... ")
            self.IsNewDBID = True

        # init DB
        self.DBcon = db.connect(
            self.DBFileName, isolation_level=None, check_same_thread=False)
        self.DBcor = self.DBcon.cursor()

        # if NewDBID , Create Table
        if self.IsNewDBID:
            log.info("新DB文件, 建表及初始化 ...")

            self.createtb_testcase()
            self.createtb_loginfo()

            self.createtb_user()
            self.init_user()
            self.createtb_project()
            self.init_project()

            self.createtb_schedule_job()
            self.createtb_monitor()

            self.createtb_settings()
            self.init_settings()

            self.createtb_caserecord()

            self.refresh_caseinfo(self.project_dir, mode='force')
            #workspace = os.path.join(self.confdir, 'workspace')
            #self.load_user_and_project(workspace)

    def check_project_info(self, workdir):
        project_dir = os.environ["PROJECT_DIR"]
        if not os.path.exists(project_dir):
            log.error("无法找到目录: {}".format(project_dir))
            exit(1)
        self.project_name = os.environ["PROJECT_NAME"]
        self.project_dir = project_dir
        log.info("取得项目路径:{}".format(self.project_dir))

    def copy_project_templates(self):
        '''Copy templates to Platform dirs ...'''
        user_templates_dir = os.path.join(self.project_dir, "TEMPLATES")
        log.info("查找模版目录：{}".format(user_templates_dir))
        if os.path.exists(user_templates_dir):
            app_dir = os.path.join(user_templates_dir, '../../../')
            for t in os.listdir(user_templates_dir):
                if not os.path.isdir(os.path.join(user_templates_dir, t)):
                    continue

                log.info(">>> 发现模版，开始拷贝 {}".format(t))
                for tf in os.listdir(os.path.join(user_templates_dir, t)):
                    if os.path.splitext(tf)[1] == '.html' or os.path.splitext(tf)[1] == '.tplt':
                        src = os.path.join(user_templates_dir, t, tf)
                        des = os.path.join(app_dir, 'auto/www/templates/case_template', tf)
                        shutil.copy(src, des)
                    if os.path.splitext(tf)[1] == '.py':
                        src = os.path.join(user_templates_dir, t, tf)
                        des = os.path.join(app_dir, 'utils/case_template', tf)
                        shutil.copy(src, des)
        else:
            log.info(">>> 没有发现模版目录：{}".format(user_templates_dir))

    # TODO: DELETE
    def load_project_from_path(self, project_path):
        log.info("加载项目 path: {}".format(project_path))

        userfile = os.path.join(project_path, 'platforminterface/user.conf')
        log.info("读取用户文件: {}".format(userfile))
        if os.path.exists(userfile):
            with open(userfile, 'r') as f:
                for l in f:
                    if l.startswith('#'):
                        continue
                    if len(l.strip()) == 0:
                        continue
                    splits = l.strip().split('|')  # user.conf using '|' as splitor
                    if len(splits) != 6:
                        log.error("错误行：" + l)
                    (username, fullname, password, email,
                     category, main_project) = splits
                    log.info("新增用户: {}".format(username))
                    self.add_user(username, fullname, password,
                                  email, category, main_project)
        else:
            msg = "加载用户失败: 找不到 user.conf:{} ".format(userfile)
            log.error(msg)
            return msg

        projectfile = os.path.join(
            project_path, 'platforminterface/project.conf')
        log.info("读取项目配置文件: {}".format(projectfile))
        if os.path.exists(projectfile):
            with open(projectfile, 'r') as f:
                for l in f:
                    if l.startswith('#'):
                        continue
                    if len(l.strip()) == 0:
                        continue
                    splits = l.strip().split('|')
                    if len(splits) != 4:
                        log.error("错误行：" + l)
                    (projectname, owner, users, cron) = splits
                    log.info("创建项目，owner:{}".format(owner))
                    self.add_project(projectname, owner, users)
                    self.refresh_caseinfo(project_path, mode='force')
        else:
            msg = "加载项目失败: 找不到 project.conf:{} ".format(projectfile)
            log.error(msg)
            return msg

        return "加载项目成功"

    def get_project_name(self):
        return self.project_name

    def get_project_dir(self):
        return self.project_dir

    def get_id(self):
        return self.DBID

    def get_dbfile(self):
        return self.DBFileName

    # datetime like: 20190112091212
    def get_timenow(self):
        return date.strftime(datetime.now(), '%Y%m%d%H%M%S')

    def _reset_refreshtime(self):
        self.refresh_time = self.get_timenow()
        log.info("重置数据库刷新时间 to :"+self.refresh_time)

    def runsql(self, sql):
        log.info("RUNSQL:"+sql)
        try:
            res = self.DBcor.execute(sql)
            self.DBcon.commit()
        except Exception as e:
            log.error("异常:{}".format(e))
            return None
        return res

    def createtb_schedule_job(self):
        self.runsql('''create table schedule_job(
                       user    TEXT DEFAULT 'userORip',
                       project TEXT DEFAULT 'item',
                       task_no   TEXT DEFAULT 'task_no',
                       task_name    TEXT DEFAULT 'script',
                       method    TEXT DEFAULT '',
                       schedule_type TEXT DEFAULT '',
                       year   TEXT DEFAULT '',
                       mon    TEXT DEFAULT '',
                       day   TEXT DEFAULT '',
                       hour    TEXT DEFAULT '',
                       min   TEXT DEFAULT '',
                       sec    TEXT DEFAULT '',
                       week   TEXT DEFAULT '',
                       day_of_week    TEXT DEFAULT '',
                       start_date    TEXT DEFAULT '',
                       end_date    TEXT DEFAULT '',
                       sponsor TEXT DEFAULT 'unknown',
                       primary key (user,project,task_no)  
                       );''')

    def add_chedulejob(self, args):
        return self.runsql('''INSERT INTO schedule_job values(
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');
        '''.format(args['user'], args['project'], args['task_no'], args['task_name'], args['method'], args['schedule_type'],
                   args['year'], args['mon'], args['day'], args['hour'], args['min'], args['sec'], args['week'],
                   args['day_of_week'], args['start_date'], args['end_date'], args['sponsor']))

    def createtb_monitor(self):
        self.runsql('''create table monitor(
        task_no TEXT, ip TEXT, monitor_item TEXT, time_now TEXT, value TEXT, info TEXT
        );''')

    def createtb_settings(self):
        self.runsql('''create table settings(
               description TEXT,
               item TEXT UNIQUE,
               value   TEXT DEFAULT '',
               demo    TEXT DEFAULT '',
               category TEXT DEFAULT 'unknown'
               );''')

    def init_settings(self):
        self.runsql(''' DELETE FROM settings;''')
        self.runsql(
            '''INSERT INTO settings values('被测系统名称','test_project',"TBDS",'Do not modify twice.','user');''')
        self.runsql(
            '''INSERT INTO settings values('被测系统版本号','test_projectversion',"V5013",'Do not modify twice.','user');''')
        self.runsql(
            '''INSERT INTO settings values('测试用例历史记录git','history_git',"https://github.com/mawentao119/testcasehistory.git",'暂不支持commit','user');''')
        self.runsql(
            '''INSERT INTO settings values('机器列表文件','test_env_machines',"runtime/test_env_machines.conf",'ip|os|cpus|mem|ontime','user');''')
        self.runsql(
            '''INSERT INTO settings values('组件列表文件','test_env_modules',"runtime/test_env_modules.conf",'name|machines|status|ontime','user');''')
        self.runsql(
            '''INSERT INTO settings values('自动化配置文件','test_env_conf',"runtime/env.conf",'建议自动化配置项自动生成','user');''')
        self.runsql(
            '''INSERT INTO settings values('系统说明文件(ReadMe)','project_readme',"runtime/ReadMe.md",'建议自动化配置项自动生成','user');''')
        self.runsql(
            '''INSERT INTO settings values('最大任务并发数','MAX_PROCS',"20",'只限制手工并发数','system');''')

    def init_project_settings(self, key):
        log.info("Load Settings from dir: {}".format(key))

        settings_file = os.path.join(key, 'platforminterface/settings.conf')
        log.info("Read Settings file: {}".format(settings_file))
        if os.path.exists(settings_file):
            self.runsql(''' DELETE FROM settings;''')
            with open(settings_file, 'r') as f:
                for l in f:
                    if l.startswith('#'):
                        continue
                    if len(l.strip()) == 0:
                        continue
                    splits = l.strip().split('#')  # settings.conf using '#' as splitor
                    if len(splits) != 5:
                        log.error("错误行:" + l)
                    (description, item, value, demo, category) = splits
                    self.runsql(''' INSERT INTO settings values('{}','{}','{}','{}','{}');'''.format(
                        description, item, value, demo, category))
            return "Operation Success."
        else:
            msg = "找不到文件 settings.conf for project:{}".format(key)
            log.error(msg)
            return msg

    def add_setting(self, description, item, value, demo):

        return self.runsql("INSERT INTO settings values('{}','{}','{}','{}','system'); ".format(description, item, value, demo))

    def del_setting(self, item):

        return self.runsql("DELETE FROM settings WHERE item='{}'; ".format(item))

    def get_setting(self, item):

        sql = "SELECT item, value from settings WHERE item='{}'; ".format(
            item)
        res = self.runsql(sql)
        try:
            (item, value) = res.fetchone()
        except Exception as e:
            log.warn("找不到配置项：{}".format(item))
            return 'unknown'
        return value

    def createtb_user(self):
        self.runsql('''create table user(
               username TEXT UNIQUE,
               fullname TEXT,
               passwordHash   TEXT,
               email    TEXT,
               category TEXT DEFAULT 'user',
               main_project TEXT DEFAULT ''
               );''')

    def init_user(self):
        admin_pass = "pbkdf2:sha256:50000$fHCEAiyw$768c4f2ba9cabbc77513b9a25ffea1a19a77c23d8dab86e635d5f62f6fb8be6b"
        if os.path.exists( os.path.join(self.project_dir, 'AdminPass')):
            with open(os.path.join(self.project_dir , 'AdminPass'), 'r') as pf:
                admin_pass = pf.readline().strip()

        sql = '''
        INSERT INTO user 
        values('Admin','admin',"{}",'charisma@tencent.com','Admin','{}');
        '''.format(admin_pass, self.project_name)
        self.runsql(sql)

    def _case_exists(self, info_key, info_name):
        try:
            sql = "select info_key,info_name from testcase where info_key='{}' and info_name ='{}'; ".format(
                info_key, info_name)
            res = self.runsql(sql)
            (key, name) = res.fetchone()
            return True
        except TypeError:
            return False

    def set_casestatus(self, info_key, info_name, status, runuser):

        sql = '''UPDATE testcase SET ontime=datetime('now','localtime'),
                                     run_status='{}',
                                     run_user='{}',
                                     rcd_handtime=datetime('now','localtime')
                 WHERE info_key='{}' and info_name='{}'; 
                 '''.format(status, runuser, info_key, info_name)
        return self.runsql(sql)

    def set_suitestatus(self, info_key, status, runuser):

        sql = '''UPDATE testcase SET ontime=datetime('now','localtime'),
                                     run_status='{}',
                                     run_user='{}',
                                     rcd_handtime=datetime('now','localtime')
                 WHERE info_key='{}'; 
                 '''.format(status, runuser, info_key)
        return self.runsql(sql)

    def get_casestatus(self, info_key, info_name):

        sql = "select run_status,info_name from testcase where info_key='{}' and info_name ='{}'; ".format(
            info_key, info_name)
        res = self.runsql(sql)
        if not res:
            return 'unknown'
        (status, name) = res.fetchone()
        return status

    def get_suitestatus(self, info_key):

        ss = []
        sql = "select run_status,info_name from testcase where info_key='{}'; ".format(
            info_key)
        res = self.runsql(sql)
        if not res:
            return 'unknown'
        for i in res:
            (status, name) = i
            ss.append(status)
        if 'unknown' in ss or len(ss) == 0:
            return 'unknown'
        if 'FAIL' in ss:
            return 'FAIL'
        return 'PASS'

    def get_password(self, username):

        res = self.runsql(
            "select username,passwordHash from user where username='{}'; ".format(username))
        if not res:
            return None

        for r in res:
            (name, passwd) = r
            return passwd

        return None

    # TODO: DELETE
    def del_user(self, username):
        if username == 'Admin' or username == 'admin':
            return True
        self.runsql("Delete from user where username = '{}' ;".format(username))
        return True

    # TODO: DELETE
    def set_user_main_project(self, user, project):
        log.info(
            "Set user main_project: user {} ,main_project : {} ".format(user, project))
        return self.runsql("Update user set main_project='{}' where username='{}' ; ".format(project, user))

    # TODO: DELETE
    def get_user_main_project(self, user):
        res = self.runsql(
            "SELECT main_project, username from user where username='{}' ;".format(user))
        if res:
            (c, u) = res.fetchone()
            return c
        else:
            return ""

    # TODO: DELETE
    def add_user(self, username, fullname, passwordHash, email, category='User', main_project=''):
        return self.runsql("INSERT INTO user values('{}','{}','{}','{}','{}','{}'); ".format(username, fullname, passwordHash, email, category, main_project))

    def createtb_project(self):
        self.runsql('''create table project(
               projectname TEXT,
               owner TEXT,
               users TEXT DEFAULT 'myself',
               cron  TEXT DEFAULT '* * * * * *',
               primary key (projectname)
               );''')

    def init_project(self):
        sql = '''
        INSERT INTO project(projectname,owner,users) VALUES('{}','Admin','all');
        '''.format(self.project_name)
        self.runsql(sql)

    # TODO: DELETE
    def add_project(self, projectname, owner, users):
        return self.runsql("INSERT INTO project(projectname,owner,users) VALUES('{}','{}','{}');".format(
            projectname, owner, users))

    # TODO: DELETE
    def edit_project(self, pname, newname, owner):
        return self.runsql("Update project set projectname = '{}' where projectname = '{}' and owner = '{}' ;".format(
            newname, pname, owner))

    # TODO: DELETE
    def add_projectuser(self, project, newuser):
        users = []
        user = []
        res = self.runsql(
            "SELECT users FROM project WHERE projectname='{}' ;".format(project))
        for u in res:
            (us,) = u
            users.append(us)
        if len(users) > 0:
            user = users[0].split(',')
        user.append(newuser)
        user = list(set(user))
        user_str = ','.join(user)

        sql = "UPDATE project set users='{}' WHERE projectname='{}' ;".format(
            user_str, project)
        return self.runsql(sql)

    # TODO: DELETE
    def del_projectuser(self, project, newuser):
        users = []
        user = []
        res = self.runsql(
            "SELECT users FROM project WHERE projectname='{}' ;".format(project))
        for u in res:
            (us,) = u
            users.append(us)
        if len(users) > 0:
            user = users[0].split(',')
        user.remove(newuser) if newuser in user else None
        user = list(set(user))
        user_str = ','.join(user)

        sql = "UPDATE project set users='{}' WHERE projectname='{}' ;".format(
            user_str, project)
        return self.runsql(sql)

    # TODO: DELETE
    def get_ownproject(self, username):

        res = self.runsql(
            "select projectname from project where owner = '{}';".format(username))
        projects = []
        for i in res:
            (p,) = i
            projects.append(p)

        return projects

    # TODO: DELETE
    def get_projectowner(self, project):

        try:
            res = self.runsql(
                "select owner,projectname from project where projectname = '{}';".format(project))
            (owner, project) = res.fetchone()
        except Exception as e:
            return "unknown"

        return owner

    # TODO: DELETE
    def get_othproject(self, username):
        res = self.runsql("select projectname,users from project;")
        projects = []
        for i in res:
            (p, u) = i
            us = u.split(',')
            if username in us:
                projects.append(p)

        return projects

    # TODO: DELETE
    def get_allproject(self, username):
        all = [self.project_name]
        # res = self.runsql("select owner,projectname,users from project ;")
        # for i in res:
        #     (o, p, u) = i
        #     if username == 'Admin':
        #         all.append("{}:{}".format(o, p))
        #         continue
        #     if o == username:
        #         all.append("{}:{}".format(o, p))
        #     us = u.split(',')
        #     if username in us or 'all' in us:
        #         all.append("{}:{}".format(o, p))
        #
        # all = list(set(all))    # delete the same values
        # all.sort()              # order , TODO order by category

        return all

    # TODO: DELETE
    def get_projectusers(self, project):
        all = []
        isforall = False
        res = self.runsql(
            "select owner,users from project where projectname = '{}' ;".format(project))
        for i in res:
            (o, u) = i
            all.append(o)
            us = u.split(',')
            for uu in us:
                if uu == 'all':
                    isforall = True
                else:
                    all.append(uu)

        if isforall:
            res = self.runsql("select username from user;")
            for r in res:
                (u,) = r
                all.append(u)

        all = list(set(all))    # delete the same values
        all.sort()              # order , TODO order by category
        return all

    # TODO: DELETE
    def del_project(self, projectname, owner):
        return self.runsql("Delete from project where projectname = '{}' and owner = '{}' ;".format(projectname, owner))

    def createtb_testcase(self):
        '''
        保存测试用例
        :return:
        '''
        return self.runsql('''create table testcase(
                       info_key TEXT,
                       info_name TEXT,
                       info_casecontent TEXT DEFAULT '',
                       info_doc TEXT DEFAULT '',
                       info_tags TEXT DEFAULT '',
                       ontime TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                       run_status TEXT DEFAULT 'unknown',
                       run_user TEXT,
                       run_elapsedtime INTEGER DEFAULT 0,
                       run_starttime TEXT,
                       run_endtime TEXT,
                       rcd_handtime TIMESTAMP DEFAULT 0,
                       rcd_runtimes INTEGER DEFAULT 0,
                       rcd_successtimes INTEGER DEFAULT 0,
                       rcd_failtimes INTEGER DEFAULT 0,
                       rcd_runusers TEXT,
                       primary key (info_key,info_name)                       
                ); ''')

    def createtb_caserecord(self):
        '''
        用于用例的历史结果比对
        :return:
        '''
        return self.runsql('''create table caserecord(
                       info_key TEXT,
                       info_name TEXT,
                       info_testproject TEXT DEFAULT '',
                       info_projectversion TEXT DEFAULT '',
                       ontime TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                       run_status TEXT DEFAULT 'unknown',
                       run_elapsedtime INTEGER DEFAULT 0,
                       run_user TEXT,
                       primary key (info_key,info_name,ontime)                       
                ); ''')

    def save_caserecord(self, info_key, info_name):

        testproject = self.get_setting('test_project')
        projectversion = self.get_setting('test_projectversion')

        sql = '''INSERT into caserecord (info_key,info_name,info_testproject,info_projectversion,ontime,run_status,run_elapsedtime,run_user)
                 SELECT                  info_key,info_name,'{}',            '{}',               ontime,run_status,run_elapsedtime,run_user
                 FROM        testcase
                 WHERE info_key='{}' and info_name='{}'; 
                 '''.format(testproject, projectversion, info_key, info_name)
        return self.runsql(sql)

    def save_caserecord_d(self, info_key):

        testproject = self.get_setting('test_project')
        projectversion = self.get_setting('test_projectversion')

        sql = '''INSERT into caserecord (info_key,info_name,info_testproject,info_projectversion,ontime,run_status,run_elapsedtime,run_user)
                 SELECT                  info_key,info_name,'{}',            '{}',               ontime,run_status,run_elapsedtime,run_user
                 FROM        testcase
                 WHERE info_key like '{}%' ; 
                 '''.format(testproject, projectversion, info_key)
        return self.runsql(sql)

    def createtb_loginfo(self):
        '''
        保存所有执行日志，用于统计报表和审计
        :return:
        '''
        self.runsql(''' CREATE TABLE loginfo(
                       logtime TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                       user TEXT DEFAULT '',
                       target TEXT DEFAULT '',
                       action  TEXT DEFAULT '',
                       key TEXT DEFAULT '',
                       result  TEXT DEFAULT ''
                );''')

    def insert_loginfo(self, user, target, action, key, result=''):
        sql = ''' INSERT INTO loginfo(user,target,action,key,result) 
                  VALUES('{}','{}','{}','{}','{}');'''.format(user, target, action, key, result)

        return self.runsql(sql)

    def delete_suite(self, info_key):
        return self.runsql("Delete from testcase where info_key like '{}%' ;".format(info_key))

    def refresh_caseinfo(self, target, mode='normal'):
        if os.path.isdir(target):
            old = self.refresh_time
            now = self.get_timenow()

            if int(now) - int(old) < self.refresh_interval and mode == "normal":
                log.info("Do not reach the refresh time of {}s : {} ".format(
                    self.refresh_interval, target))
                return False

        log.info("Start refresh cases:"+target)

        try:
            suite = TestSuiteBuilder().build(target)
            self._refresh_rfcase(suite, mode)
        except DataError:
            log.info("没有发现 robot 用例，继续更新pytest")

        self._refresh_pycase(target, mode)

        if os.path.isdir(target):
            self._reset_refreshtime()

        return True

    def _refresh_rfcase(self, suite, mode='normal'):
        source = suite.source

        suite_cases = []

        # update each robot file

        sql = "select info_key,info_name from testcase where info_key='{}'; ".format(
            source)
        res = self.runsql(sql)
        for i in res:
            (k, n) = i
            suite_cases.append([k, n])

        # add new case
        for test in suite.tests:
            info_key = test.source
            info_name = test.name

            tags = ",".join(test.tags)
            doc = test.doc

            if [info_key, info_name] in suite_cases:
                suite_cases.remove([info_key, info_name])
                sql = '''UPDATE testcase set info_tags='{}', 
                                             info_doc='{}' 
                         WHERE info_key='{}' and info_name='{}';'''.format(tags, doc, info_key, info_name)
                self.runsql(sql)
            else:

                sql = "insert into testcase(info_key,info_name,info_tags, info_doc) \
                values('{}','{}','{}','{}');".format(info_key, info_name, tags, doc)
                res = self.runsql(sql)
                if not res:
                    log.error("Insert testcase Fail:{}".format(e))

                if not mode == 'start':
                    self.insert_loginfo('unknown', 'case',
                                        'create', info_key, info_name)



        # deleted cases and renamed cases should be deleted
        for i in suite_cases:
            if i[0].endswith('.robot'):
                sql = "delete from testcase where info_key ='{}' and info_name='{}';".format(
                  i[0], i[1])
                self.runsql(sql)

                if not mode == 'start':
                    self.insert_loginfo('unknown', 'case', 'delete', i[0], i[1])

        for child in suite.suites:
            self._refresh_rfcase(child, mode)

    def _refresh_pycase(self, target, mode):

        suite_cases = []

        # update each robot file

        sql = "select info_key,info_name from testcase where info_key like '{}%'; ".format(
            target)
        res = self.runsql(sql)
        for i in res:
            (k, n) = i
            suite_cases.append([k, n])

        from _pytest import config
        from _pytest import main

        if os.path.isfile(target) and (not os.path.splitext(target)[1] == ".py"):
            return

        conf = config.get_config(os.path.dirname(target))
        pm = conf.pluginmanager
        args = ["--co", target]
        conf = pm.hook.pytest_cmdline_parse(pluginmanager=pm, args=args)
        s = main.Session.from_config(conf)

        # conf._do_configure() :May be needed
        conf.hook.pytest_sessionstart(session=s)
        conf.hook.pytest_collection(session=s)

        #print(suite_cases)

        for it in s.items:
            info_key = it.fspath.strpath
            info_name = it.nodeid.split("::", maxsplit=1)[1]
            tags = ""
            doc = "未提供"
            #print("k:{}, n:{}".format(info_key,info_name))
            if [info_key, info_name] in suite_cases:
                suite_cases.remove([info_key, info_name])  # delete the inserted cases.
                sql = '''UPDATE testcase set info_tags='{}', 
                                             info_doc='{}' 
                         WHERE info_key='{}' and info_name='{}';'''.format(tags, doc, info_key, info_name)
                self.runsql(sql)
            else:
                sql = "insert into testcase(info_key,info_name,info_tags, info_doc) \
                values('{}','{}','{}','{}');".format(info_key, info_name, tags, doc)
                res = self.runsql(sql)
                if not res:
                    log.error("Insert testcase Fail")

                if not mode == 'start':
                    self.insert_loginfo('unknown', 'case',
                                        'create', info_key, info_name)

        # deleted cases and renamed cases should be deleted
        for i in suite_cases:
            if i[0].endswith(".py"):         # Only delete pytest cases
                sql = "delete from testcase where info_key ='{}' and info_name='{}';".format(
                    i[0], i[1])
                self.runsql(sql)

                if not mode == 'start':
                    self.insert_loginfo('unknown', 'case', 'delete', i[0], i[1])


    def get_testdata(self, target):

        suites = 0
        cases = 0
        passed = 0
        failed = 0
        unknown = 0

        sql = '''SELECT count(distinct(info_key)), count(info_name) from testcase where info_key like '{}%' ;'''.format(
            target)
        res = self.runsql(sql)
        (suites, cases) = res.fetchone()

        sql = '''SELECT count(info_name) from testcase where run_status='PASS' and info_key like '{}%' ;'''.format(
            target)
        res = self.runsql(sql)
        (passed,) = res.fetchone()

        sql = '''SELECT count(info_name) from testcase where run_status='FAIL' and info_key like '{}%' ;'''.format(
            target)
        res = self.runsql(sql)
        (failed,) = res.fetchone()

        return [suites, cases, passed, failed, cases-(passed + failed)]

    def get_testdataOLD(self, target):

        try:
            suite = TestData(source=target, extensions='robot')
        except Exception as e:
            log.error("get_testdata of source {} Exception :{}".format(target, e))
            return [0, 0, 0, 0, 0]

        suites = 0
        cases = 0
        passed = 0
        failed = 0
        unknown = 0

        def _getdata(suite=suite):
            ss = suite.source
            nonlocal suites
            nonlocal cases
            nonlocal passed
            nonlocal failed
            nonlocal unknown
            if len(suite.testcase_table) > 0:
                suites += 1
                for t in suite.testcase_table:
                    info_key = ss
                    info_name = t.name
                    status = self.get_casestatus(info_key, info_name)
                    if status == 'PASS':
                        passed += 1
                    elif status == 'FAIL':
                        failed += 1
                    else:
                        unknown += 1
                    cases += 1

            for child in suite.children:
                _getdata(child)

        _getdata(suite)

        return [suites, cases, passed, failed, unknown]


if __name__ == '__main__':
    myDB = TestDB('/Users/tester/PycharmProjects/uniRobotDev/work/DBs')
    #res = myDB.runsql("insert into everyday(item,value,demo) values('second','1112222','demo info');")
    #res = myDB.add_user('zhangsan1','zhangsan1','aaabbb','zh@e.com')
    #res = myDB.add_project('proj2','zhangsan','lisi')

    #res = myDB.runsql("select * from user ;")
    # for i in res:
    #    print(i)

    #res = myDB.runsql("select * from project ;")
    # for i in res:
    #    print(i)

    # print(myDB.get_ownproject('tbdsadmin'))
    # print(myDB.get_passwd('Admin'))
    # print(myDB.get_allproject('zhangsan'))
    #all = myDB.get_allproject('AA')
    # for o in all:
    #    print("{}:::{}".format(o.split(':')[0],o.split(':')[1]))

    # myDB.refresh_caseinfo('/Users/tester/PycharmProjects/uniRobotDev/.beats/workspace/Admin/Demo_Project/RobotTestDemo/TestCase/903dir1','force')
    file1 = '/Users/tester/PycharmProjects/uniRobotDev/.beats/workspace/Admin/Demo_Project/RobotTestDemo/TestCase/903dir1/case1.robot'

    dir1 = '/Users/tester/PycharmProjects/uniRobotDev/.beats/workspace/Admin/Demo_Project/RobotTestDemo/TestCase/903dir1'

    #res = myDB.insert_loginfo("admin","case","run case","Jest test")
    #res = myDB.runsql("select * from loginfo  ;".format(file1))
    sql = '''INSERT INTO loginfo(user,target,action,key,result) 
                  VALUES('Admin','case','debug','/Users/tester/PycharmProjects/uniRobotDev/work/workspace/Admin/Demo_Project/RobotTestDemo/TestCase/01Template.robot','OK')'''

    sql2 = ''' SELECT count(*) FROM loginfo WHERE 
                                                  logtime > datetime('now','localtime','-365 days') 
                                              and target='suite' 
                                              and ( action='create' or action='copy' )
                                              and key like '/Users/tester/PycharmProjects/uniRobotDev/work/workspace/Admin/Demo_Project%'; '''

    res = myDB.runsql("select user, target, action ,key from loginfo;")
    for u in res:
        print(u)
