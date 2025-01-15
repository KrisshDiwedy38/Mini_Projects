import requests      #for http requests 
import json          #JSON handling

def coordinates(city):
   coords_base_url = "http://api.openweathermap.org/geo/1.0/direct?"
   coords_url = coords_base_url + "q=" + city + "&appid=c685d8e7aa2a37749ae4648b042defb5"
   coords_data = requests.get(coords_url).json()
   lats,lons = coords_data[0]["lat"],coords_data[0]["lon"]
   return lats, lons


def Weather_info(city):
   base_url = "https://api.openweathermap.org/data/2.5/weather?"
   lats, lons = coordinates(city)
   weather_url = base_url + "lat=" + str(lats) + "&lon=" + str(lons) + "&appid=c685d8e7aa2a37749ae4648b042defb5"
   response = requests.get(weather_url).json()
   weather = response['weather'][0]['main']
   temp = response['main']['temp']
   humi = response['main']['humidity']
   wind_spd = response['wind']['speed']
   return weather, temp, humi, wind_spd
 

def main():
   print("Welcome! Get the weather info for any location in the world.")
   city_name= input("Enter city name: ")
   weather, temp, humidity, wind_spd= Weather_info(city_name)
   print(f"\nWeather: {weather} \nTemperature: {round(temp-273.15,2)} C \nHumidity: {humidity} \nWind Speed: {wind_spd} kmph" )


if __name__ == "__main__":
   main()
