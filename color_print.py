#-*- coding: utf-8 -*-

import datetime

"""
file: color_print.py
author: Liu
date: 2021-06-27
des: print sentence with colored
python 带颜色输出脚本
"""

def color_print(str_sentence = None, color = 'green'):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    str_sentence = str(str_sentence)
    try:
        if color is not None:
            list_str_colors = ['darkbrown', 'red', 'green', 'yellow', 'blue', 'purple', 'yank', 'white']
            assert str_sentence is not None and color in list_str_colors
            id_color = 30 + list_str_colors.index(color)
            print('\33[1;35;{}m'.format(id_color) + now + " " + str_sentence + '\033[0m')
        else:
            print(now + " " + str_sentence)
    except Exception as e:
        print('error in echosentence_color {}'.format(str(e)))
        raise
