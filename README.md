# Cropora - Field Intelligence Platform

Cropora is a geospatial field intelligence platform built on eleven years of public satellite data over Iowa cropland. It combines crop phenology analysis, rotation classification, soil moisture anomaly detection, and machine learning to produce a 2024 crop type projection and a composite Field Resilience Score for every cropland pixel in Iowa.

---

## What it does

- Extracts NDVI phenological curves for corn and soybean using MODIS satellite composites
- Classifies Iowa cropland pixels into regular rotation, monoculture, or irregular categories using an 11-year CDL time series
- Trains two Random Forest classifiers: one using NDVI phenological features (78% accuracy) and one using CDL crop history (96% accuracy)
- Projects 2024 crop type (corn vs. soybean) for every Iowa cropland pixel with a pixel-level confidence score
- Computes a Field Resilience Score (0-100) combining rotation consistency, crop diversity, and recent land use stability
- Visualizes all outputs in an interactive Streamlit dashboard with a region selector, live Iowa map, and what-if rotation threshold slider

---

## Data Sources

| Dataset | Source | Resolution | Period |
|---|---|---|---|
| Cropland Data Layer (CDL) | USDA NASS via CropScape API | 30m, annual | 2013-2023 |
| MODIS NDVI (MOD13Q1.061) | NASA AppEEARS | 250m, 16-day | 2022 |
| SMAP L4 Soil Moisture (SPL4SMGP.008) | NASA AppEEARS | 9km, 3-hourly | 2022 |

All datasets are publicly accessible and free to use.

---

## Project Structure

```
cropora/
├── Task1_NDVI_Analysis.ipynb
├── Task2_Crop_Rotation.ipynb
├── Task3_Soil_Moisture_Anomaly.ipynb
├── app.py
├── requirements.txt
├── README.md
└── outputs/
    ├── task1_ndvi_phenology.png
    ├── task1_ndvi_classifier.png
    ├── task2_rotation_map.png
    ├── task2_transition_rate_hist.png
    ├── task2_2024_projection.png
    ├── task3_smap_timeseries.png
    ├── task3_smap_anomaly_maps.png
    ├── task4_rf_evaluation.png
    ├── task4_rf_prediction_map.png
    ├── resilience_score_map.png
    ├── task1_ndvi_stats.csv
    ├── task2_rotation_stats.csv
    ├── task2_2024_projection_stats.csv
    └── resilience_by_region.csv
```

---

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cropora.git
cd cropora
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Data download

**CDL:** Downloaded automatically by the notebooks via the USDA CropScape REST API.

**NDVI:** Download from NASA AppEEARS (https://appeears.earthdatacloud.nasa.gov):
- Product: MOD13Q1.061, Layer: 250m_16_days_NDVI
- Iowa bounding box, Date: 01/01/2022 to 12/31/2022
- Output: GeoTIFF, Geographic projection
- Place files in outputs/ndvi/

**SMAP:** Same AppEEARS portal:
- Product: SPL4SMGP.008, Layer: Geophysical_Data_sm_surface
- Same Iowa bounding box, Date: 05/01/2022 to 09/30/2022
- Output: NetCDF, Geographic projection
- Place the .nc file in outputs/smap/

**Iowa bounding box GeoJSON:**
```json
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "properties": {},
    "geometry": {
      "type": "Polygon",
      "coordinates": [[
        [-96.6, 40.4], [-90.1, 40.4],
        [-90.1, 43.5], [-96.6, 43.5],
        [-96.6, 40.4]
      ]]
    }
  }]
}
```

### 4. Run the notebooks

Run notebooks in order: Task 1, Task 2, Task 3. Update BASE_DIR in Cell 3 of each notebook to match your folder path.

### 5. Run the dashboard

```bash
streamlit run app.py
```

All output images and CSVs must be in the same folder as app.py.

---

## Key Results

| Output | Value |
|---|---|
| Corn peak NDVI | 0.874 (July 12, 2022) |
| Soybean peak NDVI | 0.867 (August 13, 2022) |
| Green-up lag | 32 days (soybean lags corn) |
| NDVI-only classifier accuracy | 78% |
| CDL history classifier accuracy | 96% |
| Iowa regular rotation | 68.3% of cropland |
| Iowa monoculture | 24.9% of cropland |
| 2024 projection confidence | 0.856 mean |
| High resilience fields | 66.7% of Iowa cropland |

---

## Methodology Notes

**Rotation classification** uses a transition rate metric: the fraction of consecutive year pairs where a pixel alternates between corn and soybean. A threshold of 0.60 classifies a pixel as regular rotation. The dashboard includes a what-if slider to explore how this threshold affects the statewide distribution.

**Field Resilience Score** is a weighted composite: rotation consistency (50%), crop diversity as measured by the corn-soy balance ratio (30%), and recent stability defined as the fraction of the last three years in the corn-soy system (20%).

**2024 projection** applies rotation logic to the 2023 CDL: regular rotation pixels flip crop type, monoculture pixels retain their dominant historical crop, and irregular pixels use a majority vote of the last three years.

**SMAP anomaly detection** computes Z-scores relative to the 2022 seasonal mean. A multi-year baseline would produce more robust anomaly estimates and is noted as a limitation.

---

## Limitations

- CDL stack was downsampled from 30m to 300m to fit within memory constraints.
- SMAP anomalies are computed against a single-year seasonal baseline rather than a multi-year climatology.
- The 2024 projection assumes rotation behavior is stationary. Market shocks or extreme weather could cause fields to deviate from historical patterns.

---
