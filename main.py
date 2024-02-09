import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
from features import (
    download_and_convert_audio,
    change_wallpaper,
    play_sound,
    stop_sound
)
import os
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Media Controller")
app.geometry("1000x600")

sounds_path = 'assets/sounds'
backgrounds_path = 'assets/backgrounds'

# Function placeholder
def dummy_function():
    log("Functionality to be implemented")
    print("Functionality to be implemented")

# Function to download and convert audio from YouTube
def download_youtube_audio():
    url = youtube_url_entry.get()
    if url:
        wav_file = download_and_convert_audio(url)
        log(f"Downloaded audio from YouTube: {wav_file}")
    else:
        log("Please enter a YouTube URL.")

# Function to change the wallpaper
def change_wallpaper_handler():
    # Provide the path to the image file
    image_path = 'path_to_image.jpg'
    change_wallpaper(image_path)

# Function to play a sound
def play_sound_handler():
    # Provide the path to the sound file
    sound_path = 'path_to_sound.wav'
    play_sound(sound_path)

# Main Frames
left_frame = ctk.CTkFrame(app)
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

right_frame = ctk.CTkFrame(app)
right_frame.grid(row=0, column=1, sticky="ns", padx=(0, 10), pady=10)

app.grid_columnconfigure(0, weight=5)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Scrollable Frames for Backgrounds and Sounds
def create_scrollable_frame(parent):
    canvas = tk.Canvas(parent)
    scrollbar = ctk.CTkScrollbar(parent, command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

backgrounds_frame = create_scrollable_frame(left_frame)
sounds_frame = create_scrollable_frame(left_frame)

# Function to clear and repopulate the backgrounds frame
def refresh_backgrounds_frame():
    for widget in backgrounds_frame.winfo_children():
        widget.destroy()
    for file in os.listdir(backgrounds_path):
        ctk.CTkButton(backgrounds_frame, text=file, command=dummy_function, corner_radius=8).pack(pady=2, padx=10, fill='x')

# Function to clear and repopulate the sounds frame
def refresh_sounds_frame():
    for widget in sounds_frame.winfo_children():
        widget.destroy()
    for file in os.listdir(sounds_path):
        ctk.CTkButton(sounds_frame, text=file, command=dummy_function, corner_radius=8).pack(pady=2, padx=10, fill='x')

# Function to periodically refresh frames
def poll_folders():
    while True:
        refresh_backgrounds_frame()
        refresh_sounds_frame()
        time.sleep(5)  # Adjust the polling interval as needed

# Populate Backgrounds and Sounds initially
refresh_backgrounds_frame()
refresh_sounds_frame()

# Start polling for folder changes in a separate thread
import threading
threading.Thread(target=poll_folders, daemon=True).start()

# Misc Features Sidebar
ctk.CTkLabel(right_frame, text="Misc Features", anchor="w", padx=10).pack(anchor='nw', pady=(10, 2))
ctk.CTkButton(right_frame, text="Make Background Black", command=change_wallpaper_handler, corner_radius=8).pack(pady=2, fill='x', padx=10)
ctk.CTkButton(right_frame, text="Blank Out Screen", command=dummy_function, corner_radius=8).pack(pady=2, fill='x', padx=10)
ctk.CTkButton(right_frame, text="Panic Button", command=dummy_function, corner_radius=8).pack(pady=2, fill='x', padx=10)
ctk.CTkButton(right_frame, text="Stop Sounds", command=stop_sound, corner_radius=8).pack(pady=2, fill='x', padx=10)

# Download YouTube Audio Section
youtube_download_frame = ctk.CTkFrame(right_frame)
youtube_download_frame.pack(fill='x', padx=10, pady=(20, 0))

youtube_url_entry = ctk.CTkEntry(youtube_download_frame, placeholder_text="Enter YouTube URL")
youtube_url_entry.pack(side='left', padx=(0, 5))

download_button = ctk.CTkButton(youtube_download_frame, text="Download", command=download_youtube_audio, corner_radius=8)
download_button.pack(side='left')

# Logging Area
log_frame = ctk.CTkFrame(app, height=100)
log_frame.grid(row=1, column=0, sticky="new", padx=10)
app.grid_rowconfigure(1, weight=0)

log_text = scrolledtext.ScrolledText(log_frame, height=4)
log_text.pack(expand=True, fill='both', padx=5, pady=5)

def log(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

log("Application started...")

app.mainloop()
