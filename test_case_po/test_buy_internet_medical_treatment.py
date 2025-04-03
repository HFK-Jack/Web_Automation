"""
    互联网就诊流程测试
"""

import cv2
import allure
import pytest
import datetime
from time import *
from assert_method.assert_function import assert_function
from assert_method.open_cv import GraphicalLocator
from public_method.project_path import project_path
from public_method.data_generator import DataGenerator
from public_method.yaml_handler import yaml_handlers
from page_handler.login.page_locator.page_login import PageLogin
from page_handler.internet_hospital_management.operations_management.page_locator.page_order_management import \
    PageOrderManagement


@allure.feature("互联网管理工作站/互联网医生工作站")  # 声明模块名称
@allure.description("互联网就诊测试")  # 声明描述
@allure.suite("互联网就诊测试")
class TestBuyInternetMedicalTreatment:

    @allure.title("互联网就诊患者下单测试")
    @allure.severity("blocker")
    @pytest.mark.run(order=2)
    def test_buy_internet_medical_treatment(self, chrome_driver):
        """
        互联网就诊患者下单流程
        @param chrome_driver: 继承 conftest.py
        @return:
        """

        # 页面
        self.page_login = PageLogin(chrome_driver)
        self.page_order_management = PageOrderManagement(chrome_driver)

        # 读取case配置文件
        self.test_environment = yaml_handlers.read_yaml(project_path.test_environment)
        self.case_value = yaml_handlers.read_yaml(project_path.test_buy_internet_medical_treatment)

        # 获取当前时间
        date_now = datetime.datetime.now()
        # 随机数据
        random_data = DataGenerator()
        # 随机患者姓名
        patient_name = random_data.random_patient_name()
        # 随机手机号
        patient_mobile = random_data.random_patient_mobile()
        # 随机身份证
        identity_card = random_data.random_identity_card()

        with allure.step("访问URL:" + self.test_environment["test_url"]):
            self.page_login.open_url(self.test_environment["test_url"])

        with allure.step("用户名:" + self.test_environment["username"] + "  密码:" + self.test_environment["password"]):
            self.driver = self.page_login.user_login(self.test_environment["username"], self.test_environment["password"],
                                                     "UI自动化机构")

        with allure.step("点击‘互联网医院管理’"):
            self.page_order_management.click_internet_hospital_management()

        with allure.step("点击‘在线问诊设置’菜单"):
            self.page_order_management.click_online_inquiry_settings()

        with allure.step("输入医生姓名"):
            self.page_order_management.input_find_doctor_name("hfk-自动化专用医生")

        with allure.step("查找医生"):
            self.page_order_management.click_find_doctor()

        with allure.step("点击设置按钮"):
            self.page_order_management.click_inquiry_settings()

        with allure.step("保存在线问诊设置"):
            self.page_order_management.click_save_inquiry_settings()

        with allure.step("点击‘运营管理’"):
            self.page_order_management.click_operations_management()

        with allure.step("点击‘运营管理中的：订单管理’"):
            self.page_order_management.click_order_management()

        # with allure.step("点击下单按钮"):
        #     self.page_order_management.click_buy_visit()
        #
        # with allure.step("勾选新建档案"):
        #     self.page_order_management.click_create_patient_archives()
        #
        # with allure.step("患者档案-输入患者姓名"):
        #     self.page_order_management.input_new_patient_name(patient_name)
        #
        # with allure.step("患者档案-输入患者身份证"):
        #     self.page_order_management.input_patient_identity_card(identity_card)
        #
        # with allure.step("患者档案-输入患者手机号"):
        #     self.page_order_management.input_patient_phone(patient_mobile)
        #
        # with allure.step("保存新建患者档案"):
        #     self.page_order_management.click_save_patient_archives()
        #
        # with allure.step("选择就诊类型"):
        #     self.page_order_management.input_internet_medical_treatment_type("图文问诊")
        #
        # with allure.step("选择医生"):
        #     self.page_order_management.input_doctor_name("hfk-自动化专用医生")
        #
        # with allure.step("输入病情描述"):
        #     self.page_order_management.input_illness_description("hfk-病情描述")
        #
        # with allure.step("上传病历/诊断照片"):
        #     self.page_order_management.upload_case_history(project_path.patient_case_history_image)
        #
        # with allure.step("保存患者档案"):
        #     self.page_order_management.save_buy_visit()
        #
        # with allure.step("支付-填充支付金额"):
        #     self.page_order_management.click_cash_payment_fill_sum()
        #
        # with allure.step("支付-保存"):
        #     self.page_order_management.click_save_payment_sum()
        #
        # with allure.step("查询条件-输入患者姓名"):
        #     self.page_order_management.input_find_patient_name(patient_name)
        #
        # with allure.step("点击查询患者订单按钮"):
        #     self.page_order_management.click_find_patient_order()

        """截图对比执行结果"""
        # 预期结果图片
        expect_image = project_path.buy_internet_medical_treatment_expect_image
        # 运行结果图片
        check_image_name = project_path.buy_internet_medical_treatment_run_image
        sleep(2)

        with allure.step("断言：运行结果截图 与 期望结果 核对"):
            check_image = GraphicalLocator(expect_image, chrome_driver)  # 声明图形分析类对象，并传入一个预期图片路径
            cv2.imwrite(check_image_name, check_image.find_me())  # 对图片进行比较并保存

        shape = check_image.threshold["shape"]
        histogram = check_image.threshold["histogram"]
        title = "运行结果： "
        assert_function.assert_opencv(title, shape, histogram, check_image_name, expect_image)  # 判断OpenCV的比较结果

        with allure.step("返回everjiankang主页"):
            self.page_order_management.click_everjiankang_home()
            sleep(5)

