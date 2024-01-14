#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import dokdo

#assign colors
tab10_blue = tuple(list(sns.color_palette("tab10")[0]))
tab10_orange = tuple(list(sns.color_palette("tab10")[1]))
tab10_green = tuple(list(sns.color_palette("tab10")[2]))
tab10_red = tuple(list(sns.color_palette("tab10")[3]))
tab10_purple = tuple(list(sns.color_palette("tab10")[4]))
seaborn_gray = '#3d3d3d'

#load taxabarplot qzv
taxabarplot_file = '../../data/NCDMIC_taxa_barplot.qzv'

sns.set_style("whitegrid")
fig, [ax1, ax2, ax3, ax4, ax5, ax6] = plt.subplots(1, 6, figsize=(25, 10), gridspec_kw={'width_ratios': [7,5,6,10,5,10]})

#nigrospiracula
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    by=['species'],
    label_columns=['species'],
    include_samples={'species': ['nigrospiracula']},
    ax=ax1,
    level=7,
    count=8,
    cmap_name='tab10',
    sort_by_mean2=False,
    sort_by_mean3=False,
    legend=False
)

ax1.set_xticklabels('')
ax1.set_ylabel('Relative Abundance (%)', fontsize=22)
ax1.tick_params(axis='y', labelsize=22)
ax1.set_title("D. nigrospiracula", fontsize=22, style = "italic")


#mojavensis
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    by=['species'],
    label_columns=['species'],
    include_samples={'species': ['mojavensis']},
    ax=ax2,
    level=7,
    count=8,
    cmap_name='tab10',
    sort_by_mean2=False,
    sort_by_mean3=False,
    legend=False
)

ax2.set_xticklabels('')
ax2.set_yticklabels('')
ax2.set_ylabel('')
ax2.set_title("D. mojavensis", fontsize=22, style = "italic")

#mettleri
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    by=['species'],
    label_columns=['species'],
    include_samples={'species': ['mettleri']},
    ax=ax3,
    level=7,
    count=8,
    cmap_name='tab10',
    sort_by_mean2=False,
    sort_by_mean3=False,
    legend=False
)

ax3.set_xticklabels('')
ax3.set_yticklabels('')
ax3.set_ylabel('')
ax3.set_title("D. mettleri", fontsize=22, style = "italic")

#arizonae
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    by=['species'],
    label_columns=['species'],
    include_samples={'species': ['arizonae']},
    ax=ax4,
    level=7,
    count=8,
    cmap_name='tab10',
    sort_by_mean2=False,
    sort_by_mean3=False,
    legend=False
)

ax4.set_xticklabels('')
ax4.set_yticklabels('')
ax4.set_ylabel('')
ax4.set_title("D. arizonae", fontsize=22, style = "italic")

#melanogaster
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    by=['species'],
    label_columns=['species'],
    include_samples={'species': ['melanogaster']},
    figsize=(10, 7),
    ax=ax5,
    level=7,
    count=8,
    cmap_name='tab10',
    sort_by_mean2=False,
    sort_by_mean3=False,
    legend=False
)

ax5.set_xticklabels('')
ax5.set_yticklabels('')
ax5.set_ylabel('')
ax5.set_title("D. melanogaster", fontsize=22, style = "italic")

#plot legend
dokdo.taxa_abundance_bar_plot(
    taxabarplot_file,
    ax=ax6,
    level=7,
    count=8,
    cmap_name='tab10',
    legend_short=True
)

handles, labels = ax6.get_legend_handles_labels()

ax6.clear()
ax6.legend(handles, labels, fontsize=22)
ax6.axis('off')

plt.subplots_adjust(left=0.05,
                    bottom=0.05,
                    right=0.95,
                    top=0.95,
                    wspace=0.1,
                    hspace=0.1)

plt.savefig("../../figures/taxabarplot.pdf")
