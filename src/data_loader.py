import pandas as pd

def load_data(path):
    return pd.read_csv(path)

# Example usage:
df = load_data(r"C:\Users\omrak\OneDrive\Desktop\predict-customer-churn\data\Churn_Modelling.csv")
print(df.head())
