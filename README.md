# Audio Noise Reduction using `noisereduce`

## Overview

This Python script performs **background noise reduction** on an audio file, using the `noisereduce` library. It is especially effective for **constant background noises**, such as **fan hums**, **air conditioning noise**, or other consistent environmental sounds that tend to mask the clarity of speech in audio recordings.

This method is **best suited** for reducing unwanted noise from audio recordings with a stable, non-varying sound profile (e.g., fan, static, hum).

## Features
- **Noise reduction**: Removes background noise while maintaining audio quality.
- **Easy to use**: Simply provide an audio file and run the script.
- **Offline**: No internet required, as all processing happens locally.
- **Customizable**: You can modify the script to fit specific audio characteristics.
- **Fast**: Performs noise reduction quickly for short and medium-length audio.

## Requirements

Before running the script, make sure to install the required dependencies.

### Dependencies

- `noisereduce`: Main library for performing noise reduction
- `librosa`: For audio loading and manipulation
- `soundfile`: To save the processed output audio
- `numpy`: Underlying library for numerical operations

You can install these dependencies using `pip`:

```bash
pip install noisereduce librosa soundfile numpy
