#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import pandas as pd

#read data
data = pd.read_csv("../../data/variance_partitions.tsv", sep="\t", index_col=0)
data = data/100

sns.set_style("whitegrid")
cmap = plt.cm.get_cmap('viridis')

# Divide the colormap into 14 bins
num_bins = 3
colors = [cmap(i / num_bins) for i in range(num_bins)]
# Extract hex codes
colors = [mcolors.to_hex(color) for color in colors]
#make palette
custom_palette = sns.color_palette(colors)
sns.set_palette(custom_palette)


plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20

data.plot(kind="bar", stacked=True, figsize=(5, 8), linewidth=0)
plt.xlabel('')
plt.ylabel('Proportion of Variance Explained', fontsize=20)
plt.xticks(ticks=[0,1], labels=["Composition", "Structure"], rotation='horizontal')
plt.legend(fontsize = 15, loc="upper left")
plt.ylim(0, 1)

#save figure
plt.tight_layout()
plt.savefig("../../figures/variance_explained.pdf", bbox_inches = "tight")
