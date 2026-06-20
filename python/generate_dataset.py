"""
Generate a realistic Netflix Titles dataset for the analytics project.
Structure mirrors the well-known public Netflix Movies & TV Shows dataset:
show_id, type, title, director, cast, country, date_added,
release_year, rating, duration, listed_in (genre), description
"""

import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

n_records = 1200

types = ["Movie", "TV Show"]
type_weights = [0.69, 0.31]  # Netflix catalog is movie-heavy

countries = [
    "United States", "India", "United Kingdom", "Canada", "France",
    "Japan", "South Korea", "Spain", "Germany", "Australia",
    "Mexico", "Brazil", "Nigeria", "Egypt", "Turkey", "Italy"
]
country_weights = [0.32, 0.12, 0.08, 0.06, 0.05, 0.05, 0.05, 0.04,
                    0.04, 0.03, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02]

genres_movie = [
    "Dramas", "Comedies", "Action & Adventure", "Documentaries",
    "Horror Movies", "Romantic Movies", "Thrillers", "Children & Family Movies",
    "Independent Movies", "Sci-Fi & Fantasy"
]
genres_tv = [
    "TV Dramas", "TV Comedies", "Crime TV Shows", "Kids' TV",
    "Docuseries", "Romantic TV Shows", "TV Action & Adventure",
    "Anime Series", "Reality TV", "TV Mysteries"
]

ratings = ["TV-MA", "TV-14", "TV-PG", "R", "PG-13", "PG", "TV-Y", "TV-Y7", "TV-G", "NR"]
rating_weights = [0.27, 0.24, 0.10, 0.10, 0.09, 0.06, 0.05, 0.04, 0.03, 0.02]

first_names = ["Raj", "Anil", "Priya", "John", "Maria", "Wei", "Hana", "Carlos",
               "Fatima", "Yuki", "David", "Sara", "Tom", "Aisha", "Min", "Elena"]
last_names = ["Kumar", "Smith", "Garcia", "Tanaka", "Khan", "Lee", "Silva",
              "Rossi", "Patel", "Johnson", "Müller", "Park", "Costa", "Nair"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_cast(n=5):
    return ", ".join(random_name() for _ in range(n))

def random_title(idx, content_type):
    adjectives = ["Hidden", "Last", "Silent", "Broken", "Golden", "Dark",
                  "Endless", "Secret", "Wild", "Forgotten", "Eternal", "Lost"]
    nouns = ["Shadows", "Horizon", "Legacy", "Kingdom", "Dreams", "City",
             "Rebellion", "Promise", "Storm", "Journey", "Memory", "Empire"]
    suffix = " Chronicles" if content_type == "TV Show" and random.random() > 0.6 else ""
    return f"The {random.choice(adjectives)} {random.choice(nouns)}{suffix} {idx}"

rows = []
for i in range(1, n_records + 1):
    content_type = np.random.choice(types, p=type_weights)
    country = np.random.choice(countries, p=country_weights)
    year_range = list(range(2008, 2026))  # 18 years
    year_w = [1,1,1,2,2,2,3,3,4,5,6,7,8,9,10,9,8,7]
    release_year = int(np.random.choice(year_range, p=np.array(year_w) / sum(year_w)))
    # date_added is always >= release_year, weighted toward recent additions
    add_year = min(2026, release_year + np.random.choice([0,0,1,1,1,2,2,3,4,5]))
    add_month = random.randint(1, 12)
    add_day = random.randint(1, 28)
    date_added = f"{['January','February','March','April','May','June','July','August','September','October','November','December'][add_month-1]} {add_day}, {add_year}"

    rating = np.random.choice(ratings, p=rating_weights)

    if content_type == "Movie":
        duration = f"{random.randint(70, 180)} min"
        genre_pool = genres_movie
    else:
        duration = f"{random.randint(1, 8)} Season{'s' if random.randint(1,8) > 1 else ''}"
        genre_pool = genres_tv

    n_genres = random.randint(1, 3)
    listed_in = ", ".join(random.sample(genre_pool, min(n_genres, len(genre_pool))))

    director = random_name() if content_type == "Movie" and random.random() > 0.15 else ""
    cast = random_cast(random.randint(3, 7))

    rows.append({
        "show_id": f"s{i}",
        "type": content_type,
        "title": random_title(i, content_type),
        "director": director,
        "cast": cast,
        "country": country,
        "date_added": date_added,
        "release_year": release_year,
        "rating": rating,
        "duration": duration,
        "listed_in": listed_in,
        "description": f"A gripping {content_type.lower()} exploring themes of survival and identity in {country}."
    })

df = pd.DataFrame(rows)

# introduce some realistic missing values (like real Netflix dataset)
missing_idx_director = df.sample(frac=0.08, random_state=1).index
df.loc[missing_idx_director, "director"] = np.nan
missing_idx_country = df.sample(frac=0.03, random_state=2).index
df.loc[missing_idx_country, "country"] = np.nan

df.to_csv("data/netflix_titles.csv", index=False)
print(f"Dataset created: {len(df)} rows")
print(df.head())
print("\nMissing values:\n", df.isnull().sum())
