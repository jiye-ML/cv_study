'''

以多分辨率来解释图像的一种有效但概念简单的结构就是图像金字塔。图像金字塔最初用于机器视觉和图像压缩，
一幅图像的金字塔是一系列以金字塔形状排列的分辨率逐步降低的图像集合。金字塔的底部是待处理图像的高分辨率表示，
而顶部是低分辨率的近似。当向金字塔的上层移动时，尺寸和分辨率就降低。
在此，我们举一个高斯金字塔的应用实例，函数原型为：
'''


import numpy as np
import matplotlib.pyplot as plt
from skimage import data,transform


image = data.astronaut() #载入宇航员图片
rows, cols, dim = image.shape #获取图片的行数，列数和通道数

# 产生高斯金字塔图像#共生成了log(512)=9幅金字塔图像，加上原始图像共10幅，pyramid[0]-pyramid[1]
pyramid = tuple(transform.pyramid_gaussian(image, downscale=2))

#生成背景composite_image[:rows, :cols, :] = pyramid[0] #融合原始图像
composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)
i_row = 0
for p in pyramid[1:]:
       n_rows, n_cols = p.shape[:2]
       composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p #循环融合9幅金字塔图像
       i_row += n_rows
       pass

plt.imshow(composite_image)
plt.show()