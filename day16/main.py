
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)

incomes = np.random.lognormal(mean=10, sigma=0.5, size=1000)
scores = 100 - np.random.lognormal(mean=3, sigma=0.4, size=1000)

data = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

def analyze_distribution(data, title):
    mean_val = np.mean(data)
    median_val = np.median(data)

    plt.figure(figsize=(6,4))
    sns.histplot(data, kde=True, bins=30)
    plt.title(title)
    plt.axvline(mean_val, color='red', linestyle='--', label=f"Mean = {mean_val:.2f}")
    plt.axvline(median_val, color='green', linestyle='--', label=f"Median = {median_val:.2f}")
    plt.legend()
    plt.show()

    print(f"{title}")
    print("Mean:", mean_val)
    print("Median:", median_val)

    if mean_val > median_val:
        print("Distribution: Right-Skewed\n")
    elif mean_val < median_val:
        print("Distribution: Left-Skewed\n")
    else:
        print("Distribution: Normal\n")

analyze_distribution(data["Heights"], "Human Heights (Normal Distribution)")
analyze_distribution(data["Incomes"], "Household Incomes (Right-Skewed)")
analyze_distribution(data["Scores"], "Test Scores (Left-Skewed)")