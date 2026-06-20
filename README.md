# 🎬 Netflix Movies & TV Shows - Data Analytics Project

A complete data analytics project analyzing Netflix's content catalog using
**Python**, **SQL**, and **Power BI** — covering data cleaning, exploratory
data analysis, database querying, and interactive dashboard design.

---

## 📌 Project Overview

This project analyzes a Netflix titles dataset (1,200 records) to uncover
patterns in content type, genre popularity, regional distribution, ratings,
and platform growth over time. The goal is to simulate a real-world
analytics workflow: **raw data → cleaning → analysis → SQL insights →
visual dashboard**.

## 🛠️ Tools & Technologies
- **Python** — Pandas, Matplotlib, Seaborn (data cleaning + EDA)
- **SQL** — MySQL/PostgreSQL compatible queries (insight extraction)
- **Power BI** — Interactive dashboard & DAX measures
- **Dataset** — Netflix-style catalog (show_id, type, title, director, cast,
  country, date_added, release_year, rating, duration, listed_in, description)

## 📂 Project Structure
```
netflix_project/
├── data/
│   ├── netflix_titles.csv              # Raw dataset
│   └── netflix_titles_cleaned.csv      # Cleaned dataset (after Python processing)
├── python/
│   ├── generate_dataset.py             # Dataset generation script
│   └── analysis.py                     # Data cleaning + EDA + visualizations
├── sql/
│   └── netflix_analysis_queries.sql    # 10 SQL analysis queries
├── powerbi/
│   └── POWERBI_GUIDE.md                # Step-by-step dashboard build guide
├── docs/
│   ├── 01_content_type_distribution.png
│   ├── 02_top_countries.png
│   ├── 03_yearly_trend.png
│   ├── 04_top_genres.png
│   ├── 05_rating_distribution.png
│   ├── 06_movie_duration.png
│   ├── 07_tv_seasons.png
│   └── key_insights.txt
└── README.md
```

## 🔍 Key Insights
- **68.9%** of the catalog is Movies, **31.1%** is TV Shows
- **United States** leads content production, followed by India and the UK
- **Children & Family Movies** is the most common genre
- Content additions peaked in **2026**, showing strong platform growth
- Average movie runtime is **~126 minutes**
- **TV-MA** is the most common content rating, indicating a mature-audience skew

*(See `docs/key_insights.txt` for the full list)*

## 📊 Analysis Workflow

1. **Data Cleaning (Python)** — Handled missing values in `director` and
   `country`, parsed `date_added` into proper datetime, extracted
   `primary_genre`, `duration_minutes`, and `seasons` as separate fields.
2. **Exploratory Data Analysis (Python)** — Generated 7 visualizations
   covering content type split, country distribution, yearly trends,
   genre popularity, rating breakdown, and duration analysis.
3. **SQL Analysis** — Wrote 10 analytical queries including aggregations,
   window functions (YoY growth using `LAG()`), and subqueries for
   country/genre/director rankings.
4. **Power BI Dashboard** — Built a 3-page interactive dashboard (Overview,
   Genre & Rating Analysis, Deep Dive) with KPI cards, slicers, and DAX
   measures. See `powerbi/POWERBI_GUIDE.md` for full build steps.

## 🚀 How to Run This Project

### Python
```bash
pip install pandas numpy matplotlib seaborn
python python/generate_dataset.py   # generates data/netflix_titles.csv
python python/analysis.py           # cleans data + creates visualizations
```

### SQL
1. Create the `netflix_titles` table using the schema in
   `sql/netflix_analysis_queries.sql`
2. Import `data/netflix_titles_cleaned.csv` into the table
3. Run the analysis queries

### Power BI
1. Open Power BI Desktop
2. Import `data/netflix_titles_cleaned.csv`
3. Follow `powerbi/POWERBI_GUIDE.md` for measures, visuals, and theming

## 👤 Author
**Thangamuthumari (M Muthumari)**
BCA Graduate | Aspiring Data Analyst / Full Stack Developer
[GitHub](https://github.com/thangam2630)
