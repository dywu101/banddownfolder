# banddownfolder
[![Documentation Status](https://readthedocs.org/projects/banddownfolder/badge/?version=latest)](https://banddownfolder.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/mailhexu/banddownfolder.svg?branch=master)](https://travis-ci.com/mailhexu/banddownfolder)

BandDownfolder is a python package for build  electron/phonon/magnon/etc Wannier functions.


It has interface to:
 * Siesta (through sisl)
 * Anaddb (part of Abinit)
 * Phonopy

The online documentation can be found at:
https://banddownfolder.readthedocs.io/en/latest/index.html


## Infomation provided by the modifier
2023-08-14  

I fix some bugs in dir `wannierbuilder` and `setup.py` by simply comment out the error line of the code and minimize changes as far as possible.  
My aims is to make the scripts in dir `example/Wannier90` running, and generating correct energy bands and real space hamiltonian, i.e. `band.png` and `hr.txt`.  
I have not check other examples. I don't know whether ncfile works correctly or not.  



+ how to install (using conda env)
```
conda create -n wannierbuilder python=3.11 --yes
conda activate wannierbuilder

cd <package dir>
pip install . 
# or
pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple
```

+ how to run `example/Wannier90`
```
cd example/Wannier90
python downfold.py
```

+ new function
I add a new function called `model.downfold(write_wannier_hr_dat='Downfolded_wannier_hr.dat')`,  
this function will output real space hamiltonian in wannier90-like format.
If you don't want to use this new function, set this tag to `None`, i.e. `write_wannier_hr_dat=None`.
