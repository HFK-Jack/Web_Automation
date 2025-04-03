"""
前后置处理：项目全局
"""
import time
import pytest
from send_notification.weixin import SendWeiXinMessage
from driver_handler.webdriver_handler import GetWebdriver
from public_method.logger_handler import logger
from public_method.yaml_handler import yaml_handlers
from public_method.project_path import project_path

web_driver = GetWebdriver()  # 获取 webdriver
send_weixin_message = SendWeiXinMessage()


@pytest.fixture(scope="session", autouse=True)
def chrome_driver():
    """
    前后置处理（启动/关闭浏览器）
    :yield: 把driver放入全局，接收此函数即可直接使用 driver，无需调用
    """
    driver = web_driver.chrome_browser_mode()
    logger.info(f"获取chrome浏览器webdriver")

    yield driver

    driver.quit()
    logger.info("自动化测试结束")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    发送微信公众号通知
    @param terminalreporter: pytest 收集测试结果
    @return:
    """
    # url = os.environ['TestURL']
    test_url = yaml_handlers.read_yaml(project_path.test_environment)["test_url"]
    total = terminalreporter._numcollected  # 用例总数
    passed = len(terminalreporter.stats.get("passed", []))  # 成功数
    failed = len(terminalreporter.stats.get("failed", []))  # 失败数
    error = len(terminalreporter.stats.get("error", []))  # 异常数
    skipped = len(terminalreporter.stats.get("skipped", []))  # skip数
    deselected = len(terminalreporter.stats.get("deselected", []))  # 过滤的用例数
    rerun = len(terminalreporter.stats.get('rerun', []))  # 失败重跑总次数
    duration = time.time() - terminalreporter._sessionstarttime  # 执行时长
    success = round(passed / (total - deselected) * 100)  # 成功率
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 执行时间

    message = {"test_url": test_url, "total": total, "passed": passed, "failed": failed,
               "deselected": deselected, "skipped": skipped, "error": error,
               "success": success, "duration": duration, "click_url": "https://www.baidu.com/", "now_time": now_time}

    # 获取测试报告数据
    weixin_message = send_weixin_message.get_send_data(**message)

    # 发送报告
    # if os.environ['TestURL'] == 'https://show.everjiankang.cn':
    if test_url == 'https://show.everjiankang.cn':
        print(f"当前用例执行率{success}%,用例成功率低于100%，发送微信报告！")
        send_weixin_message.send_message(weixin_message)
    else:
        send_weixin_message.send_message(weixin_message)

    # content = f"【自动化测试报告】\t\n" \
    #           f"测试环境：{test_url}\t\n" \
    #           f"用例总数：{total}\t\n" \
    #           f"执行用例总数：{total - deselected}\t\n" \
    #           f"执行成功数：{passed} \t\n" \
    #           f"执行失败数：{failed} \t\n" \
    #           f"执行ERROR数：{error} \t\n" \
    #           f"执行SKIP数：{skipped} \t\n" \
    #           f"执行成功数：{round(passed / (total - deselected) * 100)} %\t\n" \
    #           f"执行时长：{round(duration, 2)}秒 \t\n" \
    #           f"执行时间：{now_time} \t\n"
    # logger.info(f"测试结果！\t\n{content}")

# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     """
#     发送企业微信通知
#     :param terminalreporter: 收集测试结果方法
#     :param exitstatus:
#     :param config:
#     :return:
#     """
#     url = os.environ['TestURL']
#     total = terminalreporter._numcollected  # 用例总数
#     passed = len(terminalreporter.stats.get("passed", []))  # 成功数
#     failed = len(terminalreporter.stats.get("failed", []))  # 失败数
#     error = len(terminalreporter.stats.get("error", []))  # 异常数
#     skipped = len(terminalreporter.stats.get("skipped", []))  # skip数
#     duration = time.time() - terminalreporter._sessionstarttime  # 执行时间
#     deselected = len(terminalreporter.stats.get("deselected", []))  # 过滤的用例数
#     content = f"【自动化测试报告】\t\n" \
#               f"测试环境：{os.environ['TestURL']}\t\n" \
#               f"用例总数：{total}\t\n" \
#               f"执行用例总数：{total - deselected}\t\n" \
#               f"执行成功数：{passed} \t\n" \
#               f"执行失败数：{failed} \t\n" \
#               f"执行ERROR数：{error} \t\n" \
#               f"执行SKIP数：{skipped} \t\n" \
#               f"执行成功数：{round(passed / (total - deselected) * 100)} %\t\n" \
#               f"执行时长：{round(duration, 2)}秒 \t\n"
#
#     print(content)
#     success = round(passed / (total - deselected) * 100)
#     if success != 100:
#         print(f'当前用例执行率{success}%,用例成功率低于100%，发送企业微信报告！')
#         # 通过企业微信发送测试报告
#         send_message(total=total, testurl=url, passed=passed, failed=failed, duration=duration, deselected=deselected,
#                      skipped=skipped, error=error)
#         if os.environ['TestURL'] == 'https://show.everjiankang.cn':
#             yaml_handlers.update_by_key('/thc/data/files/uiconfige.yml', 'successtag', 'F')  # 若执行失败，则将successtag标签改成F
#         else:
#             yaml_handlers.update_by_key('/thc/data/files/uiconfige2.yml', 'successtag', 'F')  # 若执行失败，则将successtag标签改成F
#     else:
#         successtag = ''
#
#         if os.environ['TestURL'] == 'https://show.everjiankang.cn':
#             successtag = yaml.safe_load(open('/thc/data/files/uiconfige.yml', encoding='utf-8'))['successtag']
#         else:
#             successtag = yaml.safe_load(open('/thc/data/files/uiconfige2.yml', encoding='utf-8'))['successtag']
#
#         if successtag == 'F':
#             # 通过企业微信发送测试报告
#             send_message(total=total, testurl=url, passed=passed, failed=failed, duration=duration,
#                          deselected=deselected, skipped=skipped, error=error)
#             if os.environ['TestURL'] == 'https://show.everjiankang.cn':
#                 yaml_handlers.update_by_key('/thc/data/files/uiconfige.yml', 'successtag', 'T')  # 若执行失败，则将successtag标签改成T
#             else:
#                 yaml_handlers.update_by_key('/thc/data/files/uiconfige2.yml', 'successtag', 'T')  # 若执行失败，则将successtag标签改成T
