"""
visualization.py — VoltBike E-bike Analysis
-------------------------------------------

    • Clear structure, explicit logic
    • Minimal abstraction (reader-friendly)
    • Professional visuals without over-engineering
    • Manual annotation placement for full control

Charts generated:
    1. Average Production Cost by Bike Type
    2. Average Assembly Time by Bike Type
    3. Average Customer Satisfaction by Bike Type
    4. ASSEMBLY TIME VARIABILITY (BOXPLOT WITHOUT OUTLIERS)
    5. CUSTOMER SATISFACTION VARIABILITY (BOXPLOT WITH OUTLIERS)
    6. PRODUCTION COST vs SATISFACTION
    7. ASSEMBLY TIME vs SATISFACTION

Author: Asma — Data Analyst
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ========== GLOBAL STYLE ==========
sns.set_style("white")  
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.labelsize": 14,
    "axes.labelweight": "bold",
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

BAR_COLOR = "#1F77B4"  # Consistent blue tone

"""
Generate visualizations for the e-bike dataset.
Straightforward coding style — intentionally explicit.
"""

# Load data
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_path, "results", "final_data.csv")
output_path = os.path.join(base_path, "visuals")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
ebike = pd.read_csv(input_path)

# Standardize bike type formatting for clean display
ebike["bike_type"] = ebike["bike_type"].str.title()

# -------------------------------------------------
# 1. AVG PRODUCTION COST
# -------------------------------------------------
bike_cost = ebike.groupby("bike_type")["production_cost"].mean().reset_index()
bike_cost = bike_cost.round(2).sort_values("production_cost", ascending=False)

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=bike_cost, x="production_cost", y="bike_type", color=BAR_COLOR)
    
padding = (bike_cost["production_cost"].max() - bike_cost["production_cost"].min()) * 0.05
for i, v in enumerate(bike_cost["production_cost"]):
    ax.text(v + padding * 0.5 ,i,f"{v:.2f}",va="center",ha="left",fontweight="bold",fontsize=12)

plt.title("Average Production Cost by Bike Type", pad=20)  
plt.xlabel("Production Cost ($)")
plt.ylabel("Bike Type")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xlim(bike_cost["production_cost"].min() - padding, bike_cost["production_cost"].max() + padding * 2)

plt.tight_layout()
plt.savefig(os.path.join(output_path, "avg_production_cost.png"), bbox_inches="tight")
plt.close()

# -------------------------------------------------
# 2. AVG ASSEMBLY TIME
# -------------------------------------------------
bike_assembly = ebike.groupby("bike_type")["assembly_time"].mean().reset_index()
bike_assembly = bike_assembly.round(2).sort_values("assembly_time", ascending=False)

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=bike_assembly, x="assembly_time", y="bike_type", color=BAR_COLOR)
    
padding = (bike_assembly["assembly_time"].max() -  bike_assembly["assembly_time"].min()) * 0.05
for i, v in enumerate(bike_assembly["assembly_time"]):
    ax.text(v + padding * 0.5 ,i,f"{v:.2f}",va="center",ha="left",fontweight="bold",fontsize=12)

plt.title("Average Assembly Time by Bike Type", pad=20)
plt.xlabel("Assembly Time (minutes)")
plt.ylabel("Bike Type")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xlim(bike_assembly["assembly_time"].min() - padding, bike_assembly["assembly_time"].max() + padding * 2)

plt.tight_layout()
plt.savefig(os.path.join(output_path, "avg_assembly_time.png"), bbox_inches="tight")
plt.close()

# -------------------------------------------------
# 3. AVG CUSTOMER SATISFACTION
# -------------------------------------------------
bike_satisfaction = ebike.groupby("bike_type")["customer_score"].mean().reset_index()
bike_satisfaction = bike_satisfaction.round(2).sort_values("customer_score", ascending=False)

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=bike_satisfaction, x="customer_score", y="bike_type", color=BAR_COLOR)
    
padding = (bike_satisfaction["customer_score"].max() - bike_satisfaction["customer_score"].min()) * 0.05
for i, v in enumerate(bike_satisfaction["customer_score"]):
    ax.text(v + padding * 0.5 ,i,f"{v:.2f}",va="center",ha="left",fontweight="bold",fontsize=12)

plt.title("Average Customer Satisfaction by Bike Type", pad=20)  
plt.xlabel("Customer Satisfaction Score")
plt.ylabel("Bike Type")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xlim(bike_satisfaction["customer_score"].min() - padding, bike_satisfaction["customer_score"].max() + padding * 2)

plt.tight_layout()
plt.savefig(os.path.join(output_path, "avg_customer_satisfaction.png"),bbox_inches="tight")
plt.close()
    
# -------------------------------------------------
# 4. ASSEMBLY TIME VARIABILITY (BOXPLOT WITHOUT OUTLIERS)
# -------------------------------------------------
# Prepare trimmed dataset (same logic as analysis)
Q1 = ebike["assembly_time"].quantile(0.25)
Q3 = ebike["assembly_time"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

data_trim = ebike[
    (ebike["assembly_time"] >= lower) &
    (ebike["assembly_time"] <= upper)]
    
plt.figure(figsize=(10, 6))
ax = sns.boxplot(data=data_trim, x="bike_type", y="assembly_time", color=BAR_COLOR)

group_means = data_trim.groupby("bike_type")["assembly_time"].mean()
for i, (bike, mean_val) in enumerate(group_means.items()):
    ax.text(
        i, mean_val,
        f"{mean_val:.2f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

plt.title("Assembly Time Variability by Bike Type (After Outlier Removal)", pad=20)
plt.xlabel("Bike Type")
plt.ylabel("Assembly Time (minutes)")

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_path, "assembly_time_variability.png"), bbox_inches="tight")
plt.close()

# -------------------------------------------------
# 5. CUSTOMER SATISFACTION VARIABILITY (BOXPLOT WITH OUTLIERS)
# -------------------------------------------------

plt.figure(figsize=(10, 6))

# Boxplot with all data – do NOT trim outliers
ax = sns.boxplot(data=ebike, x="bike_type", y="customer_score", color=BAR_COLOR)

# Retrieve and highlight outliers
Q1 = ebike["customer_score"].quantile(0.25)
Q3 = ebike["customer_score"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = ebike[(ebike["customer_score"] < lower) | (ebike["customer_score"] > upper)] 
# NOTE: Outliers detected based on customer_score (decision-focused analysis)


# Plot outliers separately (if any)
if not outliers.empty:
    sns.scatterplot(data=outliers, x="bike_type", y="customer_score",
                    edgecolor="red", facecolor="none", s=120, label="Outliers")

# Add mean values as text
group_means = ebike.groupby("bike_type")["customer_score"].mean()
for i, (bike, mean_val) in enumerate(group_means.items()):
    ax.text(
        i, mean_val,
        f"{mean_val:.2f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color="black"
        )

plt.title("Customer Satisfaction Variability by Bike Type", pad=20)
plt.xlabel("Bike Type")
plt.ylabel("Customer Satisfaction")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_path, "customer_satisfaction_variability.png"), bbox_inches="tight")
plt.close()

# -------------------------------------------------
# 6. PRODUCTION COST vs SATISFACTION
# -------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(data=ebike, x="production_cost", y="customer_score", s=45, alpha=0.6, color=BAR_COLOR)
sns.regplot(data=ebike, x="production_cost", y="customer_score", scatter=False, line_kws={"linewidth": 2})
 
# Highlight outliers if desired
if not outliers.empty:
    sns.scatterplot(
        data= outliers, 
        x="production_cost", 
        y="customer_score",
        edgecolor="red", 
        facecolor="none", 
        s=120, 
        label="Outliers"
    )
corr = np.corrcoef(ebike["production_cost"], ebike["customer_score"])[0, 1]
r_squared = corr ** 2
plt.text(
    ebike["production_cost"].max() * 0.99,
    ebike["customer_score"].max() * 0.97,
    f"R² = {r_squared:.3f}",
    fontsize=12,
    fontweight="bold",
    ha='right',
    va='top',
)  
plt.title("Production Cost vs Customer Satisfaction", pad=20)  
plt.xlabel("Production Cost ($)")
plt.ylabel("Customer Satisfaction Score")

plt.tight_layout()
plt.savefig(os.path.join(output_path, "cost_vs_satisfaction.png"),bbox_inches="tight")
plt.close()
    
# -------------------------------------------------
# 7. ASSEMBLY TIME vs SATISFACTION
# -------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(data=ebike, x="assembly_time", y="customer_score", s=45, alpha=0.6, color=BAR_COLOR)
sns.regplot(data=ebike, x="assembly_time", y="customer_score", scatter=False, line_kws={"linewidth": 2})
 
# Highlight outliers if desired
if not outliers.empty:
    sns.scatterplot(
        data=outliers, 
        x="assembly_time", 
        y="customer_score",
        edgecolor="red", 
        facecolor="none", 
        s=120, 
        label="Outliers"
    )
corr = np.corrcoef(ebike["assembly_time"], ebike["customer_score"])[0, 1]
r_squared = corr ** 2
plt.text(
    ebike["assembly_time"].max() * 0.99,
    ebike["customer_score"].max() * 0.95,
    f"R² = {r_squared:.4f}",
    fontsize=12,
    fontweight="bold",
    ha='right',
    va='top',
    )

plt.title("Assembly Time vs Customer Satisfaction", pad=20)  
plt.xlabel("Assembly Time (minutes)")
plt.ylabel("Customer Satisfaction Score")

plt.tight_layout()
plt.savefig(os.path.join(output_path, "assembly_time_vs_satisfaction.png"),bbox_inches="tight")
plt.close()
    
# -------------------------------------------------
# Final message
# -------------------------------------------------
print("\n📊 Visualization Completed")
print("=========================================================\n")
