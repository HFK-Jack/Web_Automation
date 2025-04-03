"""
    元素处理模块
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from public_method.logger_handler import logger


class ElementHandler:

    def __init__(self, driver, risk_code=None):
        self.driver = driver
        self.risk_code = risk_code

    def find_element_locator(self, find_type, path):
        """
        元组(定位方式，定位路径)
        :param find_type: 定位方式
        :param path: 定位路径
        :return: 定位元组
        """
        element_type = {"XPATH": By.XPATH, "LINK_TEXT": By.LINK_TEXT, "ID": By.ID, "NAME": By.NAME,
                        "CLASS_NAME": By.CLASS_NAME, "CSS_SELECTOR": By.CSS_SELECTOR,
                        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT, "TAG_NAME": By.TAG_NAME}

        element_locator = (element_type[find_type.upper()], path)

        return element_locator

    def wait_presence_element(self, locator, img_doc=None, wait_time=15, poll_frequency=0.5,
                              screen_shot_flag=False, ignored_exceptions=False):
        """
        显示等待：存在的元素
        :param driver：浏览器驱动
        :param locator: 定位元组，元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 定位异常截图
        :param wait_time: 等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param screen_shot_flag: 是否截屏标识
        :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
        :return: 定位到的存在的元素 或 异常截图
        """

        locator = self.find_element_locator(locator[0], locator[1])

        try:
            element_located = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator))
        except Exception as e:
            logger.error(f"查找元素“{locator}”失败，异常原因是：{e}")
            raise e
        else:
            return element_located

    def wait_visible_element(self, locator, img_doc=None, wait_time=15, poll_frequency=0.5,
                             screen_shot_flag=False, ignored_exceptions=False):
        """
        显示等待：存在并可见的元素
        :param driver: 浏览器驱动
        :param locator: 定位元组，元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 定位异常截图
        :param wait_time: 等待超时时间
        :param screen_shot_flag: 是否截屏标识
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
        :return: 定位到的可见元素 或 异常截图
        """
        locator = self.find_element_locator(locator[0], locator[1])

        try:
            element_located = WebDriverWait(self.driver, wait_time, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except:
            # 异常信息保存日志
            self.save_screenshot(img_doc)
            raise
        else:
            return element_located

    def get_presence_element(self, locator, img_doc='', wait_time=15, poll_frequency=0.5, ignore_alert=False):
        """
        获取单个存在的元素
        :param driver：浏览器驱动
        :param locator:定位元组：定位方法、定位路径
        :param img_doc: 定位异常截图
        :param wait_time:等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
        :param ignore_alert:
        :return:定位到的元素 或 异常截图
        """
        locator = self.find_element_locator(locator[0], locator[1])

        # 显示等待：获取存在的元素
        element_located = self.wait_presence_element(self.driver, locator)

        return element_located

    def get_presence_elements(self, locator, img_doc='', wait_time=20, ignore_alert=False):
        """
        获取多个元素
        :param locator:定位元组：定位方法、定位路径
        :param img_doc: 定位异常截图
        :param wait_time:等待时间
        :param ignore_alert:
        :return:
        """
        locator = self.find_element_locator(locator[0], locator[1])


        self.driver.find_element(locator)
