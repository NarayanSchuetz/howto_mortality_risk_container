#import
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pickle
import numpy as np
import pandas
import xgboost

from sklearn.linear_model import LogisticRegression


clf = pickle.load(open("xgb.p", "rb"))
cal = pickle.load(open("cal.p", "rb"))

means = {'age': 52.304, 'sex':0, 'creat':92.390, 'gluc':6.664, 'crp':47.393, 'quick':75.637, 'lac':2.004,
            'leuk':9.288}
mins = {'age':0, 'creat':5.400, 'gluc':0.400, 'crp':3, 'quick':8.0, 'lac':0.300,
            'leuk':0}
maxs = {'age':95, 'creat':1737, 'gluc':63.56, 'crp':637, 'quick':100, 'lac':597.400,
            'leuk':0}

#checks values and sets default if given value is not valid
def check_valid(value, key):
    try:
        value = float(value)
    except:
        value = np.nan
    return value

#checks if values are within range and sets them accordingly
def check_range(value, key):
    if value < mins[key]:
        value = mins[key]
    if value > maxs[key]:
        value = maxs[key]
    return value

# converts categorical string for sex into a binary variable
def get_sex(input):
    if "m" in input:
        return 0
    elif "f" in input:
        return 1
    else:
        return np.nan
      
"""
Here replace the entries in the array np.asarray[leuk,lac,creat,gluc,crp,age,sex, quick], with the respective values for those variables.
"""

leuk = 34
lac = 2
creat = 12
gluc = 123
crp = 1112
age = 100
sex = 0 # must be 0 for male and 1 for female
quick = 100

data = xgboost.DMatrix(np.asarray([leuk,lac,creat,gluc,crp,age,sex, quick]).reshape(1,-1), missing=np.NaN)

prediction = clf.predict(data)
calibrated_prediction_in_percentage = cal.predict_proba(prediction.reshape(-1,1))[:,0][0] * 100
