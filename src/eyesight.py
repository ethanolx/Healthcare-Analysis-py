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
file_name = 'data/defective-vision-rates.csv'
bad_eyesight_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('gender', 'U10'), ('per_10000_examined', int)])

# Instantiate Figure and Axes
fig = plt.figure(figsize=(10, 7))
ax1 = plt.subplot2grid((1, 5), (0, 0), colspan=3)
ax2 = plt.subplot2grid((1, 5), (0, 3), colspan=2)
plt.subplots_adjust(wspace=1)

# Summarise Data
[*all_stats] = Statistic
desc(bad_eyesight_rates, file_name, all_stats)

# Process Data
male_data: np.ndarray = bad_eyesight_rates[bad_eyesight_rates['gender']
                               == 'Male']['per_10000_examined'] / 100
female_data: np.ndarray = bad_eyesight_rates[bad_eyesight_rates['gender']
                                 == 'Female']['per_10000_examined'] / 100

# Grouped Bar Chart
years: np.ndarray = np.unique(bad_eyesight_rates['year'])

w = 0.4
ax1.bar(years - w / 2, male_data, width=w, label='Male')
ax1.bar(years + w / 2, female_data, width=w, label='Female')
ax1.set_ylim(40, 60)
ax1.set_yticks([i for i in range(40, 61, 5)])
ax1.set_xticks(years)
ax1.set_xticklabels(map(lambda y: f'{y - 2000:0>2}', years.tolist()))
ax1.set_yticklabels([str(i) for i in range(40, 61, 5)])
ax1.set_title('Trend of Defective Vision (compare gender)')
ax1.set_xlabel('Year (21st Century)')
ax1.set_ylabel('Percentage of Students with Visual Acuity / %')
ax1.legend(loc='upper right')

# Boxplot
ax2.boxplot([male_data, female_data], labels=['Male', 'Female'], patch_artist=True, boxprops={'facecolor': 'dodgerblue', 'color': 'navy'}, medianprops={
            'color': 'navy'}, whiskerprops={'linestyle': ':'}, capprops={'color': 'navy', 'linewidth': 2})
ax2.set_title('Distribution of Defective Vision (by gender)')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Percentage of Students with Visual Acuity')
ax2.text(1.1, np.median(male_data) + 0.1, f'Median (M): {np.median(male_data)}%', font={'size': 7})
ax2.text(1.15, np.median(female_data) + 0.1, f'Median (F): {np.median(female_data)}%', font={'size': 7})

# Display Chart
plt.savefig('./assets/eyesight.png')
plt.show()
