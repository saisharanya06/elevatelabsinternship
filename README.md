step1:Data Cleaning and Preprocessing


Preprocessing and Cleaning of the Marketing Campaign Dataset:
This repository contains the code and the resulting cleaned dataset from the preprocessing of the marketing_campaign.csv file. The goal of this process was to prepare the data for subsequent analysis or machine learning tasks by handling common data quality issues.

Preprocessing Steps:
Missing Values: The Income column contained missing values. These were handled by imputing them with the median value of the column, a robust method that is not heavily influenced by outliers.
Irrelevant Column Removal: Columns such as Z_CostContact, Z_Revenue, and ID were dropped as they were either constant values or unique identifiers that would not be useful for most analytical models.
Feature Engineering: New, more meaningful features were created from the existing data:
Age was calculated from the Year_Birth column.
Customer_Tenure_Days was calculated from the Dt_Customer column to measure customer loyalty.
Total_Spent was created by summing all the individual product spending columns, providing a single metric for overall customer value.
Data Type Conversion: The Dt_Customer column was converted to a proper datetime format to facilitate time-based calculations.
Categorical Data Cleaning: The Marital_Status column had inconsistent values (e.g., 'Absurd', 'YOLO', 'Alone'). These were standardized and grouped into a single, clean 'Single' category.

Resulting Dataset:
The final output is a cleaned and preprocessed CSV file named preprocessed_marketing_campaign.csv. This dataset is now ready for exploratory data analysis (EDA), visualization, or machine learning model training.
