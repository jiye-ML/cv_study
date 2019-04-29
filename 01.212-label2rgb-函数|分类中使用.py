'''
在color模块的颜色空间转换函数中，还有一个比较有用的函数是
skimage.color.label2rgb(arr), 可以根据标签值对图片进行着色。以后的图片分类后着色就可以用这个函数。
'''


# 将lena图片分成三类，然后用默认颜色对三类进行着色
from skimage import io,data,color
import numpy as np


img = data.chelsea()
gray = color.rgb2gray(img)
rows, cols = gray.shape
labels = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        if(gray[i, j] < 0.4):
            labels[i, j] = 0
        elif(gray[i,j] < 0.75):
            labels[i, j] = 1
        else:
            labels[i, j] = 2
        pass
    pass

dst = color.label2rgb(labels)
io.imshow(dst)

print()