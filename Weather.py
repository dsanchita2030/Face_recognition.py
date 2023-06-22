import requests
from bs4 import BeautifulSoup
from voice import *

def fetch(city):

    try:

            # enter city name

            # creating url and requests instance
            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content

            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

            # formatting data
            data = str.split('\n')
            time = data[0]
            sky = data[1]

            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text

            # getting other required data
            pos = strd.find('Wind')
            # other_data = strd[pos:]

            speak(f"{city} current temperature is {temp} ")
            speak(f"current  sky condition is {sky} ")
            speak(f"current  wind speed is {pos} ")
            sky = sky.lower()
            if 'rain' in sky:
                  speak('hey! sky condition is Rainy, Please use umbrella.')

            if 'light rain showers ' in sky:
                  speak('hey! sky condition is Rainy, Please carry umbrella.')

            elif 'cloudy' in sky:
                  speak('hey! sky condition is Cloudy, Please carry umbrella.')

            elif 'thunderstorms and rain' in sky:
                  speak('attention! sky condition is very bad, Please do not go this place.')



    except:
        speak("sorry! i couldn't find your city")
        pass

def weather():
    speak("Which city you want?")
    city = takecommand()
    if "none" in city:
        speak("i couldn't understand, write Which city you want?")
        city = input()
        fetch(city)
    else:
        speak(f"you want to {city} weather report?")
        ans = takecommand()
        if "yes" in ans:
            fetch(city)
        else:
            speak("write Which city you want?")
            city = input()
            fetch(city)



fetch("Ashoknagar")