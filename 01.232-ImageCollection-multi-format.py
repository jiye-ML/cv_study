'''
如果一个文件夹里，我们既存放了一些jpg格式的图片，又存放了一些png格式的图片，现在想把它们全部读取出来，该怎么做呢?
'''

import skimage.io as io
from skimage import data_dir

'''
注意这个地方'd:/pic/.jpg:d:/pic/.png' ，是两个字符串合在一起的，第一个是'd:/pic/.jpg', 第二个是'd:/pic/.png' ，
合在一起后，中间用冒号来隔开，这样就可以把d:/pic/文件夹下的jpg和png格式的图片都读取出来。
如果还想读取存放在其它地方的图片，也可以一并加进去，只是中间同样用冒号来隔开。
'''
str='d:/pic/*.jpg:d:/pic/*.png'
coll = io.ImageCollection(str)

print(len(coll))