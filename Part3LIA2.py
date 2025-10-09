
import mathplotlib.pyplot as plt
import numpy as np
dataPt, HeartDiseaseorAttack, HighBP, BMI, CholCheck, HighChol, Smoker, Stroke, Diabetes, PhysActivity, Fruits = np.loadtxt(
 "heart_disease_health_indicators_BRFSS2015.csv", usecols=(1,2,3,4,5,6,7,8,9,10,11),skiprows=1, delimiter=",", unpack=True)

x = np.array(1,100)
y = np.array(BMI)

plt.scatter(x, y)
plt.show()


