# This code creates two bar charts side by side:
    # 1. Comparing the number of people with or without heart disease based on physical activity.
    # 2. Comparing the number of people with or without heart disease based on fruit consumption.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data needed from the CSV
df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","PhysActivity","Fruits"])

# Physical Activity & Heart Disease
# Count people with ou without heart disease who are active or inactive
heart_disease_yes_active = np.sum((df["HeartDiseaseorAttack"] == 1) & (df["PhysActivity"] == 1))
heart_disease_yes_inactive = np.sum((df["HeartDiseaseorAttack"] == 1) & (df["PhysActivity"] == 0))
heart_disease_no_active = np.sum((df["HeartDiseaseorAttack"] == 0) & (df["PhysActivity"] == 1))
heart_disease_no_inactive = np.sum((df["HeartDiseaseorAttack"] == 0) & (df["PhysActivity"] == 0))

# labels, count & colors for the physical activity chart
labels1 = ["Heart Disease & Active", "Heart Disease & Inactive", " No Heart Disease & Active", " No Heart Disease & Inactive"]
count1 = [heart_disease_yes_active, heart_disease_yes_inactive, heart_disease_no_active, heart_disease_no_inactive]
colors1 = ["#DC143C", "#00FFFF","#FF7F50", "#DEB887"]

# Fruit Consumption & Heart Disease
# Count people with or without heart disease who eat fruits or not
heart_disease_yes_fruits_yes = np.sum((df["HeartDiseaseorAttack"] == 1) & (df["Fruits"] == 1))
heart_disease_no_fruits_yes = np.sum((df["HeartDiseaseorAttack"] == 0) & (df["Fruits"] == 1))
heart_disease_yes_fruits_no = np.sum((df["HeartDiseaseorAttack"] == 1) & (df["Fruits"] == 0))
heart_disease_no_fruits_no = np.sum((df["HeartDiseaseorAttack"] == 0) & (df["Fruits"] == 0))

# Labels, count & colors for fruit consumption chart
labels2 = ["Heart Disease & Fruits", "Heart Disease & No Fruits", " No Heart Disease & Fruits", " No Heart Disease & No Fruits"]
count2 = [heart_disease_yes_fruits_yes, heart_disease_no_fruits_no, heart_disease_no_fruits_yes, heart_disease_no_fruits_no]
colors2 = {"#483D8B", "#228B22", "#B22222", "#DAA520"}

# plot the two charts side by side
plt.figure(figsize=(20, 10))

# First Chart: Heart Disease vs Physical Activity
plt.subplot(1, 2, 1)
plt.bar(labels1, count1, color=colors1)
plt.title("Heart Disease vs. Physical Activity")
plt.xlabel("Group")
plt.ylabel("Number of People")
plt.xticks(rotation=90)

# Second Chart: Heart Disease vs Fruit Consumption
plt.subplot(1, 2, 2)
plt.bar(labels2, count2, color=colors2)
plt.title("Heart Disease vs. Fruits")
plt.xlabel("Group")
plt.ylabel("Number of People")
plt.xticks(rotation=90)

# Show the plot
plt.show()