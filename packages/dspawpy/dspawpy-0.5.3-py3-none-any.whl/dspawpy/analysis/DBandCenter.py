from scipy import integrate
from pymatgen.electronic_structure.core import Spin, OrbitalType

def d_band(spin,dos_data):                 #定义函数，括号里给出函数的两个变量

    dos_d = dos_data.get_spd_dos()         #定义新的变量dos_d，给变量赋值，dos_data.get_spd_dos中，dot前面的dos_data是你所定义的函数里的变量，get_spd_dos是库里的函数
    dos_d = dos_d[OrbitalType.d]           #给dos_d再次赋值
#    dos_plotter = DosPlotter(stack=False, zero_at_efermi=True)
#    dos_plotter.add_dos("d", dos_d)

    # define

    epsilon = dos_d.energies
    Efermi = dos_data.efermi
    epsilon = epsilon - Efermi  # shift d-band center

    N1 = dos_d.densities[spin]
    M1 = epsilon * N1
    SummaM1 = (integrate.simps(M1, epsilon))
    SummaN1 = (integrate.simps(N1, epsilon))

#    plt = dos_plotter.get_plot()
#    plt.show()

    return SummaM1 / SummaN1