import pandas as pd

# Load the dataset with a tab delimiter
df = pd.read_csv('data/marketing_campaign.csv', delimiter='\t')

# Display the initial info and head of the dataset
print("Initial Info:")
print(df.info())
print("\nInitial Head:")
print(df.head())

# Drop the constant columns
df = df.drop(['Z_CostContact', 'Z_Revenue', 'ID'], axis=1)

# Impute missing 'Income' values with the median
df['Income'] = df['Income'].fillna(df['Income'].median())

# Convert 'Dt_Customer' to a datetime object and create 'Customer_Tenure_Days'
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
df['Customer_Tenure_Days'] = (pd.to_datetime('2014-10-18') - df['Dt_Customer']).dt.days

# Create 'Age' from 'Year_Birth' and drop 'Year_Birth'
df['Age'] = 2024 - df['Year_Birth']
df = df.drop('Year_Birth', axis=1)

# Create 'Total_Spent' from product spending columns
product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df['Total_Spent'] = df[product_columns].sum(axis=1)

# Clean and categorize 'Marital_Status'
df['Marital_Status'] = df['Marital_Status'].replace(['Absurd', 'YOLO', 'Alone'], 'Single')
df['Marital_Status'] = df['Marital_Status'].replace(['Together'], 'Married')

# Display the info and head of the preprocessed dataset
print("\nPreprocessed Info:")
print(df.info())
print("\nPreprocessed Head:")
print(df.head())

# Save the preprocessed DataFrame to a new CSV file
df.to_csv('preprocessed_marketing_campaign.csv', index=False)