import matplotlib.pyplot as plt
import numpy as np

# 原始数据
x = np.array([1, 10, 50, 100, 200, 400, 1000, 2000])
y = np.array([100, 95, 70, 30, 10, 2, 1, 1])
sd = 2
x_smooth = np.logspace(np.log10(x.min()), np.log10(x.max()), 300) # 计算平均值曲线
y_smooth = np.interp(x_smooth, x, y)
# 计算误差条的上下界
upper_bound = y + sd
lower_bound = y - sd

plt.plot(x_smooth, y_smooth, label='Smooth Curve', linewidth=1)# 绘制平滑曲线
plt.errorbar(x, y, yerr=sd, fmt='o', capsize=3, color='red', marker='o',
             zorder=10,markerfacecolor='none', markeredgecolor='red',markersize=5, ecolor='black')# 绘制误差条
plt.xscale("symlog")# 设置对数标度的x轴

plt.xlabel('X')# 添加标签和图例
plt.ylabel('Y')
plt.title('Smooth Curve with Error Bar')
plt.legend()

plt.savefig("test.pdf")
plt.show()






