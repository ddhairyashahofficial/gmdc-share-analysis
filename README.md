# GMDC Share Value Analysis

**Data Visualization Mini Project**  
Department of Electronics and Telecommunication Engineering  
K. J. Somaiya School of Engineering, Mumbai, India

---

## Overview

This project performs a comprehensive share value analysis of **Gujarat Mineral Development Corporation Ltd. (GMDC)** — one of India's largest state-owned mining companies — using an end-to-end pipeline of Python, Tableau, and Microsoft Power BI.

The study covers historical stock data from **2015 to 2025** and produces interactive dashboards for trend analysis, volume-price correlation, peer comparison, and KPI evaluation.

---

## Tools & Technologies

| Layer | Tool | Purpose |
|---|---|---|
| Data Collection & Preprocessing | Python (`yfinance`, `pandas`) | Fetch, clean, and export stock data |
| Visual Analytics | Tableau Desktop | Time-series dashboards, moving averages, trend storytelling |
| Business Intelligence | Microsoft Power BI | KPI cards, waterfall charts, AI-driven key influencer analysis |

---

## Repository Structure

```
gmdc-share-analysis/
│
├── data_collection.py                    # Python script to fetch & export data
│
├── data/
│   ├── gmdc_daily.csv                    # Daily OHLCV data for GMDC (2015–2025)
│   └── gmdc_and_peers_close.csv          # Closing prices: GMDC, Coal India, NMDC
│
├── tableau/
│   └── DV_miniproject_16010324044.twb    # Tableau workbook (requires Tableau Desktop)
│
├── powerbi/
│   └── DV_miniproject_16010324044.pbix   # Power BI report (requires Power BI Desktop)
│
└── report/
    └── DV_miniproject_16010324044_report.docx  # Full project report
```

---

## Dataset Description

### `gmdc_daily.csv`
Daily trading records for GMDC (`GMDCLTD.NS`) sourced from Yahoo Finance.

| Column | Description |
|---|---|
| Date | Trading date |
| Open | Opening price (₹) |
| High | Daily high (₹) |
| Low | Daily low (₹) |
| Close | Closing price (₹) |
| Volume | Number of shares traded |

### `gmdc_and_peers_close.csv`
Comparative daily closing prices for GMDC and two sector peers.

| Column | Description |
|---|---|
| Date | Trading date |
| GMDCLTD.NS | GMDC closing price |
| COALINDIA.NS | Coal India closing price |
| NMDC.NS | NMDC closing price |

---

## How to Run the Data Collection Script

### Prerequisites

```bash
pip install yfinance pandas
```

### Run

```bash
python data_collection.py
```

This generates:
- `gmdc_daily.csv` — daily OHLCV data
- `gmdc_monthly.csv` — monthly resampled data
- `gmdc_and_peers_close.csv` — peer comparison closing prices

---

## Opening the Dashboards

### Tableau
- Requires [Tableau Desktop](https://www.tableau.com/products/desktop) (or Tableau Public)
- Open `tableau/DV_miniproject_16010324044.twb`
- Point the data source to the `data/` folder if prompted

### Power BI
- Requires [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free)
- Open `powerbi/DV_miniproject_16010324044.pbix`
- Refresh the data source to point to the `data/` folder if prompted

---

## Key Visualizations

**Tableau Dashboards**
- Closing price trend (line chart, 2015–2025)
- Dual-axis chart with 20-day and 50-day moving averages
- Volume vs. Price bar chart
- Stock Overview Dashboard & Comparative Analysis Dashboard

**Power BI Dashboards**
- KPI cards: Open, Close, Daily High, Daily Low
- Combo chart: Price + Volume
- Waterfall chart: Day-to-day incremental price changes
- Key Influencer visual (AI): Volume identified as the dominant price driver
- Matrix visual: Full numerical summary of stock parameters

---

## Findings

- Moving average crossovers in Tableau revealed clear trend reversal signals throughout the analysis period.
- High trading volume periods consistently preceded significant price movements.
- Power BI's Key Influencer visual confirmed **Volume** as the strongest predictor of closing price changes.
- Tableau excels at visual storytelling and pattern discovery; Power BI at KPI-driven business intelligence — the two tools are complementary.

---

## References

1. Yahoo Finance – GMDC Stock Data
2. Tableau Software, "Tableau Desktop: Technical Documentation" — [tableau.com](https://www.tableau.com)
3. Microsoft Power BI Documentation — [learn.microsoft.com/power-bi](https://learn.microsoft.com/power-bi)
4. Amala Menon et al., "Data Visualization and Predictive Analysis for Smart Healthcare," IEEE TENCON, 2021
5. Vikas Rahate et al., "Data Analytics for Betelnut's Selling Dataset Using Tableau," IEEE ICAECT, 2021
6. VanderPlas J., "Altair: Interactive Statistical Visualizations for Python," J. Open Source Softw., vol. 3, no. 32, 2018

---

## License

This project was created as an academic mini project. Data is sourced from Yahoo Finance and is subject to their terms of use.
