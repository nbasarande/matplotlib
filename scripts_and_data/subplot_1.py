import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data6.csv', sep=";").iloc[1::2, :]
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax2.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')
ax2.set_ylabel('Median Salary (USD)')

ax1.grid(alpha=0.3)
ax2.grid(alpha=0.3)
plt.tight_layout()
fig1.savefig('subplot_1.png')
plt.show()

