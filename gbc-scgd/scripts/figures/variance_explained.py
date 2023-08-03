#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#read data
data = pd.read_csv("../../data/variance_partitions.tsv", sep="\t", index_col=0)

sns.set_style("darkgrid")
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20

data.plot(kind="bar", stacked=True, figsize=(5, 8))
plt.xlabel('')
plt.ylabel('% of Variance Explained', fontsize=20)
plt.xticks(ticks=[0,1], labels=["Composition", "Structure"], rotation='horizontal')
plt.legend(fontsize = 15, loc="upper left")

#save figure
plt.tight_layout()
plt.savefig("../../figures/variance_explained.pdf", bbox_inches = "tight")
