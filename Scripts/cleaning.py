"""
cleaning.py — Data Cleaning Module for VoltBike E-bike Analysis
---------------------------------------------------------------

This script handles structured data cleaning and validation, including:
    • Text normalization
    • Data type adjustments
    • Unit removal (motor_power) and numeric conversion
    • Duplicate and negative value detection
    • Missing value review
    • Outlier identification using IQR

⚠ Analytical Decision:
    No missing value imputation or outlier removal has been applied.
    Values are retained intentionally to avoid masking potential insights
    during statistical analysis and to preserve analytical traceability.

Output:
    → Cleaned dataset exported to results/final_data.csv
    → Validation report printed to console

Author: Asma — Data Analyst
"""

import os
import pandas as pd
import numpy as np

"""
Load, validate, and clean the e-bike dataset.

Notes:
- Dataset is validated but not modified (no imputation).
- Decision based on maintaining analytical integrity.
- Cleaning actions help improve consistency without altering raw values.
"""

# Load dataset
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_path, "data", "ebike_data.csv")
ebike = pd.read_csv(input_path)
    
# Basic schema validation – required columns used in analysis & visualization
required_columns = [
    "bike_type",
    "production_cost",
    "assembly_time",
    "customer_score"]
missing_columns = [col for col in required_columns if col not in ebike.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

initial_shape = ebike.shape
# ------------------------------------------------------------
# Core Validations & Cleaning Logic
# ------------------------------------------------------------

# Duplicate check
duplicate_count = ebike.duplicated().sum()

# Text normalization
text_cols = ["bike_type", "frame_material", "battery_type"]
for col in text_cols:
    ebike[col] = ebike[col].str.lower().str.strip()

# Replace placeholder values (e.g., "-") with NaN
ebike["battery_type"] = ebike["battery_type"].replace("-", np.nan)

# Convert to categorical where appropriate
ebike["bike_type"] = ebike["bike_type"].astype("category")

# Remove 'W' from motor_power and convert to float
ebike["motor_power"] = (ebike["motor_power"].str.replace("W", "", regex=True).astype(float))

# Missing value assessment
missing_summary = ebike.isna().sum()

# Negative value check
negative_cost_count = ebike[ebike["production_cost"] < 0].shape[0]

# Outlier detection using IQR
outlier_summary = {}
for col in ["production_cost", "assembly_time", "customer_score"]:
    Q1 = ebike[col].quantile(0.25)
    Q3 = ebike[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = ebike[(ebike[col] < lower) | (ebike[col] > upper )]
    # distribution of outliers by bike type
    outlier_summary[col] = outliers["bike_type"].value_counts().to_dict() 
    
# ------------------------------------------------------------
# Export Dataset — Without Data Modification
# ------------------------------------------------------------
output_path = os.path.join(base_path, "results","final_data.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
ebike.to_csv(output_path, index=False)

# Output summary
print("\n===== Data Cleaning Summary (No Imputation Applied) =====")
print(f"Missing columns: {missing_columns}")
print(f"Dataset Shape → Initial: {initial_shape} | Final: {ebike.shape}")

print(f"Duplicate Entries Detected: {duplicate_count}")
print(f"Negative Production Cost Records: {negative_cost_count}\n")

print("Missing Values by Column:")
print(missing_summary)

print("\nOutlier Distribution (kept in dataset for analysis):")
for col, values in outlier_summary.items():
    print(f"  - {col}: {values if values else 'No outliers detected'}")

print("\n✔ Dataset exported without alteration →", output_path)
print("⚠ Raw values preserved to prevent analytical distortion.")
print("===========================================================\n")
print("🏁 Cleaning process completed.\n")


