# -*- coding: utf-8 -*
import numpy as np
import collections

#定義字典存放顏色分量上下限
#例如：{顏色: [min分量, max分量]}
#{'red': [array([160,  43,  46]), array([179, 255, 255])]}

def getColorList():
    dict = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    #灰色
    lower_gray = np.array([0, 0, 46])
    upper_gray = np.array([10, 10, 220])
    color_list = []
    color_list.append(lower_gray)
    color_list.append(upper_gray)
    dict['gray']=color_list

    # 白色
    lower_white = np.array([0, 0, 228])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list

    #紅色
    lower_red = np.array([163, 59, 88])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red']=color_list

    # 紅色2
    lower_red = np.array([0, 88, 88])
    upper_red = np.array([12, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    #橙色
    lower_orange = np.array([11, 88, 87])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list


    #黃色
    lower_yellow = np.array([23, 78, 87])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    #綠色
    lower_green = np.array([33, 60, 88])
    upper_green = np.array([85, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    #青色
    lower_cyan = np.array([84, 59, 87])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list

    #藍色
    lower_blue = np.array([95, 59, 87])
    upper_blue = np.array([135, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    lower_purple = np.array([135, 60, 88])
    upper_purple = np.array([147, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    #pink
    lower_pink = np.array([152, 59, 88])
    upper_pink = np.array([163, 255, 255])
    color_list = []
    color_list.append(lower_pink)
    color_list.append(upper_pink)
    dict['pink'] = color_list


    return dict


if __name__ == '__main__':
    color_dict = getColorList()
    print(color_dict)

    num = len(color_dict)
    print('num=',num)

    for d in color_dict:
        print('key=',d)
        print('value=',color_dict[d][1])