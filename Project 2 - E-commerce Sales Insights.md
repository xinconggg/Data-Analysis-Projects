## E-commerce Sales Insights: Unveiling Trends and Enhancing Decision-Making
### Project Objective:
Conduct a thorough analysis of the provided e-commerce sales dataset to extract actionable insights and support strategic decision-making. By exploring diverse dimensions, including sales channels, product categories, customer segments, and regional variations, the project aims to uncover underlying patterns, identify growth opportunities, and enhance the overall understanding of factors influencing sales performance. The objective is to equip stakeholders with a comprehensive foundation for informed decision-making and targeted interventions.

### Key Objectives:
**1. Sales Channel Dynamics:** 
- Analyze the performance of different sales channels.
- Identify trends and patterns contributing to the success or challenges of each channel.
- Recommend strategies to optimize and enhance the effectiveness of various sales channels.
  
**2. Product Category Analysis:** 
- Investigate the contribution of each product category to overall sales.
- Uncover seasonal variations or emerging trends in product preferences.
- Provide insights into potential product category expansions or optimizations.
  
**3. Customer Segmentation Insights:** 
- Segment customers based on purchasing behavior and preferences.
- Identify high-value customer segments and tailor marketing strategies accordingly.
- Offer personalized recommendations to enhance customer satisfaction and retention.

**4. Regional Sales Exploration:** 
- Examine sales performance across different regions or countries.
- Identify geographical areas with significant growth potential.
- Provide recommendations for localized marketing or operational adjustments.

**5. Promotion Impact Assessment:**
- Evaluate the impact of promotions on sales performance.
- Analyze the effectiveness of different promotional strategies and campaigns.
- Offer insights to optimize future promotional activities for maximum impact.

**6. Operational Efficiency Enhancement:**
- Assess fulfillment processes and courier performance.
- Identify bottlenecks or areas for improvement in the fulfillment chain.
- Propose strategies to enhance operational efficiency and customer satisfaction.

**7. Forecasting and Planning:**
- Develop a robust sales forecasting model for future planning.
- Consider seasonality, trends, and external factors influencing sales predictions.
- Provide actionable insights for inventory management and resource allocation.

**8. Interactive Visualization:**
- Utilize Tableau to create interactive visualizations.
- Enhance interpretability through visually appealing dashboards.
- Facilitate better decision-making by conveying complex insights in an accessible manner.     

### Methods and Techniques:
**1. Data Cleaning and Preprocessing:** Address missing data, outliers, and inconsistencies in the dataset.                                                                                
**2. Exploratory Data Analysis (EDA):** Use statistical and graphical methods to uncover patterns and trends.                                                                  
**3. Customer Segmentation:** Employ clustering techniques in Python for customer categorization.  
**4. Time Series Analysis:** Use Python for time series analysis to understand sales trends over time.                                                                                       
**5. Forecasting Model:** Implement time series forecasting techniques to predict future sales.

### Tools and Technologies:
**1. Data Cleaning and Analysis:** Excel, SQL                                                
**2. Visualization:** Tableau                                                            
**3. Statistical Analysis:** Python                                                              

### Significance of project:
The significance of this e-commerce sales analysis project lies in its potential to revolutionize the decision-making process within the organization. By dissecting the provided dataset encompassing crucial sales-related parameters, the project aims to unveil valuable insights that can drive strategic initiatives. From understanding the dynamics of various sales channels and product categories to deciphering customer behavior and regional variations, the analysis provides a holistic view of the e-commerce landscape. These insights, coupled with evaluations of promotional impact, operational efficiency, and forecasting models, contribute to informed decision-making. The project's significance extends beyond retrospective analysis, offering actionable recommendations for optimizing sales strategies, improving customer satisfaction, and streamlining operational processes. Ultimately, the outcomes of this project are poised to empower stakeholders with a data-driven approach, facilitating agile responses to market dynamics and positioning the organization for sustained growth in the highly competitive e-commerce industry.

--------------------

### Data Exploration and Cleaning
**Review Data Types**                                                             
Inspect the data types of each column using ```INFORMATION_SCHEMA.COLUMNS```.                                                           
```sql
SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Amazon Sale Report'
```
![Screenshot 2024-01-11 205229](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/9cd7d348-6526-4304-914e-7e11f8943cf0)                  

**Identify Missing Values**
Using ```IS NULL```.
```sql
SELECT *
FROM [Amazon Sale Report]
WHERE column_name_1 IS NULL or column_name_1 IS NULL
```
![Screenshot 2024-01-11 210720](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/b005f21b-5aa9-4cff-bbf0-6d3dc559a7cb)
**Handling Missing Values**                                                    
Since there exists missing values, we can remove the rows using ```DELETE```.               
However, becareful when removing columns, for example, ```promotion_ids``` are meant to contain missing values.                                                                      
```sql
DELETE FROM [Amazon Sale Report]
WHERE column_name_1 IS NULL or column_name_2 IS NULL
```
![Screenshot 2024-01-11 211718](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/a15cc62e-a26a-421e-82a3-8e9393226eab)                              
109547 rows consisting of missing values were cleared.

