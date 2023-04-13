import tkinter as tk
import PyQt5

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from util import *
from shortcuts import *
import json

class ShortcutsGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Main Menu')

        self.label = tk.Label(self.root, text="Shortcuts", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Start to Translate \nto Braille", font=('Arial', 14), command = self.TranslateToBraille)
        self.btn1.place(x= 100, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Enable Braille Display", font=('Arial', 14), command = self.EnableBrailleDisplay)
        self.btn2.place(x= 350, y = 100, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Toggle Navigation", font=('Arial', 14), command = self.ToggleNavigation)
        self.btn3.place(x= 600, y = 100, height = 100, width = 200)

        self.btn4 = tk.Button(self.root, text="Web Page Analytics", font=('Arial', 14), command = self.WPAnalytics)
        self.btn4.place(x= 100, y = 250, height = 100, width = 200)

        self.btn5 = tk.Button(self.root, text="Index Up", font=('Arial', 14), command = self.IndexUp)
        self.btn5.place(x= 350, y = 250, height = 100, width = 200)

        self.btn6 = tk.Button(self.root, text="Index Down", font=('Arial', 14), command = self.IndexDown)
        self.btn6.place(x= 600, y = 250, height = 100, width = 200)

        self.btn7 = tk.Button(self.root, text="Text to Speech", font=('Arial', 14), command = self.TextToSpeech)
        self.btn7.place(x= 100, y = 400, height = 100, width = 200)

        self.btn8 = tk.Button(self.root, text="Quit Translation", font=('Arial', 14), command = self.QuitTranslation)
        self.btn8.place(x= 350, y = 400, height = 100, width = 200)

        self.btn9 = tk.Button(self.root, text="Start Translation", font=('Arial', 14), command = self.StartTranslation)
        self.btn9.place(x= 600, y = 400, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Settings", font = ('Arial', 12), command = self.ReturnToSettings)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        self.root.mainloop()

    def TranslateToBraille(self):
        print("translate to braille")
    
    def EnableBrailleDisplay(self):
        print("Enable Braille Display")

    def ToggleNavigation(self):
        print("Toggle Navigation")

    def WPAnalytics(self):
        print("Web Page Analytics")

    def IndexUp(self):
        print("Index Up")

    def IndexDown(self):
        print("Index Down")

    def TextToSpeech(self):
        print("Text to Speech")

    def QuitTranslation(self):
        print("Quit Translation")

    def StartTranslation(self):
        print("Start Translation")

    def ReturnToSettings(self):
        self.root.destroy()
        SettingsGUI()

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Main Menu')

        self.label = tk.Label(self.root, text="Main Menu", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Settings", font=('Arial', 14), command = self.OpenSettings)
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Open Browser", font=('Arial', 14), command = self.OpenBrowser)
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Modes", font=('Arial', 14), command = self.OpenModes)
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

        self.root.mainloop()

    def OpenSettings(self):
        self.root.destroy()
        SettingsGUI()

    def OpenModes(self):
        self.root.destroy()
        ModesGUI()

    def OpenBrowser(self):
        print(getBrowserOpen())
        if (getBrowserOpen() == False):
            on_triggered()

class SettingsGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Settings')

        self.label = tk.Label(self.root, text="Settings", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Shortcuts", font=('Arial', 14), command = self.OpenShortcuts)
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Speech Speed", font=('Arial', 14))
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Main Menu", font = ('Arial', 12), command = self.ReturnToMain)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        self.root.mainloop()

    def OpenShortcuts(self):
        self.root.destroy()
        ShortcutsGUI()

    def ReturnToMain(self):
        self.root.destroy()
        MainMenu()

class ModesGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600+10+20")
        self.root.configure(bg='peach puff')
        self.root.title('Modes')

        self.label = tk.Label(self.root, text="Modes", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.btn1 = tk.Button(self.root, text="Assistantive Mode", font=('Arial', 14))
        self.btn1.place(x= 350, y = 100, height = 100, width = 200)

        self.btn2 = tk.Button(self.root, text="Individual Mode\n(Automatic)", font=('Arial', 14))
        self.btn2.place(x= 350, y = 250, height = 100, width = 200)

        self.btn3 = tk.Button(self.root, text="Individual Mode\n(Manual)", font=('Arial', 14))
        self.btn3.place(x= 350, y = 400, height = 100, width = 200)

        self.backBtn = tk.Button(self.root, text = "< Main Menu", font = ('Arial', 12), command = self.ReturnToMain)
        self.backBtn.place(x=10, y=10, height = 50, width = 100)

        self.root.mainloop()


    def ReturnToMain(self):
        self.root.destroy()
        MainMenu()
    