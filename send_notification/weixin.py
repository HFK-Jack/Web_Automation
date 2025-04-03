# Time        : 2023/3/2 0:25
# Coding      : * utf-8 *
# Author      : < HFK >
# FileName    : weixin.py
# Description :

import json
import requests
from public_method.logger_handler import logger
from public_method.project_path import project_path
from public_method.yaml_handler import yaml_handlers


class SendWeiXinMessage:

    def __init__(self) -> None:

        self.weixin_config = yaml_handlers.read_yaml(project_path.weixin_config)
        self.app_id = self.weixin_config["app_id"]  # 微信公众号 appID
        self.app_secret = self.weixin_config["app_secret"]  # 微信公众密钥
        self.to_user = self.weixin_config["to_user"]  # 消息接收者
        self.template_id = self.weixin_config["template_id"]  # 消息模板id

    def get_access_token(self) -> str:
        """
        获取access_token凭证
        :return: access_token
        """
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            logger.info(f"获取微信 access_token 失败，微信返回结果为：{result}")

    def get_send_data(self, **kwargs) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        @param app_id: 微信公众测试号 appID：wxcf354e0764bfe9fa
        @param app_secret: 微信公众测试号密钥：98877fc9f862aed9d90a380815188ed6
        @param touser: 消息接收者，微信号(测试号用户列表里的微信号)
        @param template_id: 消息模板id
        @param click_url: 点击通知跳转的链接（可无）
        :return: 发送的消息体
        """
        json_data = {
            "touser": self.to_user,
            "template_id": self.template_id,
            "url": kwargs["click_url"],
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "url": {
                    "value": kwargs["test_url"],  # 测试环境
                    # 字体颜色
                    "color": "#173177"
                },
                "total": {
                    "value": kwargs["total"],  # 执行用例总数
                    "color": "#173177"
                },
                "passed": {
                    "value": kwargs["passed"],  # 执行成功数量
                    "color": "#173177"
                },
                "failed": {
                    "value": kwargs["failed"],  # 执行失败数量
                    "color": "#173177"
                },
                "deselected": {
                    "value": kwargs["deselected"],  # 过滤用例数量
                    "color": "#173177"
                },
                "skipped": {
                    "value": kwargs["skipped"],  # 执行skip数量
                    "color": "#173177"
                },
                "error": {
                    "value": kwargs["error"],  # 执行error数量
                    "color": "#173177"
                },
                "success": {
                    "value": str(kwargs["success"])+" %",  # 执行成功率
                    "color": "#173177"
                },
                "duration": {
                    "value": str(kwargs["duration"])+" 秒",  # 执行时长
                    "color": "#173177"
                },
                "now_time": {
                    "value": str(kwargs["now_time"]),  # 执行时间
                    "color": "#173177"
                },
            }
        }

        return json_data

    def send_message(self, json_data) -> None:
        """
        向公众号发送消息
        :param json_data: 需要发送的数据，json格式
        :return:
        """
        self.access_token = self.get_access_token()

        # 模板消息请求地址
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(json_data)
        resp = requests.post(url, data=data)
        result = resp.json()
        if result["errcode"] == 0:
            print("测试结果成功发送至微信！")
            logger.info("测试结果成功发送至微信！")
        else:
            print(f"测试结果发送至微信失败！失败原因是{result}")
            logger.info(f"测试结果发送至微信失败！失败原因是{result}")


# if __name__ == "__main__":
#     click_url = "https://www.baidu.com/"  # 点击通知跳转的链接（可无）
#     json_data = {"test_url": "https://www.baidu.com/", "total": "100", "passed": "100",
#                  "failed": "100", "deselected": "100", "skipped": "100", "error": "100",
#                  "success": "100", "duration": "100", "click_url": click_url}
#
#     sd = SendWeiXinMessage()
#     data = sd.get_send_data(**json_data)
#     sd.send_message(data)