**Save the Cleaned Dataset**                                                             
Excel → Data → Get Data → From Database → From SQL Database → Enter Server and Database name

-------------

### Exploratory Data Analysis (EDA)
#### Performing Basic EDA in SQL                                                      
**- Calculate Total Revenue**                                                              
Using ```SUM```                                                                        
```sql
SELECT SUM(Amount) AS TotalRevenue
FROM [Amazon Sale Report];
```
![Screenshot 2024-01-13 135041](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/e591a1cc-391f-4511-89ef-1982216eef8b)                                                                        
<ins>**Total Revenue = $75,384,975.00**</ins>                                                               
                                                      
**- Calculate Average Order Value (AOV)**                                                  
Using ```SUM```                                                                        
```sql
SELECT SUM(Amount)/COUNT(DISTINCT(Order_ID)) AS AverageOrderValue
FROM [Amazon Sale Report];
```
![Screenshot 2024-01-13 135114](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/384ef9e4-45ee-4975-9055-9c4035a35ead)                                                                    
<ins>**Average Order Value = $696.26**</ins> 

**- Calculate Total Quantity Sold**                                                      
Using ```SUM```                                                                        
```sql
SELECT SUM(QTY) AS TotalQuantitySold
FROM [Amazon Sale Report];
```
![Screenshot 2024-01-13 135157](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/aaf58242-82b5-4a25-957f-0917ab791a2c)                                                                      
<ins>**Total Quantity Sold = 116,454**</ins> 

### Customer Segmentation
**Calculation of Recency, Frequency & Monetary (RFM) score in Python**
- Consider the weightage of Recency, Frequency and Monetary as 15%, 28% and 57% respectively.
- Categorize customers based on RFM score:
  - High Value Customer: RFM score ≥ 75
  - Medium Value Customer: RFM score ≥ 60
  - Low Value Customer: RFM score ≥ 40
  - Lost Customer: RFM score < 40
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Xin Cong\\OneDrive\\Desktop\\GitHub Projects\\Project 2 - E-commerce Sales Insights\\Amazon Sale Report - Cleaned.csv")

# Recency, Frequency & Monetary (RFM)
# Recency
# Convert the "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
# Group by "Order ID" and find the maximum date
df_recency = df.groupby(by="Order ID", as_index=False)["Date"].max()
# Rename Columns
df_recency.columns = ["Order ID", "Last Purchase Date"]
# Find most recent date
recent_date = df_recency["Last Purchase Date"].max()
# Calculate Recency
df_recency["Recency"] = df_recency["Last Purchase Date"].apply(lambda x: (recent_date - x).days)

# Frequency
# Group by "Order ID" and find the total number of orders
df_frequency = df.drop_duplicates().groupby(by="Order ID", as_index=False)["Date"].count()
# Rename Columns
df_frequency.columns = ["Order ID", "Frequency"]

# Monetary
# Calculate Total Sum for each order
df["Sum"] = df["Amount"] * df["Qty"]
# Group by "Order ID" and find sum for each customer
df_monetary = df.groupby(by="Order ID", as_index=False)["Sum"].sum()
# Rename Columns
df_monetary.columns = ["Order ID", "Monetary"]

# Merge RFM into 1 dataframe
df_rfm = df_recency.merge(df_frequency, on="Order ID").merge(df_monetary, on="Order ID")
# Drop "Last Purchase Date" column
df_rfm = df_rfm.drop(columns="Last Purchase Date")

# Calculate Ranks for RFM
df_rfm["R_Rank"] = df_rfm["Recency"].rank(ascending=False)
df_rfm["F_Rank"] = df_rfm["Frequency"].rank(ascending=True)
df_rfm["M_Rank"] = df_rfm["Monetary"].rank(ascending=True)

# Calculate Scores for RFM
df_rfm["R_Score"] = (df_rfm["R_Rank"] / df_rfm["R_Rank"].max()) * 100
df_rfm["F_Score"] = (df_rfm["F_Rank"] / df_rfm["F_Rank"].max()) * 100
df_rfm["M_Score"] = (df_rfm["M_Rank"] / df_rfm["M_Rank"].max()) * 100

# Drop Rank columns
df_rfm = df_rfm.drop(columns=["R_Rank", "F_Rank", "M_Rank"])

# Calculate Overall RFM score and Round up
df_rfm["RFM_Score"] = df_rfm["R_Score"]*0.15 + df_rfm["F_Score"]*0.28 + df_rfm["M_Score"]*0.57
df_rfm = df_rfm.round()

# Categorize based on RFM score
df_rfm["Customer_Segment"] = np.where(df_rfm["RFM_Score"] >= 75, "High Value Customer",
                                      np.where(df_rfm["RFM_Score"] >= 60, "Medium Value Customer",
                                               np.where(df_rfm["RFM_Score"] >= 40, "Low Value Customer", "Lost Customer")))

