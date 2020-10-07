from fastapi import FastAPI
from starlette.responses import RedirectResponse
from ratelimit import limits
import sys
import uvicorn
import requests
import json
import config

ONE_MINUTE = 60

app = FastAPI(title='Spraying conditions API',
              description='API for real-time analysis of climatic conditions generating the result whether they are suitable or not for agricultural spraying.')


@app.get("/")
async def docs():
    response = RedirectResponse(url='/docs')
    return response


@limits(calls=30, period=ONE_MINUTE)
@app.get("/spray/condition")
async def check_spray_condition(city: str):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pt&appid={config.OWM_KEY}')

        wheather_info = json.loads(response.text)
        description = wheather_info['weather'][0]['main']
        temperature = int(wheather_info['main']['temp'])
        feels_like = int(wheather_info['main']['feels_like'])
        humidity = int(wheather_info['main']['humidity'])
        wind = int(wheather_info['wind']['speed'])*3.6
        spray_condition = ''

        bad_conditions = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow']

        if (description not in bad_conditions) and (10 < temperature < 30) and (10 < feels_like < 30) and (humidity > 50) and (3 < wind < 10):
            spray_condition = 'Good weather conditions for spraying'
        else:
            if description in bad_conditions:
                spray_condition = f'Bad weather conditions for spraying: {description}'
            elif (temperature > 30) and (feels_like > 30) and (humidity > 50) and (3 < wind < 10):
                spray_condition = f'Bad weather conditions: {temperature} °C is too hot for spraying'
            elif (temperature <= 10) and (feels_like <= 10) and (humidity > 50) and (3 < wind < 10):
                spray_condition = f'Bad weather conditions: {temperature} °C is too cold for spraying'
            elif (temperature < 30) and (feels_like < 30) and (humidity < 50) and (3 < wind < 10):
                spray_condition = f'Bad weather conditions: {humidity} % air humidity. It is below that recommended for spraying'
            elif (temperature < 30) and (feels_like < 30) and (humidity > 50) and (wind < 3):
                spray_condition = f'Bad weather conditions: The wind speed of {wind} km/h is very low and not recommended for spraying'
            elif (temperature < 30) and (feels_like < 30) and (humidity > 50) and (wind > 10):
                spray_condition = f'Bad weather conditions: The wind speed of {wind} km/h is above the recommended and can cause drift.'
            else:
                spray_condition = 'Bad weather conditions for spraying'
        
        
        result = ({'city': city,
                   'description': description,
                   'temperature': f'{temperature} °C',
                   'feels_like': f'{feels_like} °C',
                   'humidity': f'{humidity} %',
                   'wind': f'{wind} km/h',
                   'spray_condition': spray_condition})
        return result
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
