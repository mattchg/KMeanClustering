# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:46:38 2019

@author: Matthew
"""

import pandas as pd
import numpy as np
from KMEAN import KMeans

try:
    stats;
except NameError:    
    import acquisiton_script
    stats = acquisiton_script.stats
    
class cluster:
    def __init__ (self,df,model):
        self.df = df
        self.model = model
    def return_clusters(self):
        groups = []
        for i in range(0,self.model.k):
            groups.append(self.df.iloc[self.model.clusters[i]])
        return groups
K = 5
pts_ast = list(zip(stats['PTS'],stats['AST']))
pts_ast_cluster = KMeans(K)
pts_ast_cluster.train(pts_ast)
pts_ast = cluster(stats[['PTS','AST']],pts_ast_cluster)    

ast_tov = list(zip(stats['AST'],stats['TOV']))
ast_tov_cluster = KMeans(K)
ast_tov_cluster.train(ast_tov)
ast_tov = cluster(stats[['AST','TOV']],ast_tov_cluster)

pts_ast_tov = list(zip(stats['PTS'],stats['AST'],stats['TOV']))
pts_ast_tov_cluster = KMeans(K)
pts_ast_tov_cluster.train(pts_ast_tov)
pts_ast_tov = cluster(stats[['PTS','AST','TOV']],pts_ast_tov_cluster)    


