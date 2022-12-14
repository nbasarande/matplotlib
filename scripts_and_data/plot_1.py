from matplotlib import pyplot as plt
import numpy as np

x = np.array(range(25, 36, 1))
y1 = np.linspace(38000, 82000, 11)
y2 = y1 * np.sin(x * np.pi / 36)

plt.plot(x, y1,label="y1", color='k', linewidth=3, linestyle="--", marker=".", markersize=15)
plt.plot(x, y2,label="y2", linewidth=3, linestyle="-.")
plt.title("My Plot", fontsize=16)
plt.xlabel("x axis",fontsize=14)
plt.ylabel("y axis",fontsize=14)
plt.legend()

plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot_1.png")
plt.show()

'''
#print(plt.style.available) #shows available style
#plt.style.use("fivethirtyeight")  # without border
#plt.xkcd()   #Comics style


'''
