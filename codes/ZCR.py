import librosa
import numpy as np
import pandas as pd

# Function to calculate ZCR for a given audio file
def calculate_zcr(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Calculate Zero Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)

    # Mean ZCR (Useful for overall measurement of cough intensity; Highly recommended)
    zcr_mean = np.mean(zcr)

    # Peak ZCR (Indicates the most intense coughing event; Highly recommended)
    zcr_peak = np.max(zcr)

    # Standard Deviation of ZCR (Helps identify variability in cough intensity; Recommended)
    zcr_std = np.std(zcr)

    # Return the results as a dictionary
    return {
        "File": audio_path,
        "Mean ZCR": zcr_mean,
        "Peak ZCR": zcr_peak,
        "Standard Deviation ZCR": zcr_std,
    }

# List to store results
results = []

# Loop through all 100 samples
for i in range(1, 101):
    audio_path = f"Final_supported_file/output{i}.wav"  # Construct the file path
    result = calculate_zcr(audio_path)  # Calculate ZCR for each audio file
    results.append(result)  # Add the result to the list

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
results_df.to_csv("zcr_results.csv", index=False)

print(f"ZCR for all files saved")