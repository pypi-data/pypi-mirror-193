# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：get_file_stream.py
import chardet


class FileStream:

    def __init__(self, file_path):
        """
        :param file_path: 文件路径
        """
        self.file_path = file_path
        self.stream = None
        self.read_yaml_file_by_self_encoding()

    def __verification_coding(self):
        """
        确定文件的编码
        :return:
        """
        with open(self.file_path, "rb") as vf:
            self.file_coding = chardet.detect(vf.read()).get("encoding")

    def verify(self):
        """
        返回文件编码
        :return:
        """
        self.__verification_coding()
        return self.file_coding

    def read_yaml_file_by_self_encoding(self):
        """
        打开文件，并返回文件流。
        :return:
        """
        self.__verification_coding()
        self.stream = open(file=self.file_path, mode="r", encoding=self.file_coding)


if __name__ == '__main__':
    """下面是一个获取文件编码的例子，请需要使用请使用你自己的yaml文件路径"""
    yaml_path = "/Volumes/huace/PiPyProject/YamlTo/test.yaml"
    print(FileStream(yaml_path).verify())
