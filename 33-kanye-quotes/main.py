
# KANYE
# 1. Make a get() request to the Kanye Rest API
# 2. Raise an exception if the request returned an unsuccessful status code
# 3. Parse the json to obtain the quote text
# 4. Display the quote in the canvas's quote_text widget

from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


get_quote()
window.mainloop()


# ================================
# ISS NOTIFICATION

# from tkinter import *
# import requests
# MY_LAT = 34.057710
# MY_LONG = -118.299800


# # sunrise-sunset.org/api
# my_params = {
#     "lat": MY_LAT,
#     "lng": MY_LONG
# }
# response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0", params=my_params)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise, sunset)