# Plot to display Customer Segments
plt.pie(df_rfm.Customer_Segment.value_counts(),
        labels=df_rfm.Customer_Segment.value_counts().index,
        autopct='%.0f%%')
plt.show()
```
![Screenshot 2024-01-13 133435](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/e27dfb8a-f189-4ae2-8f40-7b7999c3004f)

---

### Impact of Promotion
**Number of Sales with Promotion vs Number of Sales without Promotion:**               
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("C:\\Users\\Xin Cong\\OneDrive\\Desktop\\GitHub Projects\\Project 2 - E-commerce Sales Insights\\Amazon Sale Report - Cleaned.csv")

# Fill rows without Promotion with '0'
df["promotion-ids"] = df["promotion-ids"].fillna(0)
# Calculate the number of sales during promotions
sales_with_promo = df.loc[df['promotion-ids'] != 0, 'Order ID'].nunique()
# Calculate the number of sales during non-promotions
sales_without_promo = df.loc[df['promotion-ids'] == 0, 'Order ID'].nunique()

# Plot Bar graph
labels = ['Sales with Promotion', 'Sales without Promotion']
counts = [sales_with_promo, sales_without_promo]
plt.bar(labels, counts, color=['cyan', 'yellow'])
for i, count in enumerate(counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
plt.title('Impact of Promotions on Sales')
plt.xlabel('Promotion Status')
plt.ylabel('Number of Sales')
plt.show()
```
![Screenshot 2024-01-13 140522](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/7f051446-69ec-4bf3-afd7-118ab8d28739)

---

### Time Series Analysis and Forecasting
**Figure ARIMA model parameters (p, d & q)**
- **d (Order of Differencing):**
  - Start by figuring out parameter d using Augmented Dickey–Fuller test (ADF) test.
  - Value of d is the number of times needed to difference the series to make it stationary.
  - Time series is stationary when value of p ≤ 0.05.
```python
import pandas as pd
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv("C:\\Users\\Xin Cong\\OneDrive\\Desktop\\GitHub Projects\\Project 2 - E-commerce Sales Insights\\Daily Sales.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=False)
df.set_index('Date', inplace=True)

# Check for stationarity
result = adfuller(df['Amount'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
```
![Screenshot 2024-01-13 153936](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/60f9871b-59ab-44e9-8e7e-020b66e8b9a4)                                  
Since p-value ≤ 0.05, the time-series is stationary. 

- **q and p (Order of Moving Average and Order of Order of Auto-Regressive):**
  - Plot Autocorrelation Function (ACF) graph and Partial Autocorrelation Function (PACF), then interpret.
  - Look for significant spikes.
```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv("C:\\Users\\Xin Cong\\OneDrive\\Desktop\\GitHub Projects\\Project 2 - E-commerce Sales Insights\\Daily Sales.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=False)
df.set_index('Date', inplace=True)

# Plot ACF and PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# ACF Plot
plot_acf(df['Amount'].dropna(), lags=40, ax=ax1)
ax1.set_title('Autocorrelation Function (ACF)')

# PACF Plot
plot_pacf(df['Amount'].dropna(), lags=40, ax=ax2)
ax2.set_title('Partial Autocorrelation Function (PACF)')

plt.show()
```
![Screenshot 2024-01-13 155026](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/2025e9a5-ab65-49cd-b80a-e10717b55543)                                              
Both graph indicates the most significant spike happens at lag = 1. Therefore, p = q = 1.                                                                                                                
**p=1, d=0 & q=1**                                                                                                                                                                                                                                                                                                                                                                                                                      

**Visualize Forecast (For the next 30 Days)**
```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from matplotlib.ticker import FuncFormatter

# Load Data
df = pd.read_csv("C:\\Users\\Xin Cong\\OneDrive\\Desktop\\GitHub Projects\\Project 2 - E-commerce Sales Insights\\Daily Sales.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.set_index('Date')
df = df.resample('D').sum()

# Fit ARIMA model
p, d, q = 1, 0, 1
model = ARIMA(df['Amount'], order=(p, d, q))
results = model.fit()

# Forecast the next 30 Days
forecast_steps = 30
forecast = results.get_forecast(steps=forecast_steps)

# Generate date index for the forecast
forecast_index = pd.date_range(df.index[-1] + pd.DateOffset(days=1), periods=forecast_steps, freq='D')
combined_df = pd.concat([df, pd.DataFrame(index=forecast_index, data={'Amount': forecast.predicted_mean})])

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(combined_df.index, combined_df['Amount'], label='Actual', color='blue')
plt.plot(forecast_index, forecast.predicted_mean, color='red', label='Forecasted')
formatter = FuncFormatter(lambda x, _: '{:.0f}K'.format(x / 1000))
plt.gca().yaxis.set_major_formatter(formatter)
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend()
plt.show()
```
![Screenshot 2024-01-13 171606](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/a812a484-deca-44a0-984d-007bc4b64c51)

















