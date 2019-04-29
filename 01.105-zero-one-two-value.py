
'''
将lena图片进行二值化，像素值大于128的变为1，否则变为0
'''

from skimage import io,data,color

img=data.chelsea()

# 使用了color模块的rgb2gray（）函数，将彩色三通道图片转换成灰度图。转换结果为float64类型的数组，范围为[0,1]之间。
img_gray = color.rgb2gray(img)
rows, cols = img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i, j] <= 0.5):
            img_gray[i, j] = 0
        else:
            img_gray[i,j] = 1
        pass
    pass

io.imshow(img_gray)

# 将彩色三通道图片转换成灰度图,最后变成unit8, float转换为unit8是有信息损失的。