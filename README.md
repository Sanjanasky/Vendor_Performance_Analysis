# Vendor Performance Analysis 📊

## 📌 Project Overview

This project focuses on analyzing vendor performance using purchasing, sales, and inventory data to generate **data-driven insights** that help improve procurement efficiency, reduce costs, and optimize inventory management.

The analysis combines **SQL, Python (Pandas, NumPy), statistical methods, and data visualization** to evaluate vendor profitability, pricing behavior, bulk purchase benefits, and capital locked in unsold inventory.

---

## 🎯 Objectives

* Evaluate **vendor-wise sales, purchases, and profitability**
* Identify **top-performing vs low-performing vendors**
* Analyze whether **bulk purchasing reduces unit price**
* Measure **capital locked in unsold inventory per vendor**
* Perform **statistical validation** using confidence intervals and hypothesis testing
* Provide actionable insights for **vendor optimization and cost savings**

---

## 🗂️ Dataset Description

The project uses multiple CSV files ingested into an SQLite database:

* `sales.csv` → Sales transactions
* `purchases.csv` → Purchase records
* `purchase_prices.csv` → Vendor pricing data
* `begin_inventory.csv` → Opening inventory
* `end_inventory.csv` → Closing inventory
* `vendor_invoice.csv` → Vendor billing details

All datasets are ingested into **SQLite (`inventory.db`)** using SQLAlchemy.

---

## 🛠️ Tech Stack

* **Python** (Pandas, NumPy)
* **SQLite** (via SQLAlchemy)
* **Matplotlib & Seaborn** (Data Visualization)
* **SciPy** (Statistical Analysis)
* **Jupyter Notebook**

---

## 📊 Key Analyses Performed

### 1️⃣ Vendor Performance Summary

* Total sales, purchases, gross profit, and profit margins per vendor
* Identification of **top and low-performing vendors**

### 2️⃣ Bulk Purchase Analysis

* Order sizes categorized using quantiles (Small / Medium / Large)
* Unit price comparison across order sizes
* **Confidence Interval analysis** to validate bulk purchase savings

### 3️⃣ Inventory Risk Analysis

* Calculation of **Unsold Inventory Value** per vendor
* Identification of vendors with **highest capital lock-in**
* Pareto analysis to highlight critical vendors

### 4️⃣ Statistical Testing

* **95% Confidence Intervals** for profit margins
* **Welch’s Two-Sample T-Test** to compare top vs low vendors
* Effect size estimation (Cohen’s d)

---

## 📈 Visualizations

* Distribution plots for profit margins
* Boxplots comparing unit prices by order size
* Pareto charts for vendor purchase contribution
* Donut charts for capital locked in inventory
* Confidence interval comparison plots

---

## 🔍 Key Insights

* Bulk purchasing **significantly reduces unit prices** for several vendors
* A small group of vendors contributes to the **majority of inventory lock-in**
* Top-performing vendors show **higher and more stable profit margins**
* Statistical tests confirm **significant differences** between top and low vendors

---

## 📁 Project Structure

```
vendor_performance_analysis/
│
├── data/                     # Raw CSV files
├── inventory.db              # SQLite database
├── notebooks/                # Jupyter notebooks
├── logs/                     # Ingestion logs
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/vendor-performance-analysis.git
```

2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run Jupyter Notebook

```bash
jupyter notebook
```

---


## 👤 Author

**Sanjana Yadav**
Aspiring Data Analyst | Python | SQL | Data Visualization

---

⭐ If you found this project useful, feel free to star the repository!
