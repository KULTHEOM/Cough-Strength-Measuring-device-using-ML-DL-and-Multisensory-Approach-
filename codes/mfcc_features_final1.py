import librosa
import numpy as np
import pandas as pd
import os

# Directory containing the audio files
audio_dir = r"C:\Users\OM\Desktop\Anvesshan\Final_supported_file"
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]

# Create an empty DataFrame to store MFCC features
all_mfccs_df = pd.DataFrame()

# Set the window length and hop length for 30ms segments (assuming 30ms with sr = 16000)
segment_duration_ms = 30
segment_duration_samples = int((segment_duration_ms / 1000) * 16000)  # 16000 samples per second for 30ms

# Iterate through each audio file
for file in audio_files:
    file_path = os.path.join(audio_dir, file)
    
    # Load the audio file
    signal, sr = librosa.load(file_path, sr=16000)  # Use a consistent sample rate of 16000 Hz
    
    # Split the signal into 30ms segments with no overlap
    segments = librosa.util.frame(signal, frame_length=segment_duration_samples, hop_length=segment_duration_samples)
    
    mfccs_all_segments = []

    # Extract MFCCs for each segment, restricting frequency range to 100-5000 Hz and using n_fft=512
    for segment in segments.T:
        mfccs = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13, fmin=100, fmax=5000, n_fft=512)
        mfccs_all_segments.append(mfccs.mean(axis=1))  # Calculate the mean for each MFCC across the segment
    
    # Convert the list of MFCCs to a numpy array
    mfccs_all_segments = np.array(mfccs_all_segments)

    # Calculate the mean across all segments for each MFCC
    mfccs_mean = np.mean(mfccs_all_segments, axis=0)
    
    # Calculate delta and double-delta features for the mean MFCCs
    delta_mfccs_mean = librosa.feature.delta(mfccs_mean)
    delta2_mfccs_mean = librosa.feature.delta(mfccs_mean, order=2)

    # Concatenate MFCC, delta, and delta-delta features
    features = np.concatenate((mfccs_mean, delta_mfccs_mean, delta2_mfccs_mean))

    # Create a dictionary to store the feature values
    feature_dict = {}
    for i in range(13):
        feature_dict[f'mfcc_{i+1}'] = mfccs_mean[i]
    for i in range(13):
        feature_dict[f'delta_mfcc_{i+1}'] = delta_mfccs_mean[i]
    for i in range(13):
        feature_dict[f'double_delta_mfcc_{i+1}'] = delta2_mfccs_mean[i]

    # Add the file name to the feature dictionary
    feature_dict['file'] = file
    
    # Convert the dictionary to a DataFrame and concatenate it to the existing DataFrame
    temp_df = pd.DataFrame([feature_dict])
    all_mfccs_df = pd.concat([all_mfccs_df, temp_df], ignore_index=True)

# Save the final DataFrame to a CSV file
csv_file = r"C:\Users\OM\Desktop\Anvesshan\all_mfccs_features_30ms_mean.csv"
all_mfccs_df.to_csv(csv_file, index=False)

print(f"MFCC features (30ms mean, 100-5000 Hz) for all files saved to {csv_file}")
