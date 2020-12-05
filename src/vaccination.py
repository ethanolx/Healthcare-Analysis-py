# Import 3rd-Party Libraries and Custom Modules
import numpy as np
import matplotlib.pyplot as plt
from utils.stats_options import Statistic
from utils.summaries import describe as desc

# Choose Chart Style
plt.style.use('seaborn-muted')  # type: ignore

# Import Data
file_name = 'data/vaccination-and-immunisation-of-students-annual.csv'
vaccination = np.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=[
                            ('year', int), ('type', 'U30'), ('no_of_doses_k', int)])

# Instantiate Figure and Axes
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)  # type: ignore

# Summarise Data
[*all_stats] = Statistic
desc(vaccination, file_name, all_stats)  # type: ignore

# Bar Chart
x = vaccination['year']
y = vaccination['no_of_doses_k']

ax1.bar(x, y)
ax1.set_title('Number of Vaccinations Annually')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Vaccinations (1000)')
ax1.set_xticks(x)

# Boxplot
p = vaccination['type'] == 'Poliomyelitis'
p_data = vaccination[p]['no_of_doses_k']

d = vaccination['type'] == 'Diphtheria tetanus'
d_data = vaccination[d]['no_of_doses_k']

m = vaccination['type'] == 'Measles mumps rubella'
m_data = vaccination[m]['no_of_doses_k']

ax2.boxplot([p_data, d_data, m_data], labels=['P', 'D', 'M'], vert=False)
ax2.set_title('Boxplot')
ax2.set_xlabel('Number of Vaccinations (1000)')
ax2.set_ylabel('Type of Vaccinations')

# Display Charts
plt.tight_layout()
plt.show()
