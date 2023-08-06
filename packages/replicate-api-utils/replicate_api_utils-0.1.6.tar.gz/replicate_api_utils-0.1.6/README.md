# Replicate API Utils
This is a Python package for accessing the Replicate API, including various tools for data processing and management.

## Installation
To install, use pip:

```
pip install replicate-api-utils
```

## Usage
The package includes several command line interfaces (CLIs) that can be accessed from the command line. Here are the available CLIs:

whisper: transcribes audio to text using the Replicate API
stable-diffusion: creates a dataset with stable diffusion
### Whisper
To transcribe an audio file using the Replicate API, use the whisper CLI.

```
whisper transcribe /path/to/audio.wav
whisper transcribe /path/to/dir --to /path/to/dir2
```
This will transcribe the audio file and print the text to the console. The CLI includes several additional parameters for controlling the transcription, such as the output destination, format and language.


## Contributing
If you encounter a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome!