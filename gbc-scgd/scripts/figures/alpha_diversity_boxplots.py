#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib
import pandas as pd

#load data
alpha_data = pd.read_table('../../data/alpha_diversity.tsv', delimiter='\t', header='infer')

#make plot
sns.set_style('whitegrid')
cmap = plt.cm.get_cmap('viridis')

# Divide the colormap into 14 bins
num_bins = 5
colors = [cmap(i / num_bins) for i in range(num_bins)]
# Extract hex codes
colors = [mcolors.to_hex(color) for color in colors]
#make palette
custom_palette = sns.color_palette(colors)
sns.set_palette(custom_palette)

fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4, figsize=(18, 8))
sns.pointplot(data=alpha_data, x='species', y='observed_features', color='black', ax=ax1, errorbar=("ci", 95), capsize=0.4, join=False)
sns.pointplot(data=alpha_data, x='species', y='shannon_entropy', color='black', ax=ax2, errorbar=("ci", 95), capsize=0.4, join=False)
sns.pointplot(data=alpha_data, x='species', y='pielou_evenness', color='black', ax=ax3, errorbar=("ci", 95), capsize=0.4, join=False)
sns.pointplot(data=alpha_data, x='species', y='faith_pd', color='black', ax=ax4, errorbar=("ci", 95), capsize=0.4, join=False)

labels = ['D. nigrospiracula', 'D. mojavensis', 'D. mettleri', 'D. arizonae', 'D. melanogaster']
ax1.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax2.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax3.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax4.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')

ax1.set_ylabel("ASV Richness", fontsize=22)
ax1.tick_params(axis='y', labelsize=22)

ax2.set_ylabel("Shannon Entropy", fontsize=22)
ax2.tick_params(axis='y', labelsize=22)

ax3.set_ylabel("Pielou's Evenness", fontsize=22)
ax3.tick_params(axis='y', labelsize=22)

ax4.set_ylabel("Phylogenetic Diversity", fontsize=22)
ax4.tick_params(axis='y', labelsize=22)

ax1.set(xlabel=None)
ax2.set(xlabel=None)
ax3.set(xlabel=None)
ax4.set(xlabel=None)

ax1.set_ylim(95,575)
ax2.set_ylim(2,5.25)
ax3.set_ylim(0.3,0.65)
ax4.set_ylim(20,140)

ax1.text(-0.3, 540, "A", fontdict={'fontsize':30})
ax2.text(-0.3, 5, "B", fontdict={'fontsize':30})
ax3.text(-0.3, 0.625, "C", fontdict={'fontsize':30})
ax4.text(-0.3, 130, "D", fontdict={'fontsize':30})


plt.tight_layout()
plt.savefig('../../figures/alpha_diversity.pdf')