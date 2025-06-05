# 📍 Utrecht Mobility Hub Analysis  
**Geospatial Analysis of Transport Access and Infrastructure Gaps**

---

##  Project Overview  
This project explores where new or upgraded **mobility hubs** should be located across the Province of Utrecht to meet **rising transport demand** and ensure **equitable, multimodal access**. Using a combination of **spatial datasets**, **feature engineering**, and **unsupervised clustering techniques (UMAP + HDBSCAN)**, we identified underserved zones and infrastructure mismatches to guide data-driven planning decisions.

---

##  Repository Structure

```
├── 1.0_data/ # Raw tabular and geospatial data* (jobs, housing, mobility)
├── 2.0_notebooks/ # Jupyter Notebooks for analysis (EDA, feature engineering, clustering)
│ ├── 0.0_outputs/ # Exported maps and spatial outputs (clusters, jobs, PT, etc.)
│ ├── 1.0_data_preparation_housing.ipynb
│ ├── 2.0_API_collection_OVfiets_Cargoroo_CROW.ipynb
│ ├── 2.1_shared_mobility_cleaning.ipynb
│ ├── 3.1_feature_engineering_part1.ipynb
│ ├── 3.2_feature_engineering_part2.ipynb
│ ├── 4.0_clustering_HDBSCAN_UMAP.ipynb
│ └── plotting_globals.py
├── 3.0_report/ # Final PDF report, maps, and outputs
│ └── Utrecht_Mobility_Hub_Report.pdf
├── config/ # Path config file for notebook automation
├── requirements.txt # Project dependencies
└── README.md # Project overview and instructions

\*Note: Data in `1.0_data/` was not shared on GitHub due to licensing restrictions.

```

---

##  Main Tools & Techniques

- Python (Pandas, GeoPandas, Scikit-learn, HDBSCAN, UMAP)
- QGIS for pre-processing and mapping
- Spatial joins, hexagonal aggregation (EPSG:28992)
- Clustering to identify **high-priority intervention zones**
- Feature sets based on:
  - Projected housing demand
  - Job accessibility by mode
  - Mobility hub scoring
  - PT access and shared mobility availability

---

## Project Highlights

- Conducted extensive **exploratory data analysis (EDA)** on housing growth, job distribution, and shared mobility coverage  
- Created a **hex-based accessibility model** covering all of Utrecht Province (250m resolution)  
- Engineered spatial features from multiple sources: jobs, housing projections, shared mobility availability, public transport, and mobility hubs  
- Visualized individual layers (housing, jobs, PT lines, mobility hubs) and their spatial relationships using **thematic maps**  
- Used **UMAP + HDBSCAN** to identify **clusters of unmet mobility demand** and mobility infrastructure gaps  
- Developed a custom **gap score** to rank underserved areas and guide future hub siting strategies  
- Delivered a final report with **interpretable clusters**, **summary statistics**, **maps**, and **actionable recommendations** for urban planners  


---

###  Notebook: `1.0_data_preparation_housing.ipynb`  
**Purpose:** Prepare and clean housing data for spatial analysis.

This notebook gathers, cleans, and aggregates housing development data across the Province of Utrecht. The focus is on creating geospatially aligned datasets for later analysis in feature engineering and clustering.

**Key steps:**
-  **Data sources**:
  - CBS (Centraal Bureau voor de Statistiek)
  - PDOK (Publieke Dienstverlening Op de Kaart)
  - Utrecht in Cijfers
-  **Cleaning**:
  - Standardized column names
  - Addressed missing values
  - Resolved mismatches between spatial and tabular data
-  **Aggregation**:
  - Calculated growth metrics (absolute & percentage)
  - Merged with spatial boundaries (wijk/buurt shapefiles)

**Output:** Cleaned housing dataset and geospatial layer ready for hex-based aggregation and clustering.

---


###  Notebook: `2.0_API_collection_OVfiets_Cargoroo_CROW.ipynb`  
**Purpose:** Collect real-time shared mobility data from public and private APIs.

This notebook fetches and processes data from key APIs and online sources related to shared mobility services in Utrecht. It focuses on capturing the availability and distribution of bikes, cargo bikes, and other shared vehicles.

**Key steps:**
-  **Data collection**:
  - **CROW API** – inventory of shared mobility providers
  - **Cargoroo API** – real-time cargo bike locations
  - **OV-fiets** – scraped bike station data from NS
-  **Filtering**:
  - Focused on vehicles within a 50km radius of Utrecht
  - Extracted attributes: location, type, system ID
-  **Output**:
  - Cleaned CSV files for spatial analysis and QGIS
- ⏱ **Temporal analysis**:
  - 24-hour script for capturing fluctuations in vehicle availability



---

###  Notebook: `2.1_shared_mobility_cleaning.ipynb`  
**Purpose:** Clean and consolidate shared mobility data collected via APIs.

This notebook processes 24-hour data on shared mobility vehicles (bikes, cargo bikes, cars) and prepares it for geospatial analysis and modeling.

**Key steps:**
-  **Data loading**:
  - Loaded CSVs for Cargoroo, OVFiets, and CROW data
  - Added metadata (e.g., service, modality) and extracted timestamps
