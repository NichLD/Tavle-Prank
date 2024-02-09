import tkinter as tk
import ctypes
import winsound
import os

backgrounds_path = 'assets/backgrounds'
sounds_path = 'assets/sounds'

app = tk.Tk()
app.title("Background and Sound Controller")
app.geometry("400x600")

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def play_sound(sound_path):
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

for background_file in os.listdir(backgrounds_path):
    full_path = os.path.join(backgrounds_path, background_file)
    btn = tk.Button(app, text=f"Set {background_file}", command=lambda p=full_path: change_wallpaper(p))
    btn.pack(pady=5)

for sound_file in os.listdir(sounds_path):
    full_path = os.path.join(sounds_path, sound_file)
    btn = tk.Button(app, text=f"Play {sound_file}", command=lambda p=full_path: play_sound(p))
    btn.pack(pady=5)

app.mainloop()