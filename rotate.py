from ase.io import read, write
import numpy as np

surf = read('scf.pwi')
print(surf)

O  = surf.get_positions()[156,:]
Pd = surf.get_positions()[0,:]

a = Pd - O
v = np.array([0,0,2.058])
surf.rotate(center=O,a = a, v = v, rotate_cell = True)
surf.write('test.xsf')
surf.write('rotate.pwi')
