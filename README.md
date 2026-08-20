# Text-to-Speech Generator

A simple Python script that converts written text into spoken audio using Google's Text-to-Speech (gTTS) API.

## Features

- Converts any input string into an `.mp3` audio file
- Uses Google's gTTS engine for natural-sounding speech
- Lightweight — minimal dependencies, easy to run

## Requirements

- Python 3.x
- [gTTS](https://pypi.org/project/gTTS/) library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/lynngatwiri/text-to-speech-generator.git
   cd text-to-speech-generator
   ```

2. Install the required dependency:
   ```bash
   pip install gtts
   ```

## Usage

Run the script:
```bash
python txt-to-speech-generator.py
```

By default, it converts the sample text in the script into speech and saves it as `voice.mp3` in the project folder.

To convert your own text, open `txt-to-speech-generator.py` and edit the `text` variable:
```python
text = "your custom text goes here"
```

Then run the script again — a new `voice.mp3` file will be generated with your custom text.

## Example

```python
from gtts import gTTS

text = "hello everyone welcome to my page"
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("audio saved successfully")
```

## Output

The script generates an `.mp3` file (`voice.mp3`) that can be played with any standard audio player.

## Future Improvements

- Accept text input from the command line or a `.txt` file
- Support multiple languages
- Add a simple GUI or web interface

## License

This project is open source and available for personal or educational use.
