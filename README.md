# banddownfolder
[![Documentation Status](https://readthedocs.org/projects/banddownfolder/badge/?version=latest)](https://banddownfolder.readthedocs.io/en/latest/?badge=latest)
![Static Badge](https://img.shields.io/badge/:badgeContent)

BandDownfolder is a python package for build  electron/phonon/magnon/etc Wannier functions.


It has interface to:
 * Siesta (through sisl)
 * Anaddb (part of Abinit)
 * Phonopy

The online documentation can be found at:
https://banddownfolder.readthedocs.io/en/latest/index.html


# Infomation from modified coder
2023-08-14 forked from [mailhexu/banddownfolder](https://github.com/mailhexu/banddownfolder)  
[original author's documents](https://banddownfolder.readthedocs.io/en/latest/index.html)  

+ debug 
I fix some bugs and typos in dir `wannierbuilder` and `setup.py` by simply comment out the error line of the code, I try to minimize changes as far as possible.
My aims is to make the scripts in dir `example/Wannier90` and `example/Phonopy/PbTiO3` running, and generating correct energy bands and real space hamiltonian, i.e. `band.png` and `hr.txt`. 
I have not check other examples. I don't know whether ncfile works correctly or not.

+ new function
I add a new function called `model.downfold(write_wannier_hr_dat='Downfolded_wannier_hr.dat')`,  
this function will output real space hamiltonian in wannier90-like format. example is also updated.  
If you don't want to use this new function, set this tag to `None`, i.e. `write_wannier_hr_dat=None`.

I add a new tag in `model.plot_band_fitting(linestyle='-')`. Usage suggetion:  
```
model.plot_band_fitting(linestyle='-',marker='')  # pure line
model.plot_band_fitting(linestyle='', marker='o')  # pure empty points
model.plot_band_fitting(linestyle='-',marker='o')  # with line-points
```


+ tested example
see `example/Wannier90` and `example/Phonopy/PbTiO3`.

## installation and example

+ how to install (using conda env)

```
conda create -n wannierbuilder python=3.11 --yes
conda activate wannierbuilder

cd <package dir>    #say wannierbuilder or banddownfolder
pip install . 

# or, if you use tuna mirror of pip
pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple
```

+ how to run `example/Wannier90`
```
cd example/Wannier90
python downfold.py
```

