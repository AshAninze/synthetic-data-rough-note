import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r'C:\Users\ashionye.aninze\Documents\synthetic-data-rough-note\data\artificial_hes_ae_202302_v1_sample\artificial_hes_ae_0708.csv')


# Creating dataset that has only columns that are needed for analysis
# ARRIVALAGE: The patient's age when they arrived at the A&E department
# SEX: The patient's sex, with 1 for male, 2 for female and 0 for unknown
# DIAG3_01: The primary diagnosis given to the patient, based on ICD-10 
# TREAT3_01: The primary treatment or procedure the patient received, based on ICD-10 
# AEATTENDDISP: The outcome of the patient's visit to the A&E department (e.g., admitted to a hospital bed, discharged)
# AEARRIVALMODE: How the patient arrived at the A&E department, such as by 1 for ambulance, 2 for other means and 9 for unknown


rel_data = data[['ARRIVALAGE', 'SEX', 'DIAG3_01', 'TREAT3_01','AEATTENDDISP', 'AEARRIVALMODE' ]]

# Replace all NaN values with 0
rel_data = rel_data.fillna(0)

encoded = rel_data.copy()

# Encoding all variables
label_encoders = {}
for column in encoded.columns:
    le = LabelEncoder()
    encoded[column] = le.fit_transform(encoded[column].astype(str))
    label_encoders[column] = le
    
correlation_matrix = encoded.corr(numeric_only=True)
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", mask=mask)
plt.title('Correlation Matrix of Data')
plt.show()

def ambulance_rule(data):
    '''Rule: If ARRIVALAGE is 1 (Brought in by an ambulance),
    then set AEATTENDDISP to 1 (hospital bed)'''
    data.loc[data['AEARRIVALMODE'] == 1, 'AEATTENDDISP'] = 1
    return data

ambulance_rule(rel_data)

label_encoders = {}
for column in rel_data.columns:
    le = LabelEncoder()
    rel_data[column] = le.fit_transform(rel_data[column].astype(str))
    label_encoders[column] = le

correlation_matrix = rel_data.corr(numeric_only=True)
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", mask=mask)
plt.title('Correlation Matrix of Data')
plt.show()