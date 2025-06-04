import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
fs = 100  # Sampling frequency (100 Hz)
T = 10  # Duration (10 seconds)
t = np.linspace(0, T, fs * T)  # Time vector

# Normal vibration (sinusoidal wave)
freq = 5  # Frequency of vibration (5 Hz)
signal = np.sin(2 * np.pi * freq * t)

# Add random noise (normal distribution)
noise = 0.3 * np.random.randn(len(t))  # Noise with standard deviation of 0.3
signal += noise

# Inject anomalies (e.g., spikes in the signal)
signal[500:600] += 5  # sudden spike between indices 500-600
signal[900:950] -= 4  # sudden drop between indices 900-950

# Create DataFrame for easier handling
df = pd.DataFrame({'Time': t, 'Acceleration': signal})

# Save to CSV
df.to_csv('vibration.csv', index=False)

# Plot the signal
plt.figure(figsize=(10, 5))
plt.plot(t, signal, label='Vibration Signal')
plt.title("Simulated Vibration Data with Anomalies")
plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration")
plt.legend()
plt.show()
