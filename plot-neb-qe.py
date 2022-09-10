import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

from ase.io import read, write
from ase.visualize import view

import sys

energy     = sys.argv[1]
energy_int = sys.argv[2]

dis,     e = np.loadtxt(energy, usecols = (0,1), unpack = True)
dis_1, e_1 = np.loadtxt(energy_int, usecols = (0,1), unpack = True)

###best
fig = plt.figure(figsize = [3.5,2.625])
ax = fig.gca()
ax.tick_params(labelsize='small', direction = 'in',width=1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
#set font
#plt.rcParams["mathtext.fontset"]="dejavuserif"
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

plt.xlabel('Reaction coordinate (arb. units)', fontdict = font)
plt.ylabel('Energy (eV)', fontdict = font)

plt.plot(dis,e, 'o', color = 'red', markersize = 5,linewidth=2)
plt.plot(dis_1,e_1, '-', color = 'grey', markersize = 5,linewidth=2)
plt.tight_layout()
plt.savefig('path.pdf', dpi=300)
plt.show()
