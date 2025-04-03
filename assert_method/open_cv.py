"""
测试图片对比
"""

import cv2
import numpy
from io import BytesIO
from PIL import Image


# 图形定位器
class GraphicalLocator:

    def __init__(self, img_path, driver):
        self.locator = img_path
        self.driver = driver

        # x, y 位置（以像素为单位）从左开始计数
        self.start_x = None  # 图片匹配的起始宽的坐标
        self.start_y = None  # 图片匹配的起始高的坐标
        self.base_img = cv2.imread(img_path)  # 根据基准图片路径，读取基准图片
        self.base_height = self.base_img.shape[0]  # 获取基准图片的高
        self.base_width = self.base_img.shape[1]  # 获取基准图片的宽
        self.threshold = None

    def find_me(self):
        # 清除最后找到的坐标
        self.start_x = self.start_y = None
        # 获取当前网页截图,此时获取的是一个PNG格式的图片
        new_img = self.driver.get_screenshot_as_png()

        # 通过BytesIO方法，读取PNG格式的图片在内存中的bytes，并返回一个BytesIO对象，供Image.open方法读取
        # 通过Image.open方法，读取BytesIO对象中的bytes数据，并返回一个image对象，供numpy.asarray方法转换
        new_img = Image.open(BytesIO(new_img))

        # 因OpenCV读取图片后返回的数据类型为numpy.ndarray，所以需要通过numpy.asarray方法将图片转换为numpy.ndarray类型的数据，
        # 至此，才算是将截屏出来的图片完全转换成为OpenCV可用的数据
        new_img = numpy.asarray(new_img, dtype=numpy.uint8)

        # 将图像从 BGR 转换为 RGB 格式
        new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

        '''-------------------------------------------------图形匹配-------------------------------------------------'''
        # 图像匹配
        # 1、将比较的图片从RGB转换为GRAY（灰度图）
        # 2、归一化相关系数匹配法

        matchresult = cv2.matchTemplate(cv2.cvtColor(new_img, cv2.COLOR_RGB2GRAY),
                                        cv2.cvtColor(self.base_img, cv2.COLOR_BGR2GRAY),
                                        cv2.TM_CCOEFF_NORMED)

        # 获取匹配结果矩阵中的最大值及其坐标，最小值及其坐标
        img_match = cv2.minMaxLoc(matchresult)
        '''-------------------------------------------------直方图匹配------------------------------------------------'''

        # 获取匹配度最大值的位置坐标，因匹配度最大的值存储在与模板图像左上角相对应的的原图像位置。所以该位置也是图像匹配的左上起始位置。
        self.start_x = img_match[3][0]
        self.start_y = img_match[3][1]

        # 从原图片中裁剪出与模板相匹配的图像，即（左上角高的位置+模板的高度）和（左上角宽的位置+模板的宽度）
        new_img_crop = new_img[self.start_y:(self.start_y + self.base_height),
                       self.start_x:(self.start_x + self.base_width)]

        # 计算模板和匹配图像的颜色直方图
        new_img_hist = cv2.calcHist([new_img_crop], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        base_img_hist = cv2.calcHist([self.base_img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

        # 直方图对比
        comp_hist = cv2.compareHist(base_img_hist, new_img_hist, cv2.HISTCMP_CORREL)
        '''-----------------------------------------------END------------------------------------------------------'''

        # 保存匹配结果：图形图像和图像直方图
        # 并对结果做保留2位小数操作
        self.threshold = {'shape': round(img_match[1], 4),
                          'histogram': round(comp_hist, 4)}

        # 在原图片中将与模板对比的部分画框
        return cv2.rectangle(new_img, (self.start_x, self.start_y),
                             (self.start_x + self.base_width, self.start_y + self.base_height),
                             (0, 0, 255), 2)

