# The True Cost of Fast Fashion: A Data Analysis

A Python data analysis project exploring sustainability, worker welfare, and environmental
impact across five major fast fashion brands — Shein, Zara, H&M, Forever 21, and Uniqlo.

## Objective

Fast fashion brands generate massive social media buzz — but at what cost to workers and
the planet? This project analyzes 3,000 records spanning 2015–2024 to find out.

## Key Questions Explored

1. Which brands score highest and lowest on sustainability?
2. Is there a relationship between worker wages and ethical ratings?
3. Do brands with more social media attention tend to be less sustainable?
4. How have carbon emissions trended over time by brand?
5. Does a lower item price mean a higher hidden environmental cost?

## Key Findings

- **Sustainability scores vary widely** across brands — some invest meaningfully in
  responsible production while others lag significantly behind
- **Higher worker wages correlate with better ethical ratings**, suggesting labor
  practices and brand values are genuinely linked
- **Viral ≠ responsible** — social media popularity shows little correlation with
  sustainability performance
- **Low prices hide real costs** — cheaper brands tend to score worse on environmental
  impact, suggesting the true cost is paid by workers and ecosystems, not consumers

## Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pandas | Data loading, cleaning, aggregation |
| Matplotlib | Custom charts and visualizations |
| Seaborn | Statistical scatter plots |
| NumPy | Trend line calculation |
| Google Colab | Development environment |

## Project Structure

```
fast-fashion-analysis/
│
├── fast_fashion_brand_analysis.py   # Full analysis script
├── true_cost_fast_fashion.xlsx      # Dataset (3,000 rows × 25 columns)
├── README.md                        # This file
│
└── charts/
    ├── chart_sustainability_by_brand.png
    ├── chart_wages_vs_ethics.png
    ├── chart_social_vs_sustainability.png
    ├── chart_carbon_over_time.png
    └── chart_price_vs_sustainability.png
```

## How to Run

1. Clone this repo
2. Upload `true_cost_fast_fashion.xlsx` to your environment
3. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn openpyxl
   ```
4. Run the script:
   ```bash
   python fast_fashion_brand_analysis.py
   ```
   Or open in [Google Colab](https://colab.research.google.com/) and run all cells.

## Business Implications

- **For marketers**: Sustainability claims must be backed by data — consumers increasingly
  cross-reference brand messaging against third-party scores
- **For analysts**: Environmental cost indices and ethical ratings are becoming material
  to brand valuation, especially for ESG-focused investors
- **For businesses**: The cheapest supply chain is not always the lowest-risk one when
  accounting for reputational and regulatory exposure

## About

Created by Omar Oudrari, CIS & Marketing student with a concentration in Business Analytics
and Digital Marketing. Interested in the intersection of data, consumer behavior, and
brand strategy.

[LinkedIn](https://linkedin.com/in/omaroudrari/) · [GitHub](https://github.com/yrgomar)
