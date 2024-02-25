import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

""" 
This script reads in a wav file, runs an FFT against it, 
and then stores the magnitude plot as a couple of .png images 

How It Works

1. Reading the WAV File: We start by reading the pink noise WAV file using wavfile.read(file_name). This gives us the sample rate and the audio data.
2. FFT (Fast Fourier Transform): We compute the FFT of the audio data using np.fft.fft(data). This transforms the time-domain signal into the frequency domain.
3. Magnitude: We extract the real and imaginary parts from the FFT result. The magnitude is calculated as the square root of the sum of squares of the real and imaginary parts.
4. Magnitude in dB: To visualize the magnitude, we convert it to decibels (dB) using 20 * np.log10(magnitude). This allows us to plot it on a logarithmic scale.
5. Frequency Axis: We create a frequency axis using np.fft.fftfreq(len(magnitude), 1/sample_rate).
6. Positive Frequencies Only: We keep only the positive frequencies (since the FFT result is symmetric). Otherwise, we get a mirrored version on the left.
7. Plotting: We plot the magnitude in dB and the phase against frequency. The resulting plots are saved as PNG images.

"""

def analyze_wav_file(file_name):
    sample_rate, data = wavfile.read(file_name)

    # Perform the FFT
    fft_result = np.fft.fft(data)

    # Get real and imaginary parts
    real_part = np.real(fft_result)
    imag_part = np.imag(fft_result)

    # Calculate magnitude
    magnitude = np.sqrt(real_part**2 + imag_part**2)

    # Convert magnitude to dB (To plot a log)
    magnitude_db = 20 * np.log10(magnitude)

    # Create frequency axis
    freq = np.fft.fftfreq(len(magnitude), 1/sample_rate)

    # Only keep positive frequencies
    positive_freq_mask = freq >= 0
    freq = freq[positive_freq_mask]
    magnitude_db = magnitude_db[positive_freq_mask]

    # Plot the magnitude in dB
    plt.figure(figsize=(12, 6))
    plt.plot(freq, magnitude_db)
    plt.title(f'FFT Magnitude (dB) for {file_name}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude [dB]')
    plt.savefig(f'magnitude_{file_name}.png')  # Save the figure as 'magnitude.png'
    plt.close()  # Close the figure to free up memory

# Read the .wav file
file_name = 'pink_noise.wav'
analyze_wav_file(file_name)
