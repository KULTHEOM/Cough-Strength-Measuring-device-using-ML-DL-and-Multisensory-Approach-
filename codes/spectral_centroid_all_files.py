import os
import librosa
import numpy as np

# Define the folder containing your .wav files
folder_path = "C:/Users/OM/Desktop/Anvesshan/Final_supported_file"

# Function to extract spectral centroid from a single audio file
def extract_spectral_centroid(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    
    # Get the mean, max, min, and standard deviation of the spectral centroid
    mean_centroid = np.mean(spectral_centroid)
    std_centroid = np.std(spectral_centroid)
    max_centroid = np.max(spectral_centroid)
    min_centroid = np.min(spectral_centroid)
    
    return {
        'mean': mean_centroid,
        'std': std_centroid,
        'max': max_centroid,
        'min': min_centroid
    }

# Loop through all .wav files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.wav'):
        file_path = os.path.join(folder_path, file_name)
        print(f"Processing {file_name}...")
        
        # Extract spectral centroid
        centroid_stats = extract_spectral_centroid(file_path)
        
        # Print or store the results
        print(f"Spectral Centroid for {file_name}:")
        print(f"  Mean: {centroid_stats['mean']}")
        print(f"  Std Dev: {centroid_stats['std']}")
        print(f"  Max: {centroid_stats['max']}")
        print(f"  Min: {centroid_stats['min']}")
        print()
