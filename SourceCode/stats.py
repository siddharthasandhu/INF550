import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import brewer2mpl
from matplotlib import rcParams

#colorbrewer2 Dark2 qualitative color table
dark2_cmap = brewer2mpl.get_map('Dark2', 'Qualitative', 7)
dark2_colors = dark2_cmap.mpl_colors

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[0]
rcParams['font.family'] = 'StixGeneral'


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks

    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()


tester = []
path  = "/home/squirrel/Documents/INF 550 Dataset/results"
with open(path,"r") as infile:
    for row in infile:
        row = row.strip("c^").split("\n")
        tester.append(row[0])

the_brain = {}
feature_set = []
totalScores = []

for value in tester[1:]:
    totalScores.append((value.split()[0], value.split()[5]))
    feature = value.split()[0].rsplit('_', 1)[0]
    score = float(value.split()[5].strip("%"))
    if feature not in the_brain:
        feature_set.append(feature)
        the_brain[feature] = [score]
    else:
        the_brain[feature].append(score)
print len(feature_set)


fig, axes=plt.subplots(figsize=(23,15), nrows=6, ncols=5)
fig.subplots_adjust(hspace = 0.8)
fig.subplots_adjust(wspace = 0.6)

for ix in np.arange(6):
    for ix2 in np.arange(5):
        if (ix*6 + ix2) < len(feature_set):
            axes[ix][ix2].hist2d(the_brain[feature_set[ix*6+ix2]], bins=10)
            axes[ix][ix2].set_title(feature_set[ix*6+ix2])
            axes[ix][ix2].set_ylabel("Count")
            axes[ix][ix2].set_xlabel("Weight")
            remove_border(axes[ix][ix2])
        else:
            fig.delaxes(axes[ix][ix2])

lessThanAbsOne = [e1[0] for e1 in totalScores if e1[1] < 1 and e1[1] > -1]

with open('featureRemove.csv', 'w') as fp:
    a = csv.writer(fp, delimiter='\n')
    data = lessThanAbsOne
    a.writerow(data)

