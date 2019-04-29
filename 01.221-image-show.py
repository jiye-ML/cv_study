'''

* 实际上前面我们就已经用到了图像的绘制，
```
io.imshow(img)
```

* 这一行代码的实质是利用matplotlib包对图片进行绘制，绘制成功后，返回一个matplotlib类型的数据。因此，我们也可以这样写：
```
import matplotlib.pyplot as plt
plt.imshow(img)
```

* imshow()函数格式为： `matplotlib.pyplot.imshow(X, cmap=None)`
* X: 要绘制的图像或数组。
* cmap: 颜色图谱（colormap), 默认绘制为RGB(A)颜色空间。其它可选的颜色图谱如下列表：
```
颜色图谱                          描述
autumn                        红-橙-黄
bone                          黑-白，x线
cool                          青-洋红
copper                         黑-铜
flag                           红-白-蓝-黑
gray                              黑-白
hot                            黑-红-黄-白
hsv                hsv颜色空间， 红-黄-绿-青-蓝-洋红-红
inferno                     黑-红-黄
jet                             蓝-青-黄-红
magma                      黑-红-白
pink                               黑-粉-白
plasma                       绿-红-黄
prism                         红-黄-绿-蓝-紫-...-绿模式
spring                             洋红-黄
summer                             绿-黄
viridis                             蓝-绿-黄
winter                             蓝-绿
```
* 用的比较多的有gray,jet等，如
`
plt.imshow(image,plt.cm.gray)
plt.imshow(img,cmap=plt.cm.jet)
`



'''


from skimage import io,data

img = data.astronaut()
dst = io.imshow(img)
print(type(dst))   # <class 'matplotlib.image.AxesImage'>
io.show()




# 可以看到，类型是'matplotlib.image.AxesImage'。显示一张图片，我们通常更愿意这样写
import matplotlib.pyplot as plt
from skimage import io,data
img=data.astronaut()
plt.imshow(img)
plt.show()