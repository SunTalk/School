import matplotlib.pyplot as plt

def Newtonfun(dataX,dataY,MINX,MAXX,OUT):

    DiffTable = list()
    DiffTable.append(dataY)
    for i in range(1,len(dataX)):
        Tableset = list()
        for j in range(0,len(dataX)-i):
            numerator   = DiffTable[i-1][j+1]-DiffTable[i-1][j]
            denominator = dataX[i+j]-dataX[j]
            Tableset.append(numerator/denominator)
        DiffTable.append(Tableset)

    x = MINX
    resX = list()
    resY = list()
    
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

    plt.cla()
    plt.clf()
    plt.title("Newton"+OUT)
    ORI, = plt.plot(dataX,dataY,'bo')
    RES, = plt.plot(resX,resY,'r:')
    plt.legend([RES,ORI],["Result","Origin"])

    plt.savefig("./out/Newton/"+OUT+".png")




