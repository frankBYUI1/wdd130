'''
- Full Name: Francesco Lezano
- Teacher: Bro. Codling
- Title: music_player.py
- Number of hours that I worked on this project: seven hours
- A list of the documentation that you read, the videos that 
  you watched, and the coding experiments that you tried:
  + Python GUI Tkinter (geeksforgeeks.org)
  + Cool fonts for tkinter code
  + Introduction to tkinter stringvar 
  + tkinter pack geometry manager
  + how to get started with tkinter on a mac (video)
  + tkinter (GUI Programming, pythonbasics.org)
  + Methods in tkinter (geeksforgeeks.org)
- A description or list of the work that you finished on your program:
  This is a really basic program of a music player that let the user interact with 
  songs that are already on a music folder created by the user. This program help 
  the user to have a free widget that actually plays any song or audio file that 
  the user feels free to choose. It performs a real world task and the most important
  it is completely free.
'''

import pygame
import tkinter as tk # Import the tkinter widgets
from tkinter.filedialog import askdirectory # To open the directory 
import os # To interact with the operating system

music_player = tk.Tk()

# Super creative tittle to this work
music_player.title("Music Player Version 1")

# Dimensions of the box of the music_player
music_player.geometry("500x350")

# To select a folder and save the path
directory = askdirectory()

# Method to change the current working directory to specified path
os.chdir(directory)

# Method to get the list of all files and directories 
song_list = os.listdir()

play_list = tk.Listbox(music_player, font="Helvetica 12 bold", bg='black', selectmode=tk.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

#Initialize Pygame Mixer
pygame.init()
pygame.mixer.init() 

# Create player control buttons:
# Play selected song
def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

# Stop playing current song
def stop():
    pygame.mixer.music.stop()

# Pause song
def pause():
    pygame.mixer.music.pause()

# Unpause song
def unpause():
    pygame.mixer.music.unpause()
Button1 = tk.Button(music_player, width=5, height=3, font="Helvetica 14 bold", text="PLAY", command=play, bg="gray", fg="green")
Button2 = tk.Button(music_player, width=5, height=3, font="Helvetica 14 bold", text="STOP", command=stop, bg="gray", fg="red")
Button3 = tk.Button(music_player, width=5, height=3, font="Helvetica 14 bold", text="PAUSE", command=pause, bg="gray", fg="yellow")
Button4 = tk.Button(music_player, width=5, height=3, font="Helvetica 14 bold", text="UNPAUSE", command=unpause, bg="gray", fg="brown")

# Class from tkinter to analize changes to variables if they occur
var = tk.StringVar() 
song_title = tk.Label(music_player, font="Helvetica 12 bold", textvariable=var)

# Packs all the widgets one after the other in a window
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

music_player.mainloop()