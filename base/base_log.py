import logging
import os
import time


class Log:
    # 创建logger对象
    logger = logging.getLogger()
    # 设置logger对象的日志级别
    logger.setLevel(logging.WARNING)
    # 获取当前脚本的上上级路径，即整个项目的真实路径
    project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 日志文件路径
    log_path = project_path + r'\logs' + r'\{}.logs'.format(time.strftime('%Y_%m_%d__%H时%M分%S秒'))
    # 设置处理器，并指定文件名和读写模式
    file_handler = logging.FileHandler(filename=log_path, mode='w')
    # 处理器设置日志级别
    file_handler.setLevel(logging.WARNING)
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 添加日志格式到处理器中
    file_handler.setFormatter(formatter)
    # 添加处理器到logger对象中
    logger.addHandler(file_handler)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    print(Log().project_path)