"""
自定义 allure报告 的运行方式，支持选择不同方式收集测试结果
"""

"""
os.system：执行系统命令

allure 命令行指令：
    allure generate ： 固定写法
    -s : 打印调试信息
    ../test_report：json格式的临时报告的目录
    -o ../test_report ： 输出报告的地址（报告生成的地址）
    --clean ： 清除已经存在的报告
    --allure-severities ： 指定case的重要级别，配置后 allure 只会收集对应级别的报告
"""

import os
from public_method.project_path import project_path
from public_method.logger_handler import logger


class AllureReportHandler:

    def __init__(self):

        # 拼接：生成allure报告的指令：allure generate ./test_report_data/ -o ./test_report/ --clean
        self.generate_report_command = "allure generate {} -o {} --clean".format(project_path.test_report_json_path,
                                                                                 project_path.test_report_path)
        # 拼接：打开报告的指令：allure open -h 127.0.0.1 -p 8866 ./test_report/
        self.open_report_command = f"allure open -h 127.0.0.1 -p 8866 {project_path.test_report_path}"

    def all_case_report(self):
        """
        收集所有 case 的测试结果
        :return:
        """
        logger.info("正在收集所有Case的测试结果：生成Allure报告。")

        # 拼接：收集所有测试结果的指令：pytest -sq --alluredir ./test_report_data/
        collect_results_command = "pytest -sq --alluredir %s" % project_path.test_report_json_path

        os.system(collect_results_command)  # 收集所有测试结果
        os.system(self.generate_report_command)  # 生成allure报告
        os.system(self.open_report_command)  # 打开报告

    def case_severities_report(self, severities=0):
        """
        按照 case 重要性收集测试结果
        此方法需在想要执行的 case 方法中使用装饰器(@allure.severity)标识重要等级

        allure 提供的枚举类等级如下:
            blocker：阻塞缺陷(功能未实现，无法下一步) ，重要性指数 >= 80
            critical：严重缺陷(功能点缺失)，60 < 重要性指数 <= 80
            normal： 一般缺陷(边界情况，格式错误)， 40 < 重要性指数 <= 60
            minor：次要缺陷(界面错误与ui需求不符)，20 < 重要性指数 <= 40
            trivial： 轻微缺陷(必须项无提示，或者提示不规范)，重要性指数 <= 20
        :param severities:
                            int, 指定 case 的重要性程度，程序会按照 case 重要性程度收集测试结果
                            默认重要性程度为：0，收集全部 case 的执行结果
        :return:
        """

        # 判断需要收集那些重要程度的 case 执行结果，从而等到对应的重要性程度
        if int(severities) <= 20:
            judge_severities = "trivial,minor,normal,critical,blocker"
        elif 20 < int(severities) <= 40:
            judge_severities = "minor,normal,critical,blocker"
        elif 40 < int(severities) <= 60:
            judge_severities = "normal,critical,blocker"
        elif 60 < int(severities) <= 80:
            judge_severities = "critical,blocker"
        elif 80 < int(severities):
            judge_severities = "blocker"
        else:
            judge_severities = "trivial,minor,normal,critical,blocker"

        logger.info(f"正在收集重要性程度为【{judge_severities}】的Case的测试结果：生成Allure报告。")

        # 拼接：按重要级别收集测试结果的指令：pytest -sq --alluredir ./test_report_data/ --allure-severities=minor,normal,critical,blocker
        collect_severities_command = f"pytest -sq --alluredir {project_path.test_report_json_path} --allure-severities={judge_severities}"

        os.system(collect_severities_command)  # 按重要级别收集测试结果
        os.system(self.generate_report_command)  # 生成allure报告
        os.system(self.open_report_command)  # 打开报告

    def case_file_report(self, file_path):
        """
        按照 case 文件收集测试结果
        :param file_path: str,需要运行的 case 文件路径
        :return:
        """
        logger.info(f"正在收集【{file_path}.py】的Case的测试结果：生成Allure报告。")

        # 拼接：按照 case 文件收集测试结果的指令：pytest test_001.py -sq --alluredir=./test_report_data/
        collect_case_file_command = f"pytest {file_path}.py -sq --alluredir {project_path.test_report_json_path}"

        os.system(collect_case_file_command)  # 收集所有测试结果
        os.system(self.generate_report_command)  # 生成allure报告
        os.system(self.open_report_command)  # 打开报告

# if __name__ == "__main__":
#     arh = AllureReportHandler()
#
#     print(arh.project_path.test_report_json_path)
#     print(arh.generate_report_command)
#     print(arh.open_report_command)
#     arh.all_case_report()
#     arh.case_severities_report(severities=50)
#     arh.case_file_report("test001")
