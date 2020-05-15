import matplotlib.pyplot as plt

def DrawOriFun(fun,MINX,MAXX,OUT):
    resX = list()
    resY = list()

    x = MINX
    while x <= MAXX :
        resX.append(x)
        resY.append(fun(x))
        x += 0.001

    plt.cla()
    plt.clf()
    plt.title("OriFunction")
    plt.plot(resX,resY,'r:')

    plt.savefig("./out/ori"+OUT+".png")


