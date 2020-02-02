import skimage.io as io
from skimage import data_dir

str=data_dir + '/*.png'
coll = io.ImageCollection(str)

# 显示结果为25, 说明系统自带了25张png的示例图片，这些图片都读取了出来，放在图片集合coll里。
print(len(coll))

# 如果我们想显示其中一张图片，则可以在后加上一行代码：
io.imshow(coll[10])