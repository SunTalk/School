import matplotlib.pyplot as plt

def Lagrange(dataX,dataY,fun):

    resX = list()
    resY = list()

    x = 2.5
    for k in range(5000):
        ans = 0
        for i in range(len(dataX)):
            tmp = 1
            for j in range(len(dataX)):
                if i == j :
                    continue
                tmp *= (x-dataX[j])/(dataX[i]-dataX[j])
            ans += tmp*dataY[i]
        
        resX.append(x)
        resY.append(ans)
        x += 0.001

    plt.plot(resX,resY,'r:')

    oriX = list()
    oriY = list()

    x = 2.5
    for k in range(5000):
        oriX.append(x)
        oriY.append(fun(x))
        x += 0.001

    plt.plot(oriX,oriY,'b:')
    
    plt.show()







