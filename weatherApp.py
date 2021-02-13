import tkinter as tk
import weathercom
from PIL import Image,ImageTk
from pathlib import Path
import requests


# ENTER API KEY HERE
apiKey = "INSERT API KEY HERE"


# Change Image
'''image2 =  ImageTk.PhotoImage(Image.open(currPath / 'sunny.png'))
        labelPhoto.configure(image = image2)
        labelPhoto.image = image2'''



# Gets weather pic name 
weatherPicDict = {
    "Clouds":"cloudy.png",
    "Clear":"sunny.png",
    "Rain":"rainy.png",
    "Snow":"snow.png",
    }

# Gets Weather after hitting enter
def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=" + apiKey
    json_data = requests.get(api).json()

    #Invalid City
    if json_data['cod'] == '404':
        final_info = "Invalid City"
        label1.config(text = "Invalid City")
        label2.config(text = "")

        #Valid City 
    else:
        #Updates Pic otherwise doesn't change (Will make ? icon later)
        if json_data['weather'][0]['main'] in weatherPicDict:
            picIconPath = weatherPicDict[json_data['weather'][0]['main']]
            image2 = ImageTk.PhotoImage(Image.open(currPath / picIconPath ))
            labelPhoto.configure(image = image2)
            labelPhoto.image = image2

        # Gets Location Information
        temp = int(json_data['main']['temp']* 9/5 - 459.67)
        feelsLike = int(json_data['main']['feels_like']*9/5-459.67)
        windSpeed = (json_data['wind']['speed'])

        # Updates labels 
        final_info = str(temp) + "°F"
        feelsLike = str(feelsLike) + "°F"
        windSpeed = str(windSpeed)
        label1.config(text = "Current: " + final_info)
        label2.config(text="Feelslike: " + feelsLike + "\n" + "Wind Speed: " 
        + windSpeed + "mph")


    



# Gets Current Path of working directory and moves into image files folder
currPath = Path.cwd() / 'ImageFiles'

# TKINTER Setup
canvas = tk.Tk()
canvas.resizable(width = False, height= False)
canvas.configure(background = "white")
canvas.geometry("500x500")
canvas.title("Weather App")


f = ("poppins",15,"bold")
t = ("poppins", 35, "bold")

photo = ImageTk.PhotoImage(Image.open(currPath / 'sunny.png'))
labelPhoto = tk.Label(canvas, image=photo)
labelPhoto.configure(background = "white")


textfield = tk.Entry(canvas, font = t,width=15)
textfield.pack(pady = 20);
textfield.focus()
textfield.bind("<Return>", getWeather)
labelPhoto.pack()

label1 = tk.Label(canvas, font = t)
label1.config(text = "Enter a City")
label1.configure(background = "white")
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.configure(background = "white")
label2.pack()

canvas.mainloop()
