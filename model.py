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
from keras.src.layers import TimeDistributed
from sklearn.model_selection import train_test_split
from keras.layers import Input, Dense, LSTM, RepeatVector
from keras.models import Model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from tensorflow.python.keras.layers import Dropout

warnings.filterwarnings("ignore", category=DeprecationWarning)

# # Load your data
df = pd.read_csv("C:/Users/DELL/Desktop/Graduation Project/dataset/SWaT_Dataset_Attack_v01.csv")
# to remove and clean any whitespaces in columns data
df.columns = df.columns.str.strip()


# Preprocess the data
df = df.drop(columns=['Timestamp'])
df['Normal/Attack'] = df['Normal/Attack'].map({'Normal': 0, 'Attack': 1})
target_label = df['Normal/Attack']
df_without_labels = df.drop(columns=['Normal/Attack'])

#df.to_csv('C:/Users/DELL/Desktop/Graduation Project/dataset/firstformatted.csv', index=False)

# for c in df.columns[:-2]:
#     df[c] = pd.to_numeric(df[c])

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

# #PCA for dimensionality reduction
# pca = PCA(n_components=15)
# reduced_data = pca.fit_transform(df_concat)

#create dataframe with scaled features
df_final = pd.DataFrame(df_concat)

#Add target column Normal/Attack to the scaled dataframe
#df_final['Normal/Attack'] = target_values
#df_final = df_final.map(lambda x: 1 if x == 'TRUE' else (0 if x == 'FALSE' else x))

#df_final.to_csv('C:/Users/DELL/Desktop/Graduation Project/dataset/scaledtosplit.csv', index=False)


# Identify NaN values in target_label
nan_indices = target_label.index[target_label.isna()].tolist()

# Remove samples with NaN values
target_label = target_label.dropna()
df_final = df_final.drop(index=nan_indices)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df_final, target_label, test_size=0.2, random_state=42,stratify=target_label)


# Reshape data for LSTM input (assuming your data is sequential)
X_train = np.asarray(X_train).reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = np.asarray(X_test).reshape((X_test.shape[0], 1, X_test.shape[1]))

y_test = np.asarray(y_test)
y_train = np.asarray(y_train)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

# Define the LSTM autoencoder model
model = Sequential()
model.add(LSTM(128, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dropout(rate=0.2))
model.add(RepeatVector(X_train.shape[1]))
model.add(LSTM(128, activation='relu', return_sequences=True))
model.add(Dropout(rate=0.2))
model.add(TimeDistributed(Dense(X_train.shape[2], activation='linear')))
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, X_train, epochs=20, batch_size=32, validation_data=(X_test, X_test), verbose=2)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) for each sample
mse = np.mean(np.square(X_test - predictions), axis=1)

# Set a threshold for anomaly detection (you may need to adjust this based on your data)
threshold = 0.5


predictions_labels = np.where(mse > threshold, 1, 0)
predictions_labels = np.argmax(predictions_labels, axis=1)


print("pred shape:", predictions_labels.shape)
print("y test shape:", y_test.shape)
print("predictions_labels:", predictions_labels)
print("y_test:", y_test)


# Evaluate the model on the test set labels
# precision = precision_score(y_test, predictions_labels)
# recall = recall_score(y_test, predictions_labels)
# f1 = f1_score(y_test, predictions_labels)
accuracy = (np.sum(predictions_labels == y_test) / len(y_test)) *100
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1-score:", f1)
print("Accuracy:", accuracy)
