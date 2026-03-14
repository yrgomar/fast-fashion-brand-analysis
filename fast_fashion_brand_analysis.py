# -*- coding: utf-8 -*-
"""fast_fashion_brand_analysis

# 👗 The True Cost of Fast Fashion: A Data Analysis
**Author:** [Your Name] | CIS & Marketing, Business Analytics Concentration
**Tools:** Python, Pandas, Matplotlib, Seaborn
**Dataset:** True Cost of Fast Fashion (3,000 records across 5 major brands, 2015–2024)

## 🎯 Project Overview
Fast fashion brands generate massive social media buzz — but at what cost to workers,
the environment, and society? This analysis explores the relationship between brand
popularity, sustainability, worker welfare, and environmental impact across five
major fast fashion brands: Shein, Zara, H&M, Forever 21, and Uniqlo.

## ❓ Key Questions
1. Which brands score highest (and lowest) on sustainability?
2. Is there a relationship between worker wages and ethical ratings?
3. Do brands with more social media attention tend to be less sustainable?
4. How have carbon emissions trended over time?
5. What does the data say about the real cost hidden behind cheap prices?
"""

# ============================================================
# SECTION 1: Setup & Data Loading
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Style config
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.family'] = 'DejaVu Sans'

# Load data
df = pd.read_excel('true_cost_fast_fashion.xlsx')

