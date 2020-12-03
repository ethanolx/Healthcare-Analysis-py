# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('ggplot')  # type: ignore

# Import Data
file_name = 'data/number-of-pharmacists.csv'
pharmacists = np.genfromtxt(file_name, delimiter=',',
                            skip_header=1, dtype=[('year', int), ('sector', 'U25'), ('count', int)])

# Summarise Data
[*all_stats] = Statistic
desc(pharmacists, file_name, all_stats, 3) #type: ignore

# Scatterplot
private = pharmacists['sector'] == 'Private Sector'
public = pharmacists['sector'] == 'Public Sector'
inactive = pharmacists['sector'] == 'Not in Active Practice'

sectors = private, public, inactive
types = 'private', 'public', 'inactive'

for i, s in enumerate(sectors):
    x = pharmacists[s]['year']
    y = pharmacists[s]['count']

    m, c, *_ = np.polyfit(x, y, 1)
    plt.plot(x, m * x + c)
    plt.scatter(x, y, label=types[i])

plt.title('Number of Pharmacists in Singapore (by sector)')
plt.legend(loc='upper left')

# Display Chart
plt.show()
