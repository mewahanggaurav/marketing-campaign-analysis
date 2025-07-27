📊 Marketing Campaign Performance Analysis

This project simulates a real-world marketing data analysis scenario where 10,000 rows of campaign performance data were analyzed using Python and Tableau. The goal was to derive actionable insights to improve marketing ROI, reduce customer acquisition costs, and optimize overall campaign performance across various channels and audience segments.

---

🧠 Project Objectives

- Analyze marketing campaign data to uncover key performance drivers
- Create KPIs such as CTR, Conversion Rate, CPA, and ROI
- Visualize the data to highlight performance differences across:
  - Marketing channels (Email, Social Media, Paid Search)
  - Audience segments (Students, Professionals, Parents, Retirees)
  - Regional performance (Northeast, Midwest, South, West)
- Build a Tableau dashboard for interactive, executive-level insights
- Practice and demonstrate end-to-end data analysis workflow for portfolio use

---

## 📁 Dataset Overview

- **Total Records**: 10,000 rows
- **Simulated Fields**:
  - `Campaign_ID`: Unique identifier for each marketing campaign
  - `Channel`: Source of campaign (Email, Social Media, Paid Search)
  - `Region`: Geographic area (Northeast, Midwest, South, West)
  - `Audience_Segment`: Customer segment (Students, Professionals, Parents, Retirees)
  - `Impressions`: Number of times ads were shown
  - `Clicks`: Number of ad clicks
  - `Conversions`: Successful actions (e.g., purchases or sign-ups)
  - `Ad_Spend_USD`: Advertising cost per campaign
  - `Date`: Timestamp of campaign activity

---

## 🧪 Steps Performed

### 1. 📥 Data Loading & Inspection
- Loaded the `.xlsx` file using `pandas`
- Inspected structure, checked for nulls, and validated data types

### 2. 🧹 Data Cleaning
- Removed duplicate records
- Ensured logical consistency (e.g., Conversions ≤ Clicks)
- Formatted timestamps and ensured numerical columns were correct

### 3. 🛠 Feature Engineering
Calculated key performance indicators:
- Click-Through Rate (CTR) = Clicks / Impressions
- Conversion Rate = Conversions / Clicks
- Cost Per Click (CPC)** = Ad Spend / Clicks
- **Cost Per Acquisition (CPA)** = Ad Spend / Conversions
- **Return on Investment (ROI)** = ((Conversions × \$50) - Ad Spend) / Ad Spend

### 4. 📊 Exploratory Data Analysis
- Aggregated metrics by `Channel`, `Region`, and `Audience_Segment`
- Compared ROI, CPA, and conversion rates across different segments
- Identified top-performing channels and customer groups

### 5. 📈 Tableau Dashboard
- Built an interactive dashboard in Tableau using the enhanced dataset
- Key visuals:
  - ROI by Channel
  - CPA by Region
  - Conversion Rate by Audience Segment
  - CTR trend over time
- Filters: Channel, Region, Date Range

---

## 📂 Project Files

| File Name | Description |
|-----------|-------------|
| `marketing_campaign_data.xlsx` | Original simulated dataset |
| `analysis.py` | Python script for data cleaning, transformation, and analysis |
| `enhanced_marketing_data.xlsx` | Final processed dataset ready for Tableau |
| `dashboard_screenshots/` | Screenshots of Tableau dashboards |
| `README.md` | Project documentation |
| `tableau_dashboard_link.txt` | Link to live Tableau dashboard *(optional)* |

---

## 📌 Key Insights

- 📈 **Social Media** campaigns generated the highest average ROI.
- 💰 **Parents** were the most cost-effective audience segment based on CPA.
- 🌎 **Midwest** region had the most efficient conversion rates.
- 📉 **Email** had the lowest CTR but highest conversion rate, suggesting it works well for targeted audiences.

---

## 🚀 Skills Demonstrated

- Data Cleaning & Transformation (Pandas, Excel)
- Metric Definition & Business Logic
- Analytical Thinking (ROI, CAC, CTR, etc.)
- Data Visualization & Dashboard Design (Tableau)
- Communication of Findings (via visuals and narrative)
- GitHub project structuring & documentation

---

## 🔗 View Tableau Dashboard

📍 **[Click here to view the Tableau Public Dashboard](#)**  
*(Replace with your actual Tableau Public link)*

---

## 🤝 Connect With Me

- 📧 [mewahanggaurav@gmail.com](mailto:mewahanggaurav@gmail.com)
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/YOUR-LINKEDIN)
- 🧠 Portfolio Website (Coming Soon)

---

