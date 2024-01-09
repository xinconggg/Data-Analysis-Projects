import pandas as pd
import matplotlib.pyplot as plt


# Load the Dataset #
dataframe = pd.read_csv("C:\\Users\\Xin Cong\\Downloads\\GlobalWeatherRepository.csv")

# Explore the Dataset #
# Display First Few Rows
print(dataframe.head())
# Get Summary Statistics
print(dataframe.describe())
# Check Data Type and Missing Values
print(dataframe.info())

# Handle Missing Values #
# Check for Missing Values
print(dataframe.isnull().sum())
# Remove Rows with Missing Values
dataframe = dataframe.dropna()


# Identifying and Removing Outliers of Temperature, Precipitation, Wind Speed, Pressure and Humidity #
# Calculation of z-score
z_score_temperature = ((dataframe['temperature_celsius'] - dataframe['temperature_celsius'].mean()) /
                       dataframe['temperature_celsius'].std())
z_score_precipitation = ((dataframe['precip_mm'] - dataframe['precip_mm'].mean()) / dataframe['precip_mm'].std())
z_score_windspeed = ((dataframe['wind_kph'] - dataframe['wind_kph'].mean()) / dataframe['wind_kph'].std())
z_score_pressure = ((dataframe['pressure_mb'] - dataframe['pressure_mb'].mean()) / dataframe['pressure_mb'].std())
z_score_humidity = ((dataframe['humidity'] - dataframe['humidity'].mean()) / dataframe['humidity'].std())

# Identify Outliers
outliers_temperature = dataframe[abs(z_score_temperature) >= 3]
outliers_precipitation = dataframe[abs(z_score_precipitation) >= 3]
outliers_windspeed = dataframe[abs(z_score_windspeed) >= 3]
outliers_pressure = dataframe[abs(z_score_pressure) >= 3]
outliers_humidity = dataframe[abs(z_score_humidity) >= 3]

# Remove Outliers
dataframe = dataframe[~dataframe['temperature_celsius'].isin(outliers_temperature)]
dataframe = dataframe[~dataframe['precip_mm'].isin(outliers_precipitation)]
dataframe = dataframe[~dataframe['wind_kph'].isin(outliers_windspeed)]
dataframe = dataframe[~dataframe['pressure_mb'].isin(outliers_pressure)]
dataframe = dataframe[~dataframe['humidity'].isin(outliers_humidity)]

# Check for Data Consistency and Correctness #
# Check Unique Values in Categorical Columns
print(dataframe['country'].unique())
print(dataframe['location_name'].unique())

# Check Data Types and Consistency
print(dataframe.dtypes)



