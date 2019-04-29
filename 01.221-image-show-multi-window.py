'''

用figure函数和subplot函数分别创建主窗口与子图
分开并同时显示宇航员图片的三个通道

'''


from skimage import data
import matplotlib.pyplot as plt

img = data.astronaut()

'''
matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None)

所有参数都是可选的，都有默认值，因此调用该函数时可以不带任何参数，其中：
num: 整型或字符型都可以。如果设置为整型，则该整型数字表示窗口的序号。如果设置为字符型，则该字符串表示窗口的名称。用该参数来命名窗口，如果两个窗口序号或名相同，则后一个窗口会覆盖前一个窗口。
figsize: 设置窗口大小。是一个tuple型的整数，如figsize=（8，8）
dpi: 整形数字，表示窗口的分辨率。
facecolor: 窗口的背景颜色。
edgecolor: 窗口的边框颜色。
'''
plt.figure(num='astronaut',figsize=(8,8))  #创建一个名为astronaut的窗口,并设置大小

'''
用figure()函数创建的窗口，只能显示一幅图片，如果想要显示多幅图片，则需要将这个窗口再划分为几个子图，
在每个子图中显示不同的图片。我们可以使用subplot（）函数来划分子图，函数格式为：
    matplotlib.pyplot.subplot(nrows, ncols, plot_number)
'''
plt.subplot(2,2,1)     #将窗口分为两行两列四个子图，则可显示四幅图片
plt.title('origin image')   #第一幅图片标题
plt.imshow(img)      #绘制第一幅图片

plt.subplot(2,2,2)     #第二个子图
plt.title('R channel')   #第二幅图片标题
plt.imshow(img[:,:,0],plt.cm.gray)      #绘制第二幅图片,且为灰度图
plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,3)     #第三个子图
plt.title('G channel')   #第三幅图片标题
plt.imshow(img[:,:,1],plt.cm.gray)      #绘制第三幅图片,且为灰度图
plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,4)     #第四个子图
plt.title('B channel')   #第四幅图片标题
plt.imshow(img[:,:,2],plt.cm.gray)      #绘制第四幅图片,且为灰度图
plt.axis('off')     #不显示坐标尺寸

plt.show()   #显示窗口