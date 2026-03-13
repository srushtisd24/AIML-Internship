
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
data = np.random.lognormal(mean=2, sigma=1, size=10000)

sample_means = []

for i in range(1000):
    sample = np.random.choice(data, size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
plt.figure(figsize=(8,5))
sns.histplot(sample_means, kde=True, bins=30)

plt.title("Distribution of Sample Means (Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()