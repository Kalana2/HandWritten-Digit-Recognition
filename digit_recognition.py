import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt
import cs2

height = 500
width = 500

# main Window
window = tk.Tk()

# image
image = Image.new("RGB", (width, height), (0, 0, 0))
imageDraw = ImageDraw.Draw(image)

def eventFunction(point):
    x1 = point.x - 20
    x2 = point.x + 20
    y1 = point.y - 20
    y2 = point.y + 20

    canvas.create_oval((x1, y1, x2, y2), fill="green2", outline="")
    imageDraw.ellipse((x1, y1, x2, y2), fill="white")
    

def save():
    imageArry = np.array(image)
    plt.imshow(imageArry)
    plt.show()



canvas = tk.Canvas(window, width=width, height=height, bg='gray12')
canvas.grid(row=1, column=0, columnspan=4)
canvas.bind("<B1-Motion>", eventFunction)

buttonSave = tk.Button(window, text='Save', bg="DodgerBlue2", fg="white", command=save)
buttonSave.grid(row=2, column=0)

buttonSave = tk.Button(window, text='Predict', bg="DodgerBlue2", fg="white")
buttonSave.grid(row=2, column=1)

buttonSave = tk.Button(window, text='Clear', bg="DodgerBlue2", fg="white")
buttonSave.grid(row=2, column=2)

buttonSave = tk.Button(window, text='Exit', bg="red3", fg="white")
buttonSave.grid(row=2, column=3)

predictedVlaue = tk.Label(window, text="Predicted Digit : ")
predictedVlaue.grid(row=0)

window.mainloop()


