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

    # 紫色衣服
    lower_purple = np.array([133, 24, 201])
    upper_purple = np.array([153, 44, 281])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['light purple'] = color_list

    # 紫色裙子
    lower_purple = np.array([151, 203, 38])
    upper_purple = np.array([171, 223, 118])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple1'] = color_list

    #灰色
    lower_gray = np.array([0, 0, 46])
    upper_gray = np.array([180, 43, 220])
    color_list = []
    color_list.append(lower_gray)
    color_list.append(upper_gray)
    dict['gray']=color_list

    # 白色
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list

    #紅色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red']=color_list

    # 紅色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    #橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

     #橙色
    lower_orange = np.array([0, 220, 141])
    upper_orange = np.array([27, 265, 295])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange1'] = color_list

    #黃色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    #綠色
    lower_green = np.array([21, 43, 46])
    upper_green = np.array([98, 265, 295])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    #青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list

    #lime
    lower_lime = np.array([50, 245, 215])
    upper_lime = np.array([70, 265, 295])
    color_list = []
    color_list.append(lower_lime)
    color_list.append(upper_lime)
    dict['lime'] = color_list

    #blue
    lower_blue = np.array([81, 64, 77])
    upper_blue = np.array([138, 265, 295])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue2'] = color_list

    #Magenta
    lower_magenta = np.array([140, 245, 215])
    upper_magenta = np.array([160, 265, 295])
    color_list = []
    color_list.append(lower_magenta)
    color_list.append(upper_magenta)
    dict['Magenta'] = color_list

    #Maroon
    lower_maroon = np.array([0, 245, 99])
    upper_maroon = np.array([10, 265, 179])
    color_list = []
    color_list.append(lower_maroon)
    color_list.append(upper_maroon)
    dict['Maroon'] = color_list

    #dark red
    lower_darkred = np.array([0, 245, 111])
    upper_darkred = np.array([10, 265, 191])
    color_list = []
    color_list.append(lower_darkred)
    color_list.append(upper_darkred)
    dict['dark red'] = color_list

    #brown
    lower_brown = np.array([169, 221, 138])
    upper_brown = np.array([189, 241, 218])
    color_list = []
    color_list.append(lower_brown)
    color_list.append(upper_brown)
    dict['brown'] = color_list

    #brown1
    lower_brown1 = np.array([1, 202, 108])
    upper_brown1 = np.array([26, 265, 265])
    color_list = []
    color_list.append(lower_brown1)
    color_list.append(upper_brown1)
    dict['brown1'] = color_list

    #tomato
    lower_tomato = np.array([1, 206, 108])
    upper_tomato = np.array([23, 265, 265])
    color_list = []
    color_list.append(lower_tomato)
    color_list.append(upper_tomato)
    dict['tomato'] = color_list

    #coral
    lower_coral = np.array([0, 191, 215])
    upper_coral = np.array([20, 211, 295])
    color_list = []
    color_list.append(lower_coral)
    color_list.append(upper_coral)
    dict['coral'] = color_list

    #indianred
    lower_indianred = np.array([0, 151, 179])
    upper_indianred = np.array([10, 171, 259])
    color_list = []
    color_list.append(lower_indianred)
    color_list.append(upper_indianred)
    dict['indianred'] = color_list

    #lightcoral
    lower_lightcoral = np.array([0, 126, 215])
    upper_lightcoral = np.array([10, 146, 295])
    color_list = []
    color_list.append(lower_lightcoral)
    color_list.append(upper_lightcoral)
    dict['lightcoral'] = color_list

    #darksalmon
    lower_darksalmon = np.array([0, 127, 204])
    upper_darksalmon = np.array([18, 147, 284])
    color_list = []
    color_list.append(lower_darksalmon)
    color_list.append(upper_darksalmon)
    dict['darksalmon'] = color_list

    #salmon
    lower_salmon = np.array([0, 142, 215])
    upper_salmon = np.array([13, 162, 295])
    color_list = []
    color_list.append(lower_salmon)
    color_list.append(upper_salmon)
    dict['salmon'] = color_list

    #lightsalmon
    lower_lightsalmon = np.array([0, 136, 215])
    upper_lightsalmon = np.array([20, 156, 295])
    color_list = []
    color_list.append(lower_lightsalmon)
    color_list.append(upper_lightsalmon)
    dict['lightsalmon'] = color_list

    #orangered
    lower_orangered = np.array([0, 245, 215])
    upper_orangered = np.array([14, 265, 295])
    color_list = []
    color_list.append(lower_orangered)
    color_list.append(upper_orangered)
    dict['orangered'] = color_list

    #golden_rod
    lower_golden_rod = np.array([11, 245, 150])
    upper_golden_rod = np.array([39, 265, 295])
    color_list = []
    color_list.append(lower_golden_rod)
    color_list.append(upper_golden_rod)
    dict['golden_rod'] = color_list

    #khaki
    lower_khaki = np.array([19, 111, 148])
    upper_khaki = np.array([40, 136, 279])
    color_list = []
    color_list.append(lower_khaki)
    color_list.append(upper_khaki)
    dict['khaki'] = color_list

    #olive
    lower_olive = np.array([21, 245, 92])
    upper_olive = np.array([41, 265, 172])
    color_list = []
    color_list.append(lower_olive)
    color_list.append(upper_olive)
    dict['olive'] = color_list

    #藍色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    #beige
    lower_beige = np.array([8, 21, 207])
    upper_beige = np.array([43, 74, 295])
    color_list = []
    color_list.append(lower_beige)
    color_list.append(upper_beige)
    dict['beige'] = color_list


    return dict


if __name__ == '__main__':
    color_dict = getColorList()
    print(color_dict)

    num = len(color_dict)
    print('num=',num)

    for d in color_dict:
        print('key=',d)
        print('value=',color_dict[d][1])