import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataPt, HeartDiseaseorAttack, HighBP, BMI, CholCheck, HighChol, Smoker, Stroke, Diabetes, PhysActivity, Fruits = np.loadtxt(
 "HeartDiseaseData.csv", usecols=(1,2,3,4,5,6,7,8,9,10,11),skiprows=1, delimiter=",", unpack=True)

x = np.arange(0,253680)
y = np.array(BMI)
# --- 1. Your Data Loading (Included for context, assuming this has been run) ---
# Note: I'm making a small correction here—you listed 'HighChol' twice in usecols.
# I'll use the variables you defined in your prompt.
# I've created mock data below for anyone testing this without the actual CSV file.

plt.scatter(x, y)
plt.show()
# ASSUMPTION: The following variables hold your data as 1D NumPy arrays
# dataPt, HighChol, HighBP, BMI, CholCheck, Smoker, Stroke, Diabetes, PhysActivity, Fruits 

# --- Mock Data for Testing (REPLACE this with your actual data load) ---
# Assuming these variables are already loaded from your 'loadtxt' call:
N = 253680 # Number of data points
np.random.seed(42)
dataPt = np.arange(N) + 1  # Index or similar
HighChol = np.random.randint(0, 2, N) # Binary indicator
HighBP = np.random.randint(0, 2, N)     # Binary indicator
BMI = np.random.uniform(18.5, 40, N)    # Continuous data
# --------------------------------------------------------------------------

# --- 2. Create Subplots ---
# Create a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8)) 

# Adjust the spacing between subplots
plt.tight_layout(pad=3.0) 

# --- 3. Plot Data on Each Subplot ---

# Subplot 1 (Top-Left): Scatter plot of BMI vs. dataPt index
# We use axes[row, column] to specify the plot location.


# Create 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))



# Subplot 2 (Top-Right): Histogram of BMI Distribution
# Use a histogram to see the frequency of different BMI values
axes[0, 1].hist(BMI, bins=15, color='salmon', edgecolor='black')
axes[0, 1].set_title('Distribution of BMI')
axes[0, 1].set_xlabel('BMI Value')
axes[0, 1].set_ylabel('Frequency')

# Subplot 3 (Bottom-Left): Bar plot of High Blood Pressure
# This is a good way to visualize the count of a binary variable (0 or 1)
bp_counts = np.bincount(HighBP) # Counts the occurrences of each non-negative integer
axes[1, 0].bar([0, 1], bp_counts, color=['skyblue', 'darkgreen'])
axes[1, 0].set_xticks([0, 1])
axes[1, 0].set_xticklabels(['No High BP (0)', 'High BP (1)'])
axes[1, 0].set_title('Count of High Blood Pressure')
axes[1, 0].set_ylabel('Count')

# Subplot 4 (Bottom-Right): Side-by-side box plots for BMI grouped by High Cholesterol
# Box plots are excellent for comparing distributions between groups.
# We need to separate BMI values based on the HighChol status (0 or 1).
bmi_no_chol = BMI[HighChol == 0]
bmi_high_chol = BMI[HighChol == 1]
axes[1, 1].boxplot([bmi_no_chol, bmi_high_chol], labels=['No High Chol', 'High Chol'])
axes[1, 1].set_title('BMI Distribution by High Cholesterol')
axes[1, 1].set_ylabel('BMI')
axes[1, 1].grid(axis='y', linestyle=':')

# --- 4. Display the Figure ---
fig.suptitle('Health Indicators Analysis', fontsize=16, fontweight='bold') 
plt.show()