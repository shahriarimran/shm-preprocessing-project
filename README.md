# vibration-anomaly-detection
'''
Why? Simulating realistic data in an oversimplified manner for flexibility and ease of understanding using sinusoidal waves, noise, anommaly injection and libraries like pandas and matplotlib

Steps to Simulate Vibration Data
Create a Time Vector
The time vector represents the time stamps at which measurements were taken. I defined the sampling frequency (fs) and the total duration (T) of the signal.
 
 - Sampling Frequency (fs): This defines how frequently we sample the signal. For example, a fs = 100 Hz means 100 samples per second.

 - Duration (T): The length of the time period over which we want to simulate the signal. In this case, T = 10 seconds.

 - Frequency of Vibration (freq): This is the frequency at which the vibration occurs. For simplicity, I set freq = 5 Hz, meaning the vibration repeats 5 times per second.
  
Generate the Vibration Signal
A sinusoidal signal can represent the vibration caused by some periodic source (e.g., wind, machinery). I combined this with random noise to make it more realistic.

  - To simulate a periodic vibration, I used a sine wave:

  - The equation np.sin(2 * np.pi * freq * t) generates a sine wave at the frequency specified by freq. The 2 * np.pi term converts the frequency from cycles per second (Hz)     to radians per second.

Sine wave: This is a basic and typical way to represent periodic behavior, which is common in mechanical vibrations caused by motors, wind, or structural oscillations.

  - In real-world signals, especially vibration data from sensors, there's usually random noise due to various factors (sensor errors, environmental conditions, etc.). I         added Gaussian noise using np.random.randn():
  - np.random.randn(len(t)) generates random values from a standard normal distribution (mean = 0, standard deviation = 1).
  - I then scaled the noise with a multiplier (0.3) to adjust its intensity.

Inject Anomalies
Add sudden spikes or drops to the signal to simulate abnormal behavior (this can represent something like a structural fault or unexpected load).

  - To simulate anomalous events (like equipment malfunction or unusual external factors), I added spikes and dips in the signal at specific intervals:

  - The command signal[500:600] += 5 adds a large spike in the signal between indices 500 and 600.

  - Similarly, signal[900:950] -= 4 introduces a sudden drop in the signal between indices 900 and 950.
  
Dataframe
Lastly, I used Pandas to store, organize and manipulate the time and signal values for the time-series data. Then I saved the data to a CSV.

Visualization using MATPLOTLIB
   
   
   '''

