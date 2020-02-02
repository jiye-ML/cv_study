'''
2019年04月26日21:59:34

读取图片， 程序内部包含一些图片

astronaut     航员图片      coffee     一杯咖啡图片
lena          lena美女图片   camera   拿相机的人图片
coins           硬币图片     moon    月亮图片
checkerboard   棋盘图片       horse   马图片
page   书页图片              chelsea   小猫图片
hubble_deep_field    星空图片   text   文字图片
clock    时钟图片   immunohistochemistry   结肠图片

'''

from skimage import io, data, data_dir

# 显示这些图片可用如下代码，不带任何参数
img = data.chelsea()
io.imshow(img)

# 图片名对应的就是函数名，如camera图片对应的函数名为camera().
# 这些示例图片存放在skimage的安装目录下面，路径名称为data_dir,我们可以将这个路径打印出来看看
print(data_dir)