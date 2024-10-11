import librosa
import numpy as np
import pandas as pd
import os

audio_dir = "D:/Competitions/Anveshan/Final_supported_file/"
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]

all_mfccs_df = pd.DataFrame()

for file in audio_files:
    file_path = os.path.join(audio_dir, file)
    
    signal, sr = librosa.load(file_path)
    
    # extract MFCCs and deltas
    mfccs = librosa.feature.mfcc(y=signal, n_mfcc=13, sr=sr)
    delta_mfccs = librosa.feature.delta(mfccs)
    delta2_mfccs = librosa.feature.delta(mfccs, order=2)
    
    # Concatenate all features
    mfccs_features = np.concatenate((mfccs, delta_mfccs, delta2_mfccs), axis=0)

    # create column names for MFCCs, DMFCCs, and DDMFCCs
    mfcc_columns = [f'mfcc_{i+1}' for i in range(mfccs.shape[0])]
    delta_mfcc_columns = [f'delta_mfcc_{i+1}' for i in range(delta_mfccs.shape[0])]
    delta2_mfcc_columns = [f'double_delta_mfcc_{i+1}' for i in range(delta2_mfccs.shape[0])]
    
    # concatenate all column names
    columns = mfcc_columns + delta_mfcc_columns + delta2_mfcc_columns
    
    # convert to DataFrame with column names
    mfccs_df = pd.DataFrame(mfccs_features.T, columns=columns)  # Transpose to get time steps as rows
    
    # add a column to identify the file name for each row of features
    mfccs_df['file'] = file
    
    # append to the main DataFrame
    all_mfccs_df = pd.concat([all_mfccs_df, mfccs_df], ignore_index=True)

# save the final DataFrame to a CSV file
csv_file = "all_mfccs_features.csv"
all_mfccs_df.to_csv(csv_file, index=False)

print(f"MFCC features for all files saved to {csv_file}")
