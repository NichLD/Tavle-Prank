# features.py

import os
import ctypes
import winsound
from pytube import YouTube
from pydub import AudioSegment
from pydub.playback import play
import os


def change_wallpaper(image_path):
    """Function to change the wallpaper."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def play_sound(sound_path):
    """Function to play a sound."""
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)


def download_and_convert_audio(youtube_url):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'assets', 'sounds')

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(output_path=output_dir)
        mp4_file = audio_file_path
        wav_file = os.path.splitext(audio_file_path)[0] + '.wav'
        sound = AudioSegment.from_file(mp4_file, format='mp4')
        sound.export(wav_file, format='wav')
        os.remove(mp4_file)

        print("Sound file downloaded and converted successfully:", wav_file)  # Print the path of the sound file
        return wav_file
    except Exception as e:
        return str(e)

def stop_sound():
    """Function to stop currently playing sound."""
    play(AudioSegment.silent(duration=100))  # Play silent audio to stop any currently playing sound