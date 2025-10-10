# This code create a histogram showing the distribution of BMI among people with heart disease

import matplotlib.pyplot as plt
import pandas as pd

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","BMI"])

# People who have heart disease
heart_disease = df[df["HeartDiseaseorAttack"] == 1]

# BMI values of people with heart disease
BMI = heart_disease["BMI"]
colors="#DAA520"

# Title/labels
plt.title("Distribution of BMI Among People with Heart Disease")
plt.xlabel("Body Mass Index (BMI)")
plt.ylabel("Number of People with Heart Disease")

# Create the histogram
plt.hist(BMI)

# Show the plot
plt.show()
