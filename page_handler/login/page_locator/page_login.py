"""
    登录页面
"""
from public_method.project_path import project_path
from public_method.input_action import InputAction
from public_method.mouse_action import MouseAction
from public_method.yaml_handler import yaml_handlers


class PageLogin:

    def __init__(self, driver):

        self.driver = driver
        self.input_action = InputAction(self.driver)
        self.mouse_action = MouseAction(self.driver)
        # 页面数据
        self.page_login = yaml_handlers.read_yaml(project_path.page_login)


    def open_url(self, url):
        """
        打开 URL
        :param url: 访问的 URL
        :return:
        """
        self.driver.get(url)

    def choose_tenant(self, tenant_name="UI自动化机构"):
        """
        登录页面：选择租户
        :param tenant_name: 租户名称，默认自动化
        :return:
        """

        if tenant_name == "UI自动化机构":
            locator = self.page_login['tenant_ui_automation_button']
            self.mouse_action.click(locator)

        if tenant_name == "pt002":
            locator = self.page_login['tenant_pt002_button']
            self.mouse_action.click(locator)


    def user_login(self, username, password, tenant_name, longin_flag=True):
        """
        误删互联网业务需使用
        使用账号密码登录-选择租户
        :param usernam: 账号
        :param password: 密码
        :longin_flag: 是否重新登录
        :param tenant_name: 需要登录的租户名称
        :return:
        """
        if longin_flag:

            locator = self.page_login['username_input']
            self.input_action.send_keys(locator, username, clear_flag=True)

            locator = self.page_login['password_input']
            self.input_action.send_keys(locator, password, clear_flag=True)

            locator = self.page_login['submit_button']
            self.mouse_action.click(locator)

            self.choose_tenant(tenant_name)  # 选择租户

