import json
from decouple import config
import requests

class OpenWeather(object):
  def __init__(self, city_name):
    self.city_name = city_name
    self.base_url = "https://api.openweathermap.org"
    self.api_key = config("OPEN_WEATHER_API")
    self.lat = None
    self.lon = None

  def get_lat_long(self):
    resp = requests.get(f"{self.base_url}/geo/1.0/direct?q={self.city_name}&appid={self.api_key}")
    if resp.status_code == 200:
      data = resp.json()
      if data:
        self.lat = data[0]['lat']
        self.lon = data[0]['lon']
    else:
        print("Error fetching coordinates:", resp.status_code)

  def get_current_weather(self):
    if self.lat is None or self.lon is None:
      self.get_lat_long()
    resp = requests.get(f"{self.base_url}/data/2.5/weather?lat={self.lat}&lon={self.lon}&APPID={self.api_key}")
    if resp.status_code == 200:
        return json.dumps(resp.json())
    else:
        print("Error fetching weather data:", resp.status_code)
    return None

  def get_weather_forecast(self):
    if self.lat is None or self.lon is None:
      self.get_lat_long()
    resp = requests.get(f"{self.base_url}/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}")
    if resp.status_code == 200:
        return json.dumps(resp.json())
    else:
        print("Error fetching forecast data:", resp.status_code)
    return None

  def get_current_air_pollution(self):
    if self.lat is None or self.lon is None:
      self.get_lat_long()
    resp = requests.get(f"{self.base_url}/data/2.5/air_pollution?lat={self.lat}&lon={self.lon}&appid={self.api_key}")
    if resp.status_code == 200:
        return json.dumps(resp.json())
    else:
        print("Error fetching air pollution data:", resp.status_code)
    return None

  def get_air_pollution_forecast(self):
    if self.lat is None or self.lon is None:
      self.get_lat_long()
    resp = requests.get(f"{self.base_url}/data/2.5/air_pollution/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}")
    if resp.status_code == 200:
        return json.dumps(resp.json())
    else:
        print("Error fetching air pollution forecast data:", resp.status_code)
    return None

  def get_relevant_data(self):
    if self.lat is None or self.lon is None:
      self.get_lat_long()
    if self.lat is not None and self.lon is not None:
      combined_data = {
            "current_weather": self.get_current_weather(),
            "weather_forecast": self.get_weather_forecast(),
            "current_pollution": self.get_current_air_pollution(),
            "pollution_forecast": self.get_air_pollution_forecast(),
        }
      return combined_data
    else:
      return None