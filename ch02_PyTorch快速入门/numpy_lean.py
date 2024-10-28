# 导包
from array import array

import numpy as np

# 查看版本
print("获取版本号: " + np.__version__)

# numpy的性能优势对比
# python原生实现
def sum(n:int):
    a = [i**2 for i in range(n)]
    b = [i**2 for i in range(n)]
    c = []
    for i,j in zip(a,b):
        c.append(i+j)
    return c

# numpy 实现
def sum_np(n:int):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 2
    return a + b

# 算法的时间对比，在同名文件的ipynb中


l1 = [ 1, 2, 3, 4 ]
l2 = [
    [ 2, 3, 4, 5 ],
    [ 3, 4, 5, 6]
]

arr1 = np.array(l1)
arr2 = np.array(l2)
print(type(arr1))
print(arr2)