import numpy as np
from scipy.optimize import minimize_scalar
from objectiveFn import objFn

epsilon = 1e-5 # 误差
bounds = (-10, 10) # 设定搜索范围

def run(xList):
    xBox = xList
    y = xBox
    k = 0
    xNum = len(xList)
    D = np.eye(xNum)

    while 1:
        # exploratory search
        z_j = y

        # 更新z_j
        for j in range(0,xNum):
            d_j = D[:,j]
            lambda_j = minimize_scalar(lambda x: objFn(z_j+x*d_j),bounds=bounds,method='bounded')
            z_j += lambda_j.x*d_j

        xBox2 = z_j

        # 判断是否达到精度
        objFn1 = objFn(xBox)
        objFn2 = objFn(xBox2)
        if(np.linalg.norm(xBox2-xBox) < epsilon and (objFn2 - objFn1) < epsilon):
            return [xBox2, objFn2]
        else:
            d_p = xBox2 - xBox
            lambda_bar = minimize_scalar(lambda x: objFn(xBox2+x*d_p))
            y = xBox2 + lambda_bar.x * d_p

        # 更新xBox
        xBox =xBox2
        k +=1