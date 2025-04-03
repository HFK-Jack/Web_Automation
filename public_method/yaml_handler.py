"""
    yaml-配置元件处理模块
"""

import yaml


class YamlHandlers:

    def __init__(self):

        pass
        # app_driver_config.yaml 路径
        # self.app_driver_configs_path = os.path.join(project_path.android_config_file_path, "app_driver_config.yaml")

    def read_yaml(self, file_path):
        """
        读取 yaml 文件
        :param file_path: yaml文件路径
        :return:
        """

        with open(file_path, "r", encoding="utf-8") as yaml_obj:
            file_obj = yaml_obj.read()
            yaml_data = yaml.load(file_obj, Loader=yaml.FullLoader)
            return yaml_data


    # def read_app_driver_config(self):
    #     """
    #     读取 app_driver_config.yaml
    #     :return: 文件数据
    #     """
    #
    #     return self.read_yaml(self.app_driver_configs_path)

    # 修改yaml文件
    def update_by_key(self, file_path, nodeName, newvalue):
        """
        添加/更新 yaml文件的数据
        @param file_path: 文件地址
        @param nodeName:  数据-键
        @param newvalue:  数据-值
        @return:
        """
        with open(file_path, encoding='utf-8') as file:  # 根据file_path地址指定的文件，读取文件数据
            dic_data = yaml.safe_load(file)  # 将文件数据格式化成yaml格式，并赋给 dic_data 变量
            dic_data[nodeName] = newvalue

        # 将新赋值的 dic_data 数据，重新写入file_path地址指定的文件当中
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(dic_data, stream=file, allow_unicode=True, sort_keys=False)



yaml_handlers = YamlHandlers()


# if __name__ == "__main__":
#     YH = YamlHandlers()
    # # app_driver_config.yaml 数据
    # app_driver_config_data = YH.read_app_driver_config()
    # print(app_driver_config_data)

    # log_config.yaml 数据
    # log_config_data = YH.read_yaml(project_path.test_buy_internet_medical_treatment)
    # print(log_config_data)



