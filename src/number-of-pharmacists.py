
# > Import Type Checking Modules
from typing import List, Tuple, cast

# > Import 3rd-Party Libraries
import numpy as np
import matplotlib.pyplot as plt

# > Import Custom Modules
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# > Choose Chart Style
plt.style.use('ggplot')

# > Import Data
file_name: str = 'data/number-of-pharmacists.csv'
pharmacists: np.ndarray = np.genfromtxt(file_name, delimiter=',',
                                        skip_header=1, dtype=[('year', int), ('sector', 'U25'), ('count', int)])

# Instantiate Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Summarise Data
all_stats: List[Statistic] = list(Statistic)
desc(pharmacists, file_name, all_stats, 3)

years: np.ndarray = cast(np.ndarray, np.unique(pharmacists['year']))

# Scatterplot
private: np.ndarray = pharmacists['sector'] == 'Private Sector'
public: np.ndarray = pharmacists['sector'] == 'Public Sector'
inactive: np.ndarray = pharmacists['sector'] == 'Not in Active Practice'

sectors: Tuple[np.ndarray, np.ndarray, np.ndarray] = private, public, inactive
types: Tuple[str, str, str] = 'private', 'public', 'inactive'

for i, s in enumerate(sectors):
    y: np.ndarray = pharmacists[s]['count']

    m: int; c: int
    m, c, *_ = np.polyfit(years, y, 1)

    ax1.plot(years, m * years + c)
    ax1.scatter(years, y, label=types[i])

ax1.set_title('Number of Pharmacists in Singapore (by sector)')
ax1.legend(loc='upper left')

# Bar Chart
total_pharmacists_by_year: np.ndarray = pharmacists['count'].reshape(-1, 3).sum(axis=1)
private_pct: np.ndarray = pharmacists[private]['count'] / total_pharmacists_by_year
public_pct: np.ndarray = pharmacists[public]['count'] / total_pharmacists_by_year
inactive_pct: np.ndarray = pharmacists[inactive]['count'] / total_pharmacists_by_year

ax2.bar(years, (private_pct + public_pct + inactive_pct) * 100, label='Inactive')
ax2.bar(years, (private_pct + public_pct) * 100, label='Public')
ax2.bar(years, private_pct * 100, label='Private')
ax2.plot([years.min() - 0.5, years.max() + 0.5], np.ones((2)) * 100, color='k')

ax2.set_ylim(0, 110)
ax2.set_xlim(years.min() - 0.5, years.max() + 0.5)
ax2.set_yticks([i * 10 for i in range(11)])

ax2.set_title('Proportions of Pharmacists in Singapore')
ax2.set_ylabel('Percentage of Pharmacists in Each Sector / %')
ax2.set_xlabel('Year')
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1),
           ncol=3, fancybox=True, shadow=True)

#> Display and Save Charts
plt.savefig('./assets/number-of-pharmacists.png')
plt.show()
