import requests,json
from tkinter import *
from tkinter import  messagebox
root=Tk()
root.title('Weather App')
root.geometry('600x550')
root.config(bg = 'white')
root.wm_iconbitmap("images/icon.ico")
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

def show_flag(flag):
    global img
    if str(flag) == 'NP':
        img = PhotoImage(file='images/nepal.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'IN':
        img = PhotoImage(file='images/india.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'SA':
        img = PhotoImage(file='images/saudi.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'JP':
        img = PhotoImage(file='images/japan.gif')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'AU':
        img = PhotoImage(file='images/australia.png')
        frame4 = Label(root, height=110, width=160, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'LK':
        img = PhotoImage(file='images/srilanka.png')
        frame4 = Label(root, height=110, width=150, image=img, bd=2, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'PK':
        img = PhotoImage(file='images/pakistan.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'US':
        img = PhotoImage(file='images/america.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'GB':
        img = PhotoImage(file='images/england.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)

    elif flag == 'CN':
        img = PhotoImage(file='images/china.png')
        frame4 = Label(root, height=110, width=150, image=img, bg='#34ccff')
        frame4.place(x=20, y=159)
    else:
        img = PhotoImage(file='images/imgload.png')
        frame4 = Label(root, height=110, width=150, image=img,  bg='#34ccff')
        frame4.place(x=20, y=159)
    
def description_image(x):
    global img_des
    # displaying weather in picture
    if x == 'rainy' or x == 'light rain':
        img_des = PhotoImage(file='images/rainy.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'cloudy' or x == 'few clouds' or x == 'broken clouds':
        img_des = PhotoImage(file='images/cloudy.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'sunny' :
        img_des = PhotoImage(file='images/sunny.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'scattered clouds' or x == 'overcast clouds':
        img_des = PhotoImage(file='images/scatterd_clouds.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'clear sky':
        img_des = PhotoImage(file='images/sunny.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'fog' or x == 'smoke':
        img_des = PhotoImage(file='images/smoke.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

    elif x == 'haze' :
        img_des = PhotoImage(file='images/haze.png')
        frame5 = Label(root, image=img_des, bg='#34ccff')
        frame5.place(x=420, y=200)

def show_data():
    frame3.destroy()

    framel = Frame(root, height=450, width=600, bd=2, relief=SUNKEN, bg='#34ccff')
    framel.place(x=0, y=151)

    label1 = Label(root, text = str(city_name) , font = ('Times New Roman',20,'bold'),bg = '#34ccff')
    label1.place(x = 25 , y = 290)

    label2 = Label(root, text=str(feels_like)+ " °C",
                                 font = ('Times New Roman',25,'bold'),bg = '#34ccff')
    label2.place(x=30, y=330)

    label3 = Label(root, text='wind : ' + str(wind) + 'm/s',
                                 font=('Times New Roman', 15, 'bold'), bg='#34ccff')
    label3.place(x=30, y=380)

    label7 = Label(root, text='pressure : ' + str(current_pressure) + " hPa",
                        font=('Times New Roman', 15,'bold') ,bg='#34ccff' )
    label7.place(x=30, y=410)

    label4 = Label(root, text='humidity : '+str(current_humidiy) + "%",bg='#34ccff',
                               font = ('Times New Roman',15,'bold'))
    label4.place(x=30, y=440)

    label5 = Label(root, text=str(weather_description),
                                 bg = '#34ccff',   font = ('Times New Roman',18,'bold'))
    label5.place(x=423, y=345)

    label6 = Label(root,text='latitude/longitude : ' + str(lat)+ " / " + str(lon),
                            bg = '#34ccff'  , font=('Times New Roman', 15,'bold'))
    label6.place(x=30, y=470)

def get_input():
    global weather_description,wind,lon,lat,city_name,feels_like,current_humidiy,current_pressure,flag,sunset,sunrise,complete_url,base_url,api_key
    name = city.get()
    complete_url = base_url + 'appid=' + api_key + '&q=' +name
    #print(complete_url)
    response = requests.get(complete_url)
    x = response.json()
    #print(x)
    if x["cod"] != "404":
        wind = x["wind"]['speed']
        current_pressure = x["main"]['pressure']
        current_humidiy = x['main']["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        city_name=x['name']
        lat = x['coord']['lat']
        lon = x['coord']['lon']
        feels_like =x['main']['feels_like']
        feels_like =int(feels_like-273)
        flag = x['sys']['country']
        sunrise = x['sys']['sunrise']
        sunset = x['sys']['sunset']
        show_data()
        show_flag(flag)
        description_image(weather_description)
       # btn1 = Button(root, text='    Clear    ', font=('New Times Roman', 11, 'bold')
            #          , bg='crimson', fg='white', command=lambda: self.clear())
        #btn1.place(x=220, y=450)StringVar()'

    else:
        messagebox.showerror("Error", "City Not Found \n"
                           "Please enter valid city name")
        e1.delete(0, END)

# if str(self.flag) == 'NP':
 #  logo = PhotoImage(file = 'images/india.png').
   #logo.config(x = 10 , y = 110)
#def flag_paste(self,logo):


root.mainloop()