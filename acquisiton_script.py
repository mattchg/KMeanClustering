# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:42:38 2019

@author: Matthew
"""

import numpy as np
import pandas as pd
import random

directory = "C:/Users/Matthew/Desktop/Working Here/PlayerAnalysisClustering/"
raw_data = pd.read_excel(directory + 'Seasons_Stats.xlsx', index_col = 0)
dataset = raw_data.copy()

for column in dataset.columns:
    if '%' in column:
        dataset.pop(column);

dataset = dataset.dropna()
dataset = dataset[dataset['Pos'] == 'PG']

def scrub_name (name):
    return name.partition('*')[0]

dataset['Player'] = dataset['Player'].apply(func=scrub_name)

stats = dataset.groupby(['Player']).sum()
stats.pop('Year');

for column in stats.columns:
    if(column != 'G' and column != 'Player'):
        stats[column] = stats[column]/stats['G']

to_drop = stats[stats['G'] < 300]
stats = stats.drop(to_drop.index)

to_drop = stats[stats['MP'] < 24.0]
stats = stats.drop(to_drop.index)
stats = stats[["PTS", "AST", "TOV",'MP']]        

def get_player(player):
    x = stats.index
    return stats.iloc[x.get_loc(player)]


              

              