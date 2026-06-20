/* =========================================================
   NETFLIX MOVIES & TV SHOWS - SQL ANALYSIS
   Author: Thangamuthumari
   Database: MySQL / PostgreSQL compatible
   Table: netflix_titles (load netflix_titles_cleaned.csv)
   ========================================================= */

-- ---------------------------------------------------------
-- 0. TABLE CREATION (run this first, then import the CSV)
-- ---------------------------------------------------------
CREATE TABLE netflix_titles (
    show_id          VARCHAR(10) PRIMARY KEY,
    type              VARCHAR(20),
    title             VARCHAR(255),
    director          VARCHAR(255),
    cast              TEXT,
    country           VARCHAR(100),
    date_added        DATE,
    release_year      INT,
    rating            VARCHAR(10),
    duration          VARCHAR(20),
    listed_in         VARCHAR(255),
    description       TEXT,
    year_added        INT,
    month_added       VARCHAR(20),
    primary_genre     VARCHAR(100),
    duration_minutes  INT,
    seasons           INT
);

-- Use LOAD DATA / \copy / import wizard to load netflix_titles_cleaned.csv


-- ---------------------------------------------------------
-- 1. Total number of Movies vs TV Shows
-- ---------------------------------------------------------
SELECT
    type,
    COUNT(*) AS total_titles,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM netflix_titles), 1) AS percentage
FROM netflix_titles
GROUP BY type;


-- ---------------------------------------------------------
-- 2. Top 10 countries producing the most content
-- ---------------------------------------------------------
SELECT
    country,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE country <> 'Unknown'
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;


-- ---------------------------------------------------------
-- 3. Content added per year (trend analysis)
-- ---------------------------------------------------------
SELECT
    year_added,
    COUNT(*) AS titles_added
FROM netflix_titles
GROUP BY year_added
ORDER BY year_added;


-- ---------------------------------------------------------
-- 4. Most common genres
-- ---------------------------------------------------------
SELECT
    primary_genre,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY primary_genre
ORDER BY total_titles DESC
LIMIT 10;


-- ---------------------------------------------------------
-- 5. Average movie duration by genre
-- ---------------------------------------------------------
SELECT
    primary_genre,
    ROUND(AVG(duration_minutes), 0) AS avg_duration_minutes,
    COUNT(*) AS movie_count
FROM netflix_titles
WHERE type = 'Movie'
GROUP BY primary_genre
ORDER BY avg_duration_minutes DESC;


-- ---------------------------------------------------------
-- 6. TV Shows with the most seasons (top 10)
-- ---------------------------------------------------------
SELECT
    title,
    seasons,
    country,
    release_year
FROM netflix_titles
WHERE type = 'TV Show'
ORDER BY seasons DESC
LIMIT 10;


-- ---------------------------------------------------------
-- 7. Content rating distribution
-- ---------------------------------------------------------
SELECT
    rating,
    COUNT(*) AS total_titles,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM netflix_titles), 1) AS percentage
FROM netflix_titles
GROUP BY rating
ORDER BY total_titles DESC;


-- ---------------------------------------------------------
-- 8. Year-over-year growth rate of content added
-- ---------------------------------------------------------
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


-- ---------------------------------------------------------
-- 9. Top directors by number of titles (excluding Unknown)
-- ---------------------------------------------------------
SELECT
    director,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE director <> 'Unknown'
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;


-- ---------------------------------------------------------
-- 10. Movies vs TV Shows trend by country (Top 5 countries)
-- ---------------------------------------------------------
SELECT
    country,
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE country IN (
    SELECT country FROM netflix_titles
    WHERE country <> 'Unknown'
    GROUP BY country
    ORDER BY COUNT(*) DESC
    LIMIT 5
)
GROUP BY country, type
ORDER BY country, total_titles DESC;
