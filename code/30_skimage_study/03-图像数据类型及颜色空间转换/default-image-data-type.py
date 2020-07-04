'''
一张图片的像素值范围是[0,255], 因此默认类型是unit8, 可用如下代码查看数据类型
'''

from skimage import data
img = data.chelsea()
print(img.dtype.name)