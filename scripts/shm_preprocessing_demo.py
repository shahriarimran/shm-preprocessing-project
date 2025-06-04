
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, periodogram

# Load the CSV
df = pd.read_csv(r"C:\Imran\METU\Thesis\code\shm_preprocessing_project\data\vibration.csv")
# Ensure the timestamp is in seconds and acceleration is in g   

# Extract time and acceleration
t = df['timestamp']
x = df['accel_x']

# 1. Plot raw acceleration vs. time
plt.figure(figsize=(10, 4))
plt.plot(t, x, linewidth=0.8)
plt.title('Raw Acceleration Signal (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Apply bandpass filter (0.1–1.0 Hz)
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

fs = 100  # Sampling frequency (Hz)
filtered_x = bandpass_filter(x, 0.1, 1.0, fs)

# Plot filtered signal
plt.figure(figsize=(10, 4))
plt.plot(t, filtered_x, linewidth=0.8, color='green')
plt.title('Filtered Acceleration Signal (0.1–1.0 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Plot FFT (magnitude spectrum)
f, Pxx = periodogram(filtered_x, fs)

plt.figure(figsize=(10, 4))
plt.semilogy(f, Pxx)
plt.title('Power Spectral Density (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Compute key stats
rms = np.sqrt(np.mean(filtered_x**2))
peak = np.max(np.abs(filtered_x))
dominant_freq = f[np.argmax(Pxx)]

print("RMS Acceleration: {:.3f} g".format(rms))
print("Peak Acceleration: {:.3f} g".format(peak))
print("Dominant Frequency: {:.3f} Hz".format(dominant_freq))
