# -*- coding: utf-8 -*-

__author__ = "mawentao119@gmail.com"

"""
charis made a big change of this file
"""
import os

from flask import current_app, session
from flask_restful import Resource, reqparse
from utils.file import mk_dirs, exists_path, rename_file, remove_dir
from utils.gitit import remote_clone
from utils.mylogger import getlogger


class Suite(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('method', type=str)
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('new_name', type=str)
        self.parser.add_argument('key', type=str)
        self.parser.add_argument('project_name', type=str)
        self.log = getlogger(__name__)
        self.app = current_app._get_current_object()

    def post(self):
        args = self.parser.parse_args()
        self.log.debug("**** suite post args:{}".format(args))
        method = args["method"].lower()
        if method == "create":
            result = self.__create(args)
        elif method == "edit":
            result = self.__edit(args)
        elif method == "delete":
            result = self.__delete(args)
        elif method == "refresh":
            result = self.__refreshcases(args)
        elif method == "gitclone":
            result = self.__gitclone(args)

        return result, 201

    def __create(self, args):
        result = {"status": "success", "msg": "成功：创建目录."}
        user_path = args['key'] + '/' + args['name']
        if not exists_path(user_path):
            mk_dirs(user_path)
        else:
            result["status"] = "fail"
            result["msg"] = "失败：目录已存在!"

        try:
            res = self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'dir', 'create', user_path, result['status'])
        except Exception as e:
            self.log.error("创建目录 {} 异常: {}".format(user_path,e))

        return result

    def __gitclone(self, args):
        url = args['name']
        user_path = args['key']

        (ok, info) = remote_clone(url, user_path)

        if ok:
            result = {"status": "success", "msg": info}
            self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'dir', 'gitcreate', user_path,
                                                           result['status'])
        else:
            result = {"status": "fail", "msg": info}

        return result

    def __edit(self, args):
        result = {"status": "success", "msg": "成功：重命名目录."}
        old_name = args['key']
        new_name = os.path.dirname(old_name) + '/' + args["new_name"]

        if not rename_file(old_name, new_name):
            result["status"] = "fail"
            result["msg"] = "失败：目录已存在!"
            return result

        self.app.config['DB'].delete_suite(old_name)
        isok = self.app.config['DB'].refresh_caseinfo(new_name,'force')
        if not isok:
            result["status"] = "fail"
            result["msg"] = "失败：重命名目录成功，刷新用例失败！"

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'dir', 'rename', old_name, result['status'])

        return result

    def __delete(self, args):
        result = {"status": "success", "msg": "成功：删除目录."}
        user_path = args['key']
        if exists_path(user_path):
            remove_dir(user_path)
        else:
            result["status"] = "fail"
            result["msg"] = "失败：目录不存在!"
            return result

        self.app.config['DB'].delete_suite(user_path)

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'dir', 'delete', user_path, result['status'])

        return result

    def __refreshcases(self, args):
        result = {"status": "success", "msg": "成功：刷新用例信息."}
        info_key = args['key']
        isok = self.app.config['DB'].refresh_caseinfo(info_key)

        if not isok:
            result = {"status": "fail", "msg": "失败：太频繁，稍后重试."}

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'dir', 'refresh', info_key, result['status'])

        return result
