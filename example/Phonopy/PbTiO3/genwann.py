import numpy as np
from ase.io import write
#from banddownfolder.scdm import PhonopyDownfolder
from wannierbuilder.scdm import PhonopyDownfolder
import matplotlib.pyplot as plt

fname = 'phonopy_params.yaml'
downfolder=PhonopyDownfolder(phonopy_yaml=fname)
downfolder.downfold(method='scdmk', nwann=3,
                    anchors={(0,0,0):(0,1,2)}, mu=0.03, sigma=0.1,  # acoustic phonon
                    #anchors={(0,0,0):(12,13,14)}, mu=2, sigma=1,     # optical phonon
                    use_proj=True, kmesh=(3,3,3), weight_func='Gauss')
write('POSCAR.vasp', downfolder.model.atoms, vasp5=True)
ax=downfolder.plot_band_fitting(kvectors=np.array([[0. , 0. , 0. ],
                                                   [0.5, 0.0, 0. ],
                                                   [0.5, 0.5, 0.0],
                                                   [0.5 , 0.5 , 0.5 ],
                                                   [0.5, 0.0, 0.0],
                                                   [0.0,0.0,0],
                                                   [0.5,0.5,0.5]]),
                                npoints=100, erange=[0,0.1],
                                knames=['$\\Gamma$', 'X','M', 'R', 'X', '$\\Gamma$', "R"],
                                linestyle='-', marker='',
                                savefig='df.svg', show=False)

#plt.savefig('LWF_PTO.pdf')
#plt.show()
