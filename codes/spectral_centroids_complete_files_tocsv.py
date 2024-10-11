import os
import librosa
import numpy as np
import csv

# Define the folder containing your .wav files and output CSV file path
folder_path = "C:/Users/OM/Desktop/Anvesshan/Final_supported_file"
output_csv = "C:/Users/OM/Desktop/Anvesshan/newdataset_2.csv"
# Function to extract spectral centroid from a single audio file

def extract_spectral_centroid(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    
    # Get the mean, max, min, and standard deviation of the spectral centroid
    mean_centroid = np.mean(spectral_centroid)
    std_centroid = np.std(spectral_centroid)
    max_centroid = np.max(spectral_centroid)
    min_centroid = np.min(spectral_centroid)
    return mean_centroid, std_centroid, max_centroid, min_centroid

# Create and write to the CSV file
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['File Name', 'Mean Spectral Centroid', 'Std Dev Spectral Centroid', 'Max Spectral Centroid', 'Min Spectral Centroid'])
    
    # Loop through all .wav files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing {file_name}...")
            
            # Extract spectral centroid
            mean_centroid, std_centroid, max_centroid, min_centroid = extract_spectral_centroid(file_path)
            
            # Write the results to the CSV file
            writer.writerow([file_name, mean_centroid, std_centroid, max_centroid, min_centroid])

print(f"Results saved to {output_csv}")
