"""
公共方法汇总
"""

# 项目相关方法
from public_method.allure_report_handler import AllureReportHandler
from public_method.excel_handle import ExcleHandles
from public_method.folder_handler import FolderHandler
from public_method.logger_handler import LoggerHandler
from public_method.project_path import ProjectPath
from public_method.yaml_handler import YamlHandlers

# 测试相关方法
from public_method.test_function.action_handler import ActionHandler
from public_method.data_generator import DataGenerator


class PublicMethod:

    def AllureReportHandler(self):

        return AllureReportHandler()

    def ExcleHandles(self):

        return ExcleHandles()

    def FolderHandler(self):

        return FolderHandler()

    def LoggerHandler(self):

        return LoggerHandler()

    def ProjectPath(self):

        return ProjectPath()

    def YamlHandlers(self):

        return YamlHandlers()



    def ActionHandler(self):

        return ActionHandler()

    def DataGenerator(self):

        return DataGenerator()