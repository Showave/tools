# -*- coding: utf-8 -*-

path = './test.txt'
def read_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
  
