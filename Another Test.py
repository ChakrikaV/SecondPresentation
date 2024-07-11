import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 

data = pd.read_csv('https://raw.githubusercontent.com/ChakrikaV/SecondPresentation/main/Online%20Sales%20Data.csv')

data.head()

print(data.columns)

print(data.isnull().sum())

df_data = data.dropna()
