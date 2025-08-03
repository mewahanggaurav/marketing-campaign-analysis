import pandas as pd

# Load the dataset
df = pd.read_excel('marketing_campaign_data.xlsx')

# Preview the structure of the data
print("Initial Data Overview:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Data Cleaning; removing any duplicate rows
df.drop_duplicates(inplace=True)

# To ensure conversions are not greater than clicks
df['Conversions'] = df[['Clicks', 'Conversions']].min(axis=1)

# Create key performance metrics
df['CTR'] = df['Clicks'] / df['Impressions'] # Click-through rate
df['Conversion_Rate'] = df['Conversions'] / df['Clicks'] # Conversion rate
df['CPC'] = df['Ad_Spend_USD'] / df['Clicks'] # Cost per Click
df['CPA'] = df['Ad_Spend_USD'] / df['Conversions'] # Cost per Acquisition
df['ROI'] = ((df['Conversions'] * 50) - df['Ad_Spend_USD']) / df['Ad_Spend_USD'] # Assume $50 per conversion

# Exploratory Analysis
print("\nAverage ROI by Channel:")
print(df.groupby('Channel')['ROI'].mean())

print("\nAverage CPA by Audience Segment:")
print(df.groupby('Audience_Segment')['CPA'].mean())

print("\nTotal Conversions by Region:")
print(df.groupby('Region')['Conversions'].sum())

# Save Transformed Dataset
df.to_excel('enhanced_marketing_data.xlsx', index=False)
print("\nEnhanced dataset saved to 'enhanced_marketing_data.xlsx'.")
