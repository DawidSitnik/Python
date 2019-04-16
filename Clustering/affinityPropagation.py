#Call required libraries
import time                   # To time processes
import warnings               # To suppress warnings

import numpy as np            # Data manipulation
import pandas as pd           # Dataframe manipulatio
import matplotlib.pyplot as plt                   # For graphics
import seaborn as sns
import plotly.plotly as py #For World Map
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from sklearn.preprocessing import StandardScaler  # For scaling dataset
from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation #For clustering
from sklearn.mixture import GaussianMixture #For GMM clustering

import os                     # For os related operations
import sys                    # For data size

wh = pd.read_csv("./Iris.csv") #Read the dataset
wh.describe()

print("Dimension of dataset: ")
print(wh.dtypes)

wh1 = wh[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] #Subsetting the data
# cor = wh1.corr() #Calculate the correlation of the above variables
# sns.heatmap(cor, square=True) #Plot the correlation as heat map

#Scaling of data
ss = StandardScaler()
ss.fit_transform(wh1)

def doAffinity(X):
    model = AffinityPropagation(damping = 0.5, max_iter = 250, affinity = 'euclidean')
    model.fit(X)
    clust_labels2 = model.predict(X)
    cent2 = model.cluster_centers_
    return (clust_labels2, cent2)

clust_labels2, cent2 = doAffinity(wh1)
affinity = pd.DataFrame(clust_labels2)
wh1.insert((wh1.shape[1]),'affinity',affinity)
#Plotting the cluster obtained using Affinity algorithm
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['SepalLengthCm'],wh1['SepalWidthCm'],
                     c=affinity[0],s=50)
ax.set_title('Affinity Clustering')
ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('SepalWidthCm')
plt.colorbar(scatter)

classification = pd.DataFrame(wh1, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'affinity']).round(3).to_csv('./outputs/affinity_propagation.csv')


plt.show();
