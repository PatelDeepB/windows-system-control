# #Import the required libraries
# from tkinter import *

# #Create an instance of tkinter frame
# win= Tk()
# #Get the current screen width and height
# screen_width = win.winfo_screenwidth()
# screen_height = win.winfo_screenheight()

# #Print the screen size
# print("Screen width:", screen_width)
# print("Screen height:", screen_height)
from screeninfo import get_monitors
for m in get_monitors():
    print(str(m.height))