import numpy as np
from scipy.io import wavfile

def generate_pink_noise(n_samples, sample_rate):
    # Generate white noise
    white_noise = np.random.randn(n_samples)
    
    # Compute FFT of white noise
    white_fft = np.fft.rfft(white_noise)
    
    # Compute frequency bins
    freqs = np.fft.rfftfreq(n_samples, d=1/sample_rate)
    
    # Compute scaling factors for each frequency bin to create pink noise
    scale = np.zeros_like(freqs)
    scale[1:] = 1 / np.sqrt(freqs[1:])  # Exclude DC component
    
    # Apply scaling to FFT of white noise
    pink_fft = white_fft * scale
    
    # Inverse FFT to obtain pink noise
    pink_noise = np.fft.irfft(pink_fft)
    
    # Normalize to 16-bit range
    pink_noise *= 32767 / np.max(np.abs(pink_noise))
    
    return pink_noise.astype(np.int16)

# Generate pink noise
sample_rate = 44100
duration = 10  # seconds
n_samples = sample_rate * duration

pink = generate_pink_noise(n_samples, sample_rate)

# Save pink noise to WAV file
wavfile.write('pink_noise.wav', sample_rate, pink)

print("Pink noise generated and saved to 'pink_noise.wav'.")
