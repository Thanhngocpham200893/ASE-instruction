### The scrtipt to estimate entropy from Harmonic limit (usually used for adsorbate)

from ase.thermochemistry import HarmonicThermo
import numpy as np

vib_energies = np.loadtxt('vib.txt', usecols = (1), unpack = True) # read the vibrational energies in meV from output of vibrational analysis of ASE

thermo = HarmonicThermo( vib_energies = 0.001*vib_energies, # change to eV
                         potentialenergy = 0.0)
G = thermo.get_entropy( temperature = 298.15, verbose = True)
print(G)
