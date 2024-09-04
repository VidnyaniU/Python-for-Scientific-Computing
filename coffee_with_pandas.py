import pandas as pd
import re

#1. Basic Data Inspection 

#loading the dataset and printing first 10 rows
df = pd.read_csv("coffee_survey.csv")
print("\nFirst 10 rows of the dataset :: ")
print(df.head(10))

#number of rows and columns
rows , cols = df.shape
print(f"\nNumber of rows :: {rows} and Number of columns :: {cols}\n")

#data types of each column
print("Data types of each column :: ")
print(df.dtypes)

#2. Handling Missing Data
# Identify the columns with missing data and their respective counts
missing_data_count  =df.isnull().sum()
print(f"\nColumns missing data and count :: {missing_data_count[missing_data_count>0]}\n")

#Handling columns with more than 20% missing values.
#Dropping those columns from the dataset
columns_drop = missing_data_count[missing_data_count>len(df) * 0.20].index

new_df = df.drop(columns = columns_drop)
print(new_df.head())

#3. Summary Statistics
# Generate summary statistics (mean, median, mode, etc.) for numerical columns
numerical_cols = new_df.select_dtypes(include = ["float64" , "int64"]).columns
print(f"\nSummary statistics for numerical columns :: {new_df[numerical_cols].describe()}\n")

#Analysis of how does the bitterness preference vary across different age groups?
# if "coffee_a_bitterness" in new_df.columns and "age" in new_df.columns:
#since age is an object we need it to be numeric
# new_df["age"]= pd.to_numeric(new_df["age"] ,errors="coerce")
def numeric_age(age_str):
    if isinstance(age_str, str):
        match = re.search(r'\d+', age_str)
        if match:
            return int(match.group(0))
    return pd.NA
new_df["age"] = new_df["age"].apply(numeric_age)
new_df=new_df.dropna(subset=["age"])
new_df["age"]= new_df["age"].astype(int)
age_group = pd.cut(new_df["age"] , bins=[18,30,40,50,60,100],labels=["18-30" , "31-40" , "41-50","51-60" , "60+"])
bitterness_by_age = new_df.groupby(age_group)["coffee_a_bitterness"].mean()
print(bitterness_by_age)