# -*- coding: utf-8 -*-

__author__ = "mawentao119@gmail.com"

"""

"""

import os
from flask import current_app, session
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from robot.api import TestSuiteBuilder   # done

from utils.file import list_dir, mk_dirs, exists_path, rename_file, remove_dir, get_splitext, get_ownerfromkey
from utils.resource import ICONS
from utils.clear import clear_projectres
from utils.parsing import generate_high_light, generate_auto_complete
from utils.gitit import remote_clone
from utils.pytester import get_pytest_data
from utils.mylogger import getlogger

log = getlogger(__name__)


class Project(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('method', type=str)
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('new_name', type=str)
        self.parser.add_argument('key', type=str)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('manager', type=str, default="")
        self.parser.add_argument('cron', type=str, default="* * * * * *")
        self.parser.add_argument('boolean', type=str, default="ON")
        self.log = getlogger(__name__)
        self.reserved_names = ["works"]
        self.app = current_app._get_current_object()

    def get(self):
        args = self.parser.parse_args()
        method = args["method"].lower()
        if method == 'project_list':
            return self.__get_projectlist(args)

    def post(self):
        args = self.parser.parse_args()

        method = args["method"].lower()
        if method == "create":
            result = self.__create(args)
        elif method == "edit":
            result = self.__edit(args)
        elif method == "delete":
            result = self.__delete(args)
        elif method == "set_main":
            result = self.__set_main(args)
        elif method == "adduser":
            result = self.__adduser(args)
        elif method == "deluser":
            result = self.__deluser(args)
        elif method == "gitclone":
            result = self.__gitclone(args)

        return result, 201

    def __create(self, args):
        "Create Project , User , Save Settings .."
        name = args["name"]
        manager = args["manager"]
        passwd = generate_password_hash("123")

        result = {"status": "success", "msg": "成功：创建项目{}.".format(name)}

        if args["name"] in self.reserved_names:
            result = {"status": "fail", "msg": "请换一个用户名."}
            return result

        if not self.app.config['DB'].add_user(manager, manager, passwd, manager+"@qq.com", 'User', name):
            result = {"status": "fail",
                      "msg": "失败：创建项目管理员{}失败.".format(manager)}
            return result

        project_path = self.app.config["AUTO_HOME"] + \
            "/workspace/%s/%s" % (manager, name)
        if not exists_path(project_path):
            mk_dirs(project_path)
            mk_dirs(os.path.join(project_path, 'platforminterface'))
            mk_dirs(os.path.join(project_path, 'templates'))

        if not self.app.config['DB'].add_project(name, manager, ''):
            result["status"] = "fail"
            result["msg"] = "失败: 创建项目失败（？名称存在）"
            self.app.config['DB'].del_user(manager)
            return result

        self.save_project(project_path)
        self.save_user(project_path)
        self.save_settings(project_path)

        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'create', project_path, result['status'])

        return result

    def __gitclone(self, args):

        url = args['name']
        (ok, info) = remote_clone(self.app, url)

        if ok:
            projectname = self.app.config["PROJECT_NAME"]
            msg = self.app.config['DB'].load_project_from_path(info)
            result = {"status": "success",
                      "msg": "Result: {} project:{}".format(msg, projectname)}
            self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'project', 'gitcreate', info,
                                                 result['status'])
        else:
            result = {"status": "fail", "msg": info}
            self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'project', 'gitcreate', url,
                                                 result['status'])

        return result

    def __edit(self, args):
        result = {"status": "success", "msg": "成功：重命名."}

        if args["new_name"] in self.reserved_names:
            result = {"status": "fail", "msg": "失败：请用其它名字."}
            return result

        if args["name"] in self.reserved_names:
            result = {"status": "fail", "msg": "失败：无法重命名此项目."}
            return result

        owner = get_ownerfromkey(args['key'])
        if not session["username"] == "Admin":
            result["status"] = "fail"
            result["msg"] = "失败：只有Admin可以进行此操作."
            return result

        old_name = self.app.config["AUTO_HOME"] + \
            "/workspace/%s/%s" % (owner, args["name"])
        new_name = self.app.config["AUTO_HOME"] + \
            "/workspace/%s/%s" % (owner, args["new_name"])

        if not rename_file(old_name, new_name):
            result["status"] = "fail"
            result["msg"] = "失败：新名字已存在于目录中!"
        if not self.app.config['DB'].edit_project(args["name"], args["new_name"], owner):
            result["status"] = "fail"
            result["msg"] = "失败：新名字已存在于数据库中!"

        self.log.info("更新用户到主项目为 {}".format(args["new_name"]))
        self.app.config['DB'].runsql("UPDATE user set main_project='{}' where main_project='{}';".format(
            args["new_name"], args["name"]))

        self.save_project(new_name)
        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'rename', old_name, result['status'])

        # Delete resource is not dangerous, all of that can be auto generated.
        clear_projectres('usepath', old_name)

        return result

    def __delete(self, args):
        result = {"status": "success", "msg": "删除项目成功."}

        self.log.debug("删除项目 args:{}".format(args))

        project = args["name"]
        owner = self.app.config['DB'].get_projectowner(project)
        #owner = get_ownerfromkey(args['key'])

        if not session["username"] == "Admin":
            result["status"] = "fail"
            result["msg"] = "FAIL：只有Admin可以进行此操作!"
            return result

        user_path = self.app.config["AUTO_HOME"] + \
            "/workspace/%s/%s" % (owner, args["name"])
        #user_path = args['key']
        self.log.info("删除项目：开始删除项目目录 {}".format(user_path))
        if exists_path(user_path):
            remove_dir(user_path)

        if not self.app.config['DB'].del_project(args["name"], owner):
            result["status"] = "fail"
            result["msg"] = "删除失败, 项目不存在."

        # TODO 还需要删除项目目录 workspace 和 jobs 下的内容
        self.log.info("删除项目的owner：{} 和以 {} 为主项目的成员".format(owner, project))
        self.app.config['DB'].del_user(owner)
        work_path = os.path.join(
            self.app.config['AUTO_HOME'], 'workspace', owner)
        remove_dir(work_path) if os.path.exists(work_path) else None

        self.app.config['DB'].runsql(
            "Delete from user where main_project='{}' ;".format(project))

        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'delete', user_path, result['status'])

        # Delete resource is not dangerous, all of that can be auto generated.
        clear_projectres('usepath', user_path)

        return result

    def __set_main(self, args):

        main_project = self.app.config['DB'].get_user_main_project(
            self.app.config['USER_NAME'])
        owner = self.app.config['DB'].get_projectowner(main_project)

        if self.app.config['USER_NAME'] == owner:
            return {"status": "Fail", "msg": "失败：项目管理员不能切换主项目."}

        #user_path = self.app.config["AUTO_HOME"] + "/workspace/%s/%s" % (session["username"], args["name"])
        user_path = args['key']
        if exists_path(user_path):
            info = self.app.config['DB'].init_project_settings(user_path)
            projectname = self.app.config["PROJECT_NAME"]
            self.app.config['DB'].set_user_main_project(
                self.app.config['USER_NAME'], projectname)

        result = {"status": "success", "msg": info}

        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'set_main', user_path, info)

        return result

    def __adduser(self, args):
        result = {"status": "success", "msg": "成功：增加项目用户."}

        project = self.app.config["PROJECT_NAME"]
        owner = get_ownerfromkey(args['key'])
        if not session["username"] == owner:
            result["status"] = "fail"
            result["msg"] = "失败：没有权限操作，请联系管理员{}.".format(owner)
            return result

        new_name = args["new_name"]

        try:
            self.app.config['DB'].add_projectuser(project, new_name)
        except Exception:
            result["status"] = "fail"
            result["msg"] = "数据库操作失败！"

        self.save_project(args['key'])
        self.save_user(args['key'])
        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'adduser', args['key'], new_name)

        return result

    def __deluser(self, args):
        result = {"status": "success", "msg": "成功：移除用户."}

        project = self.app.config["PROJECT_NAME"]
        owner = get_ownerfromkey(args['key'])
        if not session["username"] == owner:
            result["status"] = "fail"
            result["msg"] = "失败：没有权限操作，请联系{}.".format(owner)
            return result

        new_name = args["new_name"]

        try:
            self.app.config['DB'].del_projectuser(project, new_name)
        except Exception:
            result["status"] = "fail"
            result["msg"] = "DB操作失败！"

        self.save_project(args['key'])
        self.save_user(args['key'])
        self.app.config['DB'].insert_loginfo(
            self.app.config['USER_NAME'], 'project', 'deluser', args['key'], new_name)

        return result

    def __get_projectlist(self, args):
        # project_list = {"total": 0, "rows": []}
        # res = self.app.config['DB'].runsql(
        #     "Select projectname,owner,users,cron from project;")
        # for r in res:
        #     (projectname, owner, users, cron) = r
        #     project_list["rows"].append(
        #         {"projectname": projectname, "owner": owner, "users": users, "cron": cron})
        #
        # return project_list
        return [self.app.config['DB'].get_project_name()]

    def save_project(self, project_path):
        project = self.app.config["PROJECT_NAME"]
        projectfile = os.path.join(
            project_path, 'platforminterface/project.conf')
        self.log.info("保存项目信息到文件:{}".format(projectfile))
        with open(projectfile, 'w') as f:
            f.write("# projectname|owner|users|cron\n")
            res = self.app.config['DB'].runsql(
                "select * from project where projectname='{}';".format(project))
            for i in res:
                (projectname, owner, users, cron) = i
                line = "{}|{}|{}|{}\n".format(projectname, owner, users, cron)
                self.log.info("保存项目信息:{}".format(line))
                f.write(line)

    def save_user(self, project_path):
        project = self.app.config["PROJECT_NAME"]
        owner = self.app.config['DB'].get_projectowner(project)
        userfile = os.path.join(project_path, 'platforminterface/user.conf')
        self.log.info("保存用户信息到文件:{}".format(userfile))
        with open(userfile, 'w') as f:
            f.write("# username|fullname|passworkdHash|email|category|main_project\n")
            res = self.app.config['DB'].runsql(
                "select * from user where main_project='{}';".format(project))
            for i in res:
                (username, fullname, passworkdHash,
                 email, category, main_project) = i
                f.write("{}|{}|{}|{}|{}|{}\n".format(username, fullname, passworkdHash,
                                                     email, category, main_project))

    def save_settings(self, project_path):
        project = self.app.config["PROJECT_NAME"]
        owner = self.app.config['DB'].get_projectowner(project)
        settingsfile = os.path.join(
            project_path, 'platforminterface/settings.conf')
        self.log.info("保存 settings 文件:{}".format(settingsfile))
        with open(settingsfile, 'w') as f:
            f.write("#description#item#value#demo#category\n")
            res = self.app.config['DB'].runsql("select * from settings;")
            for i in res:
                f.write('#'.join(i) + '\n')


