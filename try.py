import  requests,json
from tkinter import *
from tkinter import  messagebox
root=Tk()
root.title('Weather App')
root.geometry('600x550')
root.config(bg = 'white')
root.resizable(0,0)
api_key = 'fcf5a2b2e92818d83f5196ee2e58770b'
city = StringVar()
city_name = StringVar()
base_url = "http://api.openweathermap.org/data/2.5/weather?"
wind = StringVar()
current_humidiy = StringVar()
current_pressure =StringVar()
weather_description =StringVar()
lat = StringVar()
lon = StringVar()
feels_like = StringVar()
flag = StringVar()
img = StringVar()
img_des = StringVar()
sunrise = StringVar()
sunset = StringVar()

def userText(event):
   # print(type(self.lon))
    e1.delete(0,END)

frame1 = Frame(root , height = 70 , width = 600 , bd = 2 , relief = SUNKEN,bg = 'white' )
frame1.pack()
label1 = Label(frame1,text = 'Weather Forecast...',font = ('Helvetica',25,'bold'),fg = 'red',bg = 'white')
label1.place(x = 5 , y = 18)
frame2 = Frame(root , height = 80 , width = 600 , bd = 2 , relief = SUNKEN,bg = '#ee8841' ).place(x = 0 , y = 71)
e1 = Entry(frame2,textvariable = city , font = ('New Courier',13,'bold'),bd = 5 , relief = GROOVE,width = 25 )
e1.place(x = 95 , y = 97)

e1.insert(0, "Your City Name")
e1.bind("<Button>",userText)

btn1 = Button(root , text = '? Search' , font = ('New Times Roman',11,'bold')
             ,bg = 'crimson',fg = 'white',command = lambda :get_input())
btn1.place(x = 350 , y = 96)

frame3 = Frame(root, height=450, width=600, bd=2, relief=SUNKEN, bg='#34ccff')
frame3.place(x=0, y=151)

def get_input():
    global weather_description,wind,lon,lat,feels_like,current_humidiy,current_pressure,flag,sunset,sunrise,complete_url,base_url,api_key
    name = city.get()
    complete_url = base_url + 'appid=' + api_key + '&q=' +name
    #print(complete_url)
    response = requests.get(complete_url)
    x = response.json()
    print(x)
    if x["cod"] != "404":
        wind = x["wind"]['speed']
        current_pressure = x["main"]['pressure']
        current_humidiy = x['main']["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        lat = x['coord']['lat']
        lon = x['coord']['lon']
        feels_like =x['main']['feels_like']
        feels_like =int(feels_like-273)
        flag = x['sys']['country']
        sunrise = x['sys']['sunrise']
        sunset = x['sys']['sunset']
        show_data()
        show_flag()
        description_image()
       # btn1 = Button(root, text='    Clear    ', font=('New Times Roman', 11, 'bold')
            #          , bg='crimson', fg='white', command=lambda: self.clear())
        #btn1.place(x=220, y=450)'''

    else:
        messagebox.showerror("Error", "City Not Found \n"
                           "Please enter valid city name")
        e1.delete(0, END)

def show_data():
    global weather_description,wind,lon,lat,feels_like,current_humidiy,current_pressure,flag,sunset,sunrise
    label1 = Label(frame3, text = str(city_name) , font = ('Times New Roman',20,'bold'),bg = '#34ccff')
    label1.place(x = 25 , y = 290)

    label2 = Label(frame3, text=str(feels_like)+ " °C",
                                 font = ('Times New Roman',25,'bold'),bg = '#34ccff')
    label2.place(x=30, y=330)

    label3 = Label(frame3, text='wind : ' + str(wind) + 'm/s',
                                 font=('Times New Roman', 15, 'bold'), bg='#34ccff')
    label3.place(x=30, y=380)

    label7 = Label(frame3, text='pressure : ' + str(current_pressure) + " hPa",
                        font=('Times New Roman', 15,'bold') ,bg='#34ccff' )
    label7.place(x=30, y=410)

    label4 = Label(frame3, text='humidity : '+str(current_humidiy) + "%",bg='#34ccff',
                               font = ('Times New Roman',15,'bold'))
    label4.place(x=30, y=440)

    label5 = Label(frame3, text=str(weather_description),
                                 bg = '#34ccff',   font = ('Times New Roman',18,'bold'))
    label5.place(x=423, y=345)

    label6 = Label(frame3,text='latitude/longitude : ' + str(lat)+ " / " + str(lon),
                            bg = '#34ccff'  , font=('Times New Roman', 15,'bold'))
    label6.place(x=30, y=470)


root.mainloop()