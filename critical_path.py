#!/usr/bin/env python3
# shebang for linux

"""
MODULE DESCRIPTION

MODULE FEATURES
file, string, location of file to open
end, int, index of end point for critical path analysisi
"""

import sys
import numpy as np
import pandas as pd

file = sys.argv[1]
end_index = int(sys.argv[2])
crit_path = []

#load csv of template format
df = pd.read_csv(file)
print(df.head())

#search for end point
predecessors = df.loc[df['index'] == end_index][['predecessor_index_1','predecessor_index_2','predecessor_index_3','predecessor_index_4','predecessor_index_5','predecessor_index_6']].values.tolist()[0]

#search backwards from each dependency
nan_count = 0

def pre(predecessors):

    for pre in predecessors:
    
        #check if all nan
        if pre == np.nan:
            if count >=  6:
                break
            else:
                count += 1
        
        elif pre != np.nan:
        
