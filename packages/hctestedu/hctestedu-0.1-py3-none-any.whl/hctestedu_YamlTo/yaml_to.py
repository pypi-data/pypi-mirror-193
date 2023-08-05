# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：transformation.py
import yaml
from hctestedu_YamlTo.yaml_format.get_file_stream import FileStream




class To(FileStream):

    def __init__(self, path):
        super(To, self).__init__(file_path=path)

    def json(self):
        d = yaml.safe_load(self.stream)
        return d

    def list(self):
        d = yaml.safe_load(self.stream)
        print(list(d))


if __name__ == '__main__':
    print(To("/Volumes/huace/PiPyProject/YamlTo/test.yaml").list())
