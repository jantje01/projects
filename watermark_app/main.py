import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import *
import art

screen = tk.Tk()
screen.eval('tk::PlaceWindow . center')
screen.minsize(600,400)
screen.title("Watermark")

header = tk.Label(screen, text="Watermarker").pack()

inputtxt = tk.Text(screen, 
                   height = 5, 
                   width = 20,
                   ).pack()





def get_image():
    filepath = filedialog.askopenfilename()
    print(filepath)

upload_button = ttk.Button(screen, text='Upload Image', command=get_image).pack()
screen.mainloop()