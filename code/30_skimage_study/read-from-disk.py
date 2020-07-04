'''
2019年04月26日21:59:34

读取图片, 从外部读取图片，并且展示
'''

from skimage import io

# 第一参数表示图片路径，第二个参数为灰度
img=io.imread('./data/2007_000027.jpg',as_grey=True)
io.imshow(img)