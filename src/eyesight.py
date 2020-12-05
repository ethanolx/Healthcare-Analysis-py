# Import Type Checking Modules
from typing import List

# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('seaborn-colorblind')  # type: ignore

# Import Data
file_name = 'data/common-health-problems-of-students-examined-defective-vision-annual.csv'
bad_eyesight_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('gender', 'U10'), ('per_10000_examined', int)])

# Instantiate Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2)  # type: ignore

# Summarise Data
[*all_stats] = Statistic
desc(bad_eyesight_rates, file_name, all_stats)  # type: ignore

# Grouped Bar Chart
years: np.ndarray = np.unique(bad_eyesight_rates['year'])  # type: ignore
male_data = bad_eyesight_rates[bad_eyesight_rates['gender']
                               == 'Male']['per_10000_examined']
female_data = bad_eyesight_rates[bad_eyesight_rates['gender']
                                 == 'Female']['per_10000_examined']

w = 0.4
ax1.bar(years - w / 2, male_data, width=w)  # type: ignore
ax1.bar(years + w / 2, female_data, width=w)  # type: ignore
ax1.set_ylim(4000, 6000)
ax1.set_yticks([i for i in range(4000, 6100, 500)])
ax1.set_xticks(years)
ax1.set_xticklabels(map(lambda y: f'{y - 2000:0>2}', years.tolist()))
ax1.set_yticklabels([str(i / 1000) + 'k' for i in range(4000, 6100, 500)])
ax1.set_title('Number of Students with Visual Acuity')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Students with Visual Acuity')

# Boxplot
ax2.boxplot([male_data, female_data], labels=['M', 'F'], patch_artist=True, boxprops={'facecolor': 'dodgerblue', 'color': 'navy'}, medianprops={
            'color': 'navy'}, whiskerprops={'linestyle': ':'}, capprops={'color': 'navy', 'linewidth': 2})
ax2.set_title('Distribution of Students with Visual Acuity')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Number of Students with Visual Acuity')

# Display Chart
plt.tight_layout()
plt.show()
