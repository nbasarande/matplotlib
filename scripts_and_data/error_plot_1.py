from matplotlib import pyplot as plt
import numpy as np


x=[1.1, 2., 3., 3.9, 5.2, 6.7]
#err_x=[0.1, 0.4, 0.6, 0.4, 0.2,0.4]
y=[12.1, 22., 43., 53.9, 65.2, 72.]
err_y=[3.1, 3.4, 4.6, 5., 6.3, 6.5]
m,b=np.polyfit(x, y,1,w=err_y)      # m:slope and b:offset, 1 is the order of the polynomial
xx=np.linspace(1.1,6.7,6)
yy=m*xx+b

plt.errorbar(x,y,yerr=err_y,xerr=None,label='Label', linestyle='none', marker='o',
             markersize=4, capthick=2, capsize=4, linewidth=3)
plt.plot(xx,yy,  linestyle='--', label='Fit function',linewidth=3)
plt.text(2.7, 31,"y=%.2fx + %.2f" %(m,b), fontsize=8, weight='bold')


plt.title("My Plot", fontsize=16)
plt.xlabel("x axis",fontsize=14)
plt.ylabel("y axis",fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('error_plot_1.png')
plt.show()

