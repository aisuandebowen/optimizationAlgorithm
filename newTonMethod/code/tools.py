import numpy as np

# 导函数求值
def getGradFn(xList):
    x1,x2 = xList
    return np.array([4*((x1-1)**3), 2*x2])

# Hesse矩阵
def getHesseFn(xList):
    x1,x2 = xList
    return np.array([[12*(x1-1)**2,0],[0,2]])

# 函数值
def getFn(xList):
    x1,x2 = xList
    return (x1-1)**4+x2**2
