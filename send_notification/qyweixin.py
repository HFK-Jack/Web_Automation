"""
企业微信：发送通知
"""
import os
import datetime

import requests


def qyweixin(data):
    """
    对接企业微信应用消息方法,具体接口信息请参考 http://doc.everjiankang.com/pages/viewpage.action?pageId=111575339
    :param data: 发送企业信息的消息体内容
    :return:
    """
    url = 'http://test.thc/api/qyweixin'
    response = requests.post(url=url, json=data)
    print(response.text)
    return response


def send_message(total, testurl, passed, failed, duration, deselected, skipped, error):
    job_number = os.environ.get('job_number')
    job_user = os.environ.get('BUILD_USER')
    job_name = os.environ.get('JOB_NAME')

    if job_number:
        url_address = f"http://test.thc:8888/jenkins/job/{job_name}/{job_number}/allure/"
    else:
        url_address = f"http://test.thc:8888/jenkins/job/{job_name}/allure/"
    data = {
        "touser": "@all",  # 成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
        "msgtype": "markdown",  # 必填项 消息类型，此时固定为：template_card
        "agentid": 1000048,  # 必填项 企业应用的id，整型，这个写死测试组专用的应用id 不需要更改，除非换应用。
        # "textcard": {
        #     "title": "Web UI自动化测试报告",
        #     "description": f"<div class=\"gray\">{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div> "
        #                    f"\n"
        #                    f"用例总数：{total}\n"
        #                    f"执行总数：{total - deselected}\n"
        #                    f"执行成功：{passed}\n"
        #                    f"执行失败：{failed}\n"
        #                    f"执行skip：{skipped}\n"
        #                    f"执行error：{error}\n"
        #                    f"<div class=\'highlight\'>成  功  率：{round(passed / (total - deselected) * 100)} %</div>"
        #                    f"执行时长：{round(duration, 2)} 秒\n"
        #                    f"<div class=\"normal\">执  行  人：{job_user}</div>",
        #     "url": url_address,
        #     "btntxt": "查看详情"
        # },
        "markdown": {
            "content": "**Web UI自动化测试报告**\n"
                       "\n"
                       f">【用例总数】：{total}\n"
                       f">【测试地址】：{testurl}\n"
                       f">【执行总数】：{total - deselected}\n"
                       f">【执行成功】：<font color=\"#008000\">{passed}</font>\n"
                       f">【执行失败】：<font color=\"#FF0000\">{failed}</font>\n"
                       f">【执行skip】：{skipped}\n"
                       f">【执行error】：{error}\n"
                       f">【成  功  率】：<font color=\"warning\">{round(passed / (total - deselected) * 100)} %</font>\n"
                       f">【执行时长】：{round(duration, 2)} 秒\n"
                       f">【执  行  人】：{job_user}\n"
                       f"\n"
                       f"<font color=\"comment\">{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</font>\n"
                       f"[请相关人员 查看详情报告]({url_address})\n"
        }
    }

    if job_name:
        qyweixin(data)
    else:
        print("提示：检测到目前处于本地调试阶段，不需要发布报告")
