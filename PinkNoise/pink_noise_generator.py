import numpy as np
from scipy.io import wavfile

"""
    How It Works

    1. We start by generating white noise using np.random.randn(n_samples). White noise is a random signal with a flat power spectral density across all frequencies.
    2. Next, we compute the FFT (Fast Fourier Transform) of the white noise using np.fft.rfft(white_noise). This gives us the frequency domain representation of the signal.
    3. We calculate the frequency bins using np.fft.rfftfreq(n_samples, d=1/sample_rate). These represent the different frequencies in our signal.
    4. To create pink noise, we compute scaling factors for each frequency bin. The scaling factors decrease with increasing frequency, following a 1/f relationship. We exclude the DC component (bin 0) from scaling.
    5. We apply the scaling factors to the FFT of white noise, resulting in the pink noise FFT.
    6. Finally, we perform an inverse FFT on the pink noise FFT to obtain the time-domain pink noise signal.
    7. The pink noise is then normalized to fit within the 16-bit range for audio data.

"""

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
