import matplotlib.pyplot as plt

def Newtonfun(dataX,dataY,OUT):

    DiffTable = list()
    DiffTable.append(dataY)
    for i in range(1,len(dataX)):
        Tableset = list()
        for j in range(0,len(dataX)-i):
            son = DiffTable[i-1][j+1]-DiffTable[i-1][j]
            mon = dataX[i+j]-dataX[j]
            Tableset.append(son/mon)
        DiffTable.append(Tableset)
    
    # for i in range(len(DiffTable)):
    #     print(DiffTable[i],file=f)

    MINX = 10.0
    MAXX = -10.0
    for i in range(len(dataX)):
        MINX = min(dataX[i],MINX)
        MAXX = max(dataX[i],MAXX)
    
    x = MINX
    resX = list()
    resY = list()
    # for x in dataX:
    while x <= MAXX :
        ans = 0
        for i in range(len(DiffTable)):
            tmp = DiffTable[i][0]
            for j in range(i):
                tmp *= (x-dataX[j])
            ans += tmp
        resX.append(x)
        resY.append(ans)
        x += 0.001
    
    # for i in range(len(resX)):
    #     print((resX[i],resY[i]),file=f)

    plt.cla()
    plt.clf()
    plt.title("Newton"+OUT)
    ORI, = plt.plot(dataX,dataY,'bo')
    RES, = plt.plot(resX,resY,'r:')
    plt.legend([RES,ORI],["Result","Origin"])

    plt.savefig("./out/Newton/"+OUT+".png")




