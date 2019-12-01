
'''
1、gamma调整
原理：I=Ig

对原图像的像素，进行幂运算，得到新的像素值。公式中的g就是gamma值。
如果gamma>1, 新图像比原图像暗
如果gamma<1,新图像比原图像亮
函数格式为：
'''

from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt

image = img_as_float(data.moon())
gam1= exposure.adjust_gamma(image, 2) #调暗
gam2= exposure.adjust_gamma(image, 0.5) #调亮plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')
plt.show()