class ProjectList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('category', type=str, default="root")
        self.parser.add_argument('key', type=str, default="root")
        self.parser.add_argument('project', type=str)
        self.parser.add_argument('suite', type=str)
        self.parser.add_argument('splitext', type=str)
        self.log = getlogger(__name__)
        self.app = current_app._get_current_object()

    def get(self):
        args = self.parser.parse_args()

        #log.info("get projectList: args:{}".format(args))
        if args["key"] == "root":
            return get_projects(self.app, self.app.config["USER_NAME"])
        else:
            path = args["key"]

            if os.path.isfile(path):      # 单个文件
                return get_step_by_case(self.app, path)

            files = list_dir(path)
            # Omit the hidden file
            files = [f for f in files if not f.startswith('.')]
            if len(files) > 1:
                files.sort()

            children = []
            for d in files:
                ff = path + '/' + d
                if os.path.isdir(ff):     # 目录:Dir
                    icons = "icon-suite-open"
                    stat = "closed"
                    text = d

                    # For performance concern, False.
                    if self.app.config['SHOW_DIR_DETAIL']:
                        td = self.app.config['DB'].get_testdata(ff)
                        if td[0] > 0:    # [suites,cases,passed,Failed,unknown]
                            icons = "icon-suite-open_case"
                            text = d+':' + " ".join([str(ss) for ss in td])

                    children.append({
                        "text": text, "iconCls": icons, "state": stat,
                        "attributes": {
                            "name": d,
                            "category": "suite",
                            "key": ff,
                        },
                        "children": []
                    })
                else:                  # 单个文件:single file
                    text = get_splitext(ff)
                    if text[1] in ICONS:
                        icons = ICONS[text[1]]
                    else:
                        icons = "icon-file-default"

                    if text[1] in (".robot"):
                        if self.app.config['SHOW_DIR_DETAIL']:
                            # [suites,cases,passed,Failed,unknown]
                            td = self.app.config['DB'].get_testdata(ff)
                            if td[1] == td[2]:
                                icons = 'icon-robot_pass'
                            if td[3] > 0:
                                icons = 'icon-robot_fail'
                            lb = d.replace('.robot', ':') + \
                                ' '.join([str(ss) for ss in td[1:]])
                        else:
                            suite_status = self.app.config['DB'].get_suitestatus(
                                ff)
                            if suite_status == 'PASS':
                                icons = 'icon-robot_pass'
                            if suite_status == 'FAIL':
                                icons = 'icon-robot_fail'
                            lb = d.replace('.robot', '')

                        children.append({
                            "text": lb, "iconCls": icons, "state": "closed",
                            "attributes": {
                                "name": d,
                                "category": "case",
                                "key": ff,
                                "splitext": text[1]
                            },
                            "children": []
                        })
                    elif text[1] in (".resource"):
                        children.append({
                            "text": d, "iconCls": icons, "state": "closed",
                            "attributes": {
                                "name": d,
                                "category": "case",
                                "key": ff,
                                "splitext": text[1]
                            }
                        })
                    elif text[1] in (".py"):
                        children.append({
                            "text": d, "iconCls": icons, "state": "closed",
                            "attributes": {
                                "name": d,
                                "category": "case",
                                "key": ff,
                                "splitext": text[1]
                            }
                        })
                    else:
                        children.append({
                            "text": d, "iconCls": icons, "state": "open",
                            "attributes": {
                                "name": d,
                                "category": "case",
                                "key": ff,
                                "splitext": text[1]
                            }
                        })
            return children

