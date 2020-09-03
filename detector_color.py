# -*- coding: utf-8 -*
import colorsys
import PIL.Image as Image

filename=raw_input("請輸入圖片: ")
def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count,(r,g,b) in image.getcolors(image.size[0]*image.size[1]):
        # 轉爲HSV標準
        saturation = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)[1]
        y = min(abs(r*2104+g*4130+b*802+4096+131072)>>13,235)
        y = (y-16.0)/(235-16)

        #忽略高亮色
        if y > 0.9:
            continue
        score = (saturation+0.1)*count
        if score > max_score:
            max_score = score
            dominant_color = (r,g,b)
    return dominant_color


if __name__ == '__main__':
    image = Image.open(filename)
    image = image.convert('RGB')
    print(get_dominant_color(image))