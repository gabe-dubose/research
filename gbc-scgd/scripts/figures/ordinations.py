#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import colors
import matplotlib.font_manager as fm
import dokdo

#function to compute confidence ellipse
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):

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

sns.set_style('darkgrid')
sns.set_palette("tab10")
fig, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(30, 8))

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

# scatter points on the main axes
sns.scatterplot(data=undata, x='PC1', y='PC2', hue='species', s=250, ax=ax1, edgecolor=seaborn_gray, legend=False)
sns.scatterplot(data=wdata, x='PC1', y='PC2', hue='species', s=250, ax=ax2, edgecolor=seaborn_gray, legend=False)

ax1.set_xlabel("PC1: 18.83%", fontsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_ylabel("PC2: 8.98%", fontsize=22)
ax1.tick_params(axis='y', labelsize=22)
ax2.set_xlabel("PC1: 38.19%", fontsize=22)
ax2.tick_params(axis='x', labelsize=22)
ax2.set_ylabel("PC2: 16.18%", fontsize=22)
ax2.tick_params(axis='y', labelsize=22)

font = fm.FontProperties(style='italic', size=22)

ax1.set_title('Unweighted UniFrac', fontdict={'fontsize': 22})
ax1.text(-0.99, 0.425, "A", fontdict={'fontsize':30})
ax1.set_xlim(-0.75, 0.6)
ax1.set_ylim(-0.5, 0.5)

ax2.set_title('Weighted UniFrac', fontdict={'fontsize': 22})
ax2.text(-1.45, 0.74, "B", fontdict={'fontsize':30})
ax2.set_xlim(-1, 1.5)
ax2.set_ylim(-0.9, 0.85)

#D. nigrospiraclula confidence ellipse
confidence_ellipse(x=unDni_data['PC1'], y=unDni_data['PC2'], edgecolor=tab10_blue, ax=ax1, n_std=2.0)
confidence_ellipse(x=wDni_data['PC1'], y=wDni_data['PC2'], edgecolor=tab10_blue, ax=ax2, n_std=2.0)

#D. mojavensis confidence ellipse
confidence_ellipse(x=unDmo_data['PC1'], y=unDmo_data['PC2'], edgecolor=tab10_orange, ax=ax1, n_std=2.0)
confidence_ellipse(x=wDmo_data['PC1'], y=wDmo_data['PC2'], edgecolor=tab10_orange, ax=ax2, n_std=2.0)

#D. mettleri confidence ellipse
confidence_ellipse(x=unDmet_data['PC1'], y=unDmet_data['PC2'], edgecolor=tab10_green, ax=ax1, n_std=2.0)
confidence_ellipse(x=wDmet_data['PC1'], y=wDmet_data['PC2'], edgecolor=tab10_green, ax=ax2, n_std=2.0)

#D. arizonae confidence ellipse
confidence_ellipse(x=unDaz_data['PC1'], y=unDaz_data['PC2'], edgecolor=tab10_red, ax=ax1, n_std=2.0)
confidence_ellipse(x=wDaz_data['PC1'], y=wDaz_data['PC2'], edgecolor=tab10_red, ax=ax2, n_std=2.0)

#D. melanogaster confidence ellipse
confidence_ellipse(x=unDmel_data['PC1'], y=unDmel_data['PC2'], edgecolor=tab10_purple, ax=ax1, n_std=2.0)
confidence_ellipse(x=wDmel_data['PC1'], y=wDmel_data['PC2'], edgecolor=tab10_purple, ax=ax2, n_std=2.0)

#add aitchison
taxonomy_file = '../../data/NCDMIC_taxonomy.qza'
pcoa_results = '../../data/aithcison_ordination_results.qza'
metadata_file = '../../data/NCDMIC_metadata.tsv'

ax = dokdo.beta_2d_plot(pcoa_results,
                        hue='species',
                        metadata=metadata_file,
                        edgecolor=seaborn_gray,
                        s = 250,
                        figsize=(12, 8),
                        ax=ax3)

dokdo.addbiplot(pcoa_results,
                ax=ax3,
                count=5,
                dim=2,
                taxonomy=taxonomy_file,
                name_type='taxon',
                fontsize=22,
                level=6)

ax3.set_xlabel("PC1: 50.61%", fontsize=22)
ax3.tick_params(axis='x', labelsize=22)
ax3.set_ylabel("PC2: 39.25%", fontsize=22)
ax3.tick_params(axis='y', labelsize=22)

font = fm.FontProperties(style='italic', size=22)
ax3.legend(prop=font, markerscale=2, ncol=1, loc='lower left', bbox_to_anchor=(1, -0.025))

font = fm.FontProperties(size=22)
ax3.set_title('Aitchison Distances', fontdict={'fontsize': 22})
ax3.text(-0.53, 0.275, "C", fontdict={'fontsize':30})

plt.tight_layout()
plt.savefig("../../figures/ordinations.pdf")

