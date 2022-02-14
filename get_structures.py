
# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

from ase.io import read, write
from ase.visualize import view

import sys

runs_name = sys.argv[1]
e_window  = float(sys.argv[2])

structures = []
traj_path =  runs_name
traj = read(traj_path, index=':')

###best
E = np.array([a.get_potential_energy() for a in traj])
index_best = np.argmin(E)
Ebest = E[index_best]
a_best = traj[index_best]
print(E)

for index,e in enumerate(E):
    if e < Ebest + e_window:
        print(index,e)
        structures.append(traj[index])
write('temp.traj', structures)
view(structures)
