import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x100")

        # initialize pygame mixer
        pygame.mixer.init()

        # create UI elements
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music)
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.load_button.pack()
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()

        # initialize music variables
        self.music_file = None
        self.playing = False
        self.paused = False

    def load_music(self):
        self.music_file = filedialog.askopenfilename(initialdir="/", title="Select Music File",
                                                     filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav")))
        pygame.mixer.music.load(self.music_file)

    def play_music(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False

# create root window and start program
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
