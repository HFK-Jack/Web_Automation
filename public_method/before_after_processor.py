"""
    前后置处理模块
"""

import os
import socket
import subprocess
import warnings

from appium import webdriver
from datetime import datetime
from public_method.logger_handler import logger
from public_method.project_path import ProjectPath


class BeforeAfterProcessor:

    def __init__(self):
        pass


    def check_port(self,app_json,host='127.0.0.1'):
        """
        检测指定的端口是否被占用 port 传端口号，启动 appium server服务
        :return:
        """
        # ResourceWarning忽略与资源使用相关的警告：此处忽略占用端口号抛出的异常
        warnings.simplefilter('ignore', ResourceWarning)
        # 创建套接字对象
        sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sockfd.connect((host,app_json["port"]))
        except OSError as errorMsg:
            logger.info(r"port：{}未占用，需启动 appium 服务!".format(app_json["port"]))
            logger.info('port %s 未占用 需启动appium服务! ' % app_json['port'])
            cmd_start_appium = 'appium -p ' + str(app_json['port']) + ' -U ' + str(app_json['deviceName'])
            subprocess.Popen(cmd_start_appium, shell=True,
                             stdout=open(os.path.join(ProjectPath.test_logging_path, f"{str(app_json['port'])}.log"), mode='w',
                                         encoding='gbk'),
                             stderr=subprocess.STDOUT)
            logger.info('启动appium服务中' + cmd_start_appium)
        else:
            logger.info('port %s 已占用 无需启动appium服务! ' % app_json['port'])
        # 输入法切换 如果返回unknow 就安装
        input_type = 'adb -s %s shell ime set com.android.adbkeyboard/.AdbIME' % str(app_json['deviceName'])
        result = os.popen(input_type).read()
        # if 'Unknown' in result:
        #     install_input_apk = f'adb -s {str(etong_json["deviceName"])} install {os.path.join(p_path.DATA_PATH, "ADBKeyboard.apk")}'
        #     os.system(install_input_apk)
        #     sleep(0.5)
        #     os.system(input_type)

    def release_port(self,port):
        """
        释放指定的端口，结束进程
        :param port: 端口号
        :return:
        """
        # 查找对应端口的pid
        cmd_find_pid = 'netstat -aon | findstr %s' % port
        # 返回命令执行后的结果
        listPid = os.popen(cmd_find_pid).read()
        logger.info(listPid)
        if str(port) and 'LISTENING' in listPid:
            # 获取端口对应的pid进程
            i = listPid.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = listPid.index('\n')
            pid = listPid[start:end]
            # 关闭被占用端口的pid
            cmd_kill_pid = 'taskkill -f -pid %s' % pid
            logger.info(cmd_kill_pid)
            os.popen(cmd_kill_pid)
            logger.info(str(port) + '端口已被kill')
        else:
            logger.info('port %s 未占用无需释放 !' % port)

    def start_app(self,app_devices_info,*args,**kwargs):
        """
        启动 APP 程序
        :param app_devices_info: APP设备信息，dict格式
        :return:
        """
        # 如果端口未占用，则启动appium服务，暂时不使用：尚未解析
        # self.check_port(app_devices_info)
        logger.info("开始启动APP... ...")
        app_start_time = datetime.now()
        app_driver = None
        for i in range(2):
            try:
                app_driver = webdriver.Remote("http://" + str(app_devices_info["ip"]) + ":" + str(app_devices_info["port"]) + "/wd/hub",app_devices_info)
            except Exception as e:
                logger.warning(f"启动 app_driver 异常，异常原因是：{e}")
            else:
                logger.error(f"启动 app_driver 成功！终止循环！")
                break
        app_end_time = datetime.now()
        logger.info(f"APP已启动，开始时间为：{app_start_time}，结束时间为：{app_end_time}，启动APP共耗时：{app_end_time - app_start_time}")
        return app_driver


    # def loginApp(loginAccount=None, loginPassword=None):
    #     """
    #     登录 APP
    #     1.未登录，使用账户密码
    #     2.已登录：滑动解锁
    #     :param loginAccount: 登录账户
    #     :param loginPassword: 登录密码
    #     :return:
    #     """
    #     if 1:
    #         pass
    #
    #     else:
    #         pass
    #
    # def logoutAPP(self):
    #     """
    #     退出APP
    #     :return:
    #     """
    #     pass



# if __name__ == "__main__":
#     pass
    # print(dir())
    # yaml_data = YamlHandlers()
    # radc = yaml_data.read_app_driver_config()
    # print(radc)
    # app_data = radc["dict_app_driver_config"][0]["devices_info"]
    # print(app_data)
    # ASP = BeforeAfterProcessor()
    # ASP.start_app(app_data)