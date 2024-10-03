# Pink Noise Generator

This project generates pink noise and saves it as a WAV file. The pink noise is created by transforming white noise using a Fast Fourier Transform (FFT) and applying a 1/f scaling factor.

## How It Works

1. **Generate White Noise**: White noise is generated using `np.random.randn(n_samples)`.
2. **Compute FFT**: The FFT of the white noise is computed using `np.fft.rfft(white_noise)`.
3. **Calculate Frequency Bins**: Frequency bins are calculated using `np.fft.rfftfreq(n_samples, d=1/sample_rate)`.
4. **Compute Scaling Factors**: Scaling factors for each frequency bin are computed to create pink noise, following a 1/f relationship.
5. **Apply Scaling**: The scaling factors are applied to the FFT of the white noise.
6. **Inverse FFT**: An inverse FFT is performed to obtain the time-domain pink noise signal.
7. **Normalize**: The pink noise is normalized to fit within the 16-bit range for audio data.

## Installation

### Prerequisites

- Docker
- Python 3.x
- `numpy` and `scipy` libraries

### Docker Setup

1. **Create a Dockerfile**

    ```dockerfile
    # Use the official Python image from the Docker Hub
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir numpy scipy

    # Run the script
    CMD ["python", "your_script.py"]
    ```

2. **Build the Docker Image**

    ```sh
    docker build -t pink-noise-generator .
    ```

3. **Run the Docker Container**

    ```sh
    docker run -v $(pwd):/app pink-noise-generator
    ```

### Running Locally

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/pink-noise-generator.git
    cd pink-noise-generator
    ```

2. **Install Dependencies**

    ```sh
    pip install numpy scipy
    ```

3. **Run the Script**

    ```sh
    python your_script.py
    ```

## Output

The generated pink noise will be saved as `pink_noise.wav` in the current directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
