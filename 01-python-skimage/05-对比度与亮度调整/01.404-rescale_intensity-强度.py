'''
in_range 表示输入图片的强度范围，默认为'image', 表示用图像的最大/最小像素值作为范围
out_range 表示输出图片的强度范围，默认为'dype', 表示用图像的类型的最大/最小值作为范围
默认情况下，输入图片的[min,max]范围被拉伸到[dtype.min, dtype.max]，如果dtype=uint8, 那么dtype.min=0, dtype.max=255


'''

import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
mat=exposure.rescale_intensity(image)
print(mat)

'''
0 127 255]
即像素最小值由51变为0，最大值由153变为255，整体进行了拉伸，但是数据类型没有变，还是uint8
前面我们讲过，可以通过img_as_float()函数将unit8类型转换为float型，实际上还有更简单的方法，就是乘以1.0
'''

import numpy as np
image = np.array([51, 102, 153], dtype=np.uint8)
print(image*1.0)

'''
即由[51,102,153]变成了[ 51. 102. 153.]
而float类型的范围是[0,1]，因此对float进行rescale_intensity 调整后，范围变为[0,1],而不是[0,255]
'''
import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=exposure.rescale_intensity(tmp)
print(mat)


'''
结果为[ 0. 0.5 1. ]
如果原始像素值不想被拉伸，只是等比例缩小，就使用in_range参数，如：
'''