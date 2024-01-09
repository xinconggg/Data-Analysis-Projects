## Exploring Global Temperature Trends - A Comparative Analysis with Singapore
### Project Objective:
To analyze and compare the short-term historical temperature trends between global locations and Singapore, focusing on the time range from August 29, 2023, to January 8, 2024. Utilizing a dataset encompassing temperature, air quality, wind speed, and other relevant environmental factors, the aim is to identify patterns, variations, and potential correlations, providing insights into how Singapore's climate compares to global temperature trends during this specific timeframe.

### Key Objectives:
**1.	Global Temperature Trend Analysis:** Examine the historical temperature trends on a global scale within the limited time range. Identify short-term patterns and variations in temperature across different global locations.                                                          
**2.	Singapore Climate Investigation:** Explore the specific climate patterns and trends in Singapore during the time period. Highlight unique characteristics of Singapore's climate within this short-term context.                                         
**3.	Comparative Climate Study for the Specified Timeframe:** Conduct a detailed comparison between global temperature trends and those observed in Singapore. Uncover any short-term similarities, differences, and notable deviations.                                         
**4.	Short-term Environmental Factors Correlation:** Investigate potential correlations between temperature and other key environmental factors, such as air quality and wind speed, during the short-term period.                                         
**5.	Data Visualization for Short-term Insights:** Utilize effective data visualization techniques to visually communicate short-term trends and patterns within the specified timeframe, enhancing the interpretability of the analysis.

### Methods and Techniques:
**1.	Data Cleaning and Preparation:** Handle missing values, ensure data consistency, and convert data types if needed.                                         
**2.	Exploratory Data Analysis (EDA):** Explore data distributions, identify trends, and uncover patterns.                                         
**3.	Time Series Analysis:** Examine how temperature varies over time for both global locations and Singapore.                                         
**4.	Statistical Analysis:** Use statistical measures to quantify similarities or differences in temperature trends.                                         
**5.	Data Visualization:** Create visualizations (line charts, scatter plots, etc.) to present insights clearly.                                         
**6.	Correlation Analysis:** Explore relationships between temperature and other environmental variables.                                         

### Tools and Technologies:
**1.	Programming Language:** Python (utilizing libraries such as Pandas, NumPy, Matplotlib, Seaborn).          
**2.	Data Analysis:** Jupyter Notebooks for interactive and documented analysis.                  
**3.	Statistical Analysis:** SciPy and StatsModels for statistical tests.                            
**4.	Data Visualization:** Matplotlib and Seaborn for static visualizations, Plotly for interactive visualizations.

### Significance of project:
The significance of this project lies in its exploration of short-term global temperature trends and their comparison with the unique climate of Singapore during the specific timeframe from August 29, 2023, to January 8, 2024. By analyzing a diverse dataset encompassing temperature, air quality, wind speed, and other environmental variables, this study aims to uncover patterns, variations, and potential correlations, shedding light on how Singapore's climate aligns with or deviates from global temperature trends over this short duration. The insights gained from this analysis could have implications for understanding the dynamic nature of climate patterns, providing valuable information for local environmental planning, resource management, and contributing to the broader discourse on climate studies. Furthermore, the project showcases practical skills in data analysis, statistical methods, and data visualization, offering a tangible demonstration of the ability to derive meaningful conclusions from real-world data.

-----------------------------------------------------------------------------------
### Understand the Data
**1.** Examine the data columns and understand the information they contain.              
**2.** Identify which columns are relevant for the analysis.
![Screenshot 2024-01-09 223321](https://github.com/xinconggg/Weather-Trend/assets/82378681/1295ddca-35ee-4b97-99c0-4dafde4ad867)

### Relevant Columns
| Country     | Location         | Last Updated      | Temperature (C) | Wind Speed (kph) | Pressure (mb) | Precipitation (mm) | Humidity (%) |
|-------------|------------------|-------------------|------------------|------------------|----------------|---------------------|--------------|
| Afghanistan | Kabul            | 29/8/2023 14:00  | 28.8             | 11.5             | 1004           | 0                   | 19           |
| Albania     | Tirana           | 29/8/2023 11:30  | 27               | 6.1              | 1006           | 0                   | 54           |
| Algeria     | Algiers          | 29/8/2023 10:30  | 28               | 13               | 1014           | 0                   | 30           |
| Andorra     | Andorra La Vella | 29/8/2023 11:30  | 10.2             | 9.7              | 1015           | 0                   | 51           |
| Angola      | Luanda           | 29/8/2023 10:30  | 25               | 3.6              | 1016           | 0                   | 69           |

---------------------

### Preparing the Environment
**Import Libraries**
Import required libraries such as:
- Pandas - Data Manipulation
- Matplotlib & Seaborn - Data Visualization
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

**Read Dataset**                             
Read Dataset using ```pd.read_csv("dataset location")```
```python
data = pd.read_csv("C:\\Users\\Xin Cong\\Downloads\\Data Analyst Project\\GlobalWeatherRepository.csv")
```

---------------------

### Exploring the Data Set
**Display First 5 Rows**            
- Get a glimpse of the data            
- Using ```.head()```                            

**Input:**
```python
print(data.head())
```
**Output:**![Screenshot 2024-01-09 233046](https://github.com/xinconggg/Weather-Trend/assets/82378681/206f0148-748c-4b05-a8fd-0809f183d3be)

**Get Summary Statistics**                       
- Provides summary statistics such as mean, standard deviation, etc.            
- Using ```.describe()```               

**Input:**
```python
print(data.describe())
```
**Output:**![Screenshot 2024-01-09 234019](https://github.com/xinconggg/Weather-Trend/assets/82378681/82271f63-5eb7-4c9e-87ca-eb2b63a7894a)

**Check Data Type and Missing Values**                       
- Provides an overview of the data types of each column and the number of non-null values.      
- Using ```.info()```               

**Input:**
```python
print(data.info())
```
**Output:**                                                    
![Screenshot 2024-01-09 234515](https://github.com/xinconggg/Weather-Trend/assets/82378681/50510c28-0e0e-4e39-a790-632eaed798c4)

---------------------

### Data Cleaning
**asdasd**            
- asd
 



