import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans


tabl = pd.read_excel(r'C:\Users\ilyx\Desktop\for py\222222222222q.xlsx', index_col=0)
df = pd.DataFrame(tabl)


XOXO = df.iloc[:, [1, 2]].values
for i in range(len(XOXO)):
    if XOXO[i][1] < 30.0:
        XOXO[i] = 0
X = []
for i in range(len(XOXO)):
    if sum(XOXO[i]) == 0:
        pass
    elif sum(XOXO[i]) > 0:
        X.append([XOXO[i][0], XOXO[i][1]])
X = np.array(X, dtype=float)


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()




qwe = []
for i in range(len(wcss)):
    print(wcss[i])
    if i == 0:
        pass
    elif i > 0:
        qwe.append(wcss[i-1]/wcss[i])
qwe.sort()
print(qwe)
optimal_num_clusters = round(qwe[-1])
print(optimal_num_clusters)

kmeans = KMeans(n_clusters = optimal_num_clusters, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
print(X)

df2 = df
y_kmeans_list = list(y_kmeans)
for i in range(len(y_kmeans_list)):
    y_kmeans_list[i] += 1

tmp = list(df.iloc[:, 2].values)

k = 0

clusters = []

for i in range(len(tmp)):
    if int(tmp[i]) >= 30:
        clusters.append(y_kmeans_list[k])
        k+=1
    else:
        clusters.append('None')

print(clusters)

df2['Claster'] = clusters
df2.to_excel('2222222222q_clasters.xlsx')


plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters')
plt.xlabel('pickrate')
plt.ylabel('winrate')
plt.legend()
plt.show()



XOXO = df.iloc[:, [1, 2]].values
for i in range(len(XOXO)):
    if XOXO[i][1] < 30.0:
        XOXO[i] = 0
X = []
for i in range(len(XOXO)):
    if sum(XOXO[i]) == 0:
        pass
    elif sum(XOXO[i]) > 0:
        X.append([XOXO[i][0], XOXO[i][1]])
X = np.array(X, dtype=float)



dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('ratings')
plt.ylabel('Euclidean distances')
plt.show()


hc = AgglomerativeClustering(n_clusters = optimal_num_clusters, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.title('Clusters')
plt.xlabel('pickrate')
plt.ylabel('winrate')
plt.legend()
plt.show()



# print(df[df['pickrate'] == df['pickrate'].min()])
#
# print(df[df['pickrate'] == df['pickrate'].max()])
#
# print(df[df['winrate'] == df['winrate'].min()])
#
# print(df[df['winrate'] == df['winrate'].max()])