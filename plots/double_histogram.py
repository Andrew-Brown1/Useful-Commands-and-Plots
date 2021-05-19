import os
import matplotlib.pyplot as plt, numpy as np

FONTSIZE = 10
negatives = np.random.normal(0, 0.5, 1000)
positives = np.random.normal(1, 0.5, 1000)


n, bins, patches = plt.hist(x=negatives, bins=30, color='#0504aa',
                                alpha=0.7, rwidth=0.85, label='Negatives')
n, bins, patches = plt.hist(x=positives, bins=30,
                            alpha=0.7, rwidth=0.85, label='Positives')

plt.xticks(fontsize=FONTSIZE-3)
plt.yticks(fontsize=FONTSIZE-3)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('similarity score',  fontsize=FONTSIZE)
plt.ylabel('Frequency',  fontsize=FONTSIZE)
plt.title('two histograms',  fontsize=FONTSIZE)
plt.legend(loc='upper left',  fontsize=FONTSIZE)
plt.show()
