import matplotlib.pyplot as plt
import numpy as np
dataPt, HeartDiseaseorAttack, HighBP, BMI, CholCheck, HighChol, Smoker, Stroke, Diabetes, PhysActivity, Fruits = np.loadtxt(
 "heart_disease_health_indicators_BRFSS2015.csv", usecols=(1,2,3,4,5,6,7,8,9,10,11),skiprows=1, delimiter=",", unpack=True)

plt.subplot(1, 2, 1)
plt.scatter(Smoker, PhysActivity)

plt.subplot(1, 2, 2)
plt.scatter(Smoker, Stroke)

plt.show()