"""
运营管理-订单管理页：操作汇总
"""
from time import *
from public_method.project_path import project_path
from public_method.yaml_handler import yaml_handlers
from public_method.input_action import InputAction
from public_method.mouse_action import MouseAction


class PageOrderManagement:

    def __init__(self, driver):
        self.driver = driver
        self.input_action = InputAction(self.driver)
        self.mouse_action = MouseAction(self.driver)
        self.page_order_management = yaml_handlers.read_yaml(project_path.page_order_management)

    def click_internet_hospital_management(self):
        """
        点击互联网医院管理
        :return:
        """

        locator = self.page_order_management["internet_hospital_management_button"]
        self.mouse_action.click(locator)

    def click_everjiankang_home(self):
        """
        返回everjiankang主页
        :return:
        """

        locator = self.page_order_management["everjiankang_home_button"]
        self.mouse_action.click(locator)

    def hover_mouse_more(self):
        """
        鼠标悬浮 菜单栏中的：【更多】
        :return:
        """
        locator = self.page_order_management["more_button"]
        self.mouse_action.move_to_element(locator)

    def click_online_inquiry_settings(self):
        """
        点击在线问诊设置
        :return:
        """
        locator = self.page_order_management["online_inquiry_settings_button"]
        self.mouse_action.click(locator)

    def input_find_doctor_name(self, doctor_name):
        """
        查询条件-输入患者姓名
        :param doctor_name: 医生名称
        :return:
        """
        locator = self.page_order_management["find_doctor_name_input"]
        self.input_action.send_keys(locator, doctor_name)

    def click_find_doctor(self):
        """
        点击查找按钮
        :return:
        """
        locator = self.page_order_management["find_doctor_button"]
        self.mouse_action.click(locator)

    def click_inquiry_settings(self):
        """
        点击设置
        :return:
        """
        locator = self.page_order_management["inquiry_settings_button"]
        self.mouse_action.click(locator)

    def click_save_inquiry_settings(self):
        """
        点击保存
        :return:
        """
        locator = self.page_order_management["save_inquiry_settings"]
        self.mouse_action.click(locator)

    def click_operations_management(self):
        """
        点击运营管理
        :return:
        """
        locator = self.page_order_management["operations_management_button"]
        sleep(3)
        self.mouse_action.click(locator)

    def click_order_management(self):
        """
        点击订单管理
        :return:
        """

        locator = self.page_order_management["order_management_button"]
        self.mouse_action.click(locator)

    def click_buy_visit(self):
        """
        点击下单按钮
        :return:
        """
        locator = self.page_order_management["buy_visit_button"]
        self.mouse_action.click(locator)

    def click_create_patient_archives(self):
        """
        勾选新建档案
        :return:
        """

        locator = self.page_order_management["create_patient_archives_box"]
        self.mouse_action.click(locator)

    def input_new_patient_name(self, name):
        """
        患者档案-输入患者姓名
        :param name: 患者姓名
        :return:
        """

        locator = self.page_order_management["new_patient_name_input"]
        self.input_action.send_keys(locator, name)

    def input_patient_identity_card(self, identity_card):
        """
        患者档案-输入患者身份证
        :param identity_card: 患者身份证
        :return:
        """

        locator = self.page_order_management["patient_identity_card_input"]
        self.input_action.send_keys(locator, identity_card)

    def input_patient_phone(self, phone):
        """
        患者档案-输入患者手机号
        :param phone: 患者手机号
        :return:
        """

        locator = self.page_order_management["patient_phone_input"]
        self.input_action.send_keys(locator, phone)

    def click_save_patient_archives(self):
        """
        保存新建患者档案
        :return:
        """

        locator = self.page_order_management["save_patient_archives_button"]
        self.mouse_action.click(locator)

    def input_internet_medical_treatment_type(self, type):
        """
        选择就诊类型
        :param type: 就诊类型
        :return:
        """

        locator = self.page_order_management["internet_medical_treatment_type_input"]
        self.input_action.send_keys(locator, type)

        # 选择第一位满足条件的类型
        locator_first = self.page_order_management["internet_medical_treatment_type_first_input"]
        self.mouse_action.click(locator_first)

    def input_doctor_name(self, name):
        """
        选择医生
        :param name: 医生姓名
        :return:
        """

        locator = self.page_order_management["doctor_name_input"]
        self.input_action.send_keys(locator, name)

        # 选择第一位满足条件的患者
        locator_first = self.page_order_management["doctor_name_first_input"]
        self.mouse_action.click(locator_first)

    def input_illness_description(self, name):
        """
        输入病情描述
        :param name: 医生姓名
        :return:
        """

        locator = self.page_order_management["illness_description_input"]
        self.input_action.send_keys(locator, name)

    def upload_case_history(self, image_path):
        """
        上传病历/诊断照片
        @param image_path: 图片地址
        @return:
        """

        locator = self.page_order_management["upload_case_history_button"]
        self.input_action.send_keys_image(locator, image_path)

    def save_buy_visit(self):
        """
        点击下一步：保存所选就诊
        :return:
        """

        locator = self.page_order_management["save_buy_visit_button"]
        self.mouse_action.click(locator)

    def input_find_patient_name(self, name):
        """
        查询条件-患者名称输入框
        :param name: 患者姓名
        :return:
        """

        locator = self.page_order_management["find_patient_name_input"]
        self.input_action.send_keys(locator, name)

    def click_find_patient_order(self):
        """
        点击查询患者订单按钮
        :return:
        """

        locator = self.page_order_management["find_patient_order_button"]
        self.mouse_action.click(locator)

    def click_cash_payment_fill_sum(self):
        """
        填充现金支付金额
        :return:
        """

        start_locator = self.page_order_management["cash_payment_fill_sum_button"]
        self.mouse_action.click(start_locator)

    def click_save_payment_sum(self):
        """
        保存支付金额
        :return:
        """

        start_locator = self.page_order_management["save_payment_sum_button"]
        self.mouse_action.click(start_locator)
