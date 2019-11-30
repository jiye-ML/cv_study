'''
skimage.color.rgb2grey(rgb)
skimage.color.rgb2hsv(rgb)
skimage.color.rgb2lab(rgb)
skimage.color.gray2rgb(image)
skimage.color.hsv2rgb(hsv)
skimage.color.lab2rgb(lab)
'''



from skimage import io,data,color
img=data.chelsea()

gray=color.rgb2gray(img)

io.imshow(gray)


# 实际上，上面的所有转换函数，都可以用一个函数来代替
