import pandas as pd
data = pd.read_excel("data/Raw/Andre+cod+msat+dryad.xlsx", sheet_name="Andre")
marker_columns = data.columns[1:17]
marker_names = data.columns[1:17:2]
print(data.head())
print("Population groups:")
print(data["Location"].value_counts())
print("Observed heterozygosity (Ho) by population:")
for location, group in data.groupby("Location"):
    print("\nPopulation:", location)
    for marker in marker_names:
        genotypes = group[[marker, marker + ".1"]].dropna()
        heterozygous = genotypes[marker] != genotypes[marker + ".1"]
        Ho = heterozygous.mean()
        print(marker, ":", round(Ho, 4))
        marker_columns = data.columns[1:17]
        print("\nExpected heterozygosity (He) by location:")
        for location in data["Location"].dropna().unique():
            location_data = data[data["Location"] == location]
            print("\n", location)
            for i in range(0, len(marker_columns), 2):
                marker1 = marker_columns[i]
                marker2 = marker_columns[i + 1]
                alleles = pd.concat([location_data[marker1], location_data[marker2]]).dropna()
                frequencies = alleles.value_counts(normalize=True)
                He = 1 - (frequencies ** 2).sum()
                print(marker1, ":", round(He, 4))  
            population_results = []
            for location, group in data.groupby("Location"):
                for i in range(0, len(marker_columns), 2):
                    marker1 = marker_columns[i]
                    marker2 = marker_columns[i + 1]
                    genotypes = group[[marker1, marker2]].dropna()
                    Ho = (genotypes[marker1] != genotypes[marker2]).mean()
                    alleles = pd.concat([group[marker1], group[marker2]])
                    frequencies = alleles.value_counts(normalize=True)
                    He = 1 - (frequencies ** 2).sum()
                    population_results.append([location, marker1, Ho, He])
                    population_results_df = pd.DataFrame(population_results, columns=["Location", "Marker", "Ho", "He"])
                    print("\npopulation results:")
                    print(population_results_df)