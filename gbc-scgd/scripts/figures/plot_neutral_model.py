#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#load data
total_neutral_model_predictions = pd.read_csv("../../data/total_neutral_predictions.csv")
total_neutral_model_predictions['p_log'] = np.log10(total_neutral_model_predictions['p'])

generalist_neutral_model_predictions = pd.read_csv("../../data/generalist_neutral_predictions.csv")
generalist_neutral_model_predictions['p_log'] = np.log10(generalist_neutral_model_predictions['p'])

specialist_neutral_model_predictions = pd.read_csv("../../data/specialist_neutral_predictions.csv")
specialist_neutral_model_predictions['p_log'] = np.log10(specialist_neutral_model_predictions['p'])

#make figure
sns.set_style('whitegrid')
fig, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(21, 7))
colors = ["tab:gray", "tab:orange", "tab:blue"]
sns.set_palette(sns.color_palette(colors))
seaborn_gray = '#3d3d3d'

sns.scatterplot(data=total_neutral_model_predictions, x="p_log", y="freq", ax=ax1, color='black', linewidth=0, alpha=0.5)
sns.lineplot(data=total_neutral_model_predictions, x="p_log", y="pred.lwr", ax=ax1, color='black', alpha=1, linewidth=1)
sns.lineplot(data=total_neutral_model_predictions, x="p_log", y="freq.pred", ax=ax1, color='black', linewidth=3)
sns.lineplot(data=total_neutral_model_predictions, x="p_log", y="pred.upr", ax=ax1, color='black', alpha=1, linewidth=1)
ax1.fill_between(x=total_neutral_model_predictions["p_log"], y1=total_neutral_model_predictions["pred.lwr"], y2=total_neutral_model_predictions["pred.upr"], color='tab:gray', alpha=.2)
ax1.set_ylabel("Frequency", fontsize=22)
ax1.set_xlabel("$log_{10}$(Mean Relative Abundance)", fontsize=22)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_title("Total", fontsize=22)
ax1.text(-5.95, 0.7, "$R^{2}$=0.4946", fontdict={'fontsize':22})
ax1.text(-6.85, 1.075, "A", fontdict={'fontsize':30})

sns.scatterplot(data=generalist_neutral_model_predictions, x="p_log", y="freq", ax=ax2, color='black', linewidth=0, alpha=0.5)
sns.lineplot(data=generalist_neutral_model_predictions, x="p_log", y="pred.lwr", ax=ax2, color='black', alpha=1, linewidth=1)
sns.lineplot(data=generalist_neutral_model_predictions, x="p_log", y="freq.pred", ax=ax2, color='black', linewidth=3)
sns.lineplot(data=generalist_neutral_model_predictions, x="p_log", y="pred.upr", ax=ax2, color='black', alpha=1, linewidth=1)
ax2.fill_between(x=generalist_neutral_model_predictions["p_log"], y1=generalist_neutral_model_predictions["pred.lwr"], y2=generalist_neutral_model_predictions["pred.upr"], color='tab:gray', alpha=.2)
ax2.set_ylabel("", fontsize=0)
ax2.set_xlabel("$log_{10}$(Mean Relative Abundance)", fontsize=22)
ax2.tick_params(axis='y', labelsize=0)
ax2.tick_params(axis='x', labelsize=22)
ax2.set_title("Generalists", fontsize=22)
ax2.text(-5.6, 0.7, "$R^{2}$=0.523", fontdict={'fontsize':22})
ax2.text(-5.75, 1.075, "B", fontdict={'fontsize':30})

sns.scatterplot(data=specialist_neutral_model_predictions, x="p_log", y="freq", ax=ax3, color='black', linewidth=0, alpha=0.5)
sns.lineplot(data=specialist_neutral_model_predictions, x="p_log", y="pred.lwr", ax=ax3, color='black', alpha=1, linewidth=1)
sns.lineplot(data=specialist_neutral_model_predictions, x="p_log", y="freq.pred", ax=ax3, color='black', linewidth=3)
sns.lineplot(data=specialist_neutral_model_predictions, x="p_log", y="pred.upr", ax=ax3, color='black', alpha=1, linewidth=1)
ax3.fill_between(x=specialist_neutral_model_predictions["p_log"], y1=specialist_neutral_model_predictions["pred.lwr"], y2=specialist_neutral_model_predictions["pred.upr"], color='tab:gray', alpha=.2)
ax3.set_ylabel("", fontsize=0)
ax3.set_xlabel("$log_{10}$(Mean Relative Abundance)", fontsize=22)
ax3.tick_params(axis='y', labelsize=0)
ax3.tick_params(axis='x', labelsize=22)
ax3.set_title("Specialists", fontsize=22)
ax3.text(-5.65, 0.7, "$R^{2}$=0.2481", fontdict={'fontsize':22})
ax3.text(-5.85, 1.075, "C", fontdict={'fontsize':30})

plt.subplots_adjust(left=0.05,
                    bottom=0.05,
                    right=0.95,
                    top=0.95,
                    wspace=0.1,
                    hspace=0.1)

plt.tight_layout()
plt.savefig("../../figures/neutral_models.pdf")