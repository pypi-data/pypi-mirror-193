# -*- coding: utf-8 -*-

__author__ = "mawentao119@gmail.com"


"""

"""

import os
import time
from flask import current_app, session, request, send_file, make_response
from flask_restful import Resource, reqparse
import werkzeug
from robot.api import ExecutionResult  #TODO Later

from urllib.parse import quote
from utils.file import exists_path
from utils.testcaseunite import export_casexlsx, export_casexlsp, export_casexlsy, export_casezip, do_importfromxlsx ,do_importfromzip, do_uploadcaserecord, do_unzip_project
from utils.mylogger import getlogger


class ManageFile(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('data', type=str)
        self.parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', action='append')
        self.app = current_app._get_current_object()
        self.log = getlogger(__name__)

    def post(self):
        args = request.form.to_dict()
        self.log.debug("Post:args:{}".format(args))
        method = args["method"].lower()
        if method == "uploadcase":
            file = request.files.to_dict()['files']
            return self.__uploadcase(file, args['key']), 201
        elif method == "uploadproject":
            file = request.files.to_dict()['files']
            return self.__uploadproject(file), 201
        elif method == "uploadcaserecord":
            file = request.files.to_dict()['files']
            return self.__uploadcaserecord(file, args['key']), 201
        elif method == "upload":
            file = request.files.to_dict()['files']
            return self.__upload(file, args['key']), 201
        elif method == "download":
            return self.__download(args)
        elif method == "downcaseinfox":
            return self.__downcaseinfox(args)
        elif method == "downcaseinfop":
            return self.__downcaseinfop(args)
        elif method == "downcaseinfoy":
            return self.__downcaseinfoy(args)
        elif method == "downcaseinfoz":
            return self.__downcaseinfoz(args)
        elif method == "export_result":
            return self.__export_result(args)
        elif method == "downruninfo":
            return self.__downruninfo(args)

    def __uploadcase(self, file, path):

        temp_file = self.app.config['AUTO_TEMP'] + '/' + file.filename
        os.remove(temp_file) if os.path.exists(temp_file) else None
        file.save(temp_file)

        (_, f_ext) = os.path.splitext(temp_file)

        if f_ext == '.xlsx':
            (status, msg) = do_importfromxlsx(temp_file, path)
            result = {"status": status, "msg": msg}
        elif f_ext == '.zip':
            (status, msg) = do_importfromzip(temp_file, path)
            result = {"status": status, "msg": msg}
        else:
            result = {"status": "fail", "msg": "异常后缀:{}".format(f_ext)}

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'file', 'uploadcase', path, file.filename)

        return result

    def __uploadproject(self, file):

        temp_file = os.path.join(self.app.config['AUTO_TEMP'],file.filename)
        os.remove(temp_file) if os.path.exists(temp_file) else None
        file.save(temp_file)

        (_, f_ext) = os.path.splitext(temp_file)

        if f_ext == '.zip':
            path = os.path.join(self.app.config['AUTO_TEMP'],'unzipfile')
            (status, info) = do_unzip_project(temp_file, path)

            if status == 'success':
                projectname = self.app.config['PROJECT_NAME']
                msg = self.app.config['DB'].load_project_from_path(info)
                result = {"status": "success", "msg": "Result: {} project:{}".format(msg, projectname)}
                self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'project', 'upload_project', info,
                                                     result['status'])
            else:
                result = {"status": "fail", "msg": info}
                self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'project', 'upload_project', info,
                                                     result['status'])

        return result

    def __uploadcaserecord(self, file, key):
        '''
        上传用例历史执行结果，并导入到caserecord表
        :param file:
        :param key:
        :return:
        '''
        temp_file = self.app.config['AUTO_TEMP'] + '/' + file.filename
        os.remove(temp_file) if os.path.exists(temp_file) else None
        file.save(temp_file)

        (_, f_ext) = os.path.splitext(temp_file)

        if f_ext == '.his':
            (status, msg) = do_uploadcaserecord(temp_file)
            result = {"status": status, "msg": msg}
        else:
            msg = "文件后缀不符合要求(.his):{}".format(f_ext)
            result = {"status": "fail", "msg": msg}

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'file', 'uploadcaserecord', msg, file.filename)

        return result

    def __upload(self, file, path):
        result = {"status": "success", "msg": "成功：上传文件."}

        #charis added  TODO: 如果统一菜单的话，可以这里判断path是否为目录或文件
        user_path = path + '/' + file.filename
        #user_path = self.app.config["AUTO_HOME"] + "/workspace/%s" % self.app.config['USER_NAME'] + path + file.filename
        if not exists_path(user_path):
            file.save(user_path)
        else:
            result["status"] = "fail"
            result["msg"] = "失败：上传文件."

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'file', 'upload', user_path)

        return result

    def __download(self, args):
        # charis added :
        user_path = args['key']
        self.log.info("下载文件请求路径:" + user_path)

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'file', 'download', user_path)

        return self.__sendfile(user_path)

    def __downcaseinfox(self, args):
        # charis added :
        key = args['key']
        self.log.info("下载 xlsx caseinfo 目录:"+key)

        (isok, casefile) = export_casexlsx(key, self.app.config['DB'], self.app.config['AUTO_TEMP'])

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'caseinfo', 'download', key,'xlsx')

        if not isok :
            self.log.error("下载用例失败:{}".format(casefile))
            return "Fail:{}".format(casefile)

        return self.__sendfile(casefile)

    def __downcaseinfop(self, args):
        # charis added :
        key = args['key']
        self.log.info("下载智pytest研格式用例，目录:"+key)

        (isok, casefile) = export_casexlsp(key, self.app.config['DB'], self.app.config['AUTO_TEMP'])

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'caseinfo', 'download', key, 'zhiyan.xlsx')

        if not isok:
            self.log.error("下载用例失败:{}".format(casefile))
            return "Fail:{}".format(casefile)

        return self.__sendfile(casefile)

    def __downcaseinfoy(self, args):
        # charis added :
        key = args['key']
        self.log.info("下载robot智研格式用例，目录:"+key)

        (isok, casefile) = export_casexlsy(key, self.app.config['DB'], self.app.config['AUTO_TEMP'])

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'caseinfo', 'download', key, 'zhiyan.xlsx')

        if not isok:
            self.log.error("下载用例失败:{}".format(casefile))
            return "Fail:{}".format(casefile)

        return self.__sendfile(casefile)

    def __downcaseinfoz(self, args):
        # charis added :
        key = args['key']
        self.log.info("下载zip文件失败 dir:"+key)

        (isok, casefile) = export_casezip(key, self.app.config['AUTO_TEMP'])

        self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'caseinfo', 'download', key,'zip')

        if not isok :
            self.log.error("下载用例失败:{}".format(casefile))
            return "Fail:{}".format(casefile)

        return self.__sendfile(casefile)

    def __export_result(self, args):
        key = args['key']
        name = args['name']

        testproject = self.app.config['DB'].get_setting('test_project')
        projectversion = self.app.config['DB'].get_setting('test_projectversion')

        sql = '''SELECT info_key,info_name,'{}', '{}', ontime,run_status,run_elapsedtime,run_user
                 FROM   testcase
                 WHERE info_key='{}' and info_name='{}'; '''.format(testproject, projectversion, key,name)

        if name == 'export_d_i_r':
            sql = '''SELECT info_key,info_name,'{}', '{}', ontime,run_status,run_elapsedtime,run_user
                             FROM   testcase
                             WHERE info_key like '{}%' ; '''.format(testproject, projectversion, key)

        res = self.app.config['DB'].runsql(sql)
        if res:
            fname = os.path.join(self.app.config['AUTO_TEMP'], 'his_' + str(time.time_ns()) + '.his')
            with open(fname,'w') as myfile:
                for i in res:
                    (key, name, project, version, ontime, run_status, run_elapsedtime, run_user) = i
                    myfile.write("{}|{}|{}|{}|{}|{}|{}|{}\n".format(key, name, project, version, ontime,run_status,run_elapsedtime,run_user))

            self.app.config['DB'].insert_loginfo(self.app.config['USER_NAME'], 'caseinfo', 'export1result', key, name)

            return self.__sendfile(fname)
        else:
            self.log.error("Fail: exportXresult of key:{} ,name:{} ,找不到用例.".format(key,name))
            return "找不到用例."

    def __downruninfo(self, args):
        # charis added : TODO: improve
        user_path = args["key"]
        return self.__sendfile(user_path)

    def __sendfile(self, f):
        response = make_response(send_file(f))
        basename = os.path.basename(f)
        response.headers["Content-Disposition"] = \
            "attachment;" \
            "filename*=UTF-8''{utf_filename}".format(
                utf_filename=quote(basename.encode('utf-8'))
            )
        return response
