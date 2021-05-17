import numpy as np
import matplotlib
import pandas as pd
data = pd.read_csv("heart.csv")
print(data.head())
data.columns = ['Age','Sex','Chest Pain Type','Resting Blood Pressure','Serum Cholesterol in mg/dl','Fasting Blood Sugar > 120mg/dl','Resting ECG Results','Max HR Achieved','Exercise Induced Angina','Oldpeak','Slope','Number Major Vessels','Thal','Target']
print(data.head())
# Where Thal measurement; 0 = Normal, 1 = Fixed Defect and 2 = Reversible Defect
sorted_data = data.sort_values('Age')
print(sorted_data.head())






