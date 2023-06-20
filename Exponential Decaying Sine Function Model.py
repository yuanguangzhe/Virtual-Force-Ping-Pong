import numpy as np
import matplotlib.pyplot as plt

# 定义指数衰减正弦函数模型
def exponential_decay_sine(t, A, f, s):
    return A * np.sin(2 * np.pi * f * t) * np.exp(-s * t)

# 读取数据
data = np.loadtxt('date_name.csv', delimiter=',') 
ydata = data[:, 1]  # y 数据，例如观测值

# 计算时间向量
Fs = 1000  # 采样率，每秒的数据点数
delta_t = 1 / Fs  # 采样间隔，即两个数据点之间的时间间隔
t = np.arange(0, len(ydata) * delta_t, delta_t)  # 时间向量

# 手动选择参数值
A = 0.75
f = 1
s = 2

# 计算指数递减正弦函数的值
fit_data = exponential_decay_sine(t, A, f, s)

# 绘制拟合曲线和原始数据
plt.plot(t, ydata, label='data')
plt.plot(t, fit_data, 'r-', label='fit')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.show()
