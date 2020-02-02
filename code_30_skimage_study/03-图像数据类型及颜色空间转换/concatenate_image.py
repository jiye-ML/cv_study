'''
使用concatenate_images(ic)函数的前提是读取的这些图片尺寸必须一致，否则会出错。我们看看图片连接前后的维度变化：
'''

from skimage import data_dir,io,color

coll = io.ImageCollection('d:/pic/*.jpg')

print(len(coll)) #连接的图片数量
print(coll[0].shape) #连接前的图片尺寸，所有的都一样
mat=io.concatenate_images(coll)
print(mat.shape) #连接后的数组尺寸
