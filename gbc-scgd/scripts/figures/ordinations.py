#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import colors
import matplotlib.font_manager as fm

#function to compute confidence ellipse
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', linewidth=1, edgecolor='none', alpha=1, **kwargs):

    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
        width=ell_radius_x * 2,
        height=ell_radius_y * 2,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        alpha=alpha,
        **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

#Define Tab10 color options
tab10_blue = tuple(list(sns.color_palette("tab10")[0]) + [1])
tab10_orange = tuple(list(sns.color_palette("tab10")[1]) + [1])
tab10_green = tuple(list(sns.color_palette("tab10")[2]) + [1])
tab10_red = tuple(list(sns.color_palette("tab10")[3]) + [1])
tab10_purple = tuple(list(sns.color_palette("tab10")[4]) + [1])
seaborn_gray = '#3d3d3d'

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

fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(15, 5))

#Unweighted UniFrac
#Load data
undata = pd.read_table('../../data/unweighted_unifrac_pca.tsv', delimiter='\t', header='infer')
wdata = pd.read_table('../../data/weighted_unifrac_pca.tsv', delimiter='\t', header='infer')

#extract individual species data
unDni_data = undata.loc[undata['species'] == 'D. nigrospiracula']
unDmo_data = undata.loc[undata['species'] == 'D. mojavensis']
unDmet_data = undata.loc[undata['species'] == 'D. mettleri']
unDaz_data = undata.loc[undata['species'] == 'D. arizonae']
unDmel_data = undata.loc[undata['species'] == 'D. melanogaster']
wDni_data = wdata.loc[wdata['species'] == 'D. nigrospiracula']
wDmo_data = wdata.loc[wdata['species'] == 'D. mojavensis']
wDmet_data = wdata.loc[wdata['species'] == 'D. mettleri']
wDaz_data = wdata.loc[wdata['species'] == 'D. arizonae']
wDmel_data = wdata.loc[wdata['species'] == 'D. melanogaster']

#make PCoA plot
#Get PC data
unx = undata['PC1']
uny = undata['PC2']
wx = undata['PC1']
wy = undata['PC2']

ax1.set_xlabel("PCo1: 18.83%", fontsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_ylabel("PCo2: 8.98%", fontsize=22)
ax1.tick_params(axis='y', labelsize=22)
ax2.set_xlabel("PCo1: 38.19%", fontsize=22)
ax2.tick_params(axis='x', labelsize=22)
ax2.set_ylabel("PCo2: 16.18%", fontsize=22)
ax2.tick_params(axis='y', labelsize=22)

font = fm.FontProperties(style='italic', size=22)

ax1.set_title('Unweighted UniFrac', fontdict={'fontsize': 22})
ax1.text(-1.1, 0.5, "A", fontdict={'fontsize':30})
ax1.set_xlim(-0.75, 0.6)
ax1.set_ylim(-0.5, 0.5)

ax2.set_title('Weighted UniFrac', fontdict={'fontsize': 22})
ax2.text(-1.65, 0.85, "B", fontdict={'fontsize':30})
ax2.set_xlim(-1, 1.5)
ax2.set_ylim(-0.9, 0.85)

#D. nigrospiraclula confidence ellipse
confidence_ellipse(x=unDni_data['PC1'], y=unDni_data['PC2'], edgecolor=colors[0], ax=ax1, n_std=2.0, linewidth=2)
confidence_ellipse(x=wDni_data['PC1'], y=wDni_data['PC2'], edgecolor=colors[0], ax=ax2, n_std=2.0, linewidth=2)

#D. mojavensis confidence ellipse
confidence_ellipse(x=unDmo_data['PC1'], y=unDmo_data['PC2'], edgecolor=colors[1], ax=ax1, n_std=2.0, linewidth=2)
confidence_ellipse(x=wDmo_data['PC1'], y=wDmo_data['PC2'], edgecolor=colors[1], ax=ax2, n_std=2.0, linewidth=2)

#D. mettleri confidence ellipse
confidence_ellipse(x=unDmet_data['PC1'], y=unDmet_data['PC2'], edgecolor=colors[2], ax=ax1, n_std=2.0, linewidth=2)
confidence_ellipse(x=wDmet_data['PC1'], y=wDmet_data['PC2'], edgecolor=colors[2], ax=ax2, n_std=2.0, linewidth=2)

#D. arizonae confidence ellipse
confidence_ellipse(x=unDaz_data['PC1'], y=unDaz_data['PC2'], edgecolor=colors[3], ax=ax1, n_std=2.0, linewidth=2)
confidence_ellipse(x=wDaz_data['PC1'], y=wDaz_data['PC2'], edgecolor=colors[3], ax=ax2, n_std=2.0, linewidth=2)

#D. melanogaster confidence ellipse
confidence_ellipse(x=unDmel_data['PC1'], y=unDmel_data['PC2'], edgecolor=colors[4], ax=ax1, n_std=2.0, linewidth=2)
confidence_ellipse(x=wDmel_data['PC1'], y=wDmel_data['PC2'], edgecolor=colors[4], ax=ax2, n_std=2.0, linewidth=2)

# scatter points on the main axes
sns.scatterplot(data=undata, x='PC1', y='PC2', hue='species', style='species', s=200, ax=ax1, edgecolor=seaborn_gray, legend=False, markers=['D', 's', 'h', 'p', 'o'])
sns.scatterplot(data=wdata, x='PC1', y='PC2', hue='species', style='species', s=200, ax=ax2, edgecolor=seaborn_gray, legend=True, markers=['D', 's', 'h', 'p', 'o'])

handles, previous_labels = ax2.get_legend_handles_labels()
font = fm.FontProperties(style='italic', size=22)
ax2.legend(prop=font, handles=handles, 
           labels=['D. nigrospiracula', 'D. mojavensis', 'D. mettleri', 'D. arizonae', 'D. melanogaster'],
          bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=22, 
           title_fontsize = 22, labelspacing = 0.1, markerscale=2)

           
plt.tight_layout()
plt.savefig("../../figures/ordinations.pdf")
