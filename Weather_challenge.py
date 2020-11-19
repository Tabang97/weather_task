import requests, json
from tkinter import *
from tkinter import messagebox

weather = Tk()
weather.geometry('400x300')
weather.title('Weather App')
weather.configure(background="black")

#my API key
api_key = "a7570ed5e04e9158d10d20f80d9a6cf4"

#search Function
def details():
    city = site.get()
    if city == '':
        return messagebox.showerror('Error', 'Enter City Name')
    elif api_key == 'your api key':
        return messagebox.showerror('Error', 'Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
    if x["cod"] != "404":

        y = x["main"]
        current_temp = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        temperature = Label(weather, bg="gold", text='Temperature: '+str(round(current_temp-272.15))+' degree celsius').place(x=2, y=90)
        pressure = Label(weather, bg="gold", text='Atmospheric Pressure: '+str(current_pressure)+' hPa').place(x=2, y=120)
        humid = Label(weather, bg="gold", text='Humidity: '+str(current_humidiy)).place(x=2, y=150)
        Describe = Label(weather, bg="gold", text='Description: '+str(weather_description)).place(x=2, y=180)

    else:
        return messagebox.showerror('Error', 'No City Found')



site = StringVar()
#header label
Header = Label(weather, text='Weather App', font='bold', bg="Gold")
Header.grid(row=1, column=2)

#entry & label
City_lbl = Label(weather, text="Enter City:", bg="gold")
City_lbl.grid(row=4, column=1)
City_ent = Entry(weather,  textvariable=site)
City_ent.grid(row=4, column=2)

#search button
search_btn = Button(weather, text="search", bg="gold", command=details)
search_btn.grid(row=4, column=3)


weather.mainloop()
