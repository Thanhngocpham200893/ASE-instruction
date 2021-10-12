from ase.io.trajectory import Trajectory
from ase.ga.utilities import get_rdf
from ase.io import read
import matplotlib.pyplot as plt
import numpy as np

traj =  read('pd9.traj',index=-1)
traj1 =  read('bulk_new.traj',index=-1)
rdf, dis = get_rdf(atoms=traj,rmax=5., nbins=500, elements = [46,46],no_dists=False)
rdf1, dis1 = get_rdf(atoms=traj1,rmax=5., nbins=500, elements = [46,46],no_dists=False)


def spectrum(E,osc,fwhm,x):
    gE=[]
    sigma = fwhm/2.355
    for Ei in x:
        tot=0
        for Ej,os in zip(E,osc):
            tot+=os*np.exp(-((((Ej-Ei)/sigma)**2)))
        gE.append(tot)
    return gE

x=np.linspace(1,7, num=500, endpoint=True)
fwhm=0.2
gE=spectrum(dis,rdf,fwhm,x)
gE1=spectrum(dis1,rdf1,fwhm,x)

plt.ylim((0,100))
plt.xlim((1,7))
plt.xlabel('distance /$\AA$')
plt.ylabel('Radial distribution function')
plt.plot(x, gE, color='darkblue',label = 'Pd_9')
plt.plot(x, gE1, color='red',label = 'bulk fcc')
#plt.plot(dis, rdf, color='red')
plt.legend(
        loc = 0,handlelength=2, borderpad=0.2, labelspacing=0.1, fontsize=10)
plt.show()
~             