# TODO: DELETE
# def get_project_list(app, username):
#     projects = app.config["DB"].get_allproject(username)
#     return projects


def get_projects(app, username):
    # projects = app.config["DB"].get_allproject(username)
    projects = []
    project = os.path.split(os.environ.get("PROJECT_DIR", "unknown"))[1]
    projects.append(project)
    children = []
    for p in projects:
        prj = p
        key = os.environ.get("PROJECT_DIR", "unknown")
        ico = "icon-project_s"
        text_p = prj
        children.append({
            "text": text_p, "iconCls": ico, "state": "closed",
            "attributes": {
                "name": prj,
                "category": "project",
                "key": key
            },
            "children": []
        })

        generate_high_light(key)
        generate_auto_complete(key)

        app.config['DB'].init_project_settings(key)

        os.environ["ROBOT_DIR"] = key      # 用于解析 settings 中的环境变量
    #    os.environ["PROJECT_DIR"] = key
    # # 增加 works 目录，展示运行信息
    # children.append({
    #     "text": "works", "iconCls": ico, "state": "closed",
    #     "attributes": {
    #         "name": "works",
    #         "category": "project",
    #         "key": os.environ["AUTO_HOME"]
    #     },
    #     "children": []
    # })

    return [{
        "text": username, "iconCls": "icon-workspace",
        "attributes": {
            "category": "root",
            "key": "root",
        },
        "children": children}]


