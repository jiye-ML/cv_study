'''
2019年04月27日16:05:56


对小猫图片进行裁剪
'''

from skimage import io,data

img=data.chelsea()
roi=img[80:180,100:200,:]

io.imshow(roi)



