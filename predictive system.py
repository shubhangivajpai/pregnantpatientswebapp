# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# loading the saved model
loaded_model=pickle.load(open('C:/Users/shubhangi vajpai/OneDrive/Desktop/predicting health risks/trained_model.sav','rb'))

print("---------------------------------")
print("       DecisionTreeClassifier")
print("Level of Risk:1-3   low->1,medium->2,high->3")
print("__________________________________")
inpFrame=['Enter Age of Patient:','Enter systolic Blood Pressure of Patient:','Enter Diastolic Blood Pressuree of Patient:','Enter Blood Glucose Level of Patient:','Enter Body Temperarature of  Patient:','Enter Heart Rateof Patient:',]
inpArray=list()
for i in  range(6):
  temp=input(inpFrame[i])
  inpArray.append(float(temp))

patientPredict=loaded_model.predict([inpArray])
print("________________________________________")
print("Risk Level of patient is:",patientPredict[0])
print('-----------------------------------------')
