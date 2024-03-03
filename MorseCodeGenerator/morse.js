<script>
// Define Morse code mappings
const morseCodeMap = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
};

// Reverse Morse code mappings to convert from Morse to text
const reverseMorseCodeMap = Object.fromEntries(
    Object.entries(morseCodeMap).map(([key, value]) => [value, key])
);

// Function to convert text to Morse code
function convertToMorse(text) {
    return text.toUpperCase().split('').map(char => morseCodeMap[char] || '').join(' ');
}

// Function to convert Morse code to text
function convertToText(morseCode) {
    return morseCode.split(' ').map(code => reverseMorseCodeMap[code] || '').join('');
}

// Function to handle conversion to Morse code
function handleConversionToMorse() {
    const inputText = document.getElementById('inputText').value;
    const morseCode = convertToMorse(inputText);
    document.getElementById('outputMorse').textContent = morseCode;
    document.getElementById('outputMorse').style.display = 'block'; // Show the alert
    document.getElementById('copyMorseButton').style.display = 'block'; // Show the copy button
    document.getElementById('playMorseButton').style.display = 'block'; // Show the play button
    document.getElementById('playMorseButton').textContent = 'Play';
    document.getElementById('playMorseButton').onclick = () => playMorseCode(morseCode);
}

// Function to play Morse code as tones
function playMorseCode(morseCode) {
    const audioContext = new AudioContext();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);

    const dotDuration = 100; // Duration of a dot (in milliseconds)
    const dashDuration = dotDuration * 3; // Duration of a dash (in milliseconds)
    const interSymbolDelay = dotDuration; // Delay between symbols (in milliseconds)
    const interCharacterDelay = dotDuration * 3; // Delay between characters (in milliseconds)

    let time = audioContext.currentTime;

    for (const symbol of morseCode) {
        switch (symbol) {
            case '.':
                oscillator.frequency.setValueAtTime(1000, time);
                gainNode.gain.setValueAtTime(1, time);
                time += dotDuration / 1000;
                gainNode.gain.setValueAtTime(0, time);
                break;
            case '-':
                oscillator.frequency.setValueAtTime(1000, time);
                gainNode.gain.setValueAtTime(1, time);
                time += dashDuration / 1000;
                gainNode.gain.setValueAtTime(0, time);
                break;
            case ' ':
                time += interCharacterDelay / 1000;
                break;
        }
        time += interSymbolDelay / 1000;
    }

    oscillator.start();
    oscillator.stop(time);

    // Change button text to "Playing"
    const playButton = document.getElementById('playMorseButton');
    playButton.textContent = 'Playing';
    playButton.onclick = () => pauseMorseCode(oscillator);
}

// Function to pause Morse code tones
function pauseMorseCode(oscillator) {
    oscillator.stop();
    const playButton = document.getElementById('playMorseButton');
    playButton.textContent = 'Play';
    playButton.onclick = () => playMorseCode(oscillator);
}

// Function to handle conversion to text
function handleConversionToText() {
    const inputMorse = document.getElementById('inputMorse').value;
    const text = convertToText(inputMorse);
    document.getElementById('outputText').textContent = text;
    document.getElementById('outputText').style.display = 'block'; // Show the alert
    document.getElementById('copyTextButton').style.display = 'block'; // Show the copy button
}

// Function to copy the output text
function copyOutputText(elementId) {
    const outputElement = document.getElementById(elementId);
    const textToCopy = outputElement.textContent;
    navigator.clipboard.writeText(textToCopy.trim()) // Trim to remove leading/trailing spaces
        .then(() => {
            alert('Text copied to clipboard');
        })
        .catch(err => {
            console.error('Failed to copy text: ', err);
        });
}

// Function to reset the page
function resetPage() {
    location.reload();
}
</script>
