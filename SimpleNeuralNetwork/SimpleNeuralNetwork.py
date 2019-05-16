from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
feature_set, labels = datasets.make_moons(100, noise=0.10)


labels = labels.reshape(100, 1)


def LReLU_function( signal, derivative=False, leakage = 0.01 ):

    if derivative:
        return np.clip(signal > 0, leakage, 1.0)
    else:
        output = np.copy( signal )
        output[ output < 0 ] *= leakage
        return output


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid (x))


wh = np.random.rand(len(feature_set[0]),4)
wo = np.random.rand(4, 1)
lr = 0.001

errorList = []

for epoch in range(500):
    zh = np.dot(feature_set, wh)
    ah = LReLU_function(zh)

    zo = np.dot(ah, wo)
    ao = LReLU_function(zo)

    error_out = ((1 / 2) * (np.power((ao - labels), 2)))
    print(error_out.sum())
    errorList.append(error_out.sum())

    dcost_dao = ao - labels
    dao_dzo = LReLU_function(zo, True)
    dzo_dwo = ah

    dcost_wo = np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

    dcost_dzo = dcost_dao * dao_dzo
    dzo_dah = wo
    dcost_dah = np.dot(dcost_dzo , dzo_dah.T)
    dah_dzh = LReLU_function(zh, True)
    dzh_dwh = feature_set
    dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

    wh -= lr * dcost_wh
    wo -= lr * dcost_wo

print(errorList)
plt.plot(errorList)
plt.show()
