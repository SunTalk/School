import matplotlib.pyplot as plt

def GregoryForwardfun(dataX,dataY,OUT):

    DiffTable = list()
    DiffTable.append(dataY)
    for i in range(1,len(dataX)):
        Tableset = list()
        for j in range(0,len(dataX)-i):
            Tableset.append(DiffTable[i-1][j+1]-DiffTable[i-1][j])
        DiffTable.append(Tableset)
    
    # for i in range(len(DiffTable)):
    #     print(DiffTable[i])

    MINX = 10.0
    MAXX = -10.0
    for i in range(len(dataX)):
        MINX = min(dataX[i],MINX)
        MAXX = max(dataX[i],MAXX)
    H = dataX[1]-dataX[0]

    x = MINX
    resX = list()
    resY = list()

    while x <= MAXX :
        ans = 0
        for i in range(len(DiffTable)):
            tmp = DiffTable[i][0]
            S = (x-dataX[0])/H
            for j in range(1,i+1):
                tmp *= (S/j)
                S -= 1
            ans += tmp
        
        resX.append(x)
        resY.append(ans)
        x += 0.001

    plt.cla()
    plt.clf()
    plt.title("GregoryForward"+OUT)
    ORI, = plt.plot(dataX,dataY,'bo')
    RES, = plt.plot(resX,resY,'r:')
    plt.legend([RES,ORI],["Result","Origin"])

    plt.savefig("./out/GregoryForward/"+OUT+".png")




