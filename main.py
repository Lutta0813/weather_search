import tkinter as tk
import requests


def testfunc(entry):
    print('entry輸入的內容為:', entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# c630f497a26fda294b2d21380429ccf6


def get_weather(city):
    try:
        waether_key = 'c630f497a26fda294b2d21380429ccf6'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': waether_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params)
        weather = response.json()
        label['text'] = format_response(weather)

    except:
        label['text'] = 'Server didnt found your city\'s info,\nPlease check your city name correct'


def format_response(weather):
    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']

    final_str = 'City: %s \nConditions: %s   \nTemperature(°C): %s' % (name, desc, temp)

    return final_str


root = tk.Tk()
root.title('Weather Search')

canvas = tk.Canvas(root, height=500, width=600, bg='#91b2e3')
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

top_frame = tk.Frame(root, bg='#91dee3', bd=5)
top_frame.place(relwidth=0.7, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

entry = tk.Entry(top_frame, fg='pink', font='courier 24')
entry.place(relwidth=0.6, relheight=1)

button = tk.Button(top_frame, text='Search City Weather', fg='blue', bg='gray', command=lambda: get_weather(entry.get()))
button.place(relx=0.65, relwidth=0.35, relheight=1)

bottom_frame = tk.Frame(root, bg='#91dee3', bd=10)
bottom_frame.place(relwidth=0.8, relheight=0.6, relx=0.5, rely=0.25, anchor='n')

label = tk.Label(bottom_frame, bg='#fcf6b3', font='courier 18', anchor='nw', justify='left', bd=5 )
label.place(relwidth=1, relheight=1)


root.mainloop()
