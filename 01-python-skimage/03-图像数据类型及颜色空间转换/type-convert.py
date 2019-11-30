'''
在上面的表中，特别注意的是float类型，它的范围是[-1,1]或[0,1]之间。一张彩色图片转换为灰度图后，它的类型就由unit8变成了float

Function name   Description
img_as_float    Convert to 64-bit floating point.
img_as_ubyte    Convert to 8-bit uint.
img_as_uint     Convert to 16-bit uint.
img_as_int      Convert to 16-bit int.
'''

# unit8转float
from skimage import data,img_as_float, img_as_ubyte
import numpy as np

img=data.chelsea()
print(img.dtype.name)
dst = img_as_float(img)
print(dst.dtype.name)



# float转uint8
img = np.array([0, 0.5, 1], dtype=float)
print(img.dtype.name)
dst = img_as_ubyte(img)
print(dst.dtype.name)