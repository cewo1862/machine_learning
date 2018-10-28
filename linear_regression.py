import matplotlib.pyplot as plt
import numpy as np
#import math
import itertools

def main():
    type = []
    petal_width = []
    petal_length = []
    sepal_width = []
    sepal_length = []

    #type 0
    petal_width_0 = []
    petal_length_0 = []
    sepal_width_0 = []
    sepal_length_0 = []

    # type 1
    petal_width_1 = []
    petal_length_1 = []
    sepal_width_1 = []
    sepal_length_1 = []

    # type 2
    petal_width_2 = []
    petal_length_2 = []
    sepal_width_2 = []
    sepal_length_2 = []

    # d)
    sepal_length_0_1 = []
    type_0_1 = []


    with open("Fisher.txt", 'r') as f:
        next(f)
        for line in f:
            line = line.split('\t')
            type.append(line[0])
            petal_width.append(line[1])
            petal_length.append(line[2])
            sepal_width.append(line[3])
            sepal_length.append(line[4])

            if line[0] == "0":
                petal_width_0.append(int(line[1]))
                petal_length_0.append(int(line[2]))
                sepal_width_0.append(int(line[3]))
                sepal_length_0.append(int(line[4]))
                sepal_length_0_1.append(int(line[4]))
                type_0_1.append(int(line[0]))

            if line[0] == "1":
                petal_width_1.append(int(line[1]))
                petal_length_1.append(int(line[2]))
                sepal_width_1.append(int(line[3]))
                sepal_length_1.append(int(line[4]))
                sepal_length_0_1.append(int(line[4]))
                type_0_1.append(int(line[0]))

            if line[0] == "2":
                petal_width_2.append(int(line[1]))
                petal_length_2.append(int(line[2]))
                sepal_width_2.append(int(line[3]))
                sepal_length_2.append(int(line[4]))


    petal_width_0_mean = np.average(petal_width_0)
    petal_width_0_min = np.amin(petal_width_0)
    petal_width_0_max = np.amax(petal_width_0)
    petal_length_0_mean = np.average(petal_length_0)
    petal_length_0_min = np.amin(petal_length_0)
    petal_length_0_max = np.amax(petal_length_0)
    sepal_width_0_mean = np.average(sepal_width_0)
    sepal_width_0_min = np.amin(sepal_width_0)
    sepal_width_0_max = np.amax(sepal_width_0)
    sepal_length_0_mean = np.average(sepal_length_0)
    sepal_length_0_min = np.amin(sepal_length_0)
    sepal_length_0_max = np.amax(sepal_length_0)

    petal_width_1_mean = np.average(petal_width_1)
    petal_width_1_min = np.amin(petal_width_1)
    petal_width_1_max = np.amax(petal_width_1)
    petal_length_1_mean = np.average(petal_length_1)
    petal_length_1_min = np.amin(petal_length_1)
    petal_length_1_max = np.amax(petal_length_1)
    sepal_width_1_mean = np.average(sepal_width_1)
    sepal_width_1_min = np.amin(sepal_width_1)
    sepal_width_1_max = np.amax(sepal_width_1)
    sepal_length_1_mean = np.average(sepal_length_1)
    sepal_length_1_min = np.amin(sepal_length_1)
    sepal_length_1_max = np.amax(sepal_length_1)

    petal_width_2_mean = np.average(petal_length_2)
    petal_width_2_min = np.amin(petal_length_2)
    petal_width_2_max = np.amax(petal_length_2)
    petal_length_2_mean = np.average(petal_width_2)
    petal_length_2_min = np.amin(petal_width_2)
    petal_length_2_max = np.amax(petal_width_2)
    sepal_width_2_mean = np.average(sepal_length_2)
    sepal_width_2_min = np.amin(sepal_length_2)
    sepal_width_2_max = np.amax(sepal_length_2)
    sepal_length_2_mean = np.average(sepal_width_2)
    sepal_length_2_min = np.amin(sepal_width_2)
    sepal_length_2_max = np.amax(sepal_width_2)

    #type 0

    print("type 0: ", petal_width_0_mean, petal_length_0_mean,sepal_width_0_mean,sepal_length_0_mean)

    #type 1

    print("type 1: ", petal_width_1_mean, petal_length_1_mean, sepal_width_1_mean, sepal_length_1_mean)

    #type 2

    print("type 2: ", petal_width_2_mean, petal_length_2_mean, sepal_width_2_mean, sepal_length_2_mean)

    '''
    b)
    type 0 can easily be distinguished based on its mean values for petal width
    the averages for type 1 and type 2 are closer to each other but it's still perceivable that type 1 developes longer
    petals and sepals than type 2
    '''

    plt.plot(petal_length_0,sepal_length_0,'ro',petal_length_1,sepal_length_1,'bo',petal_length_2,sepal_length_2,'go')
    plt.ylabel('sepal length')
    plt.xlabel('petal length')
    plt.show()

    '''
    type_0_1_transposed = np.transpose(type_0_1)
    w = np.linalg.inv(type_0_1_transposed*type_0_1)*type_0_1*sepal_length_0_1
    '''

    sepal_length_0_1_mean = np.average(sepal_length_0_1)
    type_0_1_mean = np.average(type_0_1)
    top_sum = 0
    bot_sum = 0

    for x,y in zip(sepal_length_0_1,type_0_1):
        top_sum += (x-sepal_length_0_1_mean)*(y-type_0_1_mean)
        bot_sum += (x-sepal_length_0_1_mean)*(x-sepal_length_0_1_mean)

    w1 = top_sum / bot_sum
    print(w1)

    w0 = type_0_1_mean - w1 * sepal_length_0_1_mean
    print(w0)

    rss = 0

    for x,y in zip(sepal_length_0_1,type_0_1):
        rss += (y-w0-w1*x)*(y-w0-w1*x)

    print("RSS: ",rss)

    x = np.array(sepal_length_0_1)
    y = eval('w0+w1*x')
    plt.plot(x,y,'b-',sepal_length_0_1,type_0_1,'ro')
    plt.show()

if __name__ == "__main__":
    main()