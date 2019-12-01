'''
这个刚好和gamma相反
原理：I=log(I)
'''

from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt

image = img_as_float(data.moon())
gam1= exposure.adjust_log(image) #对数调整
plt.figure('adjust_gamma',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')
plt.subplot(122)
plt.title('log')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')
plt.show()
