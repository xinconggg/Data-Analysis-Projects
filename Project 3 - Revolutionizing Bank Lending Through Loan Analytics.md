## Revolutionizing Bank Lending Through Loan Analytics
### Project Objective:
Optimize the monitoring and evaluation of the bank's lending activities by developing visually intuitive dashboards. Utilize advanced data analytics to extract valuable insights on key loan metrics, facilitating data-driven decision-making and cultivating a thorough comprehension of the dynamic aspects within the bank's loan portfolio
### Key Objectives:
**1. Risk Management Framework:** 
- Conduct a thorough risk assessment for the bank's lending activities, identifying potential sources of risk.
- Develop and implement a robust risk management framework to monitor, evaluate, and mitigate identified risks effectively.
- Integrate risk indicators into the dashboards for real-time monitoring and early risk detection.

**2. Operational Efficiency Enhancement:**
- Conduct a detailed analysis of current lending processes to identify bottlenecks and inefficiencies.
- Propose and implement process improvements to streamline lending operations and reduce turnaround times
- Monitor and measure the impact of operational enhancements on overall efficiency and customer satisfaction

**3. Performance Benchmarking:**
- Define key performance indicators (KPIs) for loan performance based on industry benchmarks and internal goals.
- Regularly assess loan performance against established benchmarks to identify areas for improvement or optimization.
- Use benchmarking results to inform strategic decisions and enhance overall lending effectiveness.

**4. Trend Identification and Analysis:**
- Utilize advanced analytics tools to identify emerging trends within the lending landscape.
- Conduct in-depth analysis of identified trends to understand their potential impact on the bank's lending strategies.
- Implement strategies to leverage positive trends and mitigate risks associated with negative trends.

**5. Compliance and Regulatory Adherence:**
- Integrate compliance checks and adherence measures into the loan analytics framework.
- Regularly audit and update the system to ensure continuous compliance with evolving regulatory requirements.

### Methods and Techniques:
**1. Data Integration and Transformation:** Employ SQL queries and data transformation tools to clean, reshape, and standardize the dataset.                                                 
**2. Descriptive Statistics and Summary Metrics:** Perform descriptive statistical analysis to summarize key characteristics of the loan data.                                         
**3. Data Visualization:** Utilize Power BI for interactive data visualization, creating charts, graphs, and dashboards to convey key loan-related insights.                    

### Tools and Technologies:
**1. Data Cleaning and Analysis:** Excel, SQL                                                
**2. Visualization:** Power BI                                                                                                          

### Significance of project:
The project's significance lies in its transformative impact on the bank's lending operations, offering a paradigm shift towards data-driven decision-making, optimized efficiency, and strategic adaptability. By implementing visually intuitive dashboards and leveraging advanced data analytics, the project ensures real-time insights into key loan metrics, facilitating proactive risk management, compliance assurance, and strategic planning. The centralized monitoring of the loan portfolio fosters operational transparency and efficiency, while customer segmentation and tailored financial solutions enhance customer satisfaction. Ultimately, the project positions the bank for continuous improvement, empowering it to navigate market dynamics, comply with regulatory standards, and make informed decisions that contribute to long-term success in the dynamic financial landscape.

---

## Key Performance Indicators (KPIs) Requirements
### Loan Applications   
We need to calculate the total number of loan applications which is essential for monitoring performance, optimizing operations, and informing strategic decisions.  
**Total Loan Applications:**                                                                                               
```sql
SELECT COUNT(id) AS Total_Loan_Applications FROM bank_loan
```
![Screenshot 2024-01-21 203421](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/1d554557-f726-4049-b821-a9971e00955f)  
**Month-To-Date (MTD) Loan Application** (Dec 2023):  
```sql
SELECT COUNT(id) AS MTD_Loan_Applications from bank_loan
WHERE MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 205750](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/a55dbdad-edc8-4bcb-9b7c-1184f9b41906)    
        
**Previous Month-To-Date (PMTD) Loan Application** (Nov 2023):  
```sql
SELECT COUNT(id) AS PMTD_Loan_Applications from bank_loan
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 205734](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/8716bba4-e31b-4a5f-9121-2f07f2f269f9)    

