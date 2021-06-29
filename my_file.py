import torch
import torch.nn.functional as F
a=torch.randn(2,3,4,5)
b=a[0]
c=F.interpolate(a,2)[0]
d=a[None]
print('a的shape:',a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
