# Generating Pink Noise Using Python

Pink noise, also known as 1/f noise, is a type of random signal that has equal energy per octave. Unlike white noise, which has a constant power spectral density across all frequencies, pink noise decreases in power as the frequency increases. It is commonly used in audio applications, such as sound masking, music production, and testing audio equipment.

# How It Works

1. We start by generating white noise using np.random.randn(n_samples). White noise is a random signal with a flat power spectral density across all frequencies.
2. Next, we compute the FFT (Fast Fourier Transform) of the white noise using np.fft.rfft(white_noise). This gives us the frequency domain representation of the signal.
3. We calculate the frequency bins using np.fft.rfftfreq(n_samples, d=1/sample_rate). These represent the different frequencies in our signal.
4. To create pink noise, we compute scaling factors for each frequency bin. The scaling factors decrease with increasing frequency, following a 1/f relationship. We exclude the DC component (bin 0) from scaling.
5. We apply the scaling factors to the FFT of white noise, resulting in the pink noise FFT.
6. Finally, we perform an inverse FFT on the pink noise FFT to obtain the time-domain pink noise signal.
7. The pink noise is then normalized to fit within the 16-bit range for audio data.

Now you know how to generate pink noise in Python! Feel free to experiment with different parameters, such as sample rate and duration, to create custom pink noise for your projects.

Keep in mind you need to install numpy, scipy and matplotlib for this to work!

Remember to save the generated pink noise to a WAV file (like I did with ‘pink_noise.wav’) for practical use. I also converted it to an mp3 as I mentioned earlier but this was because it’s much easier to run FFT analysis on .wav files than it is for .mp3 files. Remember, .wav is raw audio and .mp3 files are compressed.

# Analyzing Pink Noise: FFT Magnitude

Above, we generated pink noise and saved it to a WAV file. Now, let’s explore how to analyze this audio signal using Python to verify if it’s actually Pink noise.

# How It Works

1. Reading the WAV File: We start by reading the pink noise WAV file using wavfile.read(file_name). This gives us the sample rate and the audio data.
2. FFT (Fast Fourier Transform): We compute the FFT of the audio data using np.fft.fft(data). This transforms the time-domain signal into the frequency domain.
3. Magnitude: We extract the real and imaginary parts from the FFT result. The magnitude is calculated as the square root of the sum of squares of the real and imaginary parts.
4. Magnitude in dB: To visualize the magnitude, we convert it to decibels (dB) using 20 * np.log10(magnitude). This allows us to plot it on a logarithmic scale.
5. Frequency Axis: We create a frequency axis using np.fft.fftfreq(len(magnitude), 1/sample_rate).
6. Positive Frequencies Only: We keep only the positive frequencies (since the FFT result is symmetric). Otherwise, we get a mirrored version on the left.
7. Plotting: We plot the magnitude in dB and the phase against frequency. The resulting plots are saved as PNG images.

# Conclusion

By analyzing the FFT magnitude and phase, we gain insights into the frequency components of the pink noise. 
