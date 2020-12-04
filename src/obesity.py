# Import Type Checking Modules
from typing import List

# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('seaborn')  # type: ignore

# Import Data
file_name = 'data/common-health-problems-of-students-examined-overweight-annual.csv'
obesity_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('age_group', 'U35'), ('gender', 'U10'), ('per_10000_examined', int)])

# Instantiate Figure and Axes
grid_dimensions = (2, 2)
fig = plt.figure(figsize=(10, 7))
ax1 = plt.subplot2grid(grid_dimensions, (0, 0), rowspan=2)
ax2 = plt.subplot2grid(grid_dimensions, (0, 1))
ax3 = plt.subplot2grid(grid_dimensions, (1, 1))

# Summarise Data
[*all_stats] = Statistic
desc(obesity_rates, file_name, all_stats)  # type: ignore

# Pie Chart
male = obesity_rates['gender'] == 'Male'
female = obesity_rates['gender'] == 'Female'

male_sum = np.sum(obesity_rates[male]['per_10000_examined'])
female_sum = np.sum(obesity_rates[female]['per_10000_examined'])

ax1.pie((female_sum, male_sum), labels=['male', 'female'], startangle=90, autopct=lambda p: f'{p:.2f}%')  # type: ignore

ax1.set_title('Proportion of Students With Obesity (by gender)') # type: ignore

# Line Chart
years = np.unique(obesity_rates['year'])
p1 = obesity_rates[obesity_rates['age_group']
                   == 'Primary 1 and equivalent age groups']
p5 = obesity_rates[obesity_rates['age_group']
                   == 'Primary 5 and equivalent age groups']

y1 = []
y2 = []

for y in years:
    y1.append(np.sum(p1[p1['year'] == y]['per_10000_examined']) / 100)
    y2.append(np.sum(p5[p5['year'] == y]['per_10000_examined']) / 100)

ax2.plot(years, np.array(y1), label='P1')  # type: ignore
ax2.plot(years, np.array(y2), label='P5')  # type: ignore
ax2.set_title('Number of Students With Obesity Annually')  # type: ignore
ax2.set_xlabel('Year')  # type: ignore
ax2.set_ylabel('Percentage of Students Obese / %')  # type: ignore
ax2.legend(loc='upper left')  # type: ignore
ax2.set_xticks(years)  # type: ignore

ax2.set_ylim((15, 40))  # type: ignore
ax2.text(2010, 2500, 'hello')  # type: ignore

# Histogram and Normal Dist Curve
obese_percent: np.ndarray = obesity_rates['per_10000_examined'] / 100

_, bins, _ = ax3.hist(obese_percent, bins=10, density=True, color='maroon', edgecolor='k')  # type: ignore
ax3.set_ylim(0, 0.3)  # type: ignore
ax3.set_xticks([i for i in range(9, 19)]) #type: ignore
ax3.set_yticks([i * 0.1 for i in range(4)])  # type: ignore
ax3.annotate('12% of all students are obese on average', xy=(12.78, 0.15), xytext=(14, 0.25), arrowprops={'facecolor': 'tab:orange', 'arrowstyle': 'fancy'}, font={'size': 9, 'family': 'Ubuntu Mono', 'weight': 'bold'}, color='tab:blue', ha='left')  # type: ignore

mu, sigma = np.mean(obese_percent), np.std(obese_percent)
ax3.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma**2)), linewidth=2, color='mediumseagreen')  # type: ignore
ax3.set_facecolor('dimgrey') #type: ignore

# Display Charts
plt.tight_layout()
plt.show()
