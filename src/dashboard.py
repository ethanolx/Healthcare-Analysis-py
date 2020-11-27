import numpy as np
import matplotlib.pyplot as plt

fig, a = plt.subplots(nrows=2, ncols=3)

# 1 - line chart
medishield_data: np.ndarray = np.loadtxt('./data/amount-of-claims-made-under-medishield-life-fund-annual.csv', delimiter=',', skiprows=1, dtype=[('year', int), ('amt', float)])

x = medishield_data['year']
y = medishield_data['amt']

a[0][0].plot(x, y, 'o-b', mfc='g')
a[0][0].set_title('Line')

# 2 - pie chart
obesity_rate = np.genfromtxt('./data/common-health-problems-of-students-examined-overweight-annual.csv', delimiter=',', skip_header=1, dtype=[('year', int), ('age_group', 'U35'), ('gender', 'U10'), ('per_10000_examined', int)])

male = obesity_rate['gender'] == 'Male'
female = obesity_rate['gender'] == 'Female'

male_sum = np.sum(obesity_rate[male]['per_10000_examined'])
female_sum = np.sum(obesity_rate[female]['per_10000_examined'])

a[0][1].pie((male_sum, female_sum), labels=['male', 'female'])
a[0][1].set_title('Pie')

# 3 - Bar Chart

vaccination = np.genfromtxt('./data/vaccination-and-immunisation-of-students-annual.csv', delimiter=',', skip_header=1, dtype=[('year', int), ('type', 'U30'), ('no_of_doses_k', int)])

x2 = vaccination['year']
y2 = vaccination['no_of_doses_k']

a[0][2].bar(x2, y2)
a[0][2].set_title('Bar')

# 4 - Boxplot

p = vaccination['type'] == 'Poliomyelitis'
p_data = vaccination[p]['no_of_doses_k']
d = vaccination['type'] == 'Diphtheria tetanus'
d_data = vaccination[d]['no_of_doses_k']
m = vaccination['type'] == 'Measles mumps rubella'
m_data = vaccination[m]['no_of_doses_k']

a[1][0].boxplot([p_data, d_data, m_data], labels = ['P', 'D', 'M'])
a[1][0].set_title('Boxplot')

# 5 - Scatterplot
pharmacists = np.genfromtxt('./data/number-of-pharmacists.csv', delimiter=',', skip_header=1, dtype=[('year', int), ('sector', 'U25'), ('count', int)])

private = pharmacists['sector'] == 'Private Sector'
public = pharmacists['sector'] == 'Public Sector'
inactive = pharmacists['sector'] == 'Not in Active Practice'

x_private = pharmacists[private]['year']
x_public = pharmacists[public]['year']
x_inactive = pharmacists[inactive]['year']

y_private = pharmacists[private]['count']
y_public = pharmacists[public]['count']
y_inactive = pharmacists[inactive]['count']

a[1][1].scatter(x_private, y_private, label='private')
a[1][1].scatter(x_public, y_public, label='public')
a[1][1].scatter(x_inactive, y_inactive, label='inactive')
a[1][1].set_title('Scatter')
a[1][1].legend(loc='upper left')
a[1][1].set(ylim=(0, 2000))

plt.show()
