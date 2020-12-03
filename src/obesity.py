# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('seaborn') #type: ignore

# Import Data
file_name = 'data/common-health-problems-of-students-examined-overweight-annual.csv'
obesity_rates: np.ndarray = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[('year', int), ('age_group', 'U35'), ('gender', 'U10'), ('per_10000_examined', int)])

# Instantiate Figure and Axes
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2) #type: ignore

# Summarise Data
[*all_stats] = Statistic
desc(obesity_rates, file_name, all_stats) #type: ignore

# Pie Chart
male = obesity_rates['gender'] == 'Male'
female = obesity_rates['gender'] == 'Female'

male_sum = np.sum(obesity_rates[male]['per_10000_examined'])
female_sum = np.sum(obesity_rates[female]['per_10000_examined'])

ax1.pie((female_sum, male_sum), labels=['male', 'female'], startangle=90, autopct=lambda p: f'{p:.2f}%')
ax1.set_title('Proportion of Students With Obesity (by gender)')

# Line Chart
years = np.unique(obesity_rates['year'])
p1 = obesity_rates[obesity_rates['age_group'] == 'Primary 1 and equivalent age groups']
p5 = obesity_rates[obesity_rates['age_group'] == 'Primary 5 and equivalent age groups']

y1 = []
y2 = []

for y in years:
    y1.append(np.sum(p1[p1['year'] == y]['per_10000_examined']))
    y2.append(np.sum(p5[p5['year'] == y]['per_10000_examined']))

ax2.plot(years, np.array(y1), label='P1')
ax2.plot(years, np.array(y2), label='P5')
ax2.set_title('Number of Students With Obesity Annually')
ax2.set_xlabel('Year')
ax2.set_ylabel('Number of Students (per 10000 examined)')
ax2.legend(loc='upper left')
ax2.set_xticks(years)

ax2.set_ylim((1900, 3500))
ax2.text(2010, 2500, 'hello')

# Display Charts
plt.tight_layout()
plt.show()