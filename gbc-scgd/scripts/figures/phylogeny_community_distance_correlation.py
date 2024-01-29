#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
import matplotlib.colors as mcolors

# load data
unweighted_unifrac_distance_matrix = pd.read_csv("../../data/unweighted_unifrac_distance_matrix.tsv", sep="\t", index_col=0)
weighted_unifrac_distance_matrix = pd.read_csv("../../data/weighted_unifrac_distance_matrix.tsv", sep="\t", index_col=0)
phylogenetic_distance_matrix = pd.read_csv("../../data/phylogenetic_distance_matrix.csv", index_col=0)
metadata = pd.read_csv("../../data/NCDMIC_metadata.tsv", sep="\t", index_col=0)

#unweighted
#initialize cache to store comparisons
comps_cache = []
#initialize dictionary to store comparisons
unweighted_unifrac_comparisons = {'sample1' : [],
                                 'sample2' : [],
                                 'unifrac_distance' : [],
                                 'phylogenetic_distance' : []}

#iterate through sample rows
for sample1 in list(unweighted_unifrac_distance_matrix.index):
    #get species
    species1 = f"D_{metadata.loc[sample1]['species'].split(' ')[1]}"
    #iterate through columns
    for sample2 in list(unweighted_unifrac_distance_matrix.index):
        #get species
        species2 = f"D_{metadata.loc[sample2]['species'].split(' ')[1]}"
        #don't collect info for same sample comparisons
        if sample1 != sample2:
            #get unifrac distance
            unifrac_distance = unweighted_unifrac_distance_matrix[sample1][sample2]
            #get phylogenetic distance
            phylogenetic_distance = phylogenetic_distance_matrix[species1][species2]
            #check if comparison has been made
            if [sample1, sample2] not in comps_cache and [sample2, sample1] not in comps_cache:
                #save
                unweighted_unifrac_comparisons['sample1'].append(sample1)
                unweighted_unifrac_comparisons['sample2'].append(sample2)
                unweighted_unifrac_comparisons['unifrac_distance'].append(unifrac_distance)
                unweighted_unifrac_comparisons['phylogenetic_distance'].append(phylogenetic_distance)
                #print(f"{sample1}\t{sample2}\t{unifrac_distance}\t{phylogenetic_distance}")
                #add to cache
                comps_cache.append([sample1, sample2])
                
unweighted_unifrac_comparisons_df = pd.DataFrame.from_dict(unweighted_unifrac_comparisons)

#weighted
#initialize cache to store comparisons
comps_cache = []
#initialize dictionary to store comparisons
weighted_unifrac_comparisons = {'sample1' : [],
                                 'sample2' : [],
                                 'unifrac_distance' : [],
                                 'phylogenetic_distance' : []}

#iterate through sample rows
for sample1 in list(weighted_unifrac_distance_matrix.index):
    #get species
    species1 = f"D_{metadata.loc[sample1]['species'].split(' ')[1]}"
    #iterate through columns
    for sample2 in list(weighted_unifrac_distance_matrix.index):
        #get species
        species2 = f"D_{metadata.loc[sample2]['species'].split(' ')[1]}"
        #don't collect info for same sample comparisons
        if sample1 != sample2:
            #get unifrac distance
            unifrac_distance = weighted_unifrac_distance_matrix[sample1][sample2]
            #get phylogenetic distance
            phylogenetic_distance = phylogenetic_distance_matrix[species1][species2]
            #check if comparison has been made
            if [sample1, sample2] not in comps_cache and [sample2, sample1] not in comps_cache:
                #save
                weighted_unifrac_comparisons['sample1'].append(sample1)
                weighted_unifrac_comparisons['sample2'].append(sample2)
                weighted_unifrac_comparisons['unifrac_distance'].append(unifrac_distance)
                weighted_unifrac_comparisons['phylogenetic_distance'].append(phylogenetic_distance)
                #print(f"{sample1}\t{sample2}\t{unifrac_distance}\t{phylogenetic_distance}")
                #add to cache
                comps_cache.append([sample1, sample2])
                
weighted_unifrac_comparisons_df = pd.DataFrame.from_dict(weighted_unifrac_comparisons)

#make plot
sns.set_style('whitegrid')
fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(5, 8))

#unweighted unifrac
sns.regplot(unweighted_unifrac_comparisons_df, x='phylogenetic_distance', y='unifrac_distance', ax=ax1, color='black')
sns.regplot(weighted_unifrac_comparisons_df, x='phylogenetic_distance', y='unifrac_distance', ax=ax2, color='black')

#clean up plot
ax1.set_ylabel('Unweighted\nUniFrac Distance', fontsize=20)
ax2.set_ylabel('Weighted\nUniFrac Distance',fontsize=20)
ax1.set_xlabel('Phylogenetic Distance',fontsize=20)
ax2.set_xlabel('Phylogenetic Distance',fontsize=20)
ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

plt.tight_layout()
plt.savefig("../../figures/phylogeny_community_correlations.pdf")