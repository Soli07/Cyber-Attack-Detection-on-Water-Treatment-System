import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Define file paths
file_path = "D:/uni/4th Year/GRAD/Attacked.csv"
output_file = "C:/Users/Mostafa/Desktop/preprocessed_dataset.csv"

# Read data
data = pd.read_csv(file_path)

# Backup original data
data_original = data.copy()

# Handle missing values
data.ffill(inplace=True)

# Define features to scale
features_to_scale = ['AIT202', 'AIT402', 'AIT502', 'DPIT301', 'FIT401', 'FIT502', 'LIT101', 'LIT301', 'LIT401']

# Create a copy of features to scale
features_copy = data[features_to_scale].copy()

# Create scaler
scaler = MinMaxScaler()

# Scale features
scaled_features = scaler.fit_transform(features_copy)

# Keep unscaled columns
unscaled_columns = [column for column in data.columns if column not in features_to_scale]

# Create preprocessed dataframe
preprocessed_data = pd.DataFrame(data=scaled_features, columns=features_to_scale)

# Combine scaled and unscaled data
preprocessed_data = pd.concat([preprocessed_data, data[unscaled_columns]], axis=1)

# Save preprocessed data
preprocessed_data.to_csv(output_file, index=False)

print(f"Preprocessed data saved to: {output_file}")


# Read the Excel file into a DataFrame
df = pd.read_csv('C:/Users/Mostafa/Desktop/preprocessed_dataset.csv')

# Replace categorical values with numerical values
df['Normal/Attack'] = df['Normal/Attack'].replace({'Normal': 0, 'Attack': 1})

# Save the modified DataFrame to a new Excel file
df.to_csv('C:/Users/Mostafa/Desktop/updated_file.csv', index=False)
