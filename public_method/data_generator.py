"""
数据生成
"""
import datetime
from faker import Faker


class DataGenerator:

    def __init__(self):
        # 获取当前时间
        self.date_now = datetime.datetime.now()
        # 初始化，设置locale为中文；默认是英文
        self.fake = Faker(locale='zh_CN')

    def random_patient_mobile(self):
        """
        随机生成手机号
        :return:
        """

        mobile = self.fake.phone_number()

        return mobile

    def random_identity_card(self):
        """
        随机生成身份证
        :return:
        """

        # 获取随机身份证
        identity_card = self.fake.ssn()

        return identity_card

    def identity_card_sex(self, identity_card):
        """
        随机生成身份证
        :return:
        """

        # 获取当前身份证的性别
        if int(identity_card[16:17]) % 2 == 0:
            identity_card_sex = "女"
        else:
            identity_card_sex = "男"

        return identity_card_sex


    def random_patient_name(self):
        """
        随机生成患者姓名
        :return:
        """
        new_patient_name = f"hfk患者-{self.date_now.date()}-{self.date_now.hour}{self.date_now.minute}"

        return new_patient_name

# dg = DataGenerator()
# print(dg.random_patient_mobile())
# print(dg.random_patient_name())
# print(dg.random_patient_identity_card())
