from ase import Atoms
from ase.io import Trajectory,read
from ase.constraints import StrainFilter
from gpaw import GPAW, FermiDirac, MixerSum
from gpaw import extra_parameters
from ase.optimize import BFGS
from ase.constraints import FixAtoms
extra_parameters['blacs'] = True
import numpy as np


bulk = read('initial.traj')
bulk.set_pbc([True,True,False])

###Sort the atoms 
Ca = bulk[[atom.index for atom in bulk if atom.symbol =='Ca']]
O  = bulk[[atom.index for atom in bulk if atom.symbol =='O']]
Ti = bulk[[atom.index for atom in bulk if atom.symbol =='Ti']]
surf = Ca + O + Ti
c = FixAtoms(indices = [atom.index for atom in surf if atom.position[2] < 8.5])
surf.set_constraint(c)
surf.set_initial_magnetic_moments(16*[0]+48*[0]+16*[2])

###calculator 
calc = GPAW(mode='lcao', basis='dzp', xc='PBE',
                occupations = {'name': 'methfessel-paxton', 'width': 0.1, 'order':0 },
                h = 0.2,
                mixer=MixerSum(beta=0.25, nmaxold=3, weight=50.0),
                spinpol=True,
                nbands='120%', kpts=(3,3,1), txt = 'eval.txt',
                parallel=dict(sl_auto=True))  # enable ScaLAPACK parallelization

surf.set_calculator(calc)

relax = BFGS(surf, trajectory='opt.traj',logfile='opt.log')
relax.run(fmax=0.05)