### Funded Amount  
Understanding the total amount of funds disbursed as loans is crucial for assessing the financial health of a lending institution, guiding strategic decisions, and ensuring effective capital allocation.  
**Total Funded Amount:**                                                                                                 
```sql
SELECT SUM(loan_amount) AS Total_Funded_Amount FROM bank_loan
```
![Screenshot 2024-01-21 210145](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/1dda178b-b778-43ed-bfbc-b92cf185d2e8)   

**MTD Funded Amount** (Dec 2023):                                                                                                
```sql
SELECT SUM(loan_amount) AS MTD_Funded_Amount FROM bank_loan
WHERE MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 210457](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/803cd008-bc71-46a9-9461-7845cf645124)      

**PMTD Funded Amount** (Nov 2023):                                                                                                
```sql
SELECT SUM(loan_amount) AS PMTD_Funded_Amount FROM bank_loan
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 210550](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/0e921e74-d09c-46b6-8f0a-fb81432ca8b8)    

### Amount Received by Bank  
Tracking the total amount received from borrowers is essential for assessing the bank's cash flow and loan repayment.  
**Total Amount Received:**                                                                                                 
```sql
SELECT SUM(total_payment) AS Total_Amount_Received FROM bank_loan
```
![Screenshot 2024-01-21 210909](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/9893c140-8135-4b7d-b8df-18acd0526942)  
**MTD Amount Received** (Dec 2023):                                                                                                  
```sql
SELECT SUM(total_payment) AS MTD_Amount_Received FROM bank_loan
WHERE MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 211032](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/7ff45949-2d19-496d-af9d-cdc8a6068b2b)  
**PMTD Amount Received** (Nov 2023):                                                                                                  
```sql
SELECT SUM(total_payment) AS PMTD_Amount_Received FROM bank_loan
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 211120](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/8d6bb63b-b9ec-4cb3-8c83-53a8c94188f5)

### Interest Rate  
Calculating average interest rate across all loans will provide insights into our lending portfolio's overall cost.
**Average Interest Rate:**                                                                                                 
```sql
SELECT ROUND(AVG(int_rate)*100 , 2) AS Average_Interest_Rate FROM bank_loan
```
![Screenshot 2024-01-21 212623](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/4329b20a-5ca5-4d75-89d1-c27b28b77c13)  
**MTD Average Interest Rate** (Dec 2023):                                                                                                  
```sql
SELECT ROUND(AVG(int_rate)*100 , 2) AS MTD_Interest_Rate FROM bank_loan
WHERE MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 212740](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/431ba745-359b-4f85-860b-eafbaebbeee2)  
**PMTD Average Interest Rate** (Nov 2023):                                                                                                  
```sql
SELECT ROUND(AVG(int_rate)*100 , 2) AS PMTD_Interest_Rate FROM bank_loan
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 212822](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/a2da9f9c-b8ef-42e8-be16-bb7057078d95)  

### Debt-To-Income Ratio (DTI)
Evaluating the average DTI for our borrowers helps us gauge their financial health.  
**Average DTI:**                                                                                                 
```sql
SELECT ROUND(AVG(dti)*100 , 2) AS Average_DTI FROM bank_loan
```
![Screenshot 2024-01-21 213005](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/530057d1-54e5-4e33-9a84-534b76d19a38)  
**MTD DTI** (Dec 2023):                                                                                                  
```sql
SELECT ROUND(AVG(dti)*100 , 2) AS MTD_DTI FROM bank_loan
WHERE MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 213050](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/993b0ac8-13b1-4c9d-803e-9fa1e5d18362)  
**PMTD DTI** (Nov 2023):                                                                                                  
```sql
SELECT ROUND(AVG(dti)*100 , 2) AS PMTD_DTI FROM bank_loan
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2023
```
![Screenshot 2024-01-21 213201](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/9497ac33-7d6c-4b61-a2a9-b77b5b5e0699)




