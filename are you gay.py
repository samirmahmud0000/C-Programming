import tkinter as tk  # Correct import for tkinter
from tkinter import messagebox  # Import messagebox correctly
import random

def no():
    
    messagebox.showinfo(' ', 'Thanks Bro')
    root.quit()  # Corrected from quit() to root.quit()

def motionMouse(event):
    
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = tk.Tk()
root.geometry('600x600')  # Corrected the '*' to 'x'
root.title('Survey')
root.resizable(width=False, height=False)
root.configure(bg='white')  # Corrected setting the background color

# Add a label to the window
label = tk.Label(root, text='Are you- gay ?', font='Arial 20 bold', bg='white')
label.pack()


btnYes = tk.Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)


btnNo = tk.Button(root, text='Yes', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)


root.mainloop()
