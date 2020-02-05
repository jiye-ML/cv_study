import math
import torch
import torch.nn as nn
import numpy as np
import torch.nn.init as init
import matplotlib.pyplot as plt


def bilinear_kernel(in_channels, out_channels, kernel_size):
  factor = (kernel_size + 1) // 2

  center = kernel_size / 2
  og = np.ogrid[:kernel_size, :kernel_size]
  filt = (1 - abs(og[0] - center) / factor) * (1 - abs(og[1] - center) / factor)
  weight = np.zeros((in_channels, out_channels, kernel_size, kernel_size), dtype='float32')
  weight[range(in_channels), range(out_channels), :, :] = filt
  return torch.from_numpy(weight)


x = plt.imread("1.jpg")
print(x.shape)
x = torch.from_numpy(x.astype('float32')).permute(2, 0, 1).unsqueeze(0)
conv_trans = nn.ConvTranspose2d(3, 3, 4, 2, 1)

# 将其定义为 bilinear kernel
conv_trans.weight.data = bilinear_kernel(3, 3, 4)
y = conv_trans(x).data.squeeze().permute(1, 2, 0).numpy()
plt.imshow(y.astype('uint8'))
print(y.shape)