from matplotlib import pyplot as plt
import numpy as np


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

width=0.25
x_indexes=np.arange(len(ages_x))
plt.bar(x_indexes-width, js_dev_y,label="y1",width=width)
plt.bar(x_indexes, py_dev_y,label="y2",color="#444433", width=width)
plt.bar(x_indexes+width, dev_y,label="y3",width=width)
plt.title("My Plot", fontsize=16)
plt.xlabel("x axis",fontsize=12)
plt.ylabel("y axis",fontsize=12)
plt.ylim((30000,90000))
plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("bar_1.png")
plt.show()