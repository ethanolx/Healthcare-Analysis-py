# type: ignore
# > Import Type Checking Modules
from typing import List, Tuple, cast
from matplotlib.axes import Axes
from matplotlib.figure import Figure

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

# > Process Data

# for all charts
years: np.ndarray = cast(np.ndarray, np.unique(pharmacists['year']))

# for scatterplot
private: np.ndarray = pharmacists['sector'] == 'Private Sector'
public: np.ndarray = pharmacists['sector'] == 'Public Sector'
inactive: np.ndarray = pharmacists['sector'] == 'Not in Active Practice'

# for bar chart
total_pharmacists_by_year: np.ndarray = pharmacists['count'].reshape(
    -1, 3).sum(axis=1)
private_pct: np.ndarray = pharmacists[private]['count'] / \
    total_pharmacists_by_year
public_pct: np.ndarray = pharmacists[public]['count'] / \
    total_pharmacists_by_year
inactive_pct: np.ndarray = pharmacists[inactive]['count'] / \
    total_pharmacists_by_year

# > Summarise Data
all_stats: List[Statistic] = list(Statistic)
desc(pharmacists, file_name, all_stats, 3)

# > Instantiate Figure and Axes
fig, (ax1, ax2) = cast(
    Tuple[Figure, Tuple[Axes, Axes]], plt.subplots(1, 2, figsize=(12, 6)))

# > Scatterplot

# Additional Data Preparation
sectors: Tuple[np.ndarray, np.ndarray, np.ndarray] = private, public, inactive
types: Tuple[str, str, str] = 'private', 'public', 'inactive'

# For each sector, plot scatter and line
for i, s in enumerate(sectors):
    count: np.ndarray = pharmacists[s]['count']

    m: int
    c: int
    m, c, *_ = np.polyfit(years, count, 1)

    ax1.plot(years, m * years + c)
    ax1.scatter(years, count, label=types[i])

# Set axis labels
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of pharmacists')

# Set title
ax1.set_title('Trend of Number of Pharmacists in SG (by sector)')

# Set legend
ax1.legend(loc='upper left')

# > Bar Chart

# Construct Bar Chart
ax2.bar(years, (private_pct + public_pct + inactive_pct) * 100, label='Inactive')
ax2.bar(years, (private_pct + public_pct) * 100, label='Public')
ax2.bar(years, private_pct * 100, label='Private')

# Construct cap and rules
ax2.plot([years.min() - 0.5, years.max() + 0.5], np.ones((2)) * 100, color='k')
ax2.plot([years.min() - 0.5, years.max() + 0.5], np.ones((2)) * 100 * private_pct[0], color='b', linewidth=0.2)
ax2.plot([years.min() - 0.5, years.max() + 0.5], np.ones((2)) * 100 * private_pct[-1], color='b', linewidth=0.2)

# Set chart boundaries
ax2.set_xlim(years.min() - 0.5, years.max() + 0.5)
ax2.set_ylim(0, 110)

# Set axis ticks
ax2.set_yticks([i * 10 for i in range(11)])

# Set title
ax2.set_title('Proportion of Pharmacists in Singapore')

# Set axis labels
ax2.set_ylabel('Percentage of pharmacists in each sector / %')
ax2.set_xlabel('Year')

# Set legend
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1),
           ncol=3, fancybox=True, shadow=True)

# > Display and Save Charts
plt.savefig('./assets/number-of-pharmacists.png')
plt.show()
