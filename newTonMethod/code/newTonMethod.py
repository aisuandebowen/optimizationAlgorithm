import tools
import numpy as np

epsilon = 1e-10
finalX = [0,0]

# 初始化数据
def _getInitData(xList):
    gradFn = tools.getGradFn(xList)  # 梯度
    normalGradFn = np.linalg.norm(gradFn)  # 梯度二范数

    return [gradFn,normalGradFn]

# 牛顿法 得极小值点和极小值
def run(xList):
    # 初始化
    gradFn,normalGradFn = _getInitData(xList)
    d = None
    print(gradFn,normalGradFn)
    # 迭代
    while normalGradFn>=epsilon:
        hesseFn = tools.getHesseFn(xList) # Hesses矩阵
        invHesseFn = np.linalg.inv(hesseFn) # 求Hesse逆矩阵

        d = -np.dot(invHesseFn,gradFn) # 方向
        xList = xList + d # 更新xList
        gradFn, normalGradFn = _getInitData(xList) # 更新相关数据

    # 终止
    fn = tools.getFn(xList)
    return [xList,fn]
