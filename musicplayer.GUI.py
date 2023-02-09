"""
1/13/2023

GUI-based version of the Python music player app where a Play, Pause, and Resume button are all built in with a nice MP3 png file to make it look more authentic


NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

ALSO NOTE: you MUST install the pygame package by running: pip install game
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from pygame import mixer
from tkinter import PhotoImage

# other imports can go here

class MusicPlayerGUI(EasyFrame):


    # definition of the __init__() method which is our class constructor
    def __init__(self):
        # call the EasyFrame constructor method
        EasyFrame.__init__(sself, title = "Music Player GUI", background = "black", resizable = False)
        self.addLabel(text = "Python Music Player", row = 0, column = 0, columspan = 3, background = "black", foreground = "orange", sticky = "NSEW", font = Font(famiy = "Impact", size = 28)
        # create a variable and add a label for our image
        self.imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 3, sticky = "NSEW", background = "black"
        # load the image into imageLabel object
        self.image = PhotoImage(file = "music_player.png")
        self.imageLabel["image"] = self.image


        #label, text field and button to load music file
        self.addLabel(text = "Enter a music file name to load:",
                row = 2, column = 0, background = "black", foreground = "orange", sticky = "NE")
        self.musicFile = self.addTextField(text = "", row = 2, column = 1, width = 35)
        self.addButton(text = "Load Song", row = 2, column = 2, command = self.loadFile)

        # 3 buttons for the music player functions
        self.playButton = self.addButton(text = "Play", row = 3, column = 0, state = "disabled", command = self.playMusic)
        self.pauseButton = self.addButton(text = "Pause", row = 3, column = 1, state = "disabled", command = self.pauseButton)
        self.resumeButton = self.addButton(text = "Resume", row = 3, column = 2, state = "disabled", command = self.resumeMusic)

        # Event handling functions for the command buttons
        def loadFile(self):
                # initialize the pygame mixer
                mixer.init()
                songFile = self.musicFile.getText()
                mixer.musuc.load(songFile)
                self.playButton["state"] = "normal"
                mixer.music.play()

        def playMusic(self):
                # play the loaded music file
                mixer.music.play()
                self.pauseButton["state"] = "normal"

        def pauseButton(self):
                 # pause the current song
                 mixer.music.pause()
                 self.resumeButton["state"] = "normal"
                 self.pauseButton["state"] = "disabled"

        def resumeMusic(self)
                 mixer.music.unpause()
                 self.resumeButton["state"] = "disabled"
                 self.pauseButton["state"] = "normal"



    # defintion of the main() method which will establish class objects
    def main():
            # instantiate an object from the class into mainloop()
            MusicPlayerGUI().mainloop()

    # global call to the main() method
    main()
                            

