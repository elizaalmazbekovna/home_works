from  pyowm.owm import  OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('0f4d8f479115fbba75256ce61d8828ee')
place=input("Введите название города:  ")
mgr = owm.weather_manager()

observation=mgr.weather_at_place(place)

w = observation.weather
t=w.temperature()
t1=t['temp']
t2=t['feels_like']
t3=t['temp_max']
t4=t['temp_min']

st=w.status                   #статус
dt=w.detailed_status         # 'clouds'
wi=w.wind()['speed']                  # {'speed': 4.6, 'deg': 330}
humi=w.humidity                # 87  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
ra=w.rain                    # {}             # None
cl=w.clouds

print(f"И город: {place} температура: {t1}, ощущается как: {t2} ,максимальная: {t3} минимальная: {t4}\n"
      f"статус: {st}, детайлы: {dt}, скорость ветра: {wi},\n ,влажность: {humi} облачность: {cl} ,"
      f" дождливость: {ra}\n")
