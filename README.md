📊 Food Wastage Dashboard
📌 Project Overview

The Food Wastage Dashboard is a data-driven solution designed to track, visualize, and analyze food donations between providers and receivers.
It helps identify patterns, reduce food wastage, and improve the efficiency of food distribution by leveraging data cleaning, database management, and interactive visualizations.

This project demonstrates end-to-end data analysis — from raw data cleaning to deploying an interactive Streamlit web app.

🎯 Objectives

Clean and preprocess food donation datasets.

Store data in a SQLite database with relational tables.

Analyze data to identify key trends and insights.

Build a Streamlit Dashboard to visualize findings interactively.

Provide actionable insights to reduce food wastage.

📂 Dataset Information

The project uses the following CSV files:

providers_data.csv → Details of food providers (restaurants, NGOs, etc.)

receivers_data.csv → Details of food receivers (food banks, charities, etc.)

food_listings_data.csv → Information on food items available for donation

claims_data.csv → Food claim transactions between providers and receivers

🛠 Tech Stack

Programming Language: Python 🐍

Data Cleaning & Analysis: Pandas, NumPy

Database: SQLite3

Visualization: Matplotlib, Seaborn

Dashboard: Streamlit

Deployment: Ngrok (for Google Colab demo)

📜 Project Phases
Phase 1 — Data Cleaning

Removed extra spaces in text columns

Handled missing and inconsistent data

Saved cleaned datasets

Phase 2 — Database Creation

Created SQLite database

Designed relational schema for providers, receivers, food listings, and claims

Inserted cleaned data into tables

Phase 3 — Data Analysis

Analyzed top cities, top providers, and popular food categories

Calculated donation frequency and volume

Generated summary statistics

Phase 4 — Visualization

Created bar charts, pie charts, and line plots for trends

Visualized top cities and most active providers

Mapped provider and receiver locations

Phase 5 — Streamlit Dashboard

Built an interactive web app to display data insights

Added filters and search options for users

Deployed using Ngrok for Colab and local run for VS Code

🚀 How to Run the Project
Option 1: Run Locally (VS Code)

Clone the repository

Install dependencies

pip install pandas numpy matplotlib seaborn streamlit sqlite3


Run the Streamlit app

streamlit run app.py

Option 2: Run on Google Colab

Upload your app.py and cleaned datasets to Colab

Install Streamlit & Ngrok

!pip install streamlit pyngrok


Run the app with Ngrok tunnel

📈 Key Insights from the Dashboard

Top Cities with the highest number of providers and receivers

Most Donated Food Items by category

Provider & Receiver Trends over time

Geographical distribution of donations

🏆 Conclusion

This dashboard provides real-time monitoring and data-backed decision-making to reduce food wastage.
It empowers NGOs, food banks, and communities to connect surplus food with those in need, fostering sustainability and social impact.

👩‍💻 Author

Gaddala Priyadarshini
📧 Email: priyadarshinigaddala52@gmail.com
