
# 验证torch是否安装成功
import torch
print( torch.__version__ )
print( torch.cuda.is_available() ) # 是否可以使用GPU

import numpy

