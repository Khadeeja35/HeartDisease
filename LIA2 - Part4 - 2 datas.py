# This code creates a bar chart comparing the number of people with heart disease
# who also have high blood pressure or high cholesterol.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack", "HighBP", "HighChol"])

# People who have heart disease
heart_disease = df[df["HeartDiseaseorAttack"] == 1]

# Count how many of them have highBP or highChol
high_bp_with_hd = np.sum(heart_disease["HighBP"] == 1)
high_chol_with_hd = np.sum(heart_disease["HighChol"] == 1)

#axis
x = ["High Blood Pressure", "High Cholesterol"]
y = [high_bp_with_hd, high_chol_with_hd]

# Title/labels
plt.title("Comparison of People with High Blood Pressure or High Cholesterol")
plt.xlabel("Health Conditon")
plt.ylabel("Number of People with Heart Disease")

# Create the bar chart
plt.bar(x, y, color=["#48D1CC", "#DB7093"])

# Show the plot
plt.show()