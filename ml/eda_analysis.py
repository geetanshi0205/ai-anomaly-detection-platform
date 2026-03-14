import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/patient_data.csv")

# 1. Basic dataset overview
print("First rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# 2. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Histograms for distribution
df.hist(figsize=(10,8))
plt.tight_layout()
plt.show()

# 4. Boxplot for outliers
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

# 5. Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()