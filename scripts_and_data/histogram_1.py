import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#plt.style.use('fivethirtyeight')
data = pd.read_csv('data4.csv')
ids=data['Responder_id']
ages=data['Age']
median_age=np.median(ages)

bins=np.arange(10,70,10)
print(bins)

plt.hist(ages, bins=bins, edgecolor='black', alpha=0.6)
plt.axvline(median_age, label='Age_Median = %.1f'%(median_age), color='#222222', linestyle='--')
plt.ylim((0,60))
plt.xlim((5,55))



plt.legend()
plt.title("My Title",fontsize=16)
plt.grid(alpha=0.3)
plt.xlabel("xlabel",fontsize=12)
plt.ylabel("ylabel",fontsize=12)
plt.tight_layout()
plt.savefig("histogram_1.png")
plt.show()