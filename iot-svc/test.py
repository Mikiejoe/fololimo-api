from iot.utils import chat_model


data = {
  "soil_data": {
    "pH": 6.5,
    "NPK": {
      "Nitrogen": 40,
      "Phosphorus": 30,
      "Potassium": 25
    },
    "Moisture": 25
  },
  "weather_data": {
    "temperature": {
      "avg_day_temp": 24,
      "avg_night_temp": 15
    },
    "precipitation": {
      "avg_rainfall": 80
    },
    "humidity": {
      "avg_humidity": 60
    }
  },
  "location": {
    "latitude": -1.286389,
    "longitude": 36.817223
  },
}

print(chat_model(data, 1))