# WAV File FFT Analyzer

This project reads a WAV file, performs a Fast Fourier Transform (FFT) on the audio data, and saves the magnitude plot as PNG images.

## How It Works

1. **Reading the WAV File**: The script reads the WAV file using `wavfile.read(file_name)`, which provides the sample rate and audio data.
2. **FFT (Fast Fourier Transform)**: The FFT of the audio data is computed using `np.fft.fft(data)`, transforming the time-domain signal into the frequency domain.
3. **Magnitude Calculation**: The magnitude is calculated from the real and imaginary parts of the FFT result.
4. **Magnitude in dB**: The magnitude is converted to decibels (dB) using `20 * np.log10(magnitude)` for logarithmic plotting.
5. **Frequency Axis**: A frequency axis is created using `np.fft.fftfreq(len(magnitude), 1/sample_rate)`.
6. **Positive Frequencies Only**: Only the positive frequencies are kept for plotting.
7. **Plotting**: The magnitude in dB is plotted against frequency, and the resulting plots are saved as PNG images.

## Installation

### Prerequisites

- Python 3.x
- `numpy`, `scipy`, and `matplotlib` libraries
- Docker

### Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/wav-file-fft-analyzer.git
    cd wav-file-fft-analyzer
    ```

2. **Install Dependencies**

    ```sh
    pip install numpy scipy matplotlib
    ```

3. **Run the Script**

    ```sh
    python analyze_wav_file.py
    ```

## Docker Setup

1. **Create a Dockerfile**

    Create a file named `Dockerfile` in the project directory with the following content:

    ```dockerfile
    # Use the official Python image from the Docker Hub
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install numpy scipy matplotlib

    # Run the script
    CMD ["python", "analyze_wav_file.py"]
    ```

2. **Build the Docker Image**

    Run the following command in the directory where your Dockerfile is located:

    ```sh
    docker build -t wav-file-fft-analyzer .
    ```

3. **Run the Docker Container**

    Run the following command to start the container:

    ```sh
    docker run -v $(pwd):/app wav-file-fft-analyzer
    ```

## Usage

1. **Prepare a WAV File**

    Ensure you have a WAV file named `file.wav` in the project directory or modify the `file_name` variable in the script to point to your WAV file.

2. **Run the Script**

    ```sh
    python analyze_wav_file.py
    ```

3. **Output**

    The script will generate a PNG image of the FFT magnitude plot and save it as `magnitude_file.wav.png` in the project directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
