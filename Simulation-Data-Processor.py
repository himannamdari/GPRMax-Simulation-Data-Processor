import os
import h5py
import numpy as np
import pandas as pd

# Define the main directory and file paths
sim_path = r"/home/hnamdari/gprMax/user_models/Simulations/200K_D/140k_real_data/134K_real_simu"
sav_path = r"/home/hnamdari/gprMax/user_models/Simulations/200K_D/140k_real_data"
labels_file = os.path.join(sav_path, 'labels.csv')
traces_ez_file = os.path.join(sav_path, 'traces_Ez.csv')

print("Paths defined successfully.")

# Read and prepare labels
labels_data = []
with open(os.path.join(sav_path, 'labels.txt'), 'r') as f:
    for line in f:
        values = line.strip().split(',')
        labels_data.append(values)

print("Labels read from file and parsed.")

# Create a DataFrame for the labels data
labels_df = pd.DataFrame(labels_data)
print("Labels DataFrame created.")

# Create empty lists to store the traces data
traces_ez_data = []

# Get the list of all files in the main directory
dir_list = sorted(os.listdir(sim_path))
num_files = len(dir_list)
print(f"Number of files in directory: {num_files}")

# Read the .out files and extract the Ez data
for i in range(1, num_files):  # Adjusting file name pattern if necessary
    file_path = os.path.join(sim_path, f'pep_3layer{i}.out')
    if os.path.exists(file_path):
        with h5py.File(file_path, 'r') as f:
            arr_ez = f.get('rxs/rx1/Ez')[:]
            traces_ez_data.append(arr_ez.tolist())
    else:
        print(f'File {file_path} does not exist.')

print("Ez data extraction complete.")

# Create DataFrames for the Ez traces data
traces_ez_df = pd.DataFrame(traces_ez_data)
print("Traces Ez DataFrame created.")

# Drop the first column from labels_df if not needed
labels_df = labels_df.drop(labels_df.columns[0], axis=1, errors='ignore')
print("First column dropped from Labels DataFrame.")
traces_ez_df = traces_ez_df.drop(traces_ez_df.columns[0], axis=1, errors='ignore')
print("First column dropped from Traces Ez DataFrame.")

# Combine the labels and traces data into a single DataFrame
combined_df = pd.concat([labels_df, traces_ez_df], axis=1)
print("Data combined into a single DataFrame.")

# Save the data to CSV files
combined_df.to_csv(labels_file, index=False)
print(f'Labels DataFrame written to CSV: {labels_file}')
