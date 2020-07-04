'''
2019年04月27日16:05:56


显示红色单通道图片
'''

from skimage import io,data
img=data.chelsea()
R=img[:,:,0]
io.imshow(R)