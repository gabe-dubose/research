#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

#load data
alpha_data = pd.read_table('../../data/alpha_diversity.tsv', delimiter='\t', header='infer')

#make plot
sns.set_style('darkgrid')
sns.set_palette("tab10")

fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4, figsize=(18, 8))
sns.boxplot(data=alpha_data, x='species', y='observed_features', ax=ax1)
sns.boxplot(data=alpha_data, x='species', y='shannon_entropy', ax=ax2)
sns.boxplot(data=alpha_data, x='species', y='pielou_evenness', ax=ax3)
sns.boxplot(data=alpha_data, x='species', y='faith_pd', ax=ax4)

labels = ['D. nigrospiracula', 'D. mojavensis', 'D. mettleri', 'D. arizonae', 'D. melanogaster']
ax1.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax2.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax3.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')
ax4.set_xticklabels(labels, fontsize=22, style = "italic", rotation=30, rotation_mode='anchor', ha='right')

ax1.set_ylabel("Observed Features", fontsize=22)
ax1.tick_params(axis='y', labelsize=22)

ax2.set_ylabel("Shannon Entropy", fontsize=22)
ax2.tick_params(axis='y', labelsize=22)

ax3.set_ylabel("Pielou's Evenness", fontsize=22)
ax3.tick_params(axis='y', labelsize=22)

ax4.set_ylabel("Faith's Phylogenetic Diversity", fontsize=22)
ax4.tick_params(axis='y', labelsize=22)

ax1.set(xlabel=None)
ax2.set(xlabel=None)
ax3.set(xlabel=None)
ax4.set(xlabel=None)

ax1.text(-3, 775, "A", fontdict={'fontsize':30})
ax2.text(-2.2, 6, "B", fontdict={'fontsize':30})
ax3.text(-2.85, 0.7, "C", fontdict={'fontsize':30})
ax4.text(-3, 205, "D", fontdict={'fontsize':30})


plt.tight_layout()
plt.savefig('../../figures/alpha_diversity.pdf')