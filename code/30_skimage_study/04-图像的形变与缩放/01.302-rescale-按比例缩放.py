from skimage import transform,data

img = data.camera()

print(img.shape) #图片原始大小
print(transform.rescale(img, 0.1).shape) #缩小为原来图片大小的0.1
print(transform.rescale(img, [0.5,0.25]).shape) #缩小为原来图片行数一半，列数四分之一
print(transform.rescale(img, 2).shape) #放大为原来图片大小的2倍