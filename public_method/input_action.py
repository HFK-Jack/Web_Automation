"""
输入相关操作
"""
from time import sleep

from public_method.element_handler import ElementHandler
from public_method.logger_handler import logger


class InputAction:

    def __init__(self, driver):
        self.driver = driver
        self.element_handler = ElementHandler(self.driver)

    def send_keys(self, locator, value, clear_flag=False):
        """
        输入文本
        :param value: 输入文本
        :param locator:定位元组：定位方法、定位路径
        :param clear_flag: 是否清除默认文本，非0非null为True,0或null为False
        :param img_doc: 异常截图
        :param wait_time:等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出 NoSuchElementException
        :return:
        """
        # 显示等待：获取存在的元素
        element_located = self.element_handler.wait_presence_element(locator)
        if clear_flag:
            element_located.click()
            element_located.clear()
            element_located.send_keys(value)
            logger.info(f"输入{value}")
        else:
            element_located.click()
            element_located.send_keys(value)
            logger.info(f"输入{value}")

    def send_keys_image(self, locator, value):
        """
        输入文本
        :param value: 输入文本
        :param locator:定位元组：定位方法、定位路径
        :param clear_flag: 是否清除默认文本，非0非null为True,0或null为False
        :param img_doc: 异常截图
        :param wait_time:等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出 NoSuchElementException
        :return:
        """
        # 显示等待：获取存在的元素
        element_located = self.element_handler.wait_presence_element(locator)
        element_located.send_keys(value)
        sleep(0.6)
        logger.info(f"输入{value}")

    def clear(self, locator):
        """
        输入账户
        :param locator: 定位元组：定位方法、定位路径
        """
        self.element_handler.wait_presence_element(locator).clear()
