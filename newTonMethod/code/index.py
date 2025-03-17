import newTonMethod

xList = [0,1]
finalXList,finalFn = newTonMethod.run(xList)

print(f'初始点：{xList}, 收敛点：{finalXList}')
print(f'最优解:{finalFn}')