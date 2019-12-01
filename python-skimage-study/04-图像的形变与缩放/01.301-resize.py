from skimage import transform,data
import matplotlib.pyplot as plt

img = data.camera()

# image: 需要改变尺寸的图片
# output_shape: 新的图片尺寸
dst=transform.resize(img, (80, 60))

# 打印
plt.figure('resize')
plt.subplot(121)
plt.title('before resize')
plt.imshow(img,plt.cm.gray)
plt.subplot(122)
plt.title('before resize')
plt.imshow(dst,plt.cm.gray)
plt.show()