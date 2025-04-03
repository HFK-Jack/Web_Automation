"""
    鼠标操作
"""
from selenium.webdriver import ActionChains
from public_method.logger_handler import logger
from public_method.element_handler import ElementHandler


class MouseAction:

    def __init__(self, driver):

        self.driver = driver
        self.mouse_action = ActionChains
        self.element_handler = ElementHandler(self.driver)

    def click(self, locator, img_doc=None, wait_time=15, poll_frequency=0.5, ignored_exceptions=False):
        """
        左单击
        :param locator: 定位元组，元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 定位异常截图
        :param wait_time: 等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
        :return:
        """
        try:
            # 显示等待：获取存在的元素
            self.element_handler.wait_presence_element(locator).click()
        except Exception as e:
            logger.error(f"点击操作失败,失败原因：{e}")
            # self.save_screenshot(img_doc)
            raise

    def move_to_element(self, locator, img_doc=None, wait_time=15, poll_frequency=0.5, ignored_exceptions=False):
        """
        鼠标悬停
        :param locator: 定位元组，元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 定位异常截图
        :param wait_time: 等待超时时间
        :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
        :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
        :return:
        """
        try:
            locator = self.element_handler.wait_presence_element(locator)
            self.mouse_action(self.driver).move_to_element(locator).perform()

        except Exception as e:
            logger.error(f"鼠标悬浮操作失败,失败原因：{e}")



    # def click_element(self, driver, locator, img_doc=None, wait_time=15, poll_frequency=0.5, ignored_exceptions=False):
    #     """
    #     鼠标悬停
    #     :param locator: 定位元组，元组类型。(元素定位策略,元素定位表达式)
    #     :param img_doc: 定位异常截图
    #     :param wait_time: 等待超时时间
    #     :param poll_frequency: 检测的间隔时间(每间隔多长时间检测一下条件是否满足)，默认为0.5秒。
    #     :param ignored_exceptions: 超时后的异常，默认情况下抛出NoSuchElementException
    #     :return:
    #     """
    #     try:
    #         # 显示等待：获取存在的元素
    #         self.wait_presence_element(locator, img_doc, wait_time, poll_frequency).click()
    #         actions(driver).move_to_element(ele).perform()  # 鼠标悬浮 菜单栏中的：【更多】
    #
    #     except Exception as e:
    #         logger.error(f"点击操作失败,失败原因：{e}")
    #         # self.save_screenshot(img_doc)
    #         raise
    #
