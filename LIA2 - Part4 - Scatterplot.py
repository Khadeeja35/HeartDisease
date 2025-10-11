# This code creates a scatter plot showing the number of epople with heart disease
# for each BMI value

import matplotlib.pyplot as plt
import pandas as pd

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","BMI"])

# People with heart disease
heart_disease = df[df["HeartDiseaseorAttack"] == 1] 

# Count how many people with heart disease have each BMI value
BMI_counts = heart_disease["BMI"].value_counts().sort_index()

# Titles/labels
plt.title("BMI vs Number of People with heart disease")
plt.xlabel("Body Mass Index (BMI)")
plt.ylabel("Number of People with heart disease")

# Create the scatter plot
plt.scatter(BMI_counts.index, BMI_counts.values)

# Show the plot
plt.show()