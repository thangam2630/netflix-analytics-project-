"""
Netflix Movies & TV Shows - Data Analysis
Author: Thangamuthumari
-------------------------------------------------
Performs data cleaning, exploratory data analysis (EDA),
and generates visualizations + a cleaned dataset for
Power BI dashboard building and SQL querying.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ----------------------------------------------------------
# 1. LOAD DATA
# ----------------------------------------------------------
df = pd.read_csv("data/netflix_titles.csv")
print("Shape:", df.shape)
print(df.info())

# ----------------------------------------------------------
# 2. DATA CLEANING
# ----------------------------------------------------------
# Fill missing director / country with 'Unknown'
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], format="%B %d, %Y", errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

# Extract primary genre (first listed genre)
df["primary_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0].strip())

# Extract numeric duration for movies, seasons for TV shows
def extract_duration_num(row):
    if row["type"] == "Movie":
        return int(row["duration"].replace(" min", ""))
    return None

df["duration_minutes"] = df.apply(extract_duration_num, axis=1)

def extract_seasons(row):
    if row["type"] == "TV Show":
        return int(row["duration"].split(" ")[0])
    return None

df["seasons"] = df.apply(extract_seasons, axis=1)

# Save cleaned dataset
df.to_csv("data/netflix_titles_cleaned.csv", index=False)
print("\nCleaned dataset saved.")

# ----------------------------------------------------------
# 3. EXPLORATORY DATA ANALYSIS
# ----------------------------------------------------------

# 3.1 Content type distribution
type_counts = df["type"].value_counts()
print("\nContent Type Distribution:\n", type_counts)

plt.figure()
plt.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%",
        colors=["#E50914", "#221F1F"], startangle=90)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("docs/01_content_type_distribution.png", bbox_inches="tight")
plt.close()

# 3.2 Top 10 countries by content
top_countries = df[df["country"] != "Unknown"]["country"].value_counts().head(10)
plt.figure()
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Number of Titles")
plt.savefig("docs/02_top_countries.png", bbox_inches="tight")
plt.close()

# 3.3 Content added per year (trend)
yearly_trend = df["year_added"].value_counts().sort_index()
plt.figure()
plt.plot(yearly_trend.index, yearly_trend.values, marker="o", color="#E50914", linewidth=2)
plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True, alpha=0.3)
plt.savefig("docs/03_yearly_trend.png", bbox_inches="tight")
plt.close()

# 3.4 Top genres
top_genres = df["primary_genre"].value_counts().head(10)
plt.figure()
sns.barplot(x=top_genres.values, y=top_genres.index, palette="rocket")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.savefig("docs/04_top_genres.png", bbox_inches="tight")
plt.close()

# 3.5 Rating distribution
plt.figure()
rating_counts = df["rating"].value_counts()
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="mako")
plt.title("Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("docs/05_rating_distribution.png", bbox_inches="tight")
plt.close()

# 3.6 Movie duration distribution
plt.figure()
sns.histplot(df[df["type"] == "Movie"]["duration_minutes"].dropna(), bins=30,
             color="#E50914", kde=True)
plt.title("Movie Duration Distribution (minutes)")
plt.xlabel("Duration (minutes)")
plt.savefig("docs/06_movie_duration.png", bbox_inches="tight")
plt.close()

# 3.7 TV Show seasons distribution
plt.figure()
sns.countplot(x="seasons", data=df[df["type"] == "TV Show"], palette="Reds_r")
plt.title("TV Shows by Number of Seasons")
plt.xlabel("Seasons")
plt.savefig("docs/07_tv_seasons.png", bbox_inches="tight")
plt.close()

print("\nAll visualizations saved to docs/ folder.")

# ----------------------------------------------------------
# 4. KEY INSIGHTS SUMMARY (for README / report)
# ----------------------------------------------------------
insights = []
insights.append(f"Total titles analyzed: {len(df)}")
insights.append(f"Movies: {type_counts.get('Movie', 0)} ({type_counts.get('Movie',0)/len(df)*100:.1f}%)")
insights.append(f"TV Shows: {type_counts.get('TV Show', 0)} ({type_counts.get('TV Show',0)/len(df)*100:.1f}%)")
insights.append(f"Top country by content: {top_countries.index[0]} ({top_countries.iloc[0]} titles)")
insights.append(f"Most common genre: {top_genres.index[0]} ({top_genres.iloc[0]} titles)")
insights.append(f"Peak content-addition year: {yearly_trend.idxmax()} ({yearly_trend.max()} titles)")
insights.append(f"Average movie duration: {df['duration_minutes'].mean():.0f} minutes")
insights.append(f"Most common rating: {rating_counts.index[0]} ({rating_counts.iloc[0]} titles)")

with open("docs/key_insights.txt", "w") as f:
    f.write("NETFLIX DATA ANALYSIS - KEY INSIGHTS\n")
    f.write("=" * 40 + "\n\n")
    for line in insights:
        f.write(f"- {line}\n")

print("\nKEY INSIGHTS:")
for line in insights:
    print(f"- {line}")