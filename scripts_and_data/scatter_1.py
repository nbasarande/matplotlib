import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#plt.style.use('seaborn')
data = pd.read_csv('data5.csv', sep=";").iloc[1::2,:]       # iloc[1::2,:] is to get rid of empty rows
view=data['view_count']/1000000
likes=data['likes']/1000000
ratio=data['ratio']
plt.scatter(view, likes, s=100, edgecolors='k',c=ratio, linewidths=1, alpha=0.4)        # s is the size of the circles
cbar=plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
#plt.legend()
plt.title("My Title",fontsize=16)
plt.grid(alpha=0.3)
plt.xlabel("Total likes (million)",fontsize=12)
plt.ylabel("View count (million)",fontsize=12)
plt.tight_layout()
plt.savefig("scatter_1.png")
plt.show()