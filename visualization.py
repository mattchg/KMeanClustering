# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:11:36 2019

@author: Matthew
"""


import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import model_generation

stats = model_generation.stats
#stats.pop('MP');
pts_ast = model_generation.pts_ast
ast_tov = model_generation.ast_tov
pts_ast_tov = model_generation.pts_ast_tov

sns.set(style="ticks")
sns.pairplot(stats,diag_kind = 'kde')

#sns.set(style="ticks")
sns.jointplot(stats['PTS'], stats['AST'], kind="hex", color="#4CB391")             

'''
plt.figure()              
cluster = pts_ast.return_clusters()              
plt.scatter(cluster[0]['PTS'],cluster[0]['AST'],color='red')
plt.scatter(cluster[1]['PTS'],cluster[1]['AST'],color='orange')
plt.scatter(cluster[2]['PTS'],cluster[2]['AST'],color='blue')
plt.title('3 Mean Clustering of PTS:AST')

plt.figure()              
cluster = ast_tov.return_clusters()              
plt.scatter(cluster[0]['AST'],cluster[0]['TOV'],color='red')
plt.scatter(cluster[1]['AST'],cluster[1]['TOV'],color='orange')
plt.scatter(cluster[2]['AST'],cluster[2]['TOV'],color='blue')
plt.title('3 Mean Clustering of AST:TOV')
'''

cluster = pts_ast_tov.return_clusters()
colors = ['red','blue','green','orange','black','yellow']
plot_cluster = list(zip(cluster,colors))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for clus in plot_cluster:
    ax.scatter(clus[0]['PTS'], clus[0]['AST'], clus[0]['TOV'], color = clus[1])
ax.set_xlabel('PTS')
ax.set_ylabel('AST')
ax.set_zlabel('TOV')
plt.show()





             



