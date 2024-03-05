import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Function to load predictions and test data
@st.cache
def load_data():
    predictions = pd.read_csv('predictions.csv', parse_dates=['Date'])  # Ensure 'Date' is the correct column name
    test_data = pd.read_csv('test_data.csv', parse_dates=['Date'])  # Ensure 'Date' is the correct column name
    return predictions, test_data

# Load data
predictions, test_data = load_data()

# Streamlit UI
st.title('Stock Price Prediction App')

# Display predictions data
st.subheader('Predictions')
st.write(predictions)

# Visualization
st.subheader('Prediction Visualization')
selected_company = st.selectbox('Select a Company', ['Apple', 'Google', 'Microsoft', 'Amazon'])  # Replace with company names

# Plotting function
def plot_predictions(test_data, predictions, selected_company):
    plt.figure(figsize=(15, 10))  # You can adjust the figure size here
    plt.plot(test_data['Date'], test_data[selected_company], label='Actual Price', marker='o')
    plt.plot(predictions['Date'], predictions[f'LSTM_{selected_company}'], label='LSTM Predictions', marker='x')
    plt.plot(predictions['Date'], predictions[f'Transformer_{selected_company}'], label='Transformer Predictions', marker='^')
    
    # Improve date ticks
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # Show a major tick for each month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format the date as Year-Month
    plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=7))  # Show a minor tick every week
    plt.xticks(rotation=90, ha='center')  # Rotate the date labels

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Predictions for {selected_company}')
    plt.legend()
    plt.tight_layout()  # Adjust the padding between and around subplots
    st.pyplot(plt)

# Show plot in Streamlit
if st.button('Show Prediction Plot'):
    plot_predictions(test_data, predictions, selected_company)
