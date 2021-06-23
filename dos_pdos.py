### scf part to get gpw file for further dos and pdos calculations
from ase import Atoms
from ase.io import Trajectory,read
from ase.constraints import StrainFilter
from gpaw import GPAW, FermiDirac, Mixer, MixerSum
from gpaw import extra_parameters
extra_parameters['blacs'] = True
from ase.optimize import BFGS
import numpy as np

bulk = read('opt.traj',index =-1)
k = 5


calc = GPAW(mode='lcao', basis='dzp', xc='PBE',
            occupations=FermiDirac(0.05),
            mixer=MixerSum(beta=0.25, nmaxold=3, weight=50.0),
            setups={'Ti': ':d,6.0'},  # U=6 eV for Ti d orbitals
            spinpol=True,
            h = 0.2,
            nbands=-48, kpts=(k, k, k), txt = 'eval.txt',
            parallel=dict(sl_auto=True))  # enable ScaLAPACK parallelization

bulk.set_calculator(calc)
bulk.get_potential_energy()
calc.write('STO.gpw')

### total dos
from ase import Atoms
from ase.io import Trajectory,read
from ase.constraints import StrainFilter
from gpaw import GPAW, FermiDirac, Mixer, restart
from gpaw import extra_parameters
extra_parameters['blacs'] = True
from ase.optimize import BFGS
import numpy as np
import matplotlib.pyplot as plt

bulk,calc = restart('STO.gpw')
e, dos_up = calc.get_dos( npts=2001, spin =0,width=0.2)
e, dos_down = calc.get_dos( npts=2001, spin =1,width=0.2)
e_f = calc.get_fermi_level()

np.savetxt('dos_up.txt',dos_up, fmt='% 12.5f')
np.savetxt('dos_down.txt',dos_down, fmt='% 12.5f')
np.savetxt('e.txt',e-e_f, fmt='% 12.5f')

### pdos for LCAO
from ase import Atoms
from ase.io import Trajectory,read
from ase.constraints import StrainFilter
from gpaw import GPAW, FermiDirac, Mixer, restart
from gpaw import extra_parameters
extra_parameters['blacs'] = True
from ase.optimize import BFGS
import numpy as np
import matplotlib.pyplot as plt
from gpaw.utilities.dos import RestartLCAODOS, fold
from ase.units import Hartree

calc = GPAW('STO.gpw')

dos = RestartLCAODOS(calc)

ef = calc.get_fermi_level()
e_Ti, pdos_Ti = calc.get_orbital_ldos(a=1,angular='d',npts=2001, width=0.2)
e_O, pdos_O   = calc.get_orbital_ldos(a=7, angular='p',npts=2001, width=0.2)

e_Ti, Ti_dos = calc.get_lcao_dos(atom_indices= 1,npts=2001, width=0.2)
e, Ti_cpdos = dos.get_subspace_pdos([5, 6, 7, 8, 9])

np.savetxt('Ti_e.txt', e_Ti-ef, fmt='% 12.5f')
np.savetxt('Ti_d.txt', pdos_Ti, fmt='% 12.5f')
np.savetxt('O_e.txt' , e_O-ef, fmt='% 12.5f')
np.savetxt('O_p.txt' , pdos_O, fmt='% 12.5f')
np.savetxt('Ti_lcao.txt', Ti_dos, fmt='% 12.5f')
np.savetxt('Ti_pdos.txt', Ti_pdos, fmt='% 12.5f')


###plot the dos with matplotlib
import numpy as np
import matplotlib.pyplot as plt
e = np.loadtxt('e.txt')
dos = np.loadtxt('dos.txt')
e_ti = np.loadtxt('Ti_e.txt')
d_ti = np.loadtxt('Ti_d.txt')
e_O = np.loadtxt('O_e.txt')
p_O = np.loadtxt('O_p.txt')

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

font2 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }

#set xrange
xll = -10
xlr = 5
ylb = 0
ylt = 4
plt.xlim(xll,xlr)
plt.ylim(ylb,ylt)
lx = np.linspace(xll,xlr,3)
#ly = lx*0
#plt.plot(lx,ly, '--', color = 'gray', linewidth=1)


#set label
plt.xlabel('$E-E_{F}$ $\mathrm{/eV}$', fontdict = font)
plt.ylabel('DOS', fontdict = font)

#set tick
#plt.yticks(np.arange(-40, 200, step=20))

#plot
p1 = plt.plot(e,dos/8, '-', color = 'grey', markersize = 5,linewidth=2)
plt.fill_between(e,dos/8,np.zeros_like(dos),facecolor='lightgrey')
p2 = plt.plot(e_O,p_O, '-', color = 'red', markersize = 5,linewidth=2)
p3 = plt.plot(e_ti,d_ti, '-', color = 'blue', markersize = 5,linewidth=2)
plt.legend((p1[0],p2[0],p3[0]),
        ('Total/8',
         'O-p',
         'Ti-d'),
        loc = 0,handlelength=2, borderpad=0.2, labelspacing=0.1, fontsize=10)

plt.tight_layout()
plt.savefig('dos.pdf', dpi=300)
plt.show()
