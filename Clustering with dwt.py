import warnings
import pandas as pd
import numpy as np
import csv
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow
import keras
import keras.layers
from keras import Sequential
from keras.layers import Input, Dense, LSTM, RepeatVector
from keras.models import Model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pywt  # Import the PyWavelets library for DWT


# Load your data
df = pd.read_csv("D:/uni/4th Year/GRAD/Project/SWaT_Dataset_Attack_v0.csv")

# Remove and clean any whitespaces in column names
df.columns = df.columns.str.strip()

# Preprocess the data
df = df.drop(columns=['Timestamp'])
df['Normal/Attack'] = df['Normal/Attack'].map({'Normal': 0, 'Attack': 1})
target_label = df['Normal/Attack']
df_without_labels = df.drop(columns=['Normal/Attack'])

for col in df_without_labels.columns:
    if len(df_without_labels[col].unique()) == 1:
        df_without_labels.drop(col, inplace=True, axis=1)

# Feature engineering and scaling
cat_col = []
num_col = []

for column in df_without_labels.columns:
    unique_values = df_without_labels[column].nunique()
    if unique_values > 10:
        num_col.append(column)
    else:
        cat_col.append(column)

one_hot_encoded_data = pd.get_dummies(df_without_labels, columns=cat_col)
processed_df = one_hot_encoded_data.copy()

min_max_scaler = MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(processed_df[num_col])
df_num = pd.DataFrame(x_scaled, index=processed_df.index, columns=num_col)

df_concat = pd.concat([df_num, processed_df.drop(columns=num_col)], axis=1)

# Apply Discrete Wavelet Transform (DWT)
def apply_dwt(data):
    transformed_data = []
    for _, row in data.iterrows():
        coeffs = pywt.wavedec(row.values, 'db1', level=3)  # 'db1' is the Daubechies wavelet
        transformed_data.append(np.concatenate(coeffs))
    return pd.DataFrame(transformed_data, columns=np.arange(len(transformed_data[0])))

df_dwt = apply_dwt(df_concat)

# Perform k-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(df_dwt)

# Print cluster counts
cluster_counts = np.bincount(clusters)
print("Cluster Counts:", cluster_counts)
