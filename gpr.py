import numpy as np
import unittest
from gpr import GPR
from bfgslinesearch_constrained import BFGSLineSearch_constrained
from descriptor.fingerprint import Fingerprint
from ase.io import read

traj = read('structures.traj', index=':50')
traj_train = traj[:40]
traj_predict = traj[40:]

Rc1 = 5
binwidth1 = 0.2
sigma1 = 0.2

Rc2 = 4
Nbins2 = 30
sigma2 = 0.2

gamma = 1
eta = 30
use_angular = False

descriptor = Fingerprint(Rc1=Rc1, Rc2=Rc2, binwidth1=binwidth1, Nbins2=Nbins2, sigma1=sigma1, sigma2=sigma2, gamma=gamma, eta=eta, use_angular=use_angular)


gpr = GPR(kernel='double', descriptor=descriptor)

gpr.train(atoms_list=traj_train)


###calculator
from gpr_calculator import gpr_calculator

calc = gpr_calculator(gpr)


for i in traj_predict:
    i.set_calculator(calc)
    print(i.get_total_energy())
    print(i.get_forces())
