import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\OM\Desktop\Anvesshan\all_mfccs_features_30ms_mean.csv")

# Sort by the 'filename' column, considering the numerical value after 'output'
df['file_number'] = df['file'].str.extract('(\d+)').astype(int)  # Extract the number from 'output' and convert to integer
df_sorted = df.sort_values('file_number')

# Drop the temporary 'file_number' column
df_sorted = df_sorted.drop(columns=['file_number'])

# Save the sorted DataFrame back to a CSV file (optional)
df_sorted.to_csv(r"C:\Users\OM\Desktop\Anvesshan\all_mfccs_features_30ms_mean.csv", index=False)

# Print the sorted DataFrame (for checking)
print(df_sorted)
