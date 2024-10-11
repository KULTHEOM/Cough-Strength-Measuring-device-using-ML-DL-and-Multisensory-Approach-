import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

# Load the audio file
audio_file = "C:/Users/OM/Desktop/Anvesshan/Final_supported_file/output10.wav"
y, sr = librosa.load(audio_file, sr=None)

# Calculate the spectral centroid
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

# Normalize the spectral centroid for visualization
frames = range(len(spectral_centroid[0]))
time = librosa.frames_to_time(frames, sr=sr)

# Print spectral centroid information
print("Spectral Centroid Shape:", spectral_centroid.shape)
print("/nSpectral Centroid Statistics:")
print(f"Mean: {np.mean(spectral_centroid):.2f} Hz")
print(f"Median: {np.median(spectral_centroid):.2f} Hz")
print(f"Standard Deviation: {np.std(spectral_centroid):.2f} Hz")
print(f"Maximum: {np.max(spectral_centroid):.2f} Hz")
print(f"Minimum: {np.min(spectral_centroid):.2f} Hz")

# Plot the spectral centroid along with the waveform
plt.figure(figsize=(10, 6))

# Plot waveform
librosa.display.waveshow(y, sr=sr, alpha=0.4, label='Waveform')

# Plot spectral centroid
plt.plot(time, spectral_centroid[0], color='r', label='Spectral Centroid')

# Add labels and legend
plt.xlabel('Time (s)')
plt.ylabel('Amplitude / Frequency (Hz)')
plt.title('Spectral Centroid and Waveform')
plt.legend()
plt.tight_layout()
plt.show()