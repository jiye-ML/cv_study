from skimage import transform,data
import matplotlib.pyplot as plt

img = data.camera()
print(img.shape) #图片原始大小
print(transform.rescale(img, 0.1).shape) #缩小为原来图片大小的0.1
print(transform.rescale(img, [0.5,0.25]).shape) #缩小为原来图片行数一半，列数四分之一
print(transform.rescale(img, 2).shape) #放大为原来图片from skimage import transform,data


img = data.camera()
print(img.shape) #图片原始大小
# angle参数是个float类型数，表示旋转的度数
# resize用于控制在旋转时，是否改变大小 ，默认为False
img1=transform.rotate(img, 60) #旋转90度，不改变大小
print(img1.shape)
img2=transform.rotate(img, 30,resize=True) #旋转30度，同时改变大小
print(img2.shape)
plt.figure('resize')
plt.subplot(121)
plt.title('rotate 60')
plt.imshow(img1,plt.cm.gray)
plt.subplot(122)
plt.title('rotate 30')
plt.imshow(img2,plt.cm.gray)
plt.show() #大小的2倍