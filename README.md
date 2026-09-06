# Atlantic Cod Population Genetics

A reproducible population genetics project using publicly available microsatellite genotype data from Atlantic cod (*Gadus morhua*).

## Project Status

Project started: August 2026

This project demonstrates a reproducible workflow for exploring population genetic variation in Atlantic cod using publicly available microsatellite genotype data. The analysis was conducted independently using public data and does not use confidential research datasets.

## Project Overview

This project explores genetic diversity in Atlantic cod using microsatellite genotype data from multiple sampling locations.

The analysis focuses on observed and expected heterozygosity and allelic diversity across sampling locations and microsatellite markers.

## Objectives

- Explore and organize microsatellite genotype data.
- Perform data quality checking and preprocessing.
- Calculate observed heterozygosity (Ho).
- Calculate expected heterozygosity (He).
- Examine genetic diversity across sampling locations.
- Compare genetic diversity among microsatellite markers.
- Calculate allele diversity for individual markers.
- Develop reproducible data-analysis and visualization workflows using Python.

## Methods

- Data exploration and quality checking
- Population grouping by sampling location
- Microsatellite genotype analysis
- Calculation of observed heterozygosity (Ho)
- Calculation of expected heterozygosity (He)
- Calculation of allele diversity
- Statistical data processing using Pandas
- Data visualization using Matplotlib
- Reproducible analysis using Python and Git/GitHub

## Results

The analysis generated population-level and marker-level summaries of genetic diversity, including observed heterozygosity (Ho), expected heterozygosity (He), and allele diversity.

### 1. Observed Heterozygosity by Location

This visualization shows observed heterozygosity (Ho) across the sampled locations. Differences among locations indicate variation in the proportion of individuals carrying different alleles across the analyzed microsatellite loci.

### 2. Expected Heterozygosity by Location

Expected heterozygosity (He) provides an estimate of genetic diversity based on allele frequencies within each sampling location. Comparing He among locations provides a descriptive overview of differences in genetic diversity across the sampled groups.

### 3. Observed vs Expected Heterozygosity by Location

This comparison shows observed (Ho) and expected (He) heterozygosity for each sampling location. Differences between observed and expected heterozygosity provide an overview of how observed genetic diversity compares with expectations based on allele frequencies.

### 4. Average Observed Heterozygosity by Marker

This visualization compares average observed heterozygosity among microsatellite markers. It highlights differences in the level of genetic variation captured by individual microsatellite loci.

### 5. Observed Heterozygosity Heatmap

The heatmap provides a location-by-marker overview of observed heterozygosity. It allows patterns of genetic diversity to be compared simultaneously across sampling locations and microsatellite loci.

### 6. Observed vs Expected Heterozygosity Scatter Plot

Each point represents a location-marker observation. The dashed diagonal line represents equal observed and expected heterozygosity (Ho = He). The plot provides a visual assessment of the relationship between observed and expected heterozygosity across the dataset.

### 7. Mean Observed and Expected Heterozygosity by Location

This visualization compares mean Ho and He values for each sampling location. It provides an overall summary of genetic diversity and the relationship between observed and expected heterozygosity among locations.

### 8. Mean Observed and Expected Heterozygosity by Marker

This visualization compares mean Ho and He across microsatellite markers. It highlights differences among markers in the level of genetic diversity observed in the sampled dataset.

### 9. Allele Diversity by Microsatellite Marker

This visualization shows the number of different alleles observed for each microsatellite marker in the public Atlantic cod dataset. Differences among markers indicate variation in the level of allelic diversity captured by individual microsatellite loci.

## Tools

- Python
- Pandas
- Matplotlib
- Visual Studio Code
- Git
- GitHub

## Dataset

The dataset contains microsatellite genotype information for Atlantic cod sampled from multiple geographic locations.

The original genotype dataset was obtained from a published scientific study and is used here as a publicly available dataset for reproducible analysis.

## Project Structure

Atlantic_cod_population_genetics/
│
├── data/
│   └── Raw/
│       └── Andre+cod+msat+dryad.xlsx
│
├── 01_explore_data.py
├── 02_population_analysis.py
├── 03_visualization.py
├── 04_fst_analysis.py
│
├── population_heterozygosity_results.csv
├── allele_diversity_by_marker.csv
│
├── Ho_by_location.png
├── He_by_location.png
├── Ho_vs_He_by_location.png
├── Mean_Ho_by_marker.png
├── Ho_heatmap.png
├── Ho_vs_He_scatter.png
├── Mean_Ho_He_by_location.png
├── Mean_Ho_He_by_marker.png
├── Allele_diversity_by_marker.png
│
└── README.md

## Future Work

- Calculate additional population genetic statistics.
- Explore genetic differentiation among sampling locations.
- Extend the analysis with additional population genetic metrics.
- Develop further visualizations of genetic diversity and population structure.

## Conclusion

This project demonstrates a reproducible workflow for exploring microsatellite genetic diversity in Atlantic cod using a publicly available dataset.

The analysis examined observed heterozygosity, expected heterozygosity, and allele diversity across sampling locations and microsatellite markers. Python-based data processing and visualization were used to summarize patterns of genetic variation and develop a reproducible bioinformatics workflow.

## Limitations

This analysis is intended as an exploratory bioinformatics project. The dataset contains uneven sample sizes among sampling locations, including locations represented by relatively few individuals. Therefore, the results should be interpreted descriptively rather than as definitive evidence of population differentiation.

The analysis uses publicly available data and is independent of confidential research datasets.

## Data Source

The genotype dataset was obtained from Dryad:

André et al. — *Population structure in Atlantic cod in the eastern North Sea-Skagerrak-Kattegat: early life stage dispersal and adult migration.*

DOI: 10.5061/dryad.m3913
