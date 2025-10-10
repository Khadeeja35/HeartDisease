# This code creates a bar chart comparing the number of people with heart disease
# who have diabetes versus those who do not

import matplotlib.pyplot as plt
import pandas as pd

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","Diabetes"])

import numpy as np

# People who have diabetes (1 = Type 1 = yes and 2 = Type 2 = yes)
diabetes = df[(df["Diabetes"] == 1) | (df["Diabetes"] == 2)]
heart_disease_with_diabetes = np.sum(diabetes["HeartDiseaseorAttack"] == 1)

# Count how many of them have heart disease
no_diabetes = df[df["Diabetes"] == 0]
heart_disease_without_diabetes = np.sum(no_diabetes["HeartDiseaseorAttack"] == 1)

# Axis
x = ["With Diabetes", "Without Diabetes"]
y = [heart_disease_with_diabetes, heart_disease_without_diabetes]

# Title/labels
plt.title("People with Heart Disease: Diabetes vs. No Diabetes")
plt.xlabel("Health Conditon")
plt.ylabel("Number of People with Heart Disease")

# Create the bar chart
plt.bar(x, y, color=["#FFA07A", "#6B8E23"])

# Show the plot
plt.show()
