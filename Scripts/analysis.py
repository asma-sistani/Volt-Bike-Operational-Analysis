"""
analysis.py — Analytical Computations for VoltBike E-bike Data
--------------------------------------------------------------

This module performs numerical/statistical analysis including:
    • Aggregated KPI computation (mean per bike type)
    • Summary statistics (mean, std)
    • Assembly time variability and impact analysis
    • Pearson correlations (cost vs satisfaction, assembly_time vs cost and satisfaction)
    • Outlier detection for key variables

Output:
    → Printed summaries
    → Analysis results returned as dictionaries (for visualization module if required)
"""

import os
import pandas as pd
import numpy as np

# Load dataset
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_path, "results", "final_data.csv")
ebike = pd.read_csv(input_path)

# Validate required columns before running analysis
required_columns = [
        "bike_type",
        "production_cost",
        "assembly_time",
        "customer_score"]

missing_columns = [col for col in required_columns if col not in ebike.columns]
if missing_columns:
    raise ValueError(f"Analysis aborted — missing required column(s): {missing_columns}")        

# Average metrics by bike type
bike_performance = {
        "cost": ebike.groupby("bike_type", observed=True)["production_cost"].mean().round(2),
        "assembly": ebike.groupby("bike_type", observed=True)["assembly_time"].mean().round(2),
        "satisfaction": ebike.groupby("bike_type", observed=True)["customer_score"].mean().round(2),
    }

# General summary statistics
stats = {
    "production_cost_mean": round(ebike["production_cost"].mean(), 2),
    "production_cost_sd": round(ebike["production_cost"].std(ddof=1), 2),
    "production_cost_min": ebike["production_cost"].min(),
    "production_cost_max": ebike["production_cost"].max(),

    "customer_score_mean": round(ebike["customer_score"].mean(), 2),
    "customer_score_sd": round(ebike["customer_score"].std(ddof=1), 2),
    "customer_score_min": ebike["customer_score"].min(),
    "customer_score_max": ebike["customer_score"].max(),     
            
    "assembly_time_mean": round(ebike["assembly_time"].mean(), 2),
    "assembly_time_sd": round(ebike["assembly_time"].std(ddof=1), 2),
    "assembly_time_min": ebike["assembly_time"].min(),
    "assembly_time_max": ebike["assembly_time"].max()
    }

# Detect outliers for all key variables using IQR (without removal)
outlier_summary = {}
for col in ["production_cost", "assembly_time", "customer_score"]:
    Q1 = ebike[col].quantile(0.25)
    Q3 = ebike[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outlier_summary[col] = int(((ebike[col] < lower) | (ebike[col] > upper)).sum())

# Assembly time variability analysis (IQR trimming ONLY for assembly time)
Q1 = ebike["assembly_time"].quantile(0.25)
Q3 = ebike["assembly_time"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
data_trim = ebike[
        (ebike["assembly_time"] >= lower) &
        (ebike["assembly_time"] <= upper)]

assembly_summary = data_trim.groupby("bike_type", observed=True)["assembly_time"].agg(
    min="min", max="max", std="std", mean="mean").round(2)

# Correlations

corr_cost_vs_satisfaction = round(np.corrcoef(
    ebike["production_cost"], ebike["customer_score"])[0, 1], 2)

corr_assembly_vs_satisfaction = round(np.corrcoef(
    ebike["assembly_time"], ebike["customer_score"])[0, 1], 4)

corr_assembly_vs_cost = round(np.corrcoef(
    ebike["assembly_time"], ebike["production_cost"])[0, 1], 4)

# Calculate proximity to mean (on trimmed data)
mean_trim = data_trim["assembly_time"].mean()
within_5 = ((data_trim["assembly_time"] >= mean_trim * 0.95) &
        (data_trim["assembly_time"] <= mean_trim * 1.05)).mean() * 100
within_10 = ((data_trim["assembly_time"] >= mean_trim * 0.90) &
            (data_trim["assembly_time"] <= mean_trim * 1.10)).mean() * 100

results = {
        "bike_performance": bike_performance,
        "stats": stats,
        "assembly_summary": assembly_summary.to_dict(),
        "correlations": {
            "cost_vs_satisfaction": corr_cost_vs_satisfaction,
            "assembly_vs_satisfaction": corr_assembly_vs_satisfaction,
            "assembly_vs_cost": corr_assembly_vs_cost
        },
        "outliers": outlier_summary,
        "variability": {
            "records_original": len(ebike),
            "records_trimmed": len(data_trim),
            "within_5_percent": round(within_5, 2),
            "within_10_percent": round(within_10, 2)
        }
    }

# Output summary

print("\n================= Data Analysis Summary =================")
for k, v in results.items():
    print(k)
    print(v)
    print("=========================================================\n")

print("\n📊 Analysis Completed")
print("=========================================================\n")







    