"""
文件夹管理
"""

import os
import shutil
from public_method.project_path import project_path

class FolderHandler:

    def __init__(self):
        pass


    def clear_(self,folder_path=None):
        """
        清除文件
        :param folder_path: 文件夹路径
        :return:
        """
        shutil.rmtree(project_path.test_report_json_path)  # 删除文件夹
        os.mkdir(project_path.test_report_json_path)  # 新建文件夹


# if __name__ == "__main__":
#     fh = FolderHandler()
#     print(project_path.test_report_json_path)
#     fh.clear_history_report()
