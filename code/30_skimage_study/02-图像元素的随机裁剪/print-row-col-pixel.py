'''
2019年04月27日16:05:56


输出小猫图片的G通道中的第20行30列的像素值
'''

from skimage import io,data
img=data.chelsea()
pixel=img[20,30,1]
print(pixel)