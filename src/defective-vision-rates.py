# type: ignore
# > Import Type Checking Modules
from typing import List, cast
from matplotlib.axes import SubplotBase

# > Import 3rd-Party Libraries
import numpy as np
import matplotlib.pyplot as plt

# > Import Custom Modules
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# > Choose Chart Style
plt.style.use('seaborn-colorblind')  # type: ignore

# > Import Data
file_name: str = 'data/defective-vision-rates.csv'
defective_vision_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('gender', 'U10'), ('per_10000_examined', int)])

# > Process Data
male_data: np.ndarray = defective_vision_rates[defective_vision_rates['gender']
                                               == 'Male']['per_10000_examined'] / 100
female_data: np.ndarray = defective_vision_rates[defective_vision_rates['gender']
                                                 == 'Female']['per_10000_examined'] / 100
years: np.ndarray = cast(np.ndarray, np.unique(defective_vision_rates['year']))

# > Summarise Data
all_stats: List[Statistic] = list(Statistic)
desc(defective_vision_rates, file_name, all_stats)

# > Instantiate Figure and Axes
fig = plt.figure(figsize=(10, 7))
ax1: SubplotBase = cast(
    SubplotBase, plt.subplot2grid((1, 5), (0, 0), colspan=3))
ax2: SubplotBase = cast(
    SubplotBase, plt.subplot2grid((1, 5), (0, 3), colspan=2))
plt.subplots_adjust(wspace=1)

# > Grouped Bar Chart

# Additional Preparation
w = 0.4     # Used to offset the bars to produce grouped bar chart

# Construct Bars
ax1.bar(years - w / 2, male_data, width=w, label='Male')
ax1.bar(years + w / 2, female_data, width=w, label='Female')

# Set limits
ax1.set_ylim(40, 60)

# Set axis ticks
ax1.set_xticks(years)
ax1.set_xticklabels(map(lambda y: f'{y - 2000:0>2}', years.tolist()))

ax1.set_yticks([i for i in range(40, 61, 5)])
ax1.set_yticklabels([str(i) for i in range(40, 61, 5)])

# Set title
ax1.set_title('Trend of Defective Vision (compare gender)')

# Set axis labels
ax1.set_xlabel('Year (21st Century)')
ax1.set_ylabel('Percentage of students with visual acuity / %')
ax1.legend(loc='upper right')

# > Boxplot

# Construct Boxplot
ax2.boxplot([male_data, female_data], labels=['Male', 'Female'], patch_artist=True, boxprops={'facecolor': 'dodgerblue', 'color': 'navy'}, medianprops={
            'color': 'navy'}, whiskerprops={'linestyle': ':'}, capprops={'color': 'navy', 'linewidth': 2})

# Set title
ax2.set_title('Distribution of Defective Vision (by gender)')

# Set axis labels
ax2.set_xlabel('Gender')
ax2.set_ylabel('Percentage of students with visual acuity')

# Add annotations
ax2.text(1.12, np.median(male_data) + 0.1,
         f'Median (M): {np.median(male_data)}%', font={'size': 7})
ax2.text(1.15, np.median(female_data) + 0.1,
         f'Median (F): {np.median(female_data)}%', font={'size': 7})

# > Display and Save Charts
plt.savefig('./assets/defective-vision-rates.png')
plt.show()
