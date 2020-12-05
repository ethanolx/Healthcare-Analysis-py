# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('ggplot')  # type: ignore

# Import Data
file_name = 'data/number-of-pharmacists.csv'
pharmacists: np.ndarray = np.genfromtxt(file_name, delimiter=',',
                            skip_header=1, dtype=[('year', int), ('sector', 'U25'), ('count', int)])

# Instantiate Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2) #type: ignore

# Summarise Data
[*all_stats] = Statistic
desc(pharmacists, file_name, all_stats, 3) #type: ignore

years: np.ndarray = np.unique(pharmacists['year']) #type: ignore

# Scatterplot
private: np.ndarray = pharmacists['sector'] == 'Private Sector'
public: np.ndarray = pharmacists['sector'] == 'Public Sector'
inactive: np.ndarray = pharmacists['sector'] == 'Not in Active Practice'

sectors = private, public, inactive
types = 'private', 'public', 'inactive'

for i, s in enumerate(sectors):
    y = pharmacists[s]['count']

    m, c, *_ = np.polyfit(years, y, 1)
    ax1.plot(years, m * years + c)
    ax1.scatter(years, y, label=types[i])

ax1.set_title('Number of Pharmacists in Singapore (by sector)')
ax1.legend(loc='upper left')

# Bar Chart
total_pharmacists_by_year = pharmacists['count'].reshape(-1, 3).sum(axis=1)
private_pct = pharmacists[private]['count'] / total_pharmacists_by_year
public_pct = pharmacists[public]['count'] / total_pharmacists_by_year
inactive_pct = pharmacists[inactive]['count'] / total_pharmacists_by_year

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

# Display Chart
plt.show()
