import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model
with open('xgb_smote.pkl', 'rb') as f:
    model = pickle.load(f)

# The list of features that the model was trained on
model_features = [
    "Age", "DailyRate", "DistanceFromHome", "HourlyRate", "JobInvolvement", 
    "NumCompaniesWorked", "StockOptionLevel", "TrainingTimesLastYear", 
    "YearsSinceLastPromotion", "YearsWithCurrManager", "OverTime_Yes", 
    "RoleStability", "PromotionFrequency", "OverallSatisfaction", "OvertimeImpact"
]

# Streamlit UI setup
st.title('Employee Attrition Risk Prediction')
st.write("Upload a CSV file or manually input employee data to predict the risk of attrition.")

# File upload section
uploaded_file = st.file_uploader("Upload Employee Data CSV", type=["csv"])

if uploaded_file is not None:
    # Read and preprocess the uploaded file
    data = pd.read_csv(uploaded_file)
    
    # Convert 'OverTime' to 'OverTime_Yes' if it exists in the data
    if 'OverTime' in data.columns:
        data['OverTime_Yes'] = data['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)
        data.drop(columns=['OverTime'], inplace=True)  # Drop the original 'OverTime' column

    # Ensure all necessary features are present
    for feature in model_features:
        if feature not in data.columns:
            # Add missing columns with default values (e.g., 0 for numeric features)
            data[feature] = 0

    # Keep only the features the model expects
    data = data[model_features]
    
    # Encode non-numeric columns if needed
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = LabelEncoder().fit_transform(data[col])
    
    # Make predictions
    predictions = model.predict(data)
    probabilities = model.predict_proba(data)[:, 1]
    
    # Add predictions to the data
    data['Attrition_Risk'] = predictions
    data['Attrition_Probability'] = probabilities.round(4)
    
    # Show results
    st.write("### Prediction Results")
    st.dataframe(data)
    
    # Option to download the results
    csv_download = data.to_csv(index=False)
    st.download_button(label="Download Predictions as CSV", data=csv_download, file_name="attrition_predictions.csv", mime="text/csv")

# Manual input section
st.write("### Manual Feature Input")
manual_input = {}
feature_comments = {
    "Age": "(Employee's age in years)",
    "DailyRate": "(Daily wage in dollars)",
    "DistanceFromHome": "(Distance from home to workplace in km)",
    "HourlyRate": "(Hourly wage in dollars)",
    "JobInvolvement": "(Level of job engagement: 1 (Low) to 4 (High))",
    "NumCompaniesWorked": "(Total number of companies worked for)",
    "StockOptionLevel": "(Level of stock options: 0 (No options) to 3 (High level of options))",
    "TrainingTimesLastYear": "(Number of training sessions attended last year)",
    "YearsSinceLastPromotion": "(Years since the last promotion)",
    "YearsWithCurrManager": "(Years under current manager)",
    "OverTime_Yes": "(Yes or No)",
    "RoleStability": "(Years in current role relative to total working years: 0 to 1)",
    "PromotionFrequency": "(Frequency of promotions: 0 to 1)",
    "OverallSatisfaction": "(Overall satisfaction score: 1 (Low) to 4 (High))",
    "OvertimeImpact": "(Impact of overtime on work-life balance: 0 to 1)"
}

for feature in model_features:
    comment = feature_comments.get(feature, "")
    if feature == "OverTime_Yes":
        manual_input[feature] = 1 if st.selectbox(f"OverTime {comment}", ["No", "Yes"]) == "Yes" else 0
    elif feature in ["RoleStability", "PromotionFrequency", "OvertimeImpact"]:
        manual_input[feature] = st.number_input(f"{feature} {comment}", min_value=0.0, max_value=1.0, step=0.01, value=0.0)
    else:
        manual_input[feature] = st.number_input(f"{feature} {comment}", min_value=0, value=0)

# Add the Predict button
if st.button("Predict Attrition Risk"):
    manual_df = pd.DataFrame([manual_input])
    prediction = model.predict(manual_df)[0]
    probability = model.predict_proba(manual_df)[0, 1].round(4)
    
    # Show result
    if prediction == 1:
        st.error(f"High risk of attrition with {probability * 100:.2f}% probability")
    else:
        st.success(f"Low risk of attrition with {(1 - probability) * 100:.2f}% probability")