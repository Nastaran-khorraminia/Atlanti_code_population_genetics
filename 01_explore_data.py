import pandas as pd
file_path = "data/Raw/Andre+cod+msat+dryad.xlsx"
data = pd.read_excel(file_path, sheet_name="Andre")
print(data.head())
print(data.columns.tolist())
print(data.info())
print("Number of individuals:", len(data))
print(data.isnull().sum())
print(data.columns.tolist())
print(data["Location"].value_counts())
print("Missing values by column:")
print(data.isnull().sum())
print("Genetic marker columns:")
print(data.columns[:16].tolist())
marker_columns = data.columns[1:17]
print("Number of genetic marker columns:", len(marker_columns))
marker_names = data.columns[1:17:2]
print("Microsatellite markers:")
print(marker_names.tolist())
print("Available data for each allele column:")
print(data[marker_columns].notnull().sum())
print("Missing data percentahe by marker:")
for marker in marker_names:
    coll = marker
    col2 = marker + ".1"
    missing = data[[coll, col2]].isnull().any(axis=1).sum()
    percentage = (missing/ len(data)) * 100
    print(marker, ":", round(percentage, 2), "%")
    print("Numbe of unique alleles by maeker:")
    for marker in marker_names:
        coll = marker
        col2 = marker + ".1"
        alleles = pd.concat([data[coll], data[col2]]).dropna().unique()
        print(marker, ":", len(alleles))
        print("Gmo2 allele frequencies:")
        alleles = pd.concat([data["Gmo2"], data["Gmo2.1"]]).dropna()
        print(alleles.value_counts(normalize=True))
        allele_counts = alleles.value_counts().sort_index()
        allele_frequencies = allele_counts/ len(alleles)
        print(allele_frequencies)
        print("Allele frequencies by marker:")
        for marker in marker_names:
            alleles = pd.concat([data[marker], data[marker + ".1"]]).dropna()
            allele_counts = alleles.value_counts().sort_index()
            allele_frequencies = allele_counts/ len(alleles)
            print("\n", marker)
            print(allele_frequencies)