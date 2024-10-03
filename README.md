# SoundProcessing

This repository contains various sound processing tools, each located in its own folder. Below is an overview of the contents and purpose of each folder.

## Contents

### 1. FFTAnalyzer

**Description**: This project reads a WAV file, performs a Fast Fourier Transform (FFT) on the audio data, and saves the magnitude plot as PNG images.

- **Script**: `fft_graph_wav_file.py`
- **Functionality**:
  - Reads a WAV file.
  - Performs FFT on the audio data.
  - Saves the magnitude plot as PNG images.

### 2. MorseCodeGenerator

**Description**: This project provides a web-based tool to convert text to Morse code and vice versa. It includes a simple HTML interface with Bootstrap for styling and JavaScript for functionality.

- **Files**:
  - `index.html`: The main HTML file for the web interface.
  - `morse.js`: JavaScript file containing the logic for converting text to Morse code and vice versa.
- **Functionality**:
  - Convert text to Morse code.
  - Convert Morse code to text.
  - Copy the converted Morse code or text to the clipboard.
  - Play the Morse code as audio.

### 3. PinkNoise

**Description**: This project generates pink noise and saves it as a WAV file. The pink noise is created by transforming white noise using a Fast Fourier Transform (FFT) and applying a 1/f scaling factor.

- **Script**: `pink_noise_generator.py`
- **Functionality**:
  - Generates white noise.
  - Transforms white noise to pink noise using FFT.
  - Saves the pink noise as a WAV file.

## Getting Started

Each folder contains its own `README.md` file with detailed instructions on how to set up and use the respective tools. Please refer to those files for more information.

## License

This repository is licensed under the MIT License - see the LICENSE file for details.