-  **Data consolidation**:
  - Combined all time-sliced datasets into a single dataframe
  - Verified consistency across formats and time windows
-  **Data cleaning**:
  - Removed duplicates, handled missing `modality`, and parsed timestamps
  - Created `date_only` and `time_only` columns for temporal filtering
-  **Geospatial prep**:
  - Converted lat/lon columns into geometry points
  - Prepared output for export as GeoDataFrame
-  **Export**:
  - Cleaned full dataset and service-specific subsets saved to CSV

---

###  Notebook: `3.1_feature_engineering_part1.ipynb`  
**Purpose:** Generate spatial features for clustering analysis.

This notebook builds the core geospatial dataset by integrating multiple layers (jobs, housing, shared mobility) into a uniform hexagonal grid across Utrecht Province.

**Key steps:**
-  **Hexagonal grid creation**:
  - 250m hex grid generated and clipped to Utrecht’s boundary (EPSG:28992)
-  **Job features**:
  - Spatial join of job postings by mode (onsite, hybrid, uncertain)
  - Computed weighted and total job density per hex
-  **Housing features**:
  - Projected housing density and growth (2015–2025)
  - Spatial join with housing plans and new developments
  - Calculated planned units and development intensity scores
-  **Shared mobility features**:
  - Joined vehicle availability data (cars, bikes, scooters) to each hex
  - Prepared for clustering with further transformations in Part 2

---

### Notebook: `3.2_feature_engineering_part2.ipynb`  
**Purpose:** Finalize spatial features for clustering by integrating infrastructure and mobility access data.

This notebook continues from Part 1 and completes the geospatial feature set by incorporating accessibility indicators and infrastructure scores into a unified dataset.

**Key steps:**
-  **Feature integration**:
  - Merged job, housing, shared mobility, public transport, and bike infrastructure features into `hex_all_features`
-  **Mobility hub features**:
  - Scored each hexagon by proximity and intensity of nearby mobility hubs
-  **OV-fiets access**:
  - Flagged access to public bike stations based on 500m buffer zones
-  **Public transport lines**:
  - Calculated distance from each hex to nearest PT line
  - Derived a categorical `pt_access_score`
-  **Bike network coverage**:
  - Analyzed integration of shared mobility zones with Utrecht’s bike network
-  **Final output**:
  - Exported the unified GeoDataFrame with ~20 engineered features per hex for use in UMAP + HDBSCAN clustering

---

#### ✅ Final Selected Features for Clustering

1. `job_weighted_log`: Log-transformed weighted job count  
2. `planned_housing_units_log`: Log-transformed planned housing units  
3. `housing_density_utrecht_2025_flag`: Binary flag for 2025 housing density (high = 1, low = 0)  
4. `pt_access_score`: Composite score based on distance to public transport  
5. `hub_overall_score`: Weighted score for proximity and quality of mobility hubs  
6. `has_ovfiets_access`: Binary flag for OV-fiets access  
7. `avg_vehicle_availability`: Used as a proxy for shared mobility availability  
8. `multimodal_access`: Used for reference, but excluded from UMAP due to binary structure

---

#### 🔧 Transformations Applied 

- **Log transformations** were used on skewed variables (`job_weighted`, `planned_housing_units`) to stabilize variance.  
- **New features** were engineered (`pt_access_score`, `hub_overall_score`) using weighted scoring systems based on multimodality and hub types.  
- Some distance-based variables were removed or replaced to reduce redundancy and improve clustering performance.


---

### Notebook: `4.0_clustering_HDBSCAN_UMAP.ipynb`  
**Purpose:** Segment Utrecht’s spatial landscape using unsupervised clustering to reveal latent mobility patterns.

This notebook applies **UMAP** for dimensionality reduction and **HDBSCAN** for clustering on hex-based geospatial features representing accessibility, mobility demand, and infrastructure.

**Key steps:**
- Loaded the final geospatial feature set (`hex_all_features`)
- Scaled selected features using `RobustScaler` to reduce outlier impact
- Applied **UMAP** to embed high-dimensional data in 2D space
- Ran **HDBSCAN** with various `min_cluster_size` and `min_samples` to explore stable groupings
- Evaluated clustering results:
  - Silhouette scores
  - Percentage of noise points
  - Cluster balance
- Mapped clusters back to hexes for spatial interpretation

**Features used in clustering included:**
- `log_vehicle_availability`
- `has_ovfiets_access`
- `hub_distance_score`
- `hub_overall_score`
- `pt_access_score`
- `job_weighted_log`
- `planned_housing_units_log`
- `housing_density_utrecht_2025_flag`

**Output:**  
Cluster labels assigned to each hex, visualizations of group characteristics, and interpretation of spatial disparities.

---



*Note: These notebooks are intended for code review only – the raw datasets accessed via API or loaded from disk are not included in this repository.*



## 📄 Final Report

📥 [Download the full PDF](3.0_report/Utrecht_Mobility_Hub_Analysis_Full_Report.pdf)  
📍 Includes methodology, maps, feature summaries, clustering results, and planning insights.


---

## 📬 Contact

Project by Manoela Calabresi
📧 manoela.calabresi@gmail.com
🌍 https://bit.ly/Utrecht_Mobility_Analysis
