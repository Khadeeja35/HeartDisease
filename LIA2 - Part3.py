import pandas as pd
import numpy as np

df = pd.read_csv("HeartDiseaseData.csv",usecols=["HeartDiseaseorAttack","HighBP","HighChol","CholCheck","BMI","Smoker","Stroke","Diabetes","PhysActivity","Fruits"])

count_underweight=0
count_normal=0
count_overweight=0
count_obese=0
count_extremlyobese=0

for index in df["BMI"]:
    
    if index < 18.5:
        count_underweight+=1
        
    elif 18.5 <= index <= 24.9:
        count_normal+=1
        
    elif 25 <= index <= 29.9:
        count_overweight+=1
        
    elif 30 <= index <= 34.9:
        count_obese+=1
        
    else:
        count_extremlyobese+=1

total = np.sum([count_underweight, count_normal, count_overweight, count_obese, count_extremlyobese])

print("In", total, "people:")
print(count_underweight, "people are underweight;")
print(count_normal, "people have normal BMI;")
print(count_overweight, "people are overweight;")
print(count_obese, "people are obese;")
print(count_extremlyobese, "people are extremly obese.")

#Explanation:
        
# This filter seperates each data to their corresponding threshold for their BMI index
# the lower the BMI, the less chance they have to get heart disease and the opposite is true.
# This will help us into knowing what is the best indicator.

