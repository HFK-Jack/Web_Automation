"""
    浏览器 webdriver 管理，支持浏览器多种运行模式。
    chrome 浏览器模式 + 环境变量已经配置chromedriver.exe使用：run_mode.chrome_browser_mode()
    chrome 浏览器模式 + 环境变量未配置chromedriver.exe使用：run_mode.chrome_browser_driver_mode()
    chrome 无头模式 + 环境变量已经配置chromedriver.exe使用：run_mode.chrome_headless_mode()
    chrome 无头模式 + 环境变量未配置chromedriver.exe使用：run_mode.chrome_headless_driver_mode()
    return webdriver
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class GetWebdriver:

    """随着selenium库的不断更新：新版本驱动导入"""
    # 环境变量未配置chromedriver.exe时：需要指定电脑的chromedriver.exe的位置
    # self.chromedriver_path = Service(r"C:\Users\Jack-\AppData\Local\Google\Chrome\Application\chromedriver.exe")

    """随着selenium库的不断更新：旧版本驱动导入"""
    # 环境变量未配置chromedriver.exe时：需要指定电脑的chromedriver.exe的位置
    chromedriver_path = r"C:\Users\Jack-\AppData\Local\Google\Chrome\Application\chromedriver.exe"

    def chrome_browser_mode(self):
        """
        chrome 浏览器模式 + 环境变量已经配置chromedriver.exe
        """

        driver = webdriver.Chrome()  # 启动浏览器获取 chrome_driver
        driver.maximize_window()  # 设置浏览器最大化
        return driver

    def chrome_browser_driver_mode(self):
        """
        chrome 浏览器模式 + 环境变量未配置chromedriver.exe
        """

        driver = webdriver.Chrome(executable_path=self.chromedriver_path)  # 启动浏览器获取 chrome_driver
        driver.maximize_window()  # 设置浏览器最大化
        return driver

    def chrome_headless_mode(self):
        """
        chrome 无头模式 + 环境变量已经配置chromedriver.exe
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 设置无头模式
        chrome_options.add_argument("--no-sandbox")  # 禁用沙箱【不加在liunx环境下运行会报错】
        chrome_options.add_argument("--disable-dev-shm-usage")  # 关闭dev-shm，此参数可解决“喔唷,崩溃啦!显示此网页时出了点问题。误代码: SIGTRAP”报错
        driver = webdriver.Chrome(options=chrome_options)  # 启动浏览器获取 chrome_driver
        driver.set_window_size(1920, 1080)  # 设置浏览器窗体的大小尺寸宽高
        return driver

    def chrome_headless_driver_mode(self):
        """
        chrome 无头模式 + 环境变量未配置chromedriver.exe
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 设置无头模式
        chrome_options.add_argument("--no-sandbox")  # 禁用沙箱【不加在liunx环境下运行会报错】
        chrome_options.add_argument("--disable-dev-shm-usage")  # 关闭dev-shm，此参数可解决“喔唷,崩溃啦!显示此网页时出了点问题。误代码: SIGTRAP”报错
        driver = webdriver.Chrome(executable_path=self.chromedriver_path, options=chrome_options)  # 启动浏览器获取 chrome_driver
        driver.set_window_size(1920, 1080)  # 设置浏览器窗体的大小尺寸宽高
        return driver


# run_mode = RunMode()
#
# driver = run_mode.chrome_browser_mode()
# # driver = run_mode.chrome_browser_driver_mode()
# # driver = run_mode.chrome_headless_mode()
# # driver = run_mode.chrome_headless_driver_mode()
#
# # 浏览器对象打开百度浏览器
# driver.get('http://www.baidu.com/')
#
# #  查看响应内容
# print(driver.page_source)
#
# sleep(5)
# # 关闭浏览器对象
# driver.quit()
