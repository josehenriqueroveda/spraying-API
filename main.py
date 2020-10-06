from fastapi import FastAPI
from starlette.responses import RedirectResponse
from ratelimit import limits
import requests
import json

ONE_MINUTE = 60
OWM_KEY = '6827dd5e08e4eae1f63be6155c0a6315'

app = FastAPI(title='Spraying conditions API', description='API for real-time analysis of climatic conditions generating the result whether they are suitable or not for agricultural spraying.')



@app.get("/")
async def docs():
    response = RedirectResponse(url='/docs')
    return response


@limits(calls=30, period=ONE_MINUTE)
@app.get("/spray/condition")
async def check_spray_condition(city: str):
    try:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pt&appid={OWM_KEY}')

        wheather_info = json.loads(response.text)
        description = wheather_info['weather'][0]['main']
        temperature = int(wheather_info['main']['temp'])
        feels_like = int(wheather_info['main']['feels_like'])
        humidity = int(wheather_info['main']['humidity'])
        wind = int(wheather_info['wind']['speed'])*3.6

        bad_conditions = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow']

        if description not in bad_conditions and (temperature < 30 and feels_like < 30 and humidity > 50 and 3 < wind < 10):
            spray_condition = 'Good weather conditions for spraying'
        else:
            spray_condition = 'Bad weather conditions for spraying'

        return {'city': city,
                'description': description,
                'temperature': f'{temperature}°C',
                'feels_like': f'{feels_like}°C',
                'humidity': f'{humidity}%',
                'wind': f'{wind}km/h',
                'spray_condition': spray_condition}
    except:
        pass