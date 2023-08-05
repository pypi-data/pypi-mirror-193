# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：transformation.py
import yaml
from hctestedu.yaml_format.get_file_stream import FileStream


class YamlTo(FileStream):

    def __init__(self, path):
        super(YamlTo, self).__init__(file_path=path)

    def json(self):
        """读取yaml文件返回json数据"""
        d = yaml.safe_load(self.stream)
        return d

    def list(self):
        """读取yaml文件返回list文件"""
        d = yaml.safe_load(self.stream)
        print(list(d))


if __name__ == '__main__':
    """下面是使用的例子，如果需要使用，请修改yaml_path"""
    yaml_path = "/Volumes/huace/PiPyProject/YamlTo/test.yaml"
    print(YamlTo(yaml_path).list())
    print(YamlTo(yaml_path).json())
