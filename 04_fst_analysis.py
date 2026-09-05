import pandas as pd
data = pd.read_excel("data/Raw/Andre+cod+msat+dryad.xlsx", engine="openpyxl")
markers = ["Gmo2", "Gmo3", "Gmo8", "Gmo19", "Gmo34", "Gmo35", "Gmo132", "Tch5"]
results = []
for marker in markers:
    alleles = pd.concat([data[marker], data[marker + ".1"]]).dropna()
    number_of_alleles = alleles.nunique()
    results.append([marker, number_of_alleles])
    allele_summary = pd.DataFrame(results, columns=["Marker", "Number_of_alleles"])
    print("\nAllele diversity by marker:")
    print(allele_summary)
    allele_summary.to_csv("allele_diversity_by_marker.csv", index=False)
    print("\nResults saved to allele_diversity_by_marker.csv")
