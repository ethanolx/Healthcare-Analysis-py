# Import Type Checking Modules
from typing import List

# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('seaborn')

# Import Data
file_name = 'data/obesity-rates.csv'
obesity_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[(
    'year', int), ('age_group', 'U35'), ('gender', 'U10'), ('per_10000_examined', int)])

# Instantiate Figure and Axes
grid_dimensions = (2, 2)
fig = plt.figure(figsize=(10, 7))
ax1 = plt.subplot2grid(grid_dimensions, (0, 0))
ax2 = plt.subplot2grid(grid_dimensions, (1, 0))
ax3 = plt.subplot2grid(grid_dimensions, (0, 1))
ax4 = plt.subplot2grid(grid_dimensions, (1, 1))
plt.subplots_adjust(hspace=0.5, right=0.9, left=0.05, wspace=0.4)

# Summarise Data
[*all_stats] = Statistic
desc(obesity_rates, file_name, all_stats)

# Pie Charts
male = obesity_rates['gender'] == 'Male'
female = obesity_rates['gender'] == 'Female'

male_obese = np.sum(obesity_rates[male]['per_10000_examined'])
male_not_obese = np.sum(10000 - obesity_rates[male]['per_10000_examined'])

female_obese = np.sum(obesity_rates[female]['per_10000_examined'])
female_not_obese = np.sum(10000 - obesity_rates[female]['per_10000_examined'])

ax1.pie((male_not_obese, male_obese), labels=[
        'Not Obese', 'Obese'], startangle=90, autopct=lambda p: f'{p:.2f}%')
ax2.pie((female_not_obese, female_obese), labels=[
        'Not Obese', 'Obese'], startangle=90, autopct=lambda p: f'{p:.2f}%')

ax1.set_title('Proportion of Students With Obesity (Male)')
ax2.set_title('Proportion of Students With Obesity (Female)')

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

ax3.plot(years, np.array(y1), label='P1')
ax3.plot(years, np.array(y2), label='P5')
ax3.set_title('Number of Students With Obesity Annually')
ax3.set_xlabel('Year (21st Century)')
ax3.set_ylabel('Percentage of Students Obese / %')
ax3.legend(loc='upper left')
ax3.set_xticks(years)
ax3.set_xticklabels(map(lambda y: f'{y - 2000:0>2}', years))

ax3.set_ylim((15, 40))

# Histogram and Normal Dist Curve
obese_percent: np.ndarray = obesity_rates['per_10000_examined'] / 100

_, bins, _ = ax4.hist(obese_percent, bins=10, density=True, edgecolor='k')
ax4.set_ylim(0, 0.3)
ax4.set_xticks([i for i in range(9, 19)])
ax4.set_yticks([i * 0.1 for i in range(4)])
ax4.annotate('13% of all students are obese on average', xy=(12.9, 0.152), xytext=(14, 0.25), arrowprops={
             'facecolor': 'tab:orange', 'arrowstyle': 'fancy'}, font={'size': 9, 'family': 'Ubuntu Mono', 'weight': 'bold'}, color='tab:orange', ha='left')

mu, sigma = np.mean(obese_percent), np.std(obese_percent)
ax4.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2)
ax4.set_xlabel('Percentage of Students Screened Who are Obese / %')
ax4.set_ylabel('Probability')
ax4.set_title('Distribution of Obesity Rates in SG')

# Display Charts
plt.savefig('./assets/obesity.png')
plt.show()
