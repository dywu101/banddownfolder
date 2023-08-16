from wannierbuilder import W90Downfolder
import numpy as np

'''
to run this script, at least two files are needed, in SMO_wannier:
abinito_w90_down_hr.dat  abinito_w90_down.win 
 

especially, we only need poscar part of abinito_w90_down.win
(cell vector and atom position, in cart)

begin unit_cell_cart
end unit_cell_cart

begin atoms_cart
end atoms_cart
'''

def main():
    # Read From Wannier90 output
    model = W90Downfolder(folder='./SMO_wannier',
                          prefix='abinito_w90_down')

    # Downfold the band structure.
    model.set_parameters(
        method='scdmk',         #scdmk, projected
        kmesh=(3,3,3),
        nwann=2,
        weight_func='Gauss',    #unity, Gauss, Fermi, window
        mu=10.0,
        sigma=3.0,
        selected_basis=None,    #[0,1,2], None
        anchors={(0,0,0): (12,13)},
        use_proj=True,
        exclude_bands=[],
        post_func=None)
 
    model.downfold(
        post_func=None,
        output_path='./',
        write_hr_nc='Downfolded_hr.nc',
        write_hr_txt='Downfolded_hr.txt',
        write_wannier_hr_dat='Downfolded_wannier_hr.dat')

    # Plot the band structure.
    model.plot_band_fitting(
        kvectors=np.array([[0,   0,   0  ], 
                           [0.5, 0,   0  ],
                           [0.5, 0.5, 0  ], 
                           [0,   0,   0  ],
                           [0.5, 0.5, 0.5]]),
        knames=['$\Gamma$', 'X', 'M', '$\Gamma$', 'R'],
        supercell_matrix=None,
        npoints=100,
        efermi=None,        #0.0
        erange=None,        #[-1,1]
        fullband_color='blue',
        downfolded_band_color='green',
        marker='o',          # '', 'o'
        ax=None,
        savefig='Downfolded_band.svg',
        show=False)

if __name__ == "__main__":
    main()

