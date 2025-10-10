# This code creates a line plot showing the number of people for each BMI value

import matplotlib.pyplot as plt
import pandas as pd

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","HighBP","HighChol","CholCheck","BMI","Smoker","Stroke","Diabetes","PhysActivity","Fruits"])

# Count how many people have each BMI value
BMI_counts = df["BMI"].value_counts().sort_index()

# Title/labels
plt.title("BMI vs Number of People")
plt.xlabel("Body Mass Index (BMI)")
plt.ylabel("Number of People")

# Create the line plot with grid
plt.plot(BMI_counts.index, BMI_counts.values)
plt.grid()

# Show the plot
plt.show()