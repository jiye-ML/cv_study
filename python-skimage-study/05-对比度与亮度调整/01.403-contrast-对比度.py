'''
3、判断图像对比度是否偏低
函数：is_low_contrast(img)
返回一个bool型值
'''

from skimage import data, exposure


image =data.moon()
result=exposure.is_low_contrast(image)
print(result)