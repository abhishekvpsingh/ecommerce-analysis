
# 🛒 End-to-End E-commerce Sales Analysis with dbt, Snowflake, and Python

> 🚀 A complete, production-style data pipeline project showcasing your skills in **Python**, **Snowflake**, and **dbt**.

---

## 📌 Project Overview

This project demonstrates how to build and orchestrate a modern data pipeline to perform e-commerce sales analytics. It extracts raw data (public or simulated), loads it into **Snowflake**, transforms it using **dbt**, and optionally analyzes insights using **Python**.

### ✅ Key Features
- 🔄 Automated ETL pipeline using Python & dbt
- 🧊 Cloud data warehousing with Snowflake
- 🧱 Modular SQL transformations (staging → intermediate → final)
- 📈 Optional data analysis & visualization using Python
- 🤖 Optional orchestration using a single command

---

## 🏗️ Architecture Diagram

```text
          +---------------------+
          | Public Dataset OR   |
          | Simulated Orders    |
          +----------+----------+
                     |
                     v
          +---------------------+
          |  extract_data.py    |   <-- Python script to fetch or simulate data
          +----------+----------+
                     |
                     v
          +---------------------+
          |   load_data.py      |   <-- Upload to Snowflake & COPY INTO staging tables
          +----------+----------+
                     |
                     v
          +---------------------+
          | Snowflake Staging   |
          +----------+----------+
                     |
                     v
          +-------------------------------+
          |         dbt Models            |
          |-------------------------------|
          |  staging → intermediate → final|
          +-------------------------------+
                     |
                     v
          +-----------------------------+
          | Final Analysis Tables       |
          +-----------------------------+
                     |
                     v
          [Optional] Python Analysis 📊
```

---

## 📦 Data Source

- **Dataset**: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) (UCI Repository)  
- Includes:
  - Invoice & transaction history
  - Product, quantity, price
  - Timestamps and customer metadata
- 💡 Optionally, simulate your own using `extract_data.py`

---

## 🛠️ Tools & Technologies

| Tool          | Purpose                                  |
|---------------|------------------------------------------|
| **Python**    | Data extraction, loading, and orchestration |
| **Snowflake** | Cloud data warehouse for storage & compute |
| **dbt**       | Data transformation & analytics modeling   |
| **pandas**    | Optional in-Python analytics               |
| **seaborn**   | Optional data visualizations               |
| **Git**       | Version control & GitHub showcase          |

---

## ⚙️ Setup Instructions

<details>
<summary><strong>🔐 1. Snowflake Configuration</strong></summary>

Use `snowflake_commands.txt` to set up:

- A dedicated **role** (e.g., `DBT_ROLE`)
- A **user** (e.g., `dbt_user`)
- A **warehouse** (e.g., `ECOMMERCE_WH`)
- A **database** and **schema** (e.g., `ECOMMERCE_DB.STAGING`)
</details>

<details>
<summary><strong>📁 2. Clone This Repository</strong></summary>

```bash
git clone https://github.com/abhishekvpsingh/e-commerce-analysis.git
cd e-commerce-analysis
```
</details>

<details>
<summary><strong>🐍 3. Set Up Python Environment</strong></summary>

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
</details>

<details>
<summary><strong>🔧 4. Configure dbt Profile</strong></summary>

Create `~/.dbt/profiles.yml`:

```yaml
ecommerce_analysis:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: <your_account>
      user: dbt_user
      password: <your_password>
      role: DBT_ROLE
      database: ECOMMERCE_DB
      warehouse: ECOMMERCE_WH
      schema: STAGING
      threads: 1
```
</details>

---

## ▶️ How to Run the Pipeline

```bash
# Step 1: Extract or simulate data
python python_scripts/extract_data.py

# Step 2: Load into Snowflake staging
python python_scripts/load_data.py

# Step 3: Transform with dbt
cd dbt_ecommerce_analysis
dbt run

# Step 4: [Optional] Orchestrate it all
python python_scripts/orchestrate_pipeline.py
```

---

## 🧠 dbt Model Layers

| Layer        | Description |
|--------------|-------------|
| **staging/** | Cleans and standardizes raw data from Snowflake |
| **intermediate/** | Joins tables, computes metrics like `total_order_value` |
| **final/** | Business-ready reporting tables |
  
### 📊 Final Output Examples
- 📅 Monthly Sales Summaries  
- 🔝 Top Products by Revenue  
- 👥 Customer Segmentation (by RFM or spend)  
- 🧮 Cohort or time-based analysis

---

## 🔮 Potential Next Steps

- 🔁 Use Airflow or Prefect for scalable orchestration  
- 🔍 Build visual dashboards (Streamlit, Tableau, Power BI)  
- ✅ Add CI/CD via GitHub Actions for dbt  
- 🧪 Implement data quality checks using dbt tests  
- 📊 Add clustering or ML-based customer segmentation  

---

## 📂 Project Structure

```text
e-commerce-analysis/
├── data/                         # Optional: small sample datasets
├── snowflake_commands.txt        # SQL setup scripts
├── dbt_ecommerce_analysis/       # dbt project
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── final/
│   ├── macros/
│   ├── analyses/
│   ├── seeds/
│   ├── tests/
│   ├── dbt_project.yml
│   └── profiles.yml
├── python_scripts/               # ETL and orchestration
│   ├── extract_data.py
│   ├── load_data.py
│   └── orchestrate_pipeline.py
├── requirements.txt              # Python dependencies
├── README.md
└── .gitignore
```

---

## 👨‍💻 Your Contributions

This project showcases your ability to:
- 💡 Design end-to-end pipelines
- ⚙️ Implement cloud-native ETL on Snowflake
- 🧱 Build modular dbt transformations
- 🤖 Orchestrate workflows using Python
- 🧑‍🎓 Apply data engineering principles in real-world scenarios

---

Let me know if you'd like me to turn this into a GitHub README file ready to upload — or if you'd like to add badges, license, or sample charts for visual punch!
