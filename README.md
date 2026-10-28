# SpaceX Falcon 9 First Stage Landing Prediction  -  Applied Data Science Capstone

## Executive Summary
This repository contains the end-to-end data science capstone project developed as part of the IBM Data Science Professional program. The primary objective is to predict whether the SpaceX Falcon 9 first-stage booster will land successfully after launch. 

SpaceX advertises Falcon 9 launches at approximately \$62 million, substantially undercutting traditional aerospace competitors whose launches frequently exceed \$165 million. A major contributor to this cost differential is rocket reusability - specifically the retrieval and refurbishment of the first stage. By building robust predictive models to anticipate stage recovery, competing launch providers and commercial entities can more accurately price missions, evaluate risk, and submit competitive bids for satellite payload deliveries.

---

## Core Objectives & Project Workflow

The capstone is organized into seven sequential milestones, mirroring an authentic industry data science pipeline:

### 1. SpaceX REST API Ingestion & Initial Cleaning
- **API Extraction**: Queried the official SpaceX REST API endpoint to retrieve historical launch records, booster payloads, core details, launchpads, and outcome metadata.
- **Data Preprocessing**: Extracted nested JSON entities, handled missing values, standardized numeric metrics, and constructed a clean preliminary tabular dataset for downstream analysis.

### 2. Falcon 9 Historical Web Scraping
- **HTML Parsing with BeautifulSoup**: Scraped historical Falcon 9 launch records from Wikipedia using Python's `BeautifulSoup` and `requests`.
- **DataFrame Construction**: Extracted structured tabular records from raw HTML tables, cleaned complex strings and citations, and transformed the records into a structured Pandas DataFrame.

### 3. Exploratory Data Analysis (EDA) & Target Classification Labels
- **Exploratory Data Analysis**: Analyzed relationships between payload mass, flight number, launch site, and mission success using statistical visualizations in Matplotlib and Seaborn.
- **Target Label Engineering**: Converted raw landing outcome descriptions into a binary classification target variable (`1` for successful landing on drone ship or ground pad, `0` for lost or unrecovered boosters).

### 4. Relational Database Management & SQL Analytics
- **Database Loading**: Imported the curated launch dataset into a relational database (SQLite / Db2).
- **Analytical SQL Queries**: Composed complex SQL statements (aggregations, date filtering, subqueries, and windowing) to answer specific business questions regarding launch frequencies, success rates across launchpads, and booster payload thresholds.

### 5. Geospatial Visualization & Proximity Analysis
- **Interactive Mapping with Folium**: Built dynamic geospatial maps using Folium, visualizing SpaceX launch pads at Cape Canaveral, Kennedy Space Center, and Vandenberg AFB.
- **Proximity & Cluster Analytics**: Evaluated proximity to coastlines, railways, highways, and population centers, measuring spatial distances using the Haversine formula and overlaying MarkerClusters colored by launch outcome.

### 6. Dynamic Visual Analytics with Plotly Dash
- **Interactive Dashboard**: Engineered a responsive web dashboard utilizing Plotly Dash and Dash Core Components.
- **User Controls**: Integrated interactive dropdown selectors (to isolate specific launch sites or view all sites combined) and dual-handle range sliders (to filter payload weight), dynamically updating success pie charts and payload-versus-outcome scatter plots.

### 7. Machine Learning Classification & Hyperparameter Optimization
- **Preprocessing & Encoding**: Scaled numerical features using `StandardScaler` and encoded categorical attributes via one-hot encoding (`pd.get_dummies`).
- **Algorithm Comparison**: Trained and validated four distinct classification algorithms:
  - Logistic Regression
  - Support Vector Machines (SVM)
  - Decision Tree Classifier
  - K-Nearest Neighbors (KNN)
- **Model Tuning**: Utilized `GridSearchCV` with cross-validation to search hyperparameter spaces for each candidate model and identify optimal configurations.

---

## Performance Summary & Model Results

All models were evaluated on an independent test dataset using classification accuracy:

| Model Architecture | Hyperparameter Optimization | Test Accuracy |
| :--- | :--- | :--- |
| **Decision Tree Classifier** | Optimized `criterion`, `splitter`, `max_depth` | **94.44% (0.9444)** |
| **Support Vector Machine (SVM)** | Optimized `kernel`, `C`, `gamma` | **83.33% (0.8333)** |
| **K-Nearest Neighbors (KNN)** | Optimized `n_neighbors`, `algorithm`, `p` | **83.33% (0.8333)** |
| **Logistic Regression** | Optimized `penalty`, `C`, `solver` | **83.33% (0.8333)** |

The **Decision Tree Classifier** demonstrated the strongest generalization performance on the test split, achieving an accuracy score of **0.9444**.

---

## Key Insights & Conclusion
- **Launch Site Specialization**: Success rates varied across sites, with Kennedy Space Center (KSC LC-39A) demonstrating higher success rates for heavier payloads.
- **Payload & Orbit Dynamics**: Polar and LEO orbits generally exhibited higher recovery rates compared to high-energy GTO missions where remaining fuel margins for landing burns were tight.
- **Predictive Feasibility**: Machine learning models can reliably forecast first-stage landing outcomes using readily available launch parameters, empowering analysts to estimate SpaceX's true mission operating margins.

---

## Acknowledgments
- **IBM Skills Network**: Curriculum design, starter toolkits, and lab guidance.
- **Coursera**: Course hosting and evaluation platform.
