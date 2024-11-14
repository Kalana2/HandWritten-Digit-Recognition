import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt
import cv2
import joblib


height = 800
width = 800
count = 0


# main Window
window = tk.Tk()

# image
image = Image.new("RGB", (width, height), (0, 0, 0))
imageDraw = ImageDraw.Draw(image)

model = joblib.load("KNN-digit_recongnition.sav")

def eventFunction(point):
    x1 = point.x - 45
    x2 = point.x + 45
    y1 = point.y -
    y2 = point.y + 45

    canvas.create_oval((x1, y1, x2, y2), fill="green2", outline="")
    imageDraw.ellipse((x1, y1, x2, y2), fill="white")
    

def save():

    global count

    imageArry = np.array(image)
    plt.imshow(imageArry)
    cv2.imwrite(f"./images/image{count}.png",imageArry)
    count+=1
    # plt.show()
    return



def clear():
    canvas.delete("all")
    global image, imageDraw
    image = Image.new("RGB", (width, height), (0, 0, 0))
    imageDraw = ImageDraw.Draw(image)


def predict(): 

    imageArry = np.array(image)
    imageArry = cv2.cvtColor(imageArry, cv2.COLOR_RGB2GRAY)

    contours, _ = cv2.findContours(imageArry, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0]) 
        imageArry = imageArry[y:y+h, x:x+w]

    imageArry = cv2.resize(imageArry, (8, 8), interpolation=cv2.INTER_AREA)
    imageArry = (imageArry / 255.0)*15

    imageArry = imageArry.reshape(1, -1)# (1, 64)
    

    predictedTarget = model.predict(imageArry)
    # print(predictedTarget)

    predictedVlaue.config(text="Predicted Digit : " + str(predictedTarget) )
    

canvas = tk.Canvas(window, width=width, height=height, bg='gray12')
canvas.grid(row=1, column=0, columnspan=4)
canvas.bind("<B1-Motion>", eventFunction)

buttonSave = tk.Button(window, text='Save', bg="DodgerBlue2", fg="white", command=save)
buttonSave.grid(row=2, column=0)

buttonPredict = tk.Button(window, text='Predict', bg="DodgerBlue2", fg="white", command=predict)
buttonPredict.grid(row=2, column=1)

buttonClear = tk.Button(window, text='Clear', bg="DodgerBlue2", fg="white", command=clear)
buttonClear.grid(row=2, column=2)

buttonExit = tk.Button(window, text='Exit', bg="red3", fg="white", command=window.destroy)
buttonExit.grid(row=2, column=3)

predictedVlaue = tk.Label(window, text="Predicted Digit : ")
predictedVlaue.grid(row=0)

window.mainloop()


