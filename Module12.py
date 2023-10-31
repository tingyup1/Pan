#1
import requests
url='https://api.chucknorris.io/jokes/random'
response = requests.get(url)
str = response.json()
print(str)
print(str['value'])

#2
import requests

def kelvin_to_celsius(kelvin):
     return kelvin-273.15
def print_infor():
    api_key=''
    url='https://api.openweathermap.org/data/3.0/onecall?'

municipality=input("Enter the name of a city:")
data={'q':municipality,'appid': api_key}

try:
    response=requests.get(url,data)
    str=response.json()

    if str['code']==200:
        weather_description=str['weather']['description']
        temperature_kelvin = str['temp']
        temperature_celsius=kelvin_to_celsius(temperature_kelvin)
        print(f'Weather in {municipality}:{weather_description}')
        print(f'Temperature:{temperature_celsius:.2f}c')
    else:
        print(f"Error:{str['message']}")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

print_infor()
