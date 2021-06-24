###read the energies in bulk.traj win index from 1 to -1 (read all trajactories except for 1st one) and do fitting
from ase.io import read
from ase.units import kJ
from ase.eos import EquationOfState
configs = read('bulk.traj@1:-1')
# Extract volumes and energies:
volumes = [sto.get_volume() for sto in configs]
energies = [sto.get_potential_energy() for sto in configs]
eos = EquationOfState(volumes, energies) ### using third order inverse polynomial fitting
### different equation of states can be used by specifying eos = ''
###eos = EquationOfState(volumes, energies, eos = 'vinet') 
v0, e0, B = eos.fit()
print('optimized lattice parameter is %12.5f Angstrom' %(v0**(1/3)))
eos.plot('fit.pdf')
