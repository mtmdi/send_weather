import requests
from ippanel import Client


def send_sms(text,phonenumber):
    # you api key that generated from panel
    api_key = ""
    # create client instance
    sms = Client(api_key)
    phonenumber = ['98'+str(phonenumber)[1:]]
    bulk_id = sms.send(
    "+98500010706050404",# originator
    phonenumber,    # recipients
    text # message
)


responds = requests.get('https://www.metaweather.com/api/location/2251945/')
time = responds.json()['time']
weather_state = responds.json()['consolidated_weather'][0]['weather_state_name']
humidity = responds.json()['consolidated_weather'][0]['humidity']
the_temp = responds.json()['consolidated_weather'][0]['the_temp']
message = """In Tehran:
time is %s 
humidity is %i percent
the tempreture is %i C 
and the weather status is %s.""" % (time[11:16], humidity, the_temp, weather_state)

send_sms(message,'09120000000')

