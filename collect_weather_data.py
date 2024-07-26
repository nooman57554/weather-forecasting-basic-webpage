import requests
import pandas as pd
from datetime import datetime, timedelta

# p8 api key : 3becb1759da057bd3b63a18a7d85d605
# additional api key : a611e8a7d5445b9bd6be0b38b647e4f1
api_key = '2172df3f3aff0c6287a4c7e14b54fb9e' 
city = 'Kalaburagi'  
start_date = datetime.now() - timedelta(days=90)
end_date = datetime.now()


def get_weather_data(date):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
  
    return {
        'date': date.strftime('%Y-%m-%d'),
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'description': data['weather'][0]['description']
    }


date_range = pd.date_range(start=start_date, end=end_date, freq='D')
weather_data = []

for single_date in date_range:
    try:
        weather_data.append(get_weather_data(single_date))
    except Exception as e:
        print(f"Failed to get data for {single_date}: {e}")

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv('weather_data.csv', index=False)

print("Data collection complete. Saved to 'weather_data.csv'")
