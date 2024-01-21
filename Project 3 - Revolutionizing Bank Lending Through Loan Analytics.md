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

---

## Good Loans vs Bad Loans
Good Loans: Fully Paid or Current
Bad Loans: Charged off
### Good and Bad Loans Percentage
Calculating good and bad loan percentages is important for assessing the quality of a loan portfolio, evaluating risk exposure, and informing proactive risk management strategies, ultimately ensuring the financial stability of a lending institution.                                                                                                        
```sql
SELECT 
	ROUND((COUNT(CASE WHEN loan_status = 'Fully Paid' OR loan_status = 'Current' THEN id end)*100.0)
	/
	COUNT(ID),2) AS Good_Loan_Percentage
FROM bank_loan

SELECT 
	ROUND((COUNT(CASE WHEN loan_status = 'Charged off' THEN id end)*100.0)
	/
	COUNT(ID),2) AS Bad_Loan_Percentage
FROM bank_loan
```
![Screenshot 2024-01-21 221649](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/25721361-de8e-45d7-9ea9-7473f4a24a7e)
![Screenshot 2024-01-21 221657](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/ec722dda-7145-4ee2-9fe3-502c0cc367fc)        
      

### Good and Bad Loans Applications
Calculating Good and Bad Loan Applications is essential for evaluating the overall health and risk profile of a lending portfolio, aiding in risk management, strategic decision-making, and ensuring financial stability by assessing the quality and performance of loans within a financial institution.                                                                                                     
```sql
SELECT COUNT(id) AS Good_Loan_Applications from bank_loan 
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'

SELECT COUNT(id) AS Bad_Loan_Applications from bank_loan 
WHERE loan_status = 'Charged off'
```
![Screenshot 2024-01-21 221207](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/26d6b5da-cc45-425b-99fe-2648306769cd)
![Screenshot 2024-01-21 221216](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/9357cc1f-437e-4347-8fb0-93677e81a612)        

### Good and Bad Loans Funded Amount
Calculating Good and Bad Loan Funded Amount provides insights into the quality and performance of loans, aiding in strategic planning, optimizing resource allocation, and ensuring the institution's long-term stability by evaluating the impact of both successful and problematic loans on the overall funding portfolio.                                                                                                   
```sql
SELECT SUM(loan_amount) AS Good_Loan_Funded_Amount FROM bank_loan
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'

SELECT SUM(loan_amount) AS Bad_Loan_Funded_Amount FROM bank_loan
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'
```
 ![Screenshot 2024-01-21 223358](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/ea341f0d-00f8-49ce-9867-924d3e863a0b)
 ![Screenshot 2024-01-21 223408](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/ef3fa5aa-1f61-451a-9761-29a69486b877)        
 

### Good and Bad Loans Total Received Amount
Analyzing the total received amounts for Good and Bad Loans is crucial for assessing the financial impact and repayment behavior of borrowers. It provides valuable insights into the overall revenue and risk associated with the loan portfolio, aiding in effective risk management, strategic decision-making, and ensuring the financial stability of the lending institution by evaluating the success of loan repayment and identifying potential areas for improvement in the lending process.                                                                                          
```sql
SELECT SUM(total_payment) AS Good_Loan_Received_Amount from bank_loan
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'

SELECT SUM(total_payment) Bad_Loan_Received_Amount from bank_loan
WHERE loan_status = 'Charged off'
```
![Screenshot 2024-01-21 222800](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/e644dccc-9cc2-4376-badd-b812db572172)
![Screenshot 2024-01-21 222809](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/088a5069-803c-4606-8d0e-a493fb9d8641)                

### Loan Status
Loan status is crucial as it serves as a key indicator, offering insights into critical metrics such as total loan applications, funded amounts, amounts received, month-to-date figures, average interest rates, and debt-to-income ratios. This information is essential for evaluating the health of the loan portfolio, assessing operational efficiency, and making data-driven decisions that impact overall financial performance and strategic planning within a lending institution.       
**Loan Count, Total Amount Received, Total Funded Amount, Average Interest Rate and Debt-to-Income Ratio**        
```sql
SELECT 
        loan_status,
        COUNT(id) AS Loan_Count,
        SUM(total_payment) AS Total_Amount_Received,
        SUM(loan_amount) AS Total_Funded_Amount,
        ROUND(AVG(int_rate * 100),2) AS Interest_Rate,
        ROUND(AVG(dti * 100),2) AS DTI
FROM
	bank_loan
GROUP BY
	loan_status
```
![Screenshot 2024-01-21 224621](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/f72864e6-b6e3-41cb-a84d-764323b549f6)        

**MTD Amount Received and MTD Funded Amount**        
```sql
SELECT 
        loan_status,
        SUM(total_payment) AS MTD_Amount_Received,
        SUM(loan_amount) AS MTD_Funded_Amount
FROM
	bank_loan
WHERE
	MONTH(issue_date) = 12 AND YEAR(issue_date) = 2023
GROUP BY
	loan_status
```
![Screenshot 2024-01-21 225113](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/3e37204e-4f0f-4a4c-8556-0c2fbbda1652)        

---

## Data Required for Data Visualization
### Monthly Trends by Issue Date
```sql
SELECT 
	MONTH(issue_date) AS Month_Number,
	DATENAME(MONTH, issue_date) AS Month_Name,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY MONTH(issue_date), DATENAME(MONTH, issue_date)
ORDER BY MONTH(issue_date)
```
![Screenshot 2024-01-21 230412](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/1591d813-307f-4d23-885f-0f929147dc63)          

### Regional Analysis by State
```sql
SELECT 
	address_state AS State,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY address_state
ORDER BY address_state
```
![Screenshot 2024-01-21 230912](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/f52852f7-53ba-4f9f-83aa-74e8d89e73e6)        

### Loan Term Analysis
```sql
SELECT 
	term AS Loan_Term,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY term
ORDER BY term
```
![Screenshot 2024-01-21 231046](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/06b69ac9-b7e0-44db-85fd-e874dad1e6dd)        

### Employment Length Analysis
```sql
SELECT 
	emp_length AS Employment_Length,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY emp_length
ORDER BY emp_length
```
![Screenshot 2024-01-21 231214](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/efe1da5a-9773-4f14-9681-7a77a7bd5717)        

### Loan Purpose Breakdown
```sql
SELECT 
	purpose AS Purpose,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY purpose
ORDER BY purpose
```
![Screenshot 2024-01-21 231349](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/7f2b01d8-66aa-45e1-859d-afa2d635e47a)        

### Home Ownership Analysis
```sql
SELECT 
	home_ownership AS Home_Ownership,
	COUNT(id) AS Total_Loan_Applicants,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan
GROUP BY home_ownership
ORDER BY home_ownership
```
![Screenshot 2024-01-21 231508](https://github.com/xinconggg/Data-Analysis-Projects/assets/82378681/64f882f0-22b9-45b8-a7f5-7bb5b83e5e80)

---










