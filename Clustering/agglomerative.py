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

def doAgglomerative(X, nclust=2):
    model = AgglomerativeClustering(n_clusters=nclust, affinity = 'euclidean', linkage = 'ward')
    clust_labels1 = model.fit_predict(X)
    return (clust_labels1)

clust_labels1 = doAgglomerative(wh1, 3)
agglomerative = pd.DataFrame(clust_labels1)
wh1.insert((wh1.shape[1]),'agglomerative',agglomerative)

#writing to the file
classification = pd.DataFrame(wh1, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'agglomerative']).round(3).to_csv('./outputs/agglomerative.csv')

#Plot the clusters obtained using Agglomerative clustering or Hierarchical clustering
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['SepalLengthCm'],wh1['SepalWidthCm'],
                     c=agglomerative[0],s=50)
ax.set_title('Agglomerative Clustering')
ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('SepalWidthCm')
plt.colorbar(scatter)

plt.show();
