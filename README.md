<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=E50914&center=true&vCenter=true&width=600&lines=🎬+Netflix+Analytics+Project;Python+%2B+SQL+%2B+Power+BI;Data+Analytics+Portfolio" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458?style=for-the-badge&logo=pandas&logoColor=white)

<br/>

> **A complete end-to-end Data Analytics project** — Raw data → Python EDA → SQL insights → Power BI Dashboard

</div>

---

## 📊 Project Stats

<div align="center">

| 📁 Dataset | 🐍 Visualizations | 🗄️ SQL Queries | 🌍 Countries |
|:---:|:---:|:---:|:---:|
| **1,200 titles** | **7 charts** | **10 queries** | **16 regions** |

</div>

---

## 🎯 Key Insights

```
📌 68.9% Movies  |  31.1% TV Shows
🌎 United States leads with 336 titles
🎭 Top Genre: Children & Family Movies (96 titles)
⏱️  Avg Movie Duration: 126 minutes
📈 Peak Year: 2026 — 207 new titles added
🔞 Most Common Rating: TV-MA
```

---

## 🔄 Analytics Workflow

```
🗂️  Raw Data (CSV)
      ↓
🐍  Python — Pandas (Data Cleaning + EDA + 7 Visualizations)
      ↓
🗄️  MySQL — 10 SQL Queries (Aggregations, Window Functions, LAG())
      ↓
📊  Power BI — Interactive Dashboard (KPI Cards, Donut Chart, Bar Charts)
      ↓
💡  Key Business Insights
```

---

## 📂 Project Structure

```
netflix_project/
├── 📁 data/
│   ├── netflix_titles.csv              ← Raw dataset (1,200 records)
│   └── netflix_titles_cleaned.csv      ← Cleaned dataset
├── 📁 python/
│   ├── generate_dataset.py             ← Dataset generation
│   └── analysis.py                     ← EDA + 7 visualizations
├── 📁 sql/
│   └── netflix_analysis_queries.sql    ← 10 SQL analysis queries
├── 📁 powerbi/
│   └── POWERBI_GUIDE.md                ← Dashboard build guide
├── 📁 docs/
│   ├── 01_content_type_distribution.png
│   ├── 02_top_countries.png
│   ├── 03_yearly_trend.png
│   ├── 04_top_genres.png
│   ├── 05_rating_distribution.png
│   ├── 06_movie_duration.png
│   └── 07_tv_seasons.png
└── README.md
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 Python (Pandas, Matplotlib, Seaborn) | Data cleaning, EDA, visualizations |
| 🗄️ MySQL + Workbench | Database creation, SQL analysis |
| 📊 Power BI | Interactive dashboard, DAX measures |
| 📁 CSV Dataset | 1,200 Netflix-style title records |

---

## 🚀 How to Run

### Python
```bash
pip install pandas numpy matplotlib seaborn
python python/generate_dataset.py   # Generate dataset
python python/analysis.py           # Run EDA + create charts
```

### SQL
```sql
-- 1. Create database
CREATE DATABASE netflix_db;
USE netflix_db;

-- 2. Import netflix_titles_cleaned.csv
-- 3. Run sql/netflix_analysis_queries.sql
```

### Power BI
```
1. Open Power BI Desktop
2. Get Data → Text/CSV → netflix_titles_cleaned.csv
3. Follow powerbi/POWERBI_GUIDE.md
```

---

## 📈 Sample SQL Query

```sql
-- Year-over-year content growth
WITH yearly AS (
    SELECT year_added, COUNT(*) AS total
    FROM netflix_titles
    GROUP BY year_added
)
SELECT
    year_added,
    total,
    total - LAG(total) OVER (ORDER BY year_added) AS yoy_change
FROM yearly
ORDER BY year_added;
```

---

## 📸 Visualizations Preview

> Charts generated using Python (Matplotlib + Seaborn) — available in `/docs` folder

| Chart | Insight |
|-------|---------|
| 📊 Content Type Distribution | 68.9% Movies vs 31.1% TV Shows |
| 🌍 Top Countries | US leads with 336 titles |
| 📈 Yearly Trend | Platform growth 2008–2026 |
| 🎭 Top Genres | Children & Family dominates |
| ⭐ Rating Distribution | TV-MA most common |
| ⏱️ Movie Duration | Avg 126 minutes |
| 📺 TV Seasons | Season count breakdown |

---

## 👤 Author

<div align="center">

**Thangamuthumari M**
BCA Graduate | Aspiring Data Analyst / Full Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-thangam2630-181717?style=for-the-badge&logo=github)](https://github.com/thangam2630)

</div>

---

<div align="center">
<sub>Built with ❤️ using Python, SQL & Power BI</sub>
</div>
