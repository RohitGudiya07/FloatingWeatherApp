from tkinter import *
import requests

def get_weather():
    city = city_entry.get().strip().title()
    api_key = "fa952cf11c0b0b524d045ee9a8967cd7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        result_label.config(text=f"Weather: {weather}\nTemperature: {temp}°C", fg="black")
    else:
        result_label.config(text="City not found!", fg="red")

app = Tk()
app.title("Weather App")
app.geometry("350x220")
app.configure(bg="#87ceeb")  # light sky blue background

# Title Label
Label(app, text="Simple Weather App", font=("Helvetica", 16, "bold"), bg="#87ceeb").pack(pady=10)

# City Input
city_entry = Entry(app, font=("Helvetica", 14), justify='center')
city_entry.pack(pady=8)
city_entry.focus()

# Button
Button(app, text="Get Weather", font=("Helvetica", 12, "bold"), bg="#007acc", fg="white", command=get_weather).pack(pady=10)

# Result Label
result_label = Label(app, text="", font=("Helvetica", 14), bg="#87ceeb")
result_label.pack(pady=10)

app.mainloop()



"""import requests

api_key = "789cc2b89e9744a074261c038814b4ed"

while True:
    print("=== Simple Weather App ===")
    city = input("Enter city name (or type 'exit' to stop): ").strip().title()

    if city.lower() == "exit":
        print("Thank you for using the weather app!")
        break

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print("Weather:", weather.capitalize())
        print("Temperature:", temp, "°C")
        print()
    else:
        print("City not found! Please try again.\n")
"""