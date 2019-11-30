'''
2019年04月27日16:05:56


对小猫图片随机添加椒盐噪声
'''

from skimage import io,data
import numpy as np
img=data.chelsea()

#随机生成5000个椒盐

rows, cols, dims = img.shape

# 这里用到了numpy包里的random来生成随机数，randint(0,cols)表示随机生成一个整数，范围在0到cols之间。
# 用img[x,y,:]=255这句来对像素值进行修改，将原来的三通道像素值，变为255
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

    pass

io.imshow(img)