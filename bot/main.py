import requests
import emoji
from bot.credentials import API_KEY

kelvin_degree_dif = 273.15

emoj = { "Thunderstorm": ":zap:","Drizzle":":snowflake:","Rain":":umbrella:","Snow":":snowflake:","Clear":":sunny:","Clouds":":cloud:"}
def configurate_answer(msg,response):
    temp = int(round(response["main"]["temp"] - kelvin_degree_dif))
    temp_feels_like = int(round(response["main"]["feels_like"] - kelvin_degree_dif))
    weather = response["weather"][0]["main"]
    answer = "{}, давайте посмотрим. На улице сейчас {} градусов, ощущается как {}".format(msg,temp,temp_feels_like)
    if weather in emoj:
        answer += ". На небе " + emoji.emojize(emoj[weather], use_aliases=True)
    return answer

def get_response(msg):
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    city_name = msg
    try:
        response = requests.get(
            URL,
            params={'q': city_name, "appid":API_KEY},
        )
        answer = configurate_answer(msg,response.json())
    except:
        answer = "Я не знаю такого города или что-то пошло не так. Давайте попорбуем ещё раз"

    print(answer)
    return answer
