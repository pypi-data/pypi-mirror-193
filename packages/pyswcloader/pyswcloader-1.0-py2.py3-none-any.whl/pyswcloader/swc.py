import pandas as pd
import numpy as np
import os, sys
from tqdm import tqdm
from treelib import Tree
import math
import seaborn as sns
from matplotlib import pyplot as plt
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def read_swc(path):
    data = pd.read_csv(path, sep=' ', header=None, comment='#')
    data.columns = ['id', 'type', 'x', 'y', 'z', 'radius', 'parent']
    data.index = np.arange(1, len(data)+1)
    return data

def swc_preprocess(path, save_path=None, save=False, check_validity=True, flip=True, dimension=[13200, 8000, 11400]):
    data = read_swc(path)
    if flip==True and float(data.loc[1, 'z'])>(11400/2):
        data.z = dimension[2] - data.z
    if check_validity==True:
        if len(data.loc[data.parent==-1])>1 or len(data.loc[data.type==1])>1:
            raise Exception('More than one soma detected.')
    if data.x.max()>dimension[0]:
        data.x = [item if item<dimension[0] else dimension[0]-1 for item in data.x]
        print('X axis exceeds boundary.')
    if data.y.max()>dimension[1]:
        data.y = [item if item<dimension[1] else dimension[1]-1 for item in data.y]
        print('Y axis exceeds boundary.')
    if data.z.max()>dimension[2]:
        data.z = [item if item<dimension[2] else dimension[2]-1 for item in data.z]
        print('Z axis exceeds boundary.')    
    if save==True:
        data.to_csv(save_path, sep=" ", header=None, index=None)
    return data

def swc_tree(path):
    tree = Tree()
    data = read_swc(path)
    for _, row in data.iterrows():
        tree.create_node(
            tag=int(row.id),
            identifier=int(row.id),
            data=row.loc[['x', 'y', 'z']].to_dict(),
            parent=row.parent if row.parent != -1 else None
        )
    return tree

def total_length(path):
    length = 0
    data = read_swc(path)
    for idx in data.index[1:]:
        parent_idx = data.loc[idx, 'parent']
        length += math.dist(data.loc[idx, 'x':'z'], data.loc[parent_idx, 'x':'z'])
    return length

def read_neuron_path(data_path):
    path_list = glob.glob(os.path.join(data_path, '**/*.swc'), recursive=True)
    return path_list

def plot_soma_distribution(data_path, **kwargs):
    path_list = read_neuron_path(data_path)
    soma_info = pd.DataFrame()
    for path in tqdm(path_list):
        data = read_swc(path)
        soma_info = soma_info.append(data.loc[1, 'x':'z'])
    fig, _ = plt.subplots(nrows=3, sharex=False, sharey=False)
    cnt = 1
    for axis in ['x', 'y', 'z']:
        plt.subplot(310+cnt)
        sns.kdeplot(list(soma_info[axis]), **kwargs)
        plt.ylabel('')
        ax = plt.gca()
        if axis == 'x':
            ax.set_title('Anterior - Posterior')
        elif axis == 'y':
            ax.set_title('Dorsal - Ventral')
        else:
            ax.set_title('Medial - Lateral')
        cnt += 1
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.subplots_adjust(hspace=1)
    plt.subplots_adjust(wspace=0)
    return fig
    
