# -*- coding: utf-8 -*
import  cv2
import numpy as np
import color_list_new


#處理圖片
def get_color(frame):
    print('go in get_color')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = color_list_new.getColorList()
    for d in color_dict:
        #mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
        mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
        cv2.imwrite(d+'.jpg',mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary,None,iterations=2)
        cnts, hiera = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum+=cv2.contourArea(c)
        if sum > maxsum :
            maxsum = sum
            color = d

    return color


if __name__ == '__main__':
    filename=raw_input("請輸入圖片: ")
    frame = cv2.imread(filename)
    print(get_color(frame))
    img=cv2.imread(filename)
    cv2.imshow("image",img)
    # 按下任意鍵則關閉所有視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()