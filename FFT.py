import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('date_name.csv', header=None)
time = data.iloc[:, 0].values
acceleration = data.iloc[:, 1].values

# 计算傅里叶变换
dt = time[1] - time[0]  # 采样间隔
n = len(time)  # 采样点数
frequencies = np.fft.fftfreq(n, dt)  # 频率轴
acceleration_fft = np.fft.fft(acceleration)

# 绘制频谱图
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.abs(acceleration_fft), color='orange')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(0, 1 / (2 * dt))  # 设置x轴范围为正频率范围
plt.ylim(0, np.max(np.abs(acceleration_fft)) * 1.1)  # 设置y轴范围
plt.show()
