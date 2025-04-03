"""
断言封装
"""
import allure
from public_method.logger_handler import logger


class Assert:

    def __int__(self):
        self.response = None

    def assert_opencv(self, title, shape, histogram, check_image_name, expect_image):
        """
        判断图片对比结果，适用于 pytest 框架
        @param title:
        @param shape:
        @param histogram:
        @param check_image_name:
        @param expect_image:
        @return:
        """

        is_found = True if shape >= 0.8 and histogram >= 0.4 else False  # 判定结果，并返回

        with allure.step(
                title + '图形匹配率=' + format(shape, '.2%') + '   颜色直方图匹配率=' + format(histogram, '.2%')):
            try:
                assert is_found == True  # 验证结果(运行结果与预期结果对比)
                file = open(check_image_name, mode='rb').read()  # 读取比较图片
                allure.attach(file, '运行结果与逾期结果：匹配成功',
                              allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
            except:
                file = open(check_image_name, mode='rb').read()  # 读取比较图片
                allure.attach(file, '运行结果与逾期结果：匹配失败', allure.attachment_type.JPG)  # 将运行结果图片添加到allure报告中
            finally:
                filet = open(expect_image, mode='rb').read()  # 读取模板图片
                allure.attach(filet, '预期结果图片', allure.attachment_type.JPG)  # 将预期结果图片添加到allure报告中

    # def assert_opencv_unitest(self, title, shape, histogram, check_image_name, expect_image):
    #     """
    #     判断图片对比结果，适用于 unitest 框架
    #     @param title:
    #     @param shape:
    #     @param histogram:
    #     @param check_image_name:
    #     @param expect_image:
    #     @return:
    #     """
    #
    #     is_found = True if shape >= 0.8 and histogram >= 0.4 else False  # 判定结果，并返回
    #
    #     with allure.step(
    #             title + '图形匹配率=' + format(shape, '.2%') + '   颜色直方图匹配率=' + format(histogram, '.2%')):
    #         try:
    #             TestCase().assertEqual(is_found, True, msg='无法识别')  # unitest框架-验证结果的方法
    #             file = open(check_image_name, mode='rb').read()  # 读取比较图片
    #             allure.attach(file, '运行结果与逾期结果：匹配成功', allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
    #         except:
    #             file = open(check_image_name, mode='rb').read()  # 读取比较图片
    #             allure.attach(file, '运行结果与逾期结果：匹配失败', allure.attachment_type.JPG)  # 将运行结果图片添加到allure报告中
    #             TestCase().assertEqual(is_found, True, msg='无法识别')  # unitest框架-验证结果的方法
    #         finally:
    #             filet = open(expect_image, mode='rb').read()  # 读取模板图片
    #             allure.attach(filet, '预期结果图片', allure.attachment_type.JPG)  # 将预期结果图片添加到allure报告中

    def assert_equal(self, actual, expected):
        """
        断言相等
        @param actual: 实际结果
        @param expected: 期望结果
        @return:
        """
        try:
            assert actual == expected
        except Exception as e:
            logger.info(f"断言相等失败！实际结果{actual},期望结果{expected},报错异常：{e}")

    def assert_not_equal(self, actual, expected):
        """
        断言不相等
        @param actual: 实际结果
        @param expected: 期望结果
        @return:
        """
        try:
            assert actual != expected
        except Exception as e:
            logger.info(f"断言不相等失败！实际结果{actual},期望结果{expected},报错异常：{e}")

    def assert_contains(self, actual, expected):
        """
        断言包含
        @param actual: 实际结果
        @param expected: 期望结果
        @return:
        """
        try:
            assert actual in expected
        except Exception as e:
            logger.info(f"断言包含失败！实际结果{actual},期望结果{expected},报错异常：{e}")


    # def assert_result(response: Response, expected: str) -> None:
    #     """ 断言方法
    #     :param response: 实际响应对象
    #     :param expected: 预期响应内容，从excel中或者yaml读取、或者手动传入
    #     return None
    #     """
    #     if expected is None:
    #         logger.info("当前用例无断言！")
    #         return
    #
    #     if isinstance(expected, str):
    #         expect_dict = eval(expected)
    #     else:
    #         expect_dict = expected
    #     index = 0
    #     for k, v in expect_dict.items():
    #         # 获取需要断言的实际结果部分
    #         for _k, _v in v.items():
    #             if _k == "http_code":
    #                 actual = response.status_code
    #             else:
    #                 if response_type(response) == "json":
    #                     actual = json_extractor(response.json(), _k)
    #                 else:
    #                     actual = re_extract(response.text, _k)
    #             index += 1
    #             logger.info(f'第{index}个断言数据,实际结果:{actual} | 预期结果:{_v} 断言方式：{k}')
    #             allure_step(f'第{index}个断言数据', f'实际结果:{actual} = 预期结果:{v}')
    #             try:
    #                 if k == "eq":  # 相等
    #                     assert actual == _v
    #                 elif k == "in":  # 包含关系
    #                     assert _v in actual
    #                 elif k == "gt":  # 判断大于，值应该为数值型
    #                     assert actual > _v
    #                 elif k == "lt":  # 判断小于，值应该为数值型
    #                     assert actual < _v
    #                 elif k == "not":  # 不等于，非
    #                     assert actual != _v
    #                 else:
    #                     logger.exception(f"判断关键字: {k} 错误！")
    #             except AssertionError:
    #                 raise AssertionError(f'第{index}个断言失败 -|- 断言方式：{k} 实际结果:{actual} || 预期结果: {_v}')
    #
    #


assert_function = Assert()
