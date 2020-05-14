import matplotlib.pyplot as plt

def Lagrangefun(dataX,dataY,OUT):

    MINX = 10.0
    MAXX = -10.0
    for i in range(len(dataX)):
        MINX = min(dataX[i],MINX)
        MAXX = max(dataX[i],MAXX)

    x = MINX
    resX = list()
    resY = list()
    while x <= MAXX :
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

    plt.cla()
    plt.clf()
    plt.title("Lagrange"+OUT)
    ORI, = plt.plot(dataX,dataY,'bo')
    RES, = plt.plot(resX,resY,'r:')
    plt.legend([RES,ORI],["Result","Origin"])

    plt.savefig("./out/Lagrange/"+OUT+".png")
