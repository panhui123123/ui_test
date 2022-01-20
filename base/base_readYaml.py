import yaml
import os


class ReadYaml:
    def read_yaml_data(self, file_path):
        file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\config\{}'.format(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            # 读出来是字符串
            data = f.read()
            # 需要用yaml.load()转化为字典
            yaml_data = yaml.load(data, Loader=yaml.Loader)
            return yaml_data
