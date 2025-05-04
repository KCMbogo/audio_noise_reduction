import noisereduce as nr
import librosa
import soundfile as sf

def noise_reduction(audio_path, save_cleaned_audio_path):
    """Reduce background noise from audio
    
    Description:
    This is a simple function that takes an audio file with background noises, 
    removes the background noises and saves the new cleaned audio in a specified
    path

    Parameters:
    audio_path (str): The path to the audio file 
    save_cleaned_audio_path (str): The path to save the cleaned audion, also specify the name the file to be saved as

    Example:
    noise_reduction("noisy_audio/example.mp3", "cleaned/clean_audio.mp3")

    NOTE:
    save_cleaned_audio_path will not create the directory if it does not exist, it will raise an error
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Reduce noise
    reduced_noise = nr.reduce_noise(y=y, sr=sr)

    # Save output
    sf.write(save_cleaned_audio_path, reduced_noise, sr)
