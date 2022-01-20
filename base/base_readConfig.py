import configparser
import os

class Config:
    def __init__(self):
        # 初始化方法，获取一个config对象
        self.config = configparser.ConfigParser()

    def read_config(self, config_filename, section, key):
        """
        :param config_filename: config文件名
        :param section: section
        :param key: key
        :return:
        """
        config_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\config\{}'.format(config_filename)
        self.config.read(config_path, encoding='utf-8')
        return self.config.get(section, key)




