# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：get_file_stream.py
import chardet


class FileStream:

    def __init__(self, file_path):
        self.file_path = file_path
        self.read_yaml_file_by_self_encoding()

    def __verification_coding(self):
        with open(self.file_path, "rb") as vf:
            self.file_coding = chardet.detect(vf.read()).get("encoding")

    def verify(self):
        self.__verification_coding()
        return self.file_coding

    def read_yaml_file_by_self_encoding(self):
        self.__verification_coding()
        self.stream = open(file=self.file_path, mode="r", encoding=self.file_coding)


if __name__ == '__main__':
    print(FileStream("/Volumes/huace/PiPyProject/YamlTo/test.yaml").verify())
