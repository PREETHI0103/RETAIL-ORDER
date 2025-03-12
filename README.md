# Retail Orders Data Analysis

## Project Overview
This project focuses on analyzing a retail orders dataset from Kaggle using Python in Google Colab. It involves data cleaning, database management, SQL queries, and data visualization to extract valuable business insights. The final product is an interactive Streamlit application hosted via Ngrok.

## Technologies Used
- **Python** (Google Colab)
- **Pandas** (Data Cleaning & Processing)
- **MySQL & PyMySQL** (Database Management)
- **TiDB Cloud** (Distributed SQL Database)
- **SQLAlchemy** (Database Connection & Query Execution)
- **Tabulate** (Displaying SQL Query Results in Tabular Format)
- **Streamlit** (Interactive Web App for Data Visualization)
- **Altair** (Declarative Statistical Visualization)
- **Ngrok** (Hosting Streamlit App Online)

## Project Workflow
### 1. **Dataset Acquisition & Preprocessing**
- Downloaded the dataset as a ZIP file from Kaggle.
- Unzipped and mounted it to Google Drive for access in Colab.
- Used Pandas to clean the data:
  - Handled missing values by replacing them with `0`.
  - Standardized column names for better readability.
- Split the dataset into two tables based on relevant grouping conditions.

### 2. **Database Setup & Management**
- Installed MySQL and PyMySQL in Google Colab.
- Established a connection between MySQL and TiDB Cloud using **Authtoken** authentication.
- Created a database titled **"Retail Orders"** in TiDB Cloud.
- Used SQLAlchemy to move the structured data into TiDB.
- Set primary and foreign keys to ensure data integrity and establish relationships between tables.

### 3. **SQL Query Execution & Analysis**
- Over **20 SQL queries** were executed to analyze various aspects, including:
  - Order trends (YoY, MoM analysis)
  - Product performance (top revenue & profit-generating items)
  - Subcategories with highest profit margins
  etc.

### 4. **Data Visualization & Streamlit Integration**
- Installed **Tabulate** in Colab to fetch and display query results in tabular format.
- Built an interactive **Streamlit** web app to present SQL query results dynamically.
- Used **Altair** to create intuitive charts for deeper insights into sales trends and customer behavior.

### 5. **Deploying Streamlit App with Ngrok**
- Since Google Colab does not natively support Streamlit, **Ngrok** was used to create a secure tunnel.
- This allowed hosting the Streamlit app online and sharing it for interactive exploration.

## Key Features
- **Data Cleaning & Preprocessing** using Pandas
- **SQL Database Management** with MySQL, PyMySQL & TiDB Cloud
- **Automated Query Execution** via PyMySQL
- **Dynamic Visualizations** using Altair in Streamlit
- **Live Web App Hosting** with Ngrok

## How to Run the Project
### Prerequisites
Ensure you have the following installed:
- Google Colab (or local Jupyter Notebook)
- MySQL & PyMySQL
- TiDB Cloud account
- Python libraries: `pandas`, `sqlalchemy`, `tabulate`, `streamlit`, `altair`, `ngrok`

### Steps to Run
1. Download the dataset from Kaggle and upload it to Google Drive.
2. Open the Google Colab notebook and execute the data preprocessing steps.
3. Connect to TiDB Cloud and run the SQL queries for analysis.
4. Launch the Streamlit app and visualize the results interactively.
5. Use Ngrok to generate a public URL for accessing the app online.

## Conclusion
This project demonstrates an end-to-end pipeline for **retail data analysis**, integrating multiple tools to process, store, analyze, and visualize data. The final Streamlit app provides a user-friendly way to explore key business insights, supporting data-driven decision-making.