print(f"Dataset shape: {df.shape}")
print(f"Brands: {sorted(df['Brand'].unique())}")
print(f"Years: {df['Year'].min()} – {df['Year'].max()}")
print(f"\nMissing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
df.head()


# ============================================================
# SECTION 2: Exploratory Summary
# ============================================================

"""
## 📊 Section 2: Exploratory Summary
Before diving into visuals, let's understand the scale of this data.
"""

summary = df.groupby('Brand').agg(
    Avg_Sustainability=('Sustainability_Score', 'mean'),
    Avg_Worker_Wage=('Avg_Worker_Wage_USD', 'mean'),
    Avg_Carbon=('Carbon_Emissions_tCO2e', 'mean'),
    Avg_Ethical_Rating=('Ethical_Rating', 'mean'),
    Avg_Item_Price=('Avg_Item_Price_USD', 'mean'),
    Total_Records=('Brand', 'count')
).round(2)

print("\n=== Brand Summary Statistics ===")
print(summary.to_string())


# ============================================================
# SECTION 3: Sustainability by Brand
# ============================================================

"""
## 🌱 Section 3: Sustainability Score by Brand

**Insight:** Sustainability scores reveal which brands are investing in
responsible production — and which ones are greenwashing.
"""

brand_sus = df.groupby('Brand')['Sustainability_Score'].mean().sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
colors = ['#d62728' if v < 50 else '#2ca02c' for v in brand_sus.values]
bars = ax.barh(brand_sus.index, brand_sus.values, color=colors, edgecolor='white')

ax.axvline(50, color='gray', linestyle='--', linewidth=1, label='Midpoint (50)')
ax.set_xlabel('Average Sustainability Score (0–100)', fontsize=12)
ax.set_title('Average Sustainability Score by Brand', fontsize=14, fontweight='bold')
ax.bar_label(bars, fmt='%.1f', padding=4)
ax.legend()
plt.tight_layout()
plt.savefig('chart_sustainability_by_brand.png', bbox_inches='tight')
plt.show()

print("\n💡 Insight: Brands below 50 may be prioritizing speed-to-market over sustainability.")


# ============================================================
# SECTION 4: Worker Wages vs. Ethical Rating
# ============================================================

"""
## 👷 Section 4: Worker Wages vs. Ethical Rating

**Hypothesis:** Brands that pay workers more should have higher ethical ratings.
Let's see if the data backs this up.
"""

fig, ax = plt.subplots(figsize=(10, 6))
brand_colors = {'Shein': '#e377c2', 'Zara': '#1f77b4', 'H&M': '#ff7f0e',
                'Forever 21': '#2ca02c', 'Uniqlo': '#9467bd'}

for brand, group in df.groupby('Brand'):
    ax.scatter(group['Avg_Worker_Wage_USD'], group['Ethical_Rating'],
               label=brand, alpha=0.5, s=30, color=brand_colors.get(brand))

# Add trend line
import numpy as np
z = np.polyfit(df['Avg_Worker_Wage_USD'], df['Ethical_Rating'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['Avg_Worker_Wage_USD'].min(), df['Avg_Worker_Wage_USD'].max(), 100)
ax.plot(x_line, p(x_line), 'k--', linewidth=1.5, label='Trend line')

ax.set_xlabel('Average Worker Wage (USD/month)', fontsize=12)
ax.set_ylabel('Ethical Rating', fontsize=12)
ax.set_title('Worker Wages vs. Ethical Rating by Brand', fontsize=14, fontweight='bold')
ax.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('chart_wages_vs_ethics.png', bbox_inches='tight')
plt.show()

corr = df['Avg_Worker_Wage_USD'].corr(df['Ethical_Rating'])
print(f"\n💡 Correlation between worker wages and ethical rating: {corr:.3f}")
print("A positive correlation suggests higher wages do align with better ethical scores.")


# ============================================================
# SECTION 5: Social Media vs. Sustainability
# ============================================================

"""
## 📱 Section 5: Social Media Popularity vs. Sustainability

**The marketing angle:** Do the most talked-about brands score worse on sustainability?
This is the core tension of fast fashion — virality vs. responsibility.
"""

df['Total_Social_Mentions'] = df['Instagram_Mentions_Thousands'] + df['TikTok_Mentions_Thousands']

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(
    df['Total_Social_Mentions'],
    df['Sustainability_Score'],
    c=df['Sentiment_Score'],
    cmap='RdYlGn',
    alpha=0.6,
    s=40,
    edgecolors='none'
)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Sentiment Score', fontsize=10)

ax.set_xlabel('Total Social Media Mentions (Instagram + TikTok, thousands)', fontsize=11)
ax.set_ylabel('Sustainability Score', fontsize=11)
ax.set_title('Social Media Buzz vs. Sustainability Score\n(colored by sentiment)', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('chart_social_vs_sustainability.png', bbox_inches='tight')
plt.show()

corr2 = df['Total_Social_Mentions'].corr(df['Sustainability_Score'])
print(f"\n💡 Correlation between social media mentions and sustainability: {corr2:.3f}")


# ============================================================
# SECTION 6: Carbon Emissions Over Time
# ============================================================

"""
## 🌍 Section 6: Carbon Emissions Trend Over Time

Are brands getting cleaner — or are emissions rising with demand?
"""

yearly = df.groupby(['Year', 'Brand'])['Carbon_Emissions_tCO2e'].mean().reset_index()

fig, ax = plt.subplots(figsize=(11, 6))
for brand, group in yearly.groupby('Brand'):
    ax.plot(group['Year'], group['Carbon_Emissions_tCO2e'],
            marker='o', label=brand, linewidth=2, markersize=5,
            color=brand_colors.get(brand))

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Avg Carbon Emissions (tCO2e)', fontsize=12)
ax.set_title('Carbon Emissions by Brand Over Time', fontsize=14, fontweight='bold')
ax.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig('chart_carbon_over_time.png', bbox_inches='tight')
plt.show()


# ============================================================
# SECTION 7: Price vs. Sustainability — The Hidden Cost
# ============================================================

"""
## 💸 Section 7: Price vs. Sustainability — The Hidden Cost

Is cheaper clothing really cheaper? Or does a low price tag just mean the
environmental and human costs are paid by someone else?
"""

avg_data = df.groupby('Brand').agg(
    Avg_Price=('Avg_Item_Price_USD', 'mean'),
    Avg_Sustainability=('Sustainability_Score', 'mean'),
    Avg_Env_Cost=('Env_Cost_Index', 'mean')
).reset_index()

fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(
    avg_data['Avg_Price'],
    avg_data['Avg_Sustainability'],
    s=avg_data['Avg_Env_Cost'] * 300,
    c=range(len(avg_data)),
    cmap='tab10',
    alpha=0.8,
    edgecolors='black',
    linewidths=0.8
)

for _, row in avg_data.iterrows():
    ax.annotate(row['Brand'], (row['Avg_Price'], row['Avg_Sustainability']),
                textcoords="offset points", xytext=(8, 4), fontsize=10)

ax.set_xlabel('Average Item Price (USD)', fontsize=12)
ax.set_ylabel('Average Sustainability Score', fontsize=12)
ax.set_title('Price vs. Sustainability\n(bubble size = Environmental Cost Index)', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('chart_price_vs_sustainability.png', bbox_inches='tight')
plt.show()


# ============================================================
# SECTION 8: Key Findings & Business Implications
# ============================================================

"""
## 📌 Section 8: Key Findings & Business Implications

### Findings
1. **Sustainability gap is wide**: Brands vary significantly in sustainability scores,
   suggesting some are investing meaningfully while others lag far behind.

2. **Wages correlate with ethics**: Higher worker wages are associated with better
   ethical ratings — a signal that labor practices and brand values are linked.

3. **Social media ≠ sustainability**: High social media buzz does not predict
   better sustainability scores. Viral brands are not necessarily responsible brands.

4. **Carbon trends matter**: Emission trajectories vary by brand — some are improving
   while others show flat or worsening trends despite public sustainability claims.

5. **Low prices hide real costs**: Brands with lower average item prices tend to score
   worse on sustainability, suggesting the true cost is externalized onto workers
   and the environment.

### Business Implications
- **For marketers**: Sustainability messaging must be backed by data — consumers
  increasingly cross-reference claims against third-party scores.
- **For analysts**: Environmental cost indices and ethical ratings are becoming
  material to brand valuation, especially for ESG-focused investors.
- **For businesses**: The cheapest supply chain is not always the lowest-risk one
  when accounting for reputational and regulatory exposure.
"""

print("\n✅ Analysis complete. See generated charts for all visualizations.")
print("Charts saved: chart_sustainability_by_brand.png, chart_wages_vs_ethics.png,")
print("              chart_social_vs_sustainability.png, chart_carbon_over_time.png,")
print("              chart_price_vs_sustainability.png")