def get_step_by_case(app, path):
    """
    Find cases from file support pytest and RF
    :param app: self app
    :param path: file path
    :return: json data of test cases
    """
    fext = os.path.splitext(path)[1]
    data = []
    if fext == ".robot":    # robot-framework
        try:
            log.info("生成RF用例:{}".format(path))
            data = get_rfcase_data(app, path)
        except Exception as e:
            log.warning("Get_case_data of {} Exception :{}".format(path, e))
            return []

    if fext == ".py":      # pytest
        log.info("生成pytest用例:{}".format(path))
        data = get_pytest_data(path)

    return data


def get_rfcase_data(app, path):
    """
    RobotFramework testcases finder
    :param app: app
    :param path: robot file path
    :return: json data
    """
    projectdir = os.environ["PROJECT_DIR"]

    suite = TestSuiteBuilder().build(path)
    children = []
    if suite:
        # add library , make it can be open if it is a file. Omited.
        # for i in suite.resource.imports._items:
        #
        #     rsfile = i.name
        #     if rsfile.find("%{ROBOT_DIR}") != -1:
        #         rsfile = rsfile.replace("%{ROBOT_DIR}", os.environ["ROBOT_DIR"])
        #     if rsfile.find("%{PROJECT_DIR}") != -1:
        #         rsfile = rsfile.replace("%{PROJECT_DIR}", os.environ["PROJECT_DIR"])
        #     if rsfile.find("%{BF_LIB}") != -1:
        #         rsfile = rsfile.replace("%{BF_LIB}", os.environ["BF_LIB"])
        #     if rsfile.find("%{BF_RESOURCE}") != -1:
        #         rsfile = rsfile.replace("%{BF_RESOURCE}", os.environ["BF_RESOURCE"])
        #
        #     # do not show System Library or rs file cannot be found.
        #     if not os.path.exists(rsfile):
        #         continue
        #
        #     if os.path.isfile(rsfile):
        #         fname = os.path.basename(rsfile)
        #         children.append({
        #             "text": fname, "iconCls": "icon-library", "state": "open",
        #             "attributes": {
        #                 "name": fname, "category": "case", "key": rsfile,
        #             }
        #         })
        for t in suite.tests:
            status = app.config['DB'].get_casestatus(path, t.name)
            icons = 'icon-step'
            if status == 'FAIL':
                icons = 'icon-step_fail'
            if status == 'PASS':
                icons = 'icon-step_pass'
            children.append({
                "text": t.name, "iconCls": icons, "state": "open",
                "attributes": {
                    "name": t.name, "category": "step", "key": path,
                },
                "children": []
            })

        ''' for v in suite.resource.variables:
            children.append({
                "text": v.name, "iconCls": "icon-variable", "state": "open",
                "attributes": {
                    "name": v.name, "category": "variable", "key": path,
                }
            }) 

        for t in suite.tests:
            keys = []
            for k in t.keywords:
                keys.append({
                    "text": k.name, "iconCls": "icon-keyword", "state": "open",
                    "attributes": {
                        "name": k.name, "category": "keyword", "key": path,
                    }
                })

            children.append({
                "text": t.name, "iconCls": "icon-step", "state": "closed",
                "attributes": {
                    "name": t.name, "category": "step", "key": path,
                },
                "children": keys
            })
        for v in suite.resource.keywords:
            children.append({
                "text": v.name, "iconCls": "icon-user-keyword", "state": "open",
                "attributes": {
                    "name": v.name, "category": "user_keyword", "key": path,
                }
            }) '''

    return children

