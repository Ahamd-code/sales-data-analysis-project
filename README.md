# Sales Data Analysis Project

## Project Overview
This project analyzes retail sales data for an e-commerce company to uncover business insights about product performance, regional trends, and monthly sales patterns.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Git & GitHub

## Dataset
- **Source:** Superstore Sales Dataset (Kaggle)
- **Size:** 9,994 rows × 21 columns
- **Fields:** Orders, Products, Regions, Dates, Sales, Profit

## Key Business Insights
- **West region** generates the highest total revenue
- **November** is the peak sales month, likely driven by holiday demand
- A small number of high-value technology products drive a large share of revenue

## Project Structure
sales-data-analysis/
├── data/
│   ├── raw/              # Original dataset (never modified)
│   └── processed/        # Cleaned dataset
├── notebooks/            # EDA and exploration
├── src/
│   ├── data_cleaning.py  # Cleaning logic
│   └── analysis.py       # Analysis logic
├── outputs/
│   ├── figures/          # Charts and visualizations
│   └── reports/          # Summary reports
├── README.md
└── requirements.txt

## How to Run
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run analysis: `python src/analysis.py`

## Future Improvements
- Add interactive dashboard (Streamlit)
- Automate daily reporting pipeline
- Introduce sales forecasting with machine learning