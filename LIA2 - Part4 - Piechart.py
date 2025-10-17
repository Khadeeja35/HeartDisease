# This code create a pie chart comparing the number of people with heart disease
# who also have diabetes, are smoker, or have had a stroke

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","Diabetes", "Stroke", "Smoker"])

# People who have diabetes (1 = Type 1 = yes and 2 = Type 2 = yes)
diabetes = df[(df["Diabetes"] == 1) | (df["Diabetes"] == 2)]

# Count how many of them have heart disease
heart_disease_with_diabetes = np.sum(diabetes["HeartDiseaseorAttack"] == 1)

# People who had a stroke
stroke = df[(df["Stroke"] == 1)]

# Count how many of them have heart disease
heart_disease_with_stroke = np.sum(stroke["HeartDiseaseorAttack"] == 1)

# People who are smokers
smoker = df[(df["Smoker"] == 1)]

# Count how many of them have heart disease
heart_disease_with_smoker = np.sum(smoker["HeartDiseaseorAttack"] == 1)

# Axis
labels = ["Diabetes", "Smoker", "Stroke"]
y = (heart_disease_with_diabetes, heart_disease_with_smoker, heart_disease_with_stroke)
colors = ["#00008B", "#8B008B", "#8B0000"]

# Title/labels
plt.title("Comparison of Heart Disease with Other Diseases")

# Create the pie chart
plt.pie(y, labels=labels, autopct="%2.1f%%", colors=colors)

# Show the plot
plt.show()