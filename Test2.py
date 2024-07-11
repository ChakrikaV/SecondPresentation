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

user_item_matrix = data.pivot_table(index='Transaction ID', columns='Product Name', values='Units Sold', fill_value=0)

print("User-Item Matrix:")
print(user_item_matrix.head())

from sklearn.neighbors import NearestNeighbors

# Previously prepped data 
user_item_matrix = data.pivot_table(index='Transaction ID', columns='Product Name', values='Units Sold', fill_value=0)

# Initialize KNN model
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')

# Fit the model
knn_model.fit(user_item_matrix.values)

# Look up for Client
#kneighbor means other products similar
user_index = 5  
distances, indices = knn_model.kneighbors(user_item_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=5)

# Get top-n recommended products
recommended_products = [user_item_matrix.columns[i] for i in indices.flatten()]

print("Recommended Products:", recommended_products)
