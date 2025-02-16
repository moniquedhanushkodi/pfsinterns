#Purpose: Generate a weather report with user inputted city
#Used: API, json, GUI, 
#Created By: Monique Priyan Dhanushkodi
#Created On: February 16 2025


import requests, json
import tkinter as tk

#GUI

window = tk.Tk()
window.title("Weather Report App")
window.geometry("800x500")

def show_report():
    apiKey = "ccef1de474f1f36ab8728dcc92c0e2cc"
    baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
    fullURL = baseURL + city_entry.get() + "&appid=" + apiKey
    report = requests.get(fullURL)
    data = report.json()

    city_label =  tk.Label(window, text="City: " + city_entry.get())
    city_label.place(x=275, y=100)

    weather_label =  tk.Label(window, text="Weather: " + data["weather"][0]["main"])
    weather_label.place(x=275, y=150)

    desc_label =  tk.Label(window, text="Weather Description: " + data["weather"][0]["description"])
    desc_label.place(x=275, y=200)
    
    temp = int((data["main"]["temp"] - 273.15) * (9/5) + 32)
    temp_label =  tk.Label(window, text="Temperature: " + str(temp) + " Degrees Farenheight")
    temp_label.place(x=275, y=250)

    wind_label =  tk.Label(window, text="Wind Speed: " + str(data["wind"]["speed"]) + " mph")
    wind_label.place(x=275, y=300)

    humidity_label =  tk.Label(window, text="Humidity: " + str(data["main"]["humidity"]) + "%")
    humidity_label.place(x=275, y=350)




label_enter_city = tk.Label(window, text="Enter City Location for Weather Report: ")
label_enter_city.place(x=20, y=40)

city_entry = tk.Entry(window, width=30)
city_entry.place(x=275, y=40)

entry_button = tk.Button(window, text="Search", command=show_report)
entry_button.place(x=575, y=40)


#print(data["weather"][0]["description"], data["main"]["temp"])
window.mainloop()
