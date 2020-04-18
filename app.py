import os
import tkinter as tk
from tkinter import filedialog
import pygame
import time


music_file_path = ''

def main():
    root = tk.Tk()
    root.title('SNot')
    root.geometry("600x400")

    number_label = tk.Label(text="the number of replay")
    number_label.place(x=30, y=10)

    number_text = tk.Entry(width=20)
    number_text.place(x=30, y=40)

    music_path_label = tk.Label(text='PATH: MusicFIle Path')
    music_path_label.place(x=30, y=120)

    select_file_button = tk.Button(root, text='Slect MusicFile', command=lambda: file_select(music_path_label))
    select_file_button.place(x=30, y=90)


    play_button = tk.Button(root, text='PLAY', command=lambda: play_music(count=int(number_text.get()) ) )
    play_button.place(x=300, y=300)

    root.mainloop()

def play_music(count):
    global music_file_path
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play(count)
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.stop()
    print('end')

def file_select(label):
    global music_file_path
    user_name = os.getlogin()
    idir = 'c:/Users/' + user_name + '/Music/iTunes/iTunes Media/Music'
    filetype = [("all", "*")]
    file_path = filedialog.askopenfilename(filetypes=filetype, initialdir=idir)
    label['text'] = 'PATH: ' + file_path
    music_file_path = file_path



if __name__ == '__main__':
    main()