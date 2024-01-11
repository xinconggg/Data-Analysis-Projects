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
**3. Customer Segmentation:** Employ clustering techniques in R for customer categorization.  
**4. Time Series Analysis:** Use R for time series analysis to understand sales trends over time.                                                                                  
**5. Geospatial Analysis:** Leverage Tableau for visualizing regional sales on a map.        
**6. Forecasting Model:** Implement time series forecasting techniques to predict future sales.

### Tools and Technologies:
**1. Data Cleaning and Analysis:** Excel, SQL                                                
**2. Visualization:** Tableau                                                            
**3. Statistical Analysis:** R                                                              

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

-------------

### Exploratory Data Analysis (EDA)
**asdasdas**







