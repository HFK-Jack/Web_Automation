from public_method.allure_report_handler import AllureReportHandler


if __name__ == "__main__":

    ARH = AllureReportHandler()
    ARH.all_case_report()   # 收集所有 case 执行结果
    # ARH.case_severities_report(severities=66)  # 根据case的重要性程度：收集 case 执行结果

    # # 通过企业微信发送测试报告
    # send_message()


# if __name__ == "__main__":

    # pytest.main()  # 运行 pytest
    # pytest.main(['-vs', './test_case_po/test_buy_internet_medical_treatment.py', '-x'])


# os.system("pytest -sq --alluredir ./test_report_data/")  # 收集所有测试结果
    # # os.system("pytest -sq --alluredir ./test_report_data/ --allure-severities=minor,normal,critical,blocker")  # 按重要级别收集测试结果
    # os.system("allure generate ./test_report_data/ -o ./百宝箱/ --clean")   # 生成allure报告
    # os.system("allure open -h 127.0.0.1 -p 8866 ./百宝箱/")    # 打开报告
    # os.system：执行系统命令
    # allure generate ： 固定写法
    # ../test_report：json格式的临时报告的目录
    # -o ../test_report ： 输出报告的地址（报告生成的地址）
    # --clean ： 清除已经存在的报告


