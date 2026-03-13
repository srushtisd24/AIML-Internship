
import pandas as pd
import numpy as np

data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G"],
    "Score": [55, 60, 65, 70, 75, 80, 150]   # 150 is an extreme value (outlier)
}

df = pd.DataFrame(data)
mean = df["Score"].mean()
std = df["Score"].std()

print("Mean:", mean)
print("Standard Deviation:", std)

df["z_score"] = (df["Score"] - mean) / std
outliers = df[np.abs(df["z_score"]) > 3]

print("\nDataset with Z-Scores:")
print(df)

print("\nOutliers (|Z| > 3):")
print(outliers)