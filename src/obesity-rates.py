# type: ignore
# > Import Type Checking Modules
from typing import List, Tuple, cast
from matplotlib.axes import SubplotBase
from matplotlib.figure import Figure

# >Import 3rd-Party Libraries
import numpy as np
import matplotlib.pyplot as plt

# > Import Custom Modules
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# > Choose Chart Style
plt.style.use('seaborn')

# > Import Data
file_name: str = 'data/obesity-rates.csv'
obesity_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('age_group', 'U35'), ('gender', 'U10'), ('per_10000_examined', int)])

# > Process Data

# for pie charts
male: np.ndarray = obesity_rates['gender'] == 'Male'
female: np.ndarray = obesity_rates['gender'] == 'Female'


# for line chart
years: np.ndarray = cast(np.ndarray, np.unique(obesity_rates['year']))
p1: np.ndarray = obesity_rates[obesity_rates['age_group']
                               == 'Primary 1 and equivalent age groups']
p5: np.ndarray = obesity_rates[obesity_rates['age_group']
                               == 'Primary 5 and equivalent age groups']

# for histogram and normal curve
obese_percent: np.ndarray = obesity_rates['per_10000_examined'] / 100

# > Summarise Data
all_stats: List[Statistic] = list(Statistic)
desc(obesity_rates, file_name, all_stats)

# > Instantiate Figure and Axes
grid_dimensions: Tuple[int, int] = (2, 2)
fig: Figure = plt.figure(figsize=(10, 7))
ax1: SubplotBase = cast(SubplotBase, plt.subplot2grid(grid_dimensions, (0, 0)))
ax2: SubplotBase = cast(SubplotBase, plt.subplot2grid(grid_dimensions, (1, 0)))
ax3: SubplotBase = cast(SubplotBase, plt.subplot2grid(grid_dimensions, (0, 1)))
ax4: SubplotBase = cast(SubplotBase, plt.subplot2grid(grid_dimensions, (1, 1)))
plt.subplots_adjust(hspace=0.5, right=0.9, left=0.05, wspace=0.3)

# > Pie Charts

# Additional Data Preparation
male_obese: int = np.sum(obesity_rates[male]['per_10000_examined'])
male_not_obese: int = np.sum(10000 - obesity_rates[male]['per_10000_examined'])

female_obese: int = np.sum(obesity_rates[female]['per_10000_examined'])
female_not_obese: int = np.sum(
    10000 - obesity_rates[female]['per_10000_examined'])

# Construct Pie Charts
ax1.pie((male_not_obese, male_obese), labels=[
        'Not Obese', 'Obese'], startangle=90, autopct=lambda p: f'{p:.2f}%')
ax2.pie((female_not_obese, female_obese), labels=[
        'Not Obese', 'Obese'], startangle=90, autopct=lambda p: f'{p:.2f}%')

# Set titles
ax1.set_title('Proportion of Students With Obesity (Male)')
ax2.set_title('Proportion of Students With Obesity (Female)')

# > Line Chart

# Additional Data Preparation
y1: List[float] = []
y2: List[float] = []

for y in years:
    y1.append(np.mean(p1[p1['year'] == y]['per_10000_examined']) / 100)
    y2.append(np.mean(p5[p5['year'] == y]['per_10000_examined']) / 100)

# Construct Line Chart
ax3.plot(years, np.array(y1), label='P1')
ax3.plot(years, np.array(y2), label='P5')

# Set chart boundaries
ax3.set_ylim((5, 20))

# Set axis ticks
ax3.set_xticks(years)
ax3.set_xticklabels(map(lambda y: f'{y - 2000:0>2}', years))

# Set axis labels
ax3.set_xlabel('Year (21st Century)')
ax3.set_ylabel('Percentage of obese students / %')

# Set title
ax3.set_title('Annual Obesity Trend')

# Set legend
ax3.legend(loc='upper left')


# > Histogram and Normal Dist Curve

# Construct Histogram
_, bins, _ = ax4.hist(obese_percent, bins=10, density=True, edgecolor='k')

# Construct Normal Distribution Curve
mu, sigma = np.mean(obese_percent), np.std(obese_percent)
ax4.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2)

# Set chart boundaries
ax4.set_ylim(0, 0.3)

# Set axis ticks
ax4.set_xticks([i for i in range(9, 19)])
ax4.set_yticks([i * 0.1 for i in range(4)])

# Set axis labels
ax4.set_xlabel('Percentage of obese students / %')
ax4.set_ylabel('Probability')

# Set title
ax4.set_title('Distribution of Obesity in SG')

# Add annotations
ax4.annotate('13% of all students are obese on average', xy=(12.9, 0.152), xytext=(14, 0.25), arrowprops={
             'facecolor': 'tab:orange', 'arrowstyle': 'fancy'}, font={'size': 9, 'family': 'Ubuntu Mono', 'weight': 'bold'}, color='tab:orange', ha='left')

# > Display and Save Charts
plt.savefig('./assets/obesity-rates.png')
plt.show()
