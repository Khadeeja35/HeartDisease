import numpy as np
dataPt, HeartDiseaseorAttack, HighBP, BMI, CholCheck, HighChol, Smoker, Stroke, Diabetes, PhysActivity, Fruits = np.loadtxt(
 "heart_disease_health_indicators_BRFSS2015.csv", usecols=(1,2,3,4,5,6,7,8,9,10,11),skiprows=1, delimiter=",", unpack=True)

count_underweight=0
count_normal=0
count_overweight=0
count_obese=0
count_extremlyobese=0

for index in BMI:
    if index < 18.5:
        count_underweight+=1
    elif 18.5<index<24.9:
        count_normal+=1
    elif 25<index<29.9:
        count_overweight+=1
    elif 30<index<34.9:
        count_obese+=1
    else:
        count_extremlyobese+=1

print(count_underweight)
print(count_normal)
print(count_overweight)
print(count_obese)
print(count_extremlyobese)
        
# This filter seperates each data to their corresponding threshold for their BMI index
# the lower the BMI, the less chance they have to get heart disease and the opposite is true.
# This will help us into knowing what is the best indicator.

