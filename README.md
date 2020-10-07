# 🌱 Spraying API 

## 🚜 What is the importance of spraying in agriculture?

Spraying is of fundamental importance in agriculture, being responsible for protecting crops against pests, diseases, insects and making nutrients available to plants, ensuring good productivity. This API aims to assist in the analysis of climatic conditions in real time, to inform whether these conditions are suitable or not for agricultural spraying.

## 💻 Using this API:

This API was built with [FastAPI](https://github.com/tiangolo/fastapi). 
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:
* **Fast:** Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
* **Fast to code:** Increase the speed to develop features by about 200% to 300%. ¹
* **Fewer bugs:** Reduce about 40% of human (developer) induced errors. ¹
* **Intuitive:** Great editor support. Completion everywhere. Less time debugging.
* **Easy:** Designed to be easy to use and learn. Less time reading docs.
* **Short:** Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust:** Get production-ready code. With automatic interactive documentation.
* **Standards-based:** Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

*¹ estimation based on tests on an internal development team, building production applications.*


To run it:

```
uvicorn main:app --reload
```

![](https://raw.githubusercontent.com/josehenriqueroveda/spraying-API/main/examples/im1.png)

☁️ **Where did climate data come from before analysis?**
The wheather data come from OpenWeatherMap, it is an online service, owned by OpenWeather Ltd, that provides global weather data, including current weather data, forecasts, nowcasts and historical data, utilising meteorological broadcast services and raw data from airport weather stations, radar stations and other weather stations. After receiving the meteorological data, the API performs the processing, returning the spray conditions

## Examples

* In this case, the city of Columbia is in good condition for spraying. 🌿
![](https://raw.githubusercontent.com/josehenriqueroveda/spraying-API/main/examples/im4.png)

* The city of Longview is not in good condition, due to the low relative humidity of the air. 🍂
![](https://raw.githubusercontent.com/josehenriqueroveda/spraying-API/main/examples/im2.png)

* Dallas is not in a good condition for agricultural spraying due to the high wind speed, which causes drift. 💨
![](https://raw.githubusercontent.com/josehenriqueroveda/spraying-API/main/examples/im3.png)

---

### About:

> - 💻 **José Henrique Roveda**
> - 📨 Contact me on [LinkedIn](https://www.linkedin.com/in/jhroveda/)

