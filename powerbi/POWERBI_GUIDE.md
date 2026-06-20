# Power BI Dashboard - Build Guide
## Netflix Movies & TV Shows Analysis

This guide walks you through building the Power BI dashboard step by step
using `netflix_titles_cleaned.csv`.

---

## STEP 1: Import Data
1. Open Power BI Desktop
2. Home → Get Data → Text/CSV
3. Select `data/netflix_titles_cleaned.csv`
4. Click **Load** (or Transform Data if you want to clean further in Power Query)

## STEP 2: Set Correct Data Types
In Power Query Editor, verify:
- `date_added` → Date
- `release_year`, `year_added`, `duration_minutes`, `seasons` → Whole Number
- `type`, `country`, `rating`, `primary_genre` → Text

## STEP 3: Create Measures (DAX)
Go to **Modeling → New Measure** and add these:

```DAX
Total Titles = COUNT(netflix_titles[show_id])

Total Movies = CALCULATE([Total Titles], netflix_titles[type] = "Movie")

Total TV Shows = CALCULATE([Total Titles], netflix_titles[type] = "TV Show")

Movie % = DIVIDE([Total Movies], [Total Titles], 0)

Avg Movie Duration = AVERAGE(netflix_titles[duration_minutes])

YoY Growth = 
VAR CurrentYear = [Total Titles]
VAR PreviousYear = CALCULATE([Total Titles], 
    DATEADD(netflix_titles[date_added], -1, YEAR))
RETURN CurrentYear - PreviousYear
```

## STEP 4: Build Dashboard Pages

### Page 1: Overview
| Visual | Field(s) | Chart Type |
|---|---|---|
| KPI Cards | Total Titles, Total Movies, Total TV Shows | Card |
| Movies vs TV Shows | type | Donut Chart |
| Content Added Over Time | year_added (axis), Total Titles (value) | Line Chart |
| Top 10 Countries | country, Total Titles | Bar Chart (horizontal) |

### Page 2: Genre & Rating Analysis
| Visual | Field(s) | Chart Type |
|---|---|---|
| Top Genres | primary_genre, Total Titles | Bar Chart |
| Rating Distribution | rating, Total Titles | Pie / Donut |
| Genre by Type | primary_genre, type, Total Titles | Stacked Bar Chart |

### Page 3: Deep Dive
| Visual | Field(s) | Chart Type |
|---|---|---|
| Movie Duration Distribution | duration_minutes | Histogram |
| TV Show Seasons | seasons | Column Chart |
| Top Directors | director, Total Titles | Bar Chart |
| Country x Type Matrix | country, type, Total Titles | Matrix Table |

## STEP 5: Add Slicers (Filters)
Add slicers for:
- `type` (Movie/TV Show)
- `release_year` (range slider)
- `country`
- `rating`

## STEP 6: Apply Netflix Theme
- Background: Black (#141414) or White
- Primary accent: Netflix Red (#E50914)
- Font: Segoe UI / Bebas Neue style headers
- View → Themes → Customize current theme → set above colors

## STEP 7: Publish / Export
- File → Export → PDF (for sharing in resume/portfolio)
- Or File → Publish → Power BI Service (if you have an account)
- Save .pbix file in `powerbi/` folder

---

## Quick Reference: Chart-to-Insight Mapping
This is useful when you explain the project in an interview:

| Chart | Business Insight It Gives |
|---|---|
| Movies vs TV Shows donut | Content strategy mix |
| Yearly trend line | Platform's content growth/investment pattern |
| Top countries bar | Regional content strategy / localization focus |
| Genre bar chart | Audience preference patterns |
| Rating distribution | Target audience demographics (mature vs family) |
| Duration histogram | Standard movie-length benchmarking |
