'''
2019年04月27日16:05:56


使用io模块的imsave（fname,arr）函数来实现。第一个参数表示保存的路径和名称，第二个参数表示需要保存的数组变量。
'''

from skimage import io,data
img=data.chelsea()
io.imshow(img)

# 保存图片的同时也起到了转换格式的作用。如果读取时图片格式为jpg图片，保存为png格式，则将图片从jpg图片转换为png图片并保存。
io.imsave('data/cat.jpg', img)