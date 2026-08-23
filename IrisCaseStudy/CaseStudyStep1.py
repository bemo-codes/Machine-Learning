import pandas as pd

Border = "-"*30

#############################################
# Step-1: Load the data set
#############################################

print(Border)
print("Step-1: Load the data set")
print(Border)

DataPath = "iris.csv"               #Accessing iris.csv through relative path

df = pd.read_csv(DataPath)          #df = Data frame i.e 2D array ex: an excel file

print("Dataset loaded successfully")
print("Initial entries from dataset are: ")
print(df.head())
