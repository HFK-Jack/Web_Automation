"""
excel数据驱动器
"""

from openpyxl import load_workbook


class ExcleHandles:
    """excel 封装"""

    def __init__(self, excel_path):
        self.excel = excel_path

    # 选择表单功能
    def get_sheet(self, sheet_index=None, sheet_name=None):
        """
        传入sheet页的名字 获取sheet表单对象
        :param sheet_name: sheet页名称
        :param sheet_index: sheet页名索引
        :return:  返回sheet表单对象
        """
        wb = load_workbook(self.excel)
        if sheet_name is not None:
            sheet = wb[sheet_name]
        else:
            sheet = wb.worksheets[sheet_index]
        # wb.close()
        return sheet

    # 读取一个单元格的数据功能
    def get_date_cell(self, row, column, sheet_name=None, sheet_index=None):
        """
        获取指定单元格内容
        :param sheet_name:  sheet页名称
        :param sheet_index:  sheet页索引
        :param row:  行号 从1开始
        :param column: 列号 从1 开始
        :return:  返回指定的单元格内容
        """
        data = self.get_sheet(sheet_name=sheet_name, sheet_index=sheet_index)
        return data.cell(row=row, column=column).value

    # 读取一行数据功能
    # 读取表单中所有数据功能)(只传入表单名称或索引)
    def get_date_row(self, sheet_name=None, sheet_index=None, row_begin=0, row_end=None):
        """
        读取某一行的单元格内容 从0开始 默认读取所有行数
        :param sheet_name:  sheet页名称
        :param sheet_index:  sheet页索引
        :param row_begin:  开始行
        :param row_end:  结束行
        :return:  数据列表
        """
        data = self.get_sheet(sheet_name=sheet_name, sheet_index=sheet_index)
        row_data = []
        for rows in list(data.rows)[row_begin: row_end]:
            tmp = []
            for cell in rows:
                if  isinstance(cell.value , str) and  '[' in cell.value:
                    tmp.append(eval(cell.value))
                else:
                    tmp.append(cell.value)
            row_data.append(tmp)
        return row_data

    # 读取一列数据功能
    def get_date_column(self, sheet_name=None, sheet_index=None, row_begin=0, row_end=None):
        """
        读取某一列的单元格内容 从0开始 默认读取所有列数
        :param sheet_name: sheet页名称
        :param sheet_index:   sheet页索引
        :param row_begin: 开始行
        :param row_end: 结束行
        :return:  数据列表
        """
        data = self.get_sheet(sheet_name=sheet_name, sheet_index=sheet_index)
        columns_data = []
        for columns in list(data.columns)[row_begin: row_end]:
            tmp = []
            for cell in columns:
                tmp.append(cell.value)
            columns_data.append(tmp)
        return columns_data

    # 往单元格中写入数据功能
    def update_date_cell(self, row, column, new_value, sheet_name=None, sheet_index=None, excel_path=None):
        """
        修改单元格内容
        :param row:  行 号
        :param column:  列号
        :param new_value:  新值
        :param sheet_name:
        """
        # 修改单元格功能。
        wb = load_workbook(self.excel)
        if sheet_name is not None:
            sheet = wb[sheet_name]
        else:
            sheet = wb.worksheets[sheet_index]
        sheet.cell(row, column).value = new_value
        self.save_data(wb, excel_path=excel_path)

    # 6、保存数据功能
    def save_data(self, wb, excel_path):
        wb.save(self.excel)
        wb.close

    def get_first_list(self, sheet_name, first_info):
        '''
        根据第1列内容获取每行的数据
        :param sheet_name:   sheet页名称
        :param first_info:  第一行内容
        :return:
        '''
        tmp_list = self.get_date_row(sheet_name=sheet_name)
        result = []
        for index in tmp_list:
            if index[0] == first_info:
                tmp = index[1:]
                # 列表推导式 去除空值
                new_list = [check_none for check_none in tmp if check_none is not None]
                result.append(new_list)
                # print(new_list)
        return result

    def headers(self):
        """获取标题"""
        self.open()
        headers = [c.value for c in self.sheet[1]]
        self.wb.close()
        return headers

    def read(self, start_row=2, start_column=1):
        """获取所有的数据"""
        self.open()
        sheet = self.sheet

        header = [c.value for c in sheet[1]]

        data = []
        for row in range(start_row, sheet.max_row + 1):
            row_data = []
            for column in range(start_column, sheet.max_column + 1):
                row_data.append(sheet.cell(row, column).value)
            row_data = dict(zip(header, row_data))
            data.append(row_data)
        self.wb.close()
        return data

    def save(self):
        """保存"""
        self.wb.save(self.file_name)
        self.wb.close()

    # 为什么之前不能做为实例属性？？
    # 静态，明白。
    def write(self, row, column, data):
        self.open()
        self.sheet.cell(row, column).value = data
        self.save()


class ExcelHandler2:
    """excel 封装"""

    # 项目来说可能不变
    # 测试数据，写代码之前之前已经写好测试数据的Excel. 文件名
    def __init__(self, file_name):
        self.file_name = file_name
        self.wb = load_workbook(file_name)
        # if isinstance(sheet_name, int):
        #     self.sheet =  self.wb.worksheets[sheet_name]
        # else:
        #     self.sheet = self.wb.get_sheet_by_name(sheet_name)

    def choose_sheet(self, sheet_name):
        """选择表单.
        sheet_name 是整数，根据索引获取。
        如果是字符串，根据名字获取 '20190920'
        """
        if isinstance(sheet_name, int):
            return self.wb.worksheets[sheet_name]
        return self.wb[sheet_name]

        # 索引

    def read_line(self, sheet_name, line):
        """获取行"""
        sheet = self.choose_sheet(sheet_name)
        sheet_data = sheet[line]
        # 元组 （Cell(1,1), Cell(1,2）
        data = []
        for c in sheet_data:
            data.append(c.value)
        return data

    def read(self, sheet_name, start_row=2, start_column=1):
        """获取所有的数据"""
        sheet = self.choose_sheet(sheet_name)
        # max_row, max column
        data = []
        for row in range(start_row, sheet.max_row + 1):
            row_data = []
            for column in range(start_column, sheet.max_column + 1):
                row_data.append(sheet.cell(row, column).value)
            data.append(row_data)
        return data

    def read_cell(self, sheet_name, row, column):
        """一个单元格的数据"""
        sheet = self.choose_sheet(sheet_name)
        return sheet.cell(row, column).value

    def save(self):
        """保存"""
        self.wb.save(self.file_name)
        self.wb.close()

    @staticmethod
    def write(file_name, sheet_name, row, column, data):
        wb = load_workbook(file_name)
        sheet = wb.get_sheet_by_name(sheet_name)
        sheet.cell(row, column).value = data
        # 保存关闭
        wb.save(file_name)
        wb.close()

