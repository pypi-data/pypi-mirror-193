# -*- coding: utf-8 -*-

import math, json
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

from numpy import pi
from scipy.interpolate import interp1d
from dspawpy.io.read import load_h5


def getEwtData(nk, nb, celtot, proj_wt, ef, de, dele):
    emin = np.min(celtot) - de
    emax = np.max(celtot) - de

    emin = np.floor(emin - 0.2)
    emax = max(math.ceil(emax)*1.0, 5.0)

    nps = int((emax - emin) / de)

    X = np.zeros((nps + 1, nk))
    Y = np.zeros((nps + 1, nk))

    X2 = []
    Y2 = []
    Z2 = []

    for ik in range(nk):
        for ip in range(nps+1):
            omega = ip * de + emin + ef
            X[ip][ik] = ik
            Y[ip][ik] = ip*de+emin
            ewts_value = 0
            for ib in range(nb):
                smearing =  dele / pi / ((omega - celtot[ib][ik]) ** 2 + dele ** 2)
                ewts_value += smearing * proj_wt[ib][ik]
            if ewts_value>0.01:
                X2.append(ik)
                Y2.append(ip*de+emin)
                Z2.append(ewts_value)

    Z2_half = max(Z2)/2

    for i,x in enumerate(Z2):
        if x > Z2_half:
            Z2[i] = Z2_half

    plt.scatter(X2, Y2, c = Z2, cmap="hot")
    plt.xlim(0,200)
    plt.ylim(emin - 0.5, 15)
    ax = plt.gca()
    plt.colorbar()
    ax.set_facecolor("black")

    return plt

def get_plot_potential_along_axis(data,axis=2,smooth=False,smooth_frac=0.8,**kwargs):
    all_axis = [0,1,2]
    all_axis.remove(axis)
    y = np.mean(data,tuple(all_axis))
    x = np.arange(len(y))
    if smooth:
        s = sm.nonparametric.lowess(y, x, frac=smooth_frac)
        plt.plot(s[:,0], s[:,1], label="macroscopic average",**kwargs)

    plt.plot(x,y,label="planar electrostatic",**kwargs)
    return plt

def plot_potential_along_axis(potential_dir:str, axis=2, smooth=False, smooth_frac=0.8, **kwargs):
    if potential_dir.endswith(".h5"):
        potential = load_h5(potential_dir)
        grid = potential["/AtomInfo/Grid"]
        # pot = np.asarray(potential["/Potential/TotalElectrostaticPotential"]).reshape(grid, order="F")
        # DS-PAW 数据写入h5 列优先
        # h5py 从h5读取数据 默认行优先
        # np.array(data_list) 默认行优先
        # 所以这里先以 行优先 把 “h5 行优先 读进来的数据” 转成一维， 再以 列优先 转成 grid 对应的维度
        tmp_pot = np.asarray(potential["/Potential/TotalElectrostaticPotential"]).reshape([-1, 1], order="C")
        pot = tmp_pot.reshape(grid, order="F")
    elif potential_dir.endswith(".json"):
        with open(potential_dir, 'r') as f:
            potential = json.load(f)

        grid = potential["AtomInfo"]["Grid"]
        pot = np.asarray(potential["Potential"]["TotalElectrostaticPotential"]).reshape(grid, order="F")
    else:
        print("file - " + potential_dir + " :  Unsupported format!")
        return

    return get_plot_potential_along_axis(pot, axis=2, smooth=False)

def plot_optical(optical_dir:str,key:str,index:int=0):
    """

    Args:
        optical_h5: optical.h5 filename
        key: "AbsorptionCoefficient","ExtinctionCoefficient","RefractiveIndex","Reflectance"
        index:

    Returns:

    """
    if optical_dir.endswith("h5"):
        data_all = load_h5(optical_dir)
        energy = data_all["/OpticalInfo/EnergyAxe"]
        data = data_all["/OpticalInfo/" + key]
    elif optical_dir.endswith("json"):
        with open(optical_dir, 'r') as fin:
            data_all = json.load(fin)

        energy = data_all["OpticalInfo"]["EnergyAxe"]
        data = data_all["OpticalInfo"][key]
    else:
        print("file - " + optical_dir + " :  Unsupported format!")
        return

    data = np.asarray(data).reshape(len(energy),6)[:,index]

    inter_f = interp1d(energy, data, kind="cubic")
    energy_spline = np.linspace(energy[0],energy[-1],2001)
    data_spline = inter_f(energy_spline)

    plt.plot(energy_spline,data_spline,c="b")
    plt.xlabel("Photon energy (eV)")
    plt.ylabel("%s %s"%(key,r"$\alpha (\omega )(cm^{-1})$"))

def plot_bandunfolding(band_dir:str, ef=0.0, de=0.05, dele= 0.06):
    if band_dir.endswith(".h5"):
        band = load_h5(band_dir)
        number_of_band = band["/BandInfo/NumberOfBand"][0]
        number_of_kpoints = band["/BandInfo/NumberOfKpoints"][0]
        data = band["/UnfoldingBandInfo/Spin1/UnfoldingBand"]
        weight = band["/UnfoldingBandInfo/Spin1/Weight"]
    elif band_dir.endswith(".json"):
        with open(band_dir, 'r') as f:
            band = json.load(f)
        number_of_band = band["BandInfo"]["NumberOfBand"]
        number_of_kpoints = band["BandInfo"]["NumberOfKpoints"]
        data = band["UnfoldingBandInfo"]["Spin1"]["UnfoldingBand"]
        weight = band["UnfoldingBandInfo"]["Spin1"]["Weight"]
    else:
        print("file - " + band_dir + " :  Unsupported format!")
        return

    celtot = np.array(data).reshape((number_of_kpoints, number_of_band)).T
    proj_wt = np.array(weight).reshape((number_of_kpoints, number_of_band)).T

    return getEwtData(number_of_kpoints, number_of_band, celtot, proj_wt, ef, de, dele)


if __name__ == "__main__":
    path = "./../test/band/2.22.1/band.h5"
    p = plot_bandunfolding(path, ef=7.6923)
    p.savefig("bandunfolding_plot.png")
    p.show()
    