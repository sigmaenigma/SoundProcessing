# Morse Code Converter

This project provides a web-based tool to convert text to Morse code and vice versa. It includes a simple HTML interface with Bootstrap for styling and JavaScript for functionality.

## Features

- Convert text to Morse code
- Convert Morse code to text
- Copy the converted Morse code or text to the clipboard
- Play the Morse code as audio

## Installation

### Prerequisites

- A web browser (e.g., Chrome, Firefox, Edge)

### Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/morse-code-converter.git
    cd morse-code-converter
    ```

2. **Directory Structure**

    Ensure your project directory contains the following files:

    ```plaintext
    morse-code-converter/
    ├── index.html
    ├── morse.js
    └── README.md
    ```

3. **Open the HTML File**

    Open `index.html` in your web browser to use the Morse Code Converter.

## Usage

1. **Convert Text to Morse Code**

    - Enter the text you want to convert in the "Enter text" input field.
    - Click the "Convert to Morse Code" button.
    - The converted Morse code will be displayed in the alert box below.
    - Use the "Copy Morse Code" button to copy the Morse code to your clipboard.
    - Use the "Play" button to hear the Morse code as audio.

2. **Convert Morse Code to Text**

    - Enter the Morse code you want to convert in the "Enter Morse code" input field.
    - Click the "Convert to Text" button.
    - The converted text will be displayed in the alert box below.
    - Use the "Copy Text" button to copy the text to your clipboard.

3. **Clear/Refresh**

    - Click the "Clear/Refresh" button to reset the page and clear all input fields and outputs.

## JavaScript File

The `morse.js` file contains the logic for converting text to Morse code and vice versa, as well as playing the Morse code as audio. Here is a brief overview of the functions:

- **convertToMorse(text)**: Converts text to Morse code.
- **convertToText(morseCode)**: Converts Morse code to text.
- **handleConversionToMorse()**: Handles the conversion of text to Morse code and updates the UI.
- **playMorseCode(morseCode)**: Plays the Morse code as audio tones.
- **pauseMorseCode(oscillator)**: Pauses the Morse code audio playback.
- **handleConversionToText()**: Handles the conversion of Morse code to text and updates the UI.
- **copyOutputText(elementId)**: Copies the output text to the clipboard.
- **resetPage()**: Resets the page to clear all inputs and outputs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
