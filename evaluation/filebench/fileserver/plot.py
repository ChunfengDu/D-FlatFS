#!/usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import csv

xs = [1,2,3,4,5,6,7]

default = [0, 0, 0, 0, 0, 0, 0]
data = {
    'ext4': default,
    'xfs': default,
    'nova': default,
    'pmfs': default,
    'betrfs': default,
    'vfs_opt': default,
    'flatfs': default
}
with open('.data') as f:
    for line in f.readlines():
        fs, nthread, thruput = line.strip().split()
        if data[fs] == default:
            data[fs] = []
        data[fs].append(float(thruput) / 1000)

ext4 = data['ext4']
xfs = data['xfs']
nova = data['nova']
pmfs = data['pmfs']
betrfs = data['betrfs']
vfs_opt = data['vfs_opt']
flatfs = data['flatfs']

plt.plot(xs, ext4, markerfacecolor='none',color='black', marker='s', markersize=10, linestyle='-', linewidth=1, label='Ext4')
plt.plot(xs, xfs, markerfacecolor='none',color='black', marker='^', markersize=10, linestyle='-', linewidth=1, label='XFS')
plt.plot(xs, nova, markerfacecolor='none',color='black', marker='x', markersize=10, linestyle='-', linewidth=1, label='NOVA')
plt.plot(xs, pmfs, markerfacecolor='none',color='black', marker='D', markersize=10, linestyle='-', linewidth=1, label='PMFS')
plt.plot(xs, betrfs, markerfacecolor='none',color='black', marker='<', markersize=10, linestyle='-', linewidth=1, label='BetrFS')
plt.plot(xs, vfs_opt, markerfacecolor='none',color='black', marker='>', markersize=10, linestyle='-', linewidth=1, label='VFS-opt')
plt.plot(xs, flatfs, markerfacecolor='none',color='black', marker='o', markersize=10, linestyle='-', linewidth=1, label='FlatFS')

font = {'size': '20','fontname': 'Times New Roman'}
plt.xlabel("Thread Number", font)
plt.ylabel("Throughput (K ops/s)", font)

font2 = {'size': '15','fontname': 'Times New Roman'}
ax = plt.gca()
xtick=[1,2,3,4,5,6,7]
ax.set_xticks(xtick)
xlabel=[1,8,16,24,32,40,48]
ax.set_xticklabels(xlabel, font2)

ytick=[0,200,400,600,800,1000]
ax.set_yticks(ytick)
ax.set_yticklabels(ytick, font2)

plt.legend(loc = 2, ncol=3, frameon=False, mode="expand", prop={'size': 14, 'family': 'Times New Roman'},handletextpad=0.2)
plt.show()
