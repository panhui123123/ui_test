from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.utils.logger import get_logger
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import logging


class BaseAction(object):
    def __init__(self):
        """
        初始化参数
        :rtype:
        """
        if not cli_setup():
            # 连接手机
            auto_setup(__file__, logdir=True, devices=["Android:///", ])
        # 获取定位元素的驱动
        self.__poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        # 将控制台log输出级别设置为Error
        logger = get_logger("airtest")
        logger.setLevel(logging.ERROR)
        # 包名
        self.__package = "com.huiian.timing"
        # 获取屏幕宽度
        self.width = G.DEVICE.display_info['width']
        # 获取屏幕高度
        self.height = G.DEVICE.display_info['height']
        # 安装包路径
        self.__filePath = ""
        # airtest中api.py内置方法
        self.__keyEvent = keyevent
        self.__setattr = setattr
        self.__quit = quit
        # airtest中api.py内置方法
        self.__touch = touch

    def start_app(self):
        """
        打开app
        :return:
        """
        start_app(self.__package)

    def clear_app(self):
        """
        清除App数据
        :return:
        """
        clear_app(self.__package)

    def stop_app(self):
        """
        关闭App
        :return:
        """
        stop_app(self.__package)

    def install_app(self):
        """
        安装app
        :return:
        """
        install(self.__filePath)

    def uninstall_app(self):
        """
        卸载app
        :return:
        """
        uninstall(self.__package)

    def kill_app(self):
        """
        杀掉app
        :return:
        """
        shell("am force-stop '{}'".format(self.__package))

    def find_element(self, feature):
        """
        通过元素特性查找元素
        :param feature: 元素查找方法
        :return: 返回元素
        """
        if "text=" in feature:
            return self.__poco(text=str(feature[6:-1])).wait(timeout=5)
        # text模糊匹配
        if "textMatches=" in feature:
            return self.__poco(textMatches=str(feature[13:-1]))[0].wait(timeout=5)
        return self.__poco(feature).wait(timeout=5)

    def find_element_parent(self, feature):
        """
        通过该元素查找父亲元素
        :param feature:
        :return:
        """
        return self.find_element(feature).parent()

    def find_element_child(self, feature, child_feature):
        """
        查找子元素
        :param feature:元素特征
        :param child_feature:子元素特征
        :return:
        """
        return self.find_element(feature).offspring(child_feature)

    def find_element_children(self, feature):
        """
        查找元素的所有子元素
        :param feature:
        :return:
        """
        return self.find_element(feature).child()

    def touch_image(self, image_file, times=1):
        """
        点击图片元素
        :param image_file: 图片所在路径
        :param times:点击次数
        :return:
        """
        self.__touch(Template(image_file), times=times)

    def click_element(self, element):
        """
        点击元素
        :param element: 元素
        :return:
        """
        self.find_element(element).click()

    def long_click_element(self, element, duration):
        """
        长按元素
        :param element:
        :param duration:
        :return:
        """
        self.find_element(element).long_click(duration=duration)

    def click_element_wait(self, element, times=5):
        """
         等待一定时长找到元素后再点击
        :param element:元素
        :param times:
        :return:
        """
        self.find_element(element).wait(timeout=times).click()

    def set_text(self, element, content):
        """
        向文本框输入内容
        :param element: 元素
        :param content: 需要输入内容
        :return:
        """
        self.find_element(element).set_text(content)

    def get_text(self, element):
        """
        获取元素文本内容
        :param element:元素
        :return:
        """
        return self.find_element(element).get_text()

    def clear_text(self, element):
        """
        清空文本框内容
        :param element: 元素
        :return:
        """
        self.find_element(element).set_text("")

    def is_element_existed(self, element):
        """
        在一定时间内判断元素是否在页面中存在
        :param element:元素
        :return:在超时间内没有找到元素，返回False,若找到返回True
        """
        return self.find_element(element).wait(timeout=5).exists()

    def touch(self, coordinate):
        '''
        坐标点击
        :param coordinate:相对坐标百分比
        :return:
        '''
        real_coordinate = int(self.width * coordinate[0]), int(self.height * coordinate[1])
        self.__touch(real_coordinate)

    def swipe_to(self, start, end, duration=1):
        """
        滑动 从start 滑动到end
        :param start: 初始坐标 参数形式[x,y] 相对坐标百分比
        :param end: 需要滑动到的位置[x,y]
        :param duration:表示滑动时长，单位s
        :return:
        """
        start = int(self.width * start[0]), int(self.height * start[1])
        end = int(self.width * end[0]), int(self.height * end[1])
        self.__poco.swipe(start, end, duration=duration)

    def swipe_by_direction(self, coordinate, direction):
        """
        按照一定的方向滑动
        :param coordinate:初始位置坐标
        :param direction:方向 参数为left=[-0.1,0] right = [0.1,0] up = [0,-0.1] down = [0,0.1]
        :return:
        """
        self.__poco.swipe(coordinate, direction=direction)

    def drag_element(self, element1, element2):
        """
        把元素1拖拽到元素2的位置
        :param element1:元素1
        :param element2:元素2
        :return:
        """
        self.find_element(element1).drag_to(self.find_element(element2))

    def drag_element_by_coordinate(self, element, coordinate, duration=1):
        """
        将某个元素拖到某个坐标
        :param element: 元素
        :param coordinate: 坐标(x,y)
        :param duration:滑动时长
        :return:
        """
        self.__poco.swipe(element, coordinate, duration=duration)

    def get_screenshot(self, filename, msg=''):
        '''
        获取当前页面截图
        :return:
        '''
        snapshot(filename=os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\screenshot\\' + filename, msg=msg)

    def key_search(self):
        """
        搜索键
        :return:
        """
        self.__keyEvent("KEYCODE_SEARCH")

    def key_back(self):
        """
        返回键
        :return:
        """
        self.__keyEvent("KEYCODE_BACK")

    def key_enter(self):
        """
        Enter键
        :return:
        """
        self.__keyEvent("KEYCODE_ENTER")

    def key_code(self, key_name):
        """
        键盘按键
        表示键盘上的按键0-9 A-Z
        :param key_name: 0-9 A-Z
        :return:
        """
        keys = "KEYCODE_" + str(key_name)
        self.__keyEvent(keys)

    def setattr(self, element, attr, value):
        '''
        修改元素属性值
        :param element:元素任意属性
        :param attr: 修改元素属性的名称
        :param value:修改元素属性的值
        :return:
        '''
        self.__setattr(self.find_element(element), attr, value)

    def quit_driver(self):
        """
        驱动退出
        :return:
        """
        self.__quit()


if __name__ == '__main__':
    A = BaseAction()
    A.get_screenshot('111.png')

