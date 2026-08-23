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

#############################################
# Step-3: Decide Independent and Dependent variables
#############################################

print(Border)
print("Step-3: Decide Independent and Dependent variables")
print(Border)

# X : Independent variable/ Features
# Y: Dependent variables/ Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[feature_cols]
Y = df["species"]

print("X shape: ", X.shape)
print("Y shape: ", Y.shape)
