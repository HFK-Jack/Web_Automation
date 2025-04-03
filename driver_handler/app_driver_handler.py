"""
创建 app_driver
"""

from appium import webdriver
from datetime import datetime
from public_method.logger_handler import logger
from public_method.yaml_handler import YamlHandlers


class CreateAppDriver:

    def __init__(self):
        # yaml获取
        yaml_data = YamlHandlers()
        # 设备信息字典
        self.app_devices_info = yaml_data.read_app_driver_config()["dict_app_driver_config"][0]["devices_info"]

    def start_app(self, app_devices_info=None, *args, **kwargs):
        """
        启动 APP：获取 app 的 webdriver 对象
        :param app_devices_info: APP设备信息，dict格式
        :return:
        """
        # 如果端口未占用，则启动appium服务，暂时不使用：尚未解析
        # self.check_port(app_devices_info)
        logger.info("开始启动APP... ...")
        app_start_time = datetime.now()
        self.app_driver = None
        for i in range(3):
            try:
                self.app_driver = webdriver.Remote(
                    "http://" + str(self.app_devices_info["ip"]) + ":" + str(self.app_devices_info["port"]) + "/wd/hub",
                    self.app_devices_info)
            except Exception as e:
                logger.warning(f"启动 app_driver 异常，异常原因是：{e}")
            else:
                logger.error(f"启动 app_driver 成功！终止循环！")
                break
        app_end_time = datetime.now()
        logger.info(
            f"APP已启动，开始时间为：{app_start_time}，结束时间为：{app_end_time}，启动APP共耗时：{app_end_time - app_start_time}")
        return self.app_driver
