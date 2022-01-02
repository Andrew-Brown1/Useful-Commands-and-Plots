import matplotlib.pyplot as plt


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
FONTSIZE = 10
color1 = 'tab:orange'
color2 = 'tab:blue'

ax1.plot(x_data, y1_data, color=color1)
ax2.plot(years, cum_durs, color=color2)


ax1.grid(axis='y', alpha=0.75)
ax1.set_xlabel('x-axis label',  fontsize=FONTSIZE)
ax1.set_title('title label',  fontsize=FONTSIZE)

ax1.tick_params(axis='y', labelsize= FONTSIZE, color=color1)
ax1.set_ylabel('y1 axis label',  fontsize=FONTSIZE, color=color1)

ax2.tick_params(axis='y', labelsize= FONTSIZE, color=color2)
ax2.set_ylabel('y2 axis label',  fontsize=FONTSIZE, color=color2)
plt.show()

