# import librosa
# import numpy as np
# import pandas as pd
# import os
# from scipy.signal import butter, lfilter

# # Bandpass filter setup
# def butter_bandpass(lowcut, highcut, fs, order=5):
#     nyq = 0.5 * fs  # Nyquist frequency
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter(order, [low, high], btype='band')
#     return b, a

# def bandpass_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# # Function to extract MFCCs
# def extract_mfccs_from_folder(audio_dir, low_freq, high_freq, csv_file):
#     audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
#     all_mfccs_df = pd.DataFrame()  # To store all extracted features
    
#     for file in audio_files:
#         file_path = os.path.join(audio_dir, file)
        
#         # Load the audio file
#         signal, sr = librosa.load(file_path, sr=None)  # Use native sampling rate
        
#         # Apply bandpass filter
#         filtered_signal = bandpass_filter(signal, low_freq, high_freq, sr)
        
#         # Extract MFCCs
#         mfccs = librosa.feature.mfcc(y=filtered_signal, sr=sr, n_mfcc=13)
#         delta_mfccs = librosa.feature.delta(mfccs)  # First-order difference (velocity)
#         delta2_mfccs = librosa.feature.delta(mfccs, order=2)  # Second-order difference (acceleration)
        
#         # Concatenate all features (MFCCs, delta, and delta2)
#         mfccs_features = np.concatenate((mfccs, delta_mfccs, delta2_mfccs), axis=0)
        
#         # Generate column names for MFCCs, Delta MFCCs, and Delta-Delta MFCCs
#         mfcc_columns = [f'mfcc_{i+1}' for i in range(mfccs.shape[0])]
#         delta_mfcc_columns = [f'delta_mfcc_{i+1}' for i in range(delta_mfccs.shape[0])]
#         delta2_mfcc_columns = [f'double_delta_mfcc_{i+1}' for i in range(delta2_mfccs.shape[0])]
#         columns = mfcc_columns + delta_mfcc_columns + delta2_mfcc_columns
        
#         # Convert MFCC features to DataFrame (transpose to make time steps as rows)
#         mfccs_df = pd.DataFrame(mfccs_features.T, columns=columns)
#         mfccs_df['file'] = file  # Add a column to track which file the features belong to
        
#         # Append to the main DataFrame
#         all_mfccs_df = pd.concat([all_mfccs_df, mfccs_df], ignore_index=True)

#     # Save the final DataFrame to a CSV file
#     all_mfccs_df.to_csv(csv_file, index=False)
#     print(f"MFCC features for all files saved to {csv_file}")

# # Parameters
# audio_dir = r"C:/Users/OM/Desktop/Anvesshan/Final_supported_file"  # Folder containing the .wav files
# low_freq = 100  # Low cutoff frequency for the bandpass filter
# high_freq = 5000  # High cutoff frequency for the bandpass filter
# csv_file = "C:/Users/OM/Desktop/Anvesshan/mfcc_features.csv"  # Output CSV file to save MFCC features

# # Extract MFCCs with bandpass filtering and save to CSV
# extract_mfccs_from_folder(audio_dir, low_freq, high_freq, csv_file)


import librosa
import numpy as np
import pandas as pd
import os
from scipy.signal import butter, lfilter

# Bandpass filter setup
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Function to extract averaged MFCC and DMFCC features
def extract_averaged_mfcc_dmfcc(audio_dir, low_freq, high_freq, csv_file):
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
    all_features_df = pd.DataFrame()  # To store all averaged features
    
    for file in audio_files:
        file_path = os.path.join(audio_dir, file)
        
        # Load the audio file
        signal, sr = librosa.load(file_path, sr=None)  # Use native sampling rate
        
        # Apply bandpass filter
        filtered_signal = bandpass_filter(signal, low_freq, high_freq, sr)
        
        # Extract MFCCs
        mfccs = librosa.feature.mfcc(y=filtered_signal, sr=sr, n_mfcc=13)
        # Extract Delta MFCCs (first-order difference)
        delta_mfccs = librosa.feature.delta(mfccs)
        
        # Compute the mean of MFCCs and DMFCCs across all time frames
        mfccs_mean = np.mean(mfccs, axis=1)
        delta_mfccs_mean = np.mean(delta_mfccs, axis=1)
        
        # Create a DataFrame for the single averaged set of MFCCs and DMFCCs
        mfcc_columns = [f'mfcc_{i+1}' for i in range(13)]
        delta_mfcc_columns = [f'delta_mfcc_{i+1}' for i in range(13)]
        
        # Combine MFCC and Delta MFCC features into a single row
        features = np.concatenate((mfccs_mean, delta_mfccs_mean))
        columns = mfcc_columns + delta_mfcc_columns
        
        # Create a DataFrame for the current file's features
        features_df = pd.DataFrame([features], columns=columns)
        features_df['file'] = file  # Add a column to track which file the features belong to
        
        # Append to the main DataFrame
        all_features_df = pd.concat([all_features_df, features_df], ignore_index=True)

    # Save the final DataFrame to a CSV file
    all_features_df.to_csv(csv_file, index=False)
    print(f"MFCC and Delta MFCC features for all files saved to {csv_file}")

# Parameters
audio_dir = r"C:\Users\OM\Desktop\Anvesshan\Final_supported_file" # Folder containing the .wav files
low_freq = 100  # Low cutoff frequency for the bandpass filter
high_freq = 5000  # High cutoff frequency for the bandpass filter
csv_file = r"C:\Users\OM\Desktop\Anvesshan\averaged_mfcc_dmfcc_features.csv"  # Output CSV file to save averaged MFCC and DMFCC features

# Extract and save averaged MFCCs and DMFCCs
extract_averaged_mfcc_dmfcc(audio_dir, low_freq, high_freq, csv_file)
