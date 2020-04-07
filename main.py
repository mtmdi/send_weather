import requests

def send_sms(text, phonenumber):
    

response = requests.get('https://www.metaweather.com/api/location/2251945/')
weather_state = response.json()['consolidated_weather'][0]['weather_state_name']
humidity = response.json()['consolidated_weather'][0]['humidity']
the_temp = response.json()['consolidated_weather'][0]['the_temp']

print ('temperature in Tehran now is %i' %the_temp)
print ('and humidity is %i' %humidity)
print ('and the current weather is %s' %weather_state)

