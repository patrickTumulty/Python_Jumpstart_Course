import requests
import bs4
import json
import collections


WeatherReport = collections.namedtuple("WeatherReport", "loc, cond, temp, tempHi, tempLo, hum")


def main():
    print_header()
    user_zip_code = input("What zipcode do you want the weather for? (60613)? : ")
    jsonStr = get_json_from_web(user_zip_code)
    report = get_weather_from_json(jsonStr)
    print("\nThe weather in {} is {}.\nThe Current temperature is {} F\nHigh of {} F\nLow of {} F\nWith {}% Humidity".format(
        report.loc,
        report.cond,
        report.temp,
        report.tempHi,
        report.tempLo,
        report.hum
    ))
    print("\n---------------------------------")


def print_header():
    print("---------------------------------")
    print("          WEATHER APP")
    print("---------------------------------\n")


def get_json_from_web(zipCode):
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID=ebd42c362de7ae2d50ac1e01048e5a1d".format(zipCode)
    response = requests.get(url)
    return response.text


def get_weather_from_json(jsonStr):
    j2p = json.loads(jsonStr)
    condition = j2p['weather'][0]['description']
    city_name = j2p['name']
    temp = int(kelvin_to_fahrenheit(j2p['main']['temp']))
    temp_hi = int(kelvin_to_fahrenheit(j2p['main']['temp_max']))
    temp_lo = int(kelvin_to_fahrenheit(j2p['main']['temp_min']))
    humidity = j2p['main']['humidity']
    report = WeatherReport(loc=city_name, cond=condition, temp=temp, tempHi=temp_hi, tempLo=temp_lo, hum=humidity)
    return report


def kelvin_to_fahrenheit(kelvin):
    f = ((kelvin - 273.15) * (9/5)) + 32
    return f

if __name__ == "__main__":
    main()


