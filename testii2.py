import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("HeartDiseaseData.csv", usecols=["HeartDiseaseorAttack", "BMI"])
dataPt = range(len(df))

# Create 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# First subplot (top-left)
axes[0, 0].scatter(dataPt, df["BMI"], color='darkblue', alpha=0.6)
axes[0, 0].set_title('BMI Across Data Points (dataPt)')
axes[0, 0].set_xlabel('Data Point Index (dataPt)')
axes[0, 0].set_ylabel('BMI')
axes[0, 0].grid(True, linestyle=':')

plt.tight_layout()
plt.show()
