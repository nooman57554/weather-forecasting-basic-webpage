import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load historical weather data
weather_df = pd.read_csv('weather_data.csv')

# Feature engineering
# Adding lagged features for prediction (previous day's values)
weather_df['temp_lag1'] = weather_df['temp'].shift(1)
weather_df['humidity_lag1'] = weather_df['humidity'].shift(1)
weather_df['pressure_lag1'] = weather_df['pressure'].shift(1)
weather_df['wind_speed_lag1'] = weather_df['wind_speed'].shift(1)

# Drop rows with missing values
weather_df.dropna(inplace=True)

# Features and target variable
X = weather_df[['temp_lag1', 'humidity_lag1', 'pressure_lag1', 'wind_speed_lag1']]
y = weather_df['temp']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model training complete. Model saved to 'model.pkl'")
