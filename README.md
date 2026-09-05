# Atlantic Cod Population Genetics
A reproducible population genetics project using publicly available microsatellite genotype data from Atlantic cod (*Gadus morhua*).

## Project Statust. 
Project started (August 2026)
This project documents my step-by-step learning journey in population genetics, Python, R, and Git/GitHub using a public Atlantic cod datase. The project is independent of my Master's thesis and uses only publicly available data.

## Project Overview
This project explores genetic diversity in Atlantic cod using microsatellite genotype data.

## Objectives
- Explore and organize the genotype data.
- Calculate observed heterozygosity (Ho).
- Calculate expected heterozygosity (He).
- Compare genetic diversity among sampling locations.
- Visualize population genetic patterns using Python.

## Methods
- Data exploration and quality checking
- Population ggrouping by sampling location
- Microsatellite genotype analysis 
- Calculation of observed heterozygosity (Ho)
- Calculation of expected heterozygosity (He)
- Visualization using Python and Matplotlib

## Results
The analysis generates population-level estimates of observed heterozygosity (Ho) and expected heterozygosity(He).
The results are summerized by sampling location and microsatellite marker.
### 1. Observed Heterozygosity by Location
This visualization shows observed heterozygosity (Ho) across the sampled locations. Differences among locations indicate variation in the proportion of individuals carrying different alleles at the analyzed microsatellite loci.
### 2. Expected Heterozygosity by locaation
Expected Heterozygosity (He) provides an estimate of genetic diversity based on allele frequencies ithin each location. Comparing He among locations helps describe differences in genetic diversity across the sampled groups.
### 3. Observed vs expected Heterozygosityby Location
This comparison shows Ho and He for each sampling location. Differences between observed and expected heterozygosity provide an overview of how the observed genetic diversity compares with expectations based on allele frequencies.
### 4. Average Observed Heterozygosity by Marker
This visualization compares the average Ho among microsatellite markers. it highlited differences in the level of genetic variation captued by individual markers.
### 5. Observed Heterozygosity Heatmap
The heatmap provides a location-by-marker overview of observed heterozygosity. It allows patterns of genetic diversity to be compared simultaneously across sampling locations and microsatellite loci.
### 6. Observed vs Expected Heterozygosity Scatter Plot
Each point represents a location-marker observation. The dashed diagonal line represents equal observed and expected heterozygosty (HO = He). The plot provides a visual assessment of how losely observed values correspond to expected values across the dataset.
### 7. Mean Observed and Expected Heterozygosity by Location
This Visualization compares the mean Ho and He values for each sampling location. It shows an overall summary of genetic diversity and the relationship between observed and expected heterozygosity among locations.
### 8. Mean Observed and Expected Heterozygosity by Marker
This graph compares mean Ho and He across the microsatellite markers. it indicates differences among markers in the genetic diversity observed in the sampled dataset.
### 9. Allele Diversity by Microsatellite Marker
This graph represents the number of different alleles observed for each microsatellite marker in the public Atlantic cod dataset. Differnces among markers indicates variation in the level of allelic diversity captured by individual microsatellite loci.

## Tools
- Python
- Pandas
- Matplotlib
- Vs Code
- Git and GitHub

## Dataset
The dataset contains microsatellite genotype using information for Atlantic cod sampled from multiple geographic locations.
The original dataset was obtained from a published scientific study and is included in this repository fpr reproduciblity.

## Project Structure
 - Data
 - 01_explore_dat.py
 - 02_population_analysis.py
 - 03_visualization.py
 - population_heterozygosity_results.csv
 - README.md

 ## Future work
 - Calculate additional population genetic statistics.
 - Explore genetic differentiation among locations.
 - Add futher visualizations of popuulation genetic diversity.
 ## Conclusion
 This project demonstrates a reproducible workflow for exploring microsatellite genetic diversity in Atlantic cod using a publicly available dataet. The analysis examined observed an expected heterozygosity and allele diversity across sampling locations and microsatellite markers. Puthon-based data processing and visualization were used to summerized patterns of genetic diversity variation.
 ## Limitation
 The analysis id intended as eploratory and educational bioinformatics project. The dataset contains uneven sample sizes among sampling locations, including locatiions represented by very few individuals. Therefore, the results should be inerpreted descriptively rather than as definitive evidence of population differentiatin. the analysis uses pulicly available data and is completely independent of confidential Master's thesis data.
 ## Data Source
 The genotype was obtained from Dryad:
 Andre et al. -Population structure in Atlantic cod in eastern North Sea-Skagerrak-Kattegat: early life stage of dispersal and adult migration.
 DOI: 10.5061/dryad.m3913