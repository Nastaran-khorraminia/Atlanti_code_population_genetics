import pandas as pd
file_path = "data/Raw/Andre+cod+msat+dryad.xlsx"
data = pd.read_excel(file_path, sheet_name="Andre")
print(data.head())
print(data.columns.tolist())
print(data.info())
print("Number of individuals:", len(data))
print(data.isnull().sum())