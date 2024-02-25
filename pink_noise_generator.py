import numpy as np
from scipy.io import wavfile

""" 
Simple tool to generate a wav file containing pink noise
"""

def pink_noise(n_samples):
    """Generates pink noise using the power law method."""
    # Generate white noise
    white = np.random.randn(n_samples)
    
    # Apply a power law to the Fourier Transform of the white noise to get pink noise
    f = np.fft.rfftfreq(n_samples)
    spectrum = np.fft.rfft(white) / np.sqrt(f**2 + 1)
    pink = np.fft.irfft(spectrum)
    
    return pink

# Generate 10 seconds of pink noise at a sample rate of 44100 Hz
sample_rate = 44100
n_samples = sample_rate * 10
pink = pink_noise(n_samples)

# Normalize to 16-bit range
max_abs_value = np.max(np.abs(pink))
if max_abs_value != 0:
    pink *= 32767 / max_abs_value
else:
    print("Warning: Maximum absolute value of generated noise is zero.")

# Convert to 16-bit data
pink = pink.astype(np.int16)

# Write data to WAV file
wavfile.write('pink_noise.wav', sample_rate, pink)
