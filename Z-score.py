import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore, norm

file_path = 'Jr.txt'  
with open(file_path, 'r') as file:
    data = np.array([float(line.strip()) for line in file])

z_scores = zscore(data)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(data, bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Original Data')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(z_scores, kde=True, color='orange', stat='density') 
plt.title('Z-Score Distribution')
plt.xlabel('Z-Scores')
plt.ylabel('Density')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(z_scores), np.std(z_scores))
plt.plot(x, p, 'r', linewidth=2)

plt.tight_layout()
plt.show()
