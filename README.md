## Car-Price-Analysis-Dashboard 
Link to streamlit app: https://car-price-analysis-dashboard-mapatha-shaun.streamlit.app/

# Introduction

This project introduces a Car Price Analysis Dashboard, an interactive tool designed to analyze and visualize car pricing trends in South Africa. Using a dataset that includes car brands, models, descriptions, prices, and engine sizes, the dashboard provides valuable insights into pricing patterns and market trends.

The tool is developed using Streamlit, a Python-based framework for building interactive web applications, and focuses on making data exploration easy and accessible for both consumers and businesses.

# Importance of the Project

1. For Consumers
Helps buyers identify car models that offer the best value for their budget.
Provides insights into pricing trends across different brands and models.
2. For Sellers
Assists dealerships and sellers in optimizing pricing strategies.
Highlights factors such as engine size and brand reputation that influence car pricing.
3. For Market Analysis
Delivers an overview of the car market in South Africa.
Supports data-driven decision-making for automotive stakeholders, including manufacturers and marketers.

# Dashboard Features

1. Overview Tab
Dataset Preview: View the raw data, including car prices, brands, and engine sizes.
Basic Statistics: Key dataset statistics, such as total records, unique brands, and unique models.
Descriptive Analytics: Basic statistical summaries of numerical features like price and engine size.
2. Price Analysis Tab
Price Distribution Boxplot: Visualizes the range, median, and outliers of car prices.
Engine Size vs Price Scatter Plot: Illustrates the relationship between engine size and car price, differentiated by brand.
3. Brand Insights Tab
Brand-wise Summary Statistics: Comprehensive price metrics (mean, median, etc.) grouped by brand.
Brand-wise Model Count: A bar chart showing the number of models available for each brand.

# How to Use

1. Prerequisites
   
Install Python (version 3.7 or later).                
Install required libraries:                              
bash                  
Copy code

pip install streamlit pandas matplotlib seaborn

3. Running the Dashboard
 
Save the application code as app.py.

Launch the dashboard using:

bash       
Copy code        
streamlit run app.py

Open the provided URL in your browser to interact with the dashboard.

# Dataset Overview
The dataset includes the following columns:

Brand: The manufacturer of the car.
Model: The car model name.
Model Description: Additional details about the model.
Price: The listed price of the car (in ZAR).
Engine Size: The size of the car’s engine (in liters).

# Project Dependencies

The project uses the following Python libraries:

Streamlit: For creating the interactive dashboard.

Pandas: For data loading and preprocessing.

Matplotlib & Seaborn: For data visualization.

# Future Enhancements

Filters: Add dynamic filters for price range, engine size, and brand.
Advanced Analytics: Integrate predictive models to estimate car prices based on input features.
Enhanced Interactivity: Enable hover and click-based data exploration in charts.
Geographic Insights: Add location-based data analysis for regional price trends.

# Acknowledgments

Dataset: Provided data on car prices in South Africa.

Libraries: Streamlit, Pandas, Matplotlib, and Seaborn for application development.

This project offers a powerful platform for understanding car pricing trends, benefiting both individual consumers and industry stakeholders.

# Contact
shaun.mapatha@gmail.com / https://www.linkedin.com/in/shaun-mapatha-1679941a1/
