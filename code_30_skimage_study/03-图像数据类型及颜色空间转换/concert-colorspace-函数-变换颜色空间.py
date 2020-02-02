'''
实际上，上面的所有转换函数，都可以用一个函数来代替
skimage.color.convert_colorspace(arr, fromspace, tospace)
'''




from skimage import io,data,color

# rgb转hsv
img=data.chelsea()
hsv=color.convert_colorspace(img, 'RGB', 'HSV')
io.imshow(hsv)
