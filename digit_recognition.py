import tkinter as tk

height = 800
width = 500

# main Window
window = tk.Tk()

canvas = tk.Canvas(window, width=width, height=height, bg='gray12')
canvas.grid(row=0, column=0, columnspan=4)

buttonSave = tk.Button(window, text='Save', bg="DodgerBlue2", fg="white")
buttonSave.grid(row=1, column=0)

buttonSave = tk.Button(window, text='Predict', bg="DodgerBlue2", fg="white")
buttonSave.grid(row=1, column=1)

buttonSave = tk.Button(window, text='Clear', bg="DodgerBlue2", fg="white")
buttonSave.grid(row=1, column=2)

buttonSave = tk.Button(window, text='Exit', bg="red3", fg="white")
buttonSave.grid(row=1, column=3)


window.mainloop()