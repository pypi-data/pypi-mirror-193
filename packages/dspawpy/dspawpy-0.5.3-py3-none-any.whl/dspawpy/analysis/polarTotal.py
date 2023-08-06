'''
用于铁电极化案例绘图
'''
import h5py
import numpy as np
import os
import matplotlib.pyplot as plt

subfolders = next(os.walk('./'))[1]
subfolders.sort()

# read only once
quantum = np.array(h5py.File('./%s/scf.h5' %
                   subfolders[0]).get('/PolarizationInfo/Quantum'))

totals = np.empty(shape=(len(subfolders), 3))
for i, fd in enumerate(subfolders):
    data = h5py.File('./%s/scf.h5' % fd)
    total = np.array(data.get('/PolarizationInfo/Total'))
    totals[i] = total
    print('Total: ', total)

fig, axes = plt.subplots(1, 3, sharey=True)
xyz = ['x', 'y', 'z']
for j in range(3):
    axes[j].plot(subfolders, totals[:, j], '.')
    for r in range(3):
        totals_up = totals + quantum*r
        totals_down = totals - quantum*r
        axes[j].plot(subfolders, totals_up[:, j], '.')
        axes[j].plot(subfolders, totals_down[:, j], '.')
    axes[j].set_title('P%s' % xyz[j])
    axes[j].set_xticklabels(labels=subfolders, rotation=90)
    axes[j].grid(axis='x', color='gray', linestyle=':', linewidth=0.5)

plt.tight_layout()
plt.savefig('pol.png')
