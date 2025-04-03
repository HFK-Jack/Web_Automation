"""
    日志处理模块
    推荐使用：logging + colorlog
"""

import logging.config
from datetime import datetime
# from colorlog import colorlog
from public_method.yaml_handler import yaml_handlers
from public_method.project_path import project_path

class LoggerHandler:

    def __init__(self):

        # 读取log配置
        log_config_data = yaml_handlers.read_yaml(project_path.log_config_path)

        # loggers 输出级别控制
        self.logger_level = log_config_data["dict_log_config"]["logger_handler"]["level"]
        # 日志文件输出级别控制
        self.file_level = log_config_data["dict_log_config"]["file_handler"]["level"]
        # 日志文件输出格式
        self.file_format = log_config_data["dict_log_config"]["file_handler"]["file_format"]
        # 日志文件名
        self.log_file_name = log_config_data["dict_log_config"]["file_handler"]["log_file_name"]
        # 日志文件保存得目录
        self.log_file_path = project_path.test_logging_path
        # 日志文件存储的最大空间
        self.max_bytes = int(log_config_data["dict_log_config"]["file_handler"]["max_bytes"])
        # 轮转保存文件的数量
        self.backup_count = int(log_config_data["dict_log_config"]["file_handler"]["backup_count"])
        # 定义输出日志的编码格式
        self.log_encoding = log_config_data["dict_log_config"]["file_handler"]["log_encoding"]
        # 控制台输出级别控制
        self.console_level = log_config_data["dict_log_config"]["console_handler"]["level"]
        # 控制台输出格式
        self.console_format = log_config_data["dict_log_config"]["console_handler"]["formatter"]
        # 日志输出颜色
        self.color_log_dist = log_config_data["dict_log_config"]["console_handler"]["color_log"]

    def log_file_paths(self):
        """
        日志文件以年月日时分命名
        :return: 日志文件名称
        """
        persent_time = datetime.now()  # 获取当前时间

        alog_file_path = f"{self.log_file_path}/{persent_time.year}_{persent_time.month}_{persent_time.day}_{persent_time.hour}_{self.log_file_name}"  # 路径 + 时间

        return alog_file_path

    def color_formatters(self,formatter_obj,log_colors):
        """
        BUG各级别输出不同颜色
        :param formatter_obj: 日志输出格式
        :param log_colors: BUG级别对应颜色，字典
        :return:
        """
        formatter_dict = colorlog.ColoredFormatter()


    def logging_config_func(self):
        """
        配置 logging_config 字典
        :return: 配置字典
        """
        # log配置字典，字典健为固定参数
        logging_config_dict = {
            # version: 版本号
            "version": 1,

            # disable_existing_loggers: 父级是否支持配置的loggers
            "disable_existing_loggers": False,

            # formatters: 定义日志输出的格式和内容
            "formatters": {
                "console_formatters": {  # 控制台输出格式
                    "format": self.console_format  # 简单版配置-控制台使用此配置
                },
                "file_formatters": {  # 日志文件输出格式
                    "format": self.file_format  # 标准版配置-日志文件使用此配置
                }
            },

            # filters: 过滤
            "filters": {},

            # handlers: 配置作用域：让日志写入文件、让控制台打印日志等
            "handlers": {
                # 输出日志到控制台
                "console_handler": {
                    "level": self.console_level,  # 输出日志级别
                    "class": "logging.StreamHandler",  # 分类为：输出日志到控制台
                    "formatter": "console_formatters"  # 输出日志到控制台，使用console_formatters格式
                },
                # 输出日志到文件，收集info及以上得日志
                "file_handler": {
                    "level": self.file_level,  # 输出日志级别
                    "class": "logging.handlers.RotatingFileHandler",  # 分类为：输出日志到文件
                    "formatter": "file_formatters",  # 输出日志到文件，使用file_formatters格式
                    "filename": self.log_file_paths(),  # 日志文件的保存路径及文件名
                    "maxBytes": 1024 * 1024 * self.max_bytes,  # 日志文件存储的最大空间，以字节(bate)为单位 10M
                    "backupCount": self.backup_count,  # 轮转保存文件的数量：保存5个文件，5个文件都存满10M时，覆盖存储在第1个文件继续轮转保存文件
                    "encoding": self.log_encoding,  # 定义输出日志的编码格式
                }
            },

            # 配置loggers
            "loggers": {
                # logging.get_logger(__name__)拿到的logger配置 ： 以上定义的：终端配置console、文件配置default
                "": {
                    "handlers": ["console_handler", "file_handler"],  # 绑定上面定义的两个handler都添加，即log数据即写入文件又打印到控制台
                    "level": self.logger_level,  # 输出日志级别
                    "propagate": True,  # 向上(更高level的logger)传递
                }
            }
        }

        return logging_config_dict

    def get_logger(self,msg=None,*args,**kwargs):
        """
        获取logger
        :param msg: 日志截图
        :param args:
        :param kwargs:
        :return: logger
        """

        logging_config_dict = self.logging_config_func()  # logging配置字典

        logging.config.dictConfig(logging_config_dict)  # 导入上面的logging配置字典

        self.logger = logging.getLogger(__name__)  # 生成一个log实例：日志实例对象

        return self.logger


# 获取 loggerO对象
logger = LoggerHandler().get_logger()


# if __name__ == "__main__":
    # LH = LoggerHandler()
    # # 创建logger对象
    # logger_object = LH.get_logger()
    # # 记录该文件的运行状态
    # logger_object.debug("debug message")  # 调试信息
    # logger_object.info("info message")  # 正常信息
    # logger_object.warning("warning message")  # 警告信息
    # logger_object.error("error message")  # 异常信息
    # logger_object.critical("critical message")  # 崩溃信息

