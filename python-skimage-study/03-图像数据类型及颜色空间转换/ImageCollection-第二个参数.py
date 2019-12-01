'''
io.ImageCollection()这个函数省略第二个参数，就是批量读取。如果我们不是想批量读取，而是其它批量操作，如批量转换为灰度图，那又该怎么做呢？
那就需要先定义一个函数，然后将这个函数作为第二个参数，如：
'''

from skimage import data_dir,io,color

def convert_gray(f):
    rgb=io.imread(f)
    return color.rgb2gray(rgb)

str=data_dir+'/*.png'
coll = io.ImageCollection(str, load_func = convert_gray)
io.imshow(coll[10])

