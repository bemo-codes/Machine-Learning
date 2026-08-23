import pandas as pd

Border = "-"*30

#############################################
# Step-1: Load the data set
#############################################

print(Border)
print("Step-1: Load the data set")
print(Border)

DataPath = "iris.csv"               

df = pd.read_csv(DataPath)          

print("Dataset loaded successfully")
print("Initial entries from dataset are: ")
print(df.head())

#############################################
# Step-2: Exploratory Data Analysis (EDA)
#############################################

print(Border)
print("Step-2: Exploratory Data Analysis (EDA)")
print(Border)

print("Shape of dataset: ", df.shape)

print("Column names: ", list(df.columns))

print("Missing values per column: ")
print(df.isnull().sum())                    #Cannonical function call

print("Class distribution (species count): ")
print(df["species"].value_counts())

print("Statistical report of dataset: ")
print(df.describe())