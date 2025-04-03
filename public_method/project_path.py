"""
    项目路径获取模块
"""

import os
from datetime import datetime

class ProjectPath:

    def __init__(self):
        # 项目文件夹路径
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.project_root_path = current_path.replace("\public_method", "")

        # 如果没有该项目文件夹，自动创建项目文件夹
        if not os.path.exists(self.project_root_path):
            os.mkdir(self.project_root_path)

        """ 公共目录 """
        # 配置文件夹
        self.config_file_path = os.path.join(self.project_root_path, r"config_file")
        # 公共方法文件夹
        self.common_method_path = os.path.join(self.project_root_path, r"public_method")
        # 测试日志文件夹
        self.test_logging_path = os.path.join(self.project_root_path, r"test_logging")
        # 测试报告文件夹
        self.test_report_path = os.path.join(self.project_root_path, r"test_report\test_report_html")
        # json格式的临时报告的目录
        self.test_report_json_path = os.path.join(self.project_root_path, r"test_report\test_report_data")

        """ 配置文件"""
        # log_config.yaml 
        self.log_config_path = os.path.join(self.config_file_path, "log_config.yaml")
        # weixin_config.yam
        self.weixin_config = os.path.join(self.config_file_path, "weixin_config.yaml")

        """ page """
        self.page_login = os.path.join(self.project_root_path, r"page_handler\login\page_data\page_login.yml")
        # 互联网医院管理-订单管理页
        self.page_order_management = os.path.join(self.project_root_path,
                                                  r"page_handler\internet_hospital_management\operations_management\page_data\page_order_management.yml")

        """ test """
        # 测试用例文件夹
        self.web_test_case_path = os.path.join(self.project_root_path, r"test_case_po")

        """ test data path """
        self.test_environment = os.path.join(self.project_root_path, r"test_data\test_environment.yml")
        self.test_buy_internet_medical_treatment = os.path.join(self.project_root_path,
                                                                r"test_data\test_buy_internet_medical_treatment.yml")

        """ case 异常截图"""
        # 报错截图文件夹
        self.error_image_path = os.path.join(self.project_root_path, r"test_image\error_image")

        """ case 期望结果图片"""
        # 期望结果文件夹
        self.expect_image_path = os.path.join(self.project_root_path, r"test_image\expect_image")
        # buy_internet_medical_treatment
        self.buy_internet_medical_treatment_expect_image = os.path.join(self.expect_image_path,
                                                                        "buy_internet_medical_treatment.jpg")

        """ case 运行结果截图"""
        # 运行结果截图文件夹
        self.run_image_path = os.path.join(self.project_root_path, r"test_image\run_image")
        # buy_internet_medical_treatment
        check_image_name = "buy_internet_medical_treatment_" + datetime.now().strftime("%Y-%m-%d %H_%M_%S") + ".jpg"  # 对比图片名称
        self.buy_internet_medical_treatment_run_image = os.path.join(self.run_image_path, check_image_name)


        """ 患者图片 """
        # 患者图片文件夹
        self.patient_image_path = os.path.join(self.project_root_path, r"test_image\patient_image")
        # 患者病历图片
        self.patient_case_history_image = os.path.join(self.patient_image_path, r"case_history.png")


# 实例化ProjectPath类：创建类对象
project_path = ProjectPath()

# if __name__ == "__main__":
#     p_path = ProjectPath()
#     print(p_path.patient_case_history_path)
#     print(p_path.test_buy_internet_medical_treatment)
