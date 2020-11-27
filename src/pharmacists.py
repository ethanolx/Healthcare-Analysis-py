import numpy as np
import matplotlib.pyplot as plt

# Scatterplot
pharmacists = np.genfromtxt('./data/number-of-pharmacists.csv', delimiter=',',
                            skip_header=1, dtype=[('year', int), ('sector', 'U25'), ('count', int)])


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

plt.show()

