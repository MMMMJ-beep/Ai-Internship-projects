# AI Recommendation Logic System (Expanded Version)
# Project 3 - Decode Labs AI Internship
# Goal: Recommend movies to a user based on their genre preferences,
# considering both genre similarity AND movie rating, with a larger dataset
# and extra details (year, rating).

# ---------- Step 1: Movie Dataset (Expanded) ----------
# Each movie has: genres, IMDb-style rating, and release year.
movies = {
    "The Dark Knight": {"genres": ["Action", "Crime", "Drama"], "rating": 9.0, "year": 2008},
    "Inception": {"genres": ["Action", "Sci-Fi", "Thriller"], "rating": 8.8, "year": 2010},
    "Titanic": {"genres": ["Romance", "Drama"], "rating": 7.9, "year": 1997},
    "The Notebook": {"genres": ["Romance", "Drama"], "rating": 7.8, "year": 2004},
    "Interstellar": {"genres": ["Sci-Fi", "Drama", "Adventure"], "rating": 8.6, "year": 2014},
    "Avengers: Endgame": {"genres": ["Action", "Sci-Fi", "Adventure"], "rating": 8.4, "year": 2019},
    "The Conjuring": {"genres": ["Horror", "Thriller"], "rating": 7.5, "year": 2013},
    "Toy Story": {"genres": ["Animation", "Comedy", "Adventure"], "rating": 8.3, "year": 1995},
    "Finding Nemo": {"genres": ["Animation", "Comedy", "Adventure"], "rating": 8.2, "year": 2003},
    "The Hangover": {"genres": ["Comedy"], "rating": 7.7, "year": 2009},
    "John Wick": {"genres": ["Action", "Thriller", "Crime"], "rating": 7.4, "year": 2014},
    "La La Land": {"genres": ["Romance", "Comedy", "Drama"], "rating": 8.0, "year": 2016},
    "The Shawshank Redemption": {"genres": ["Drama", "Crime"], "rating": 9.3, "year": 1994},
    "The Matrix": {"genres": ["Action", "Sci-Fi"], "rating": 8.7, "year": 1999},
    "Get Out": {"genres": ["Horror", "Thriller", "Drama"], "rating": 7.7, "year": 2017},
    "Coco": {"genres": ["Animation", "Adventure", "Drama"], "rating": 8.4, "year": 2017},
    "The Grand Budapest Hotel": {"genres": ["Comedy", "Drama", "Adventure"], "rating": 8.1, "year": 2014},
    "Mad Max: Fury Road": {"genres": ["Action", "Adventure", "Sci-Fi"], "rating": 8.1, "year": 2015},
    "Pride and Prejudice": {"genres": ["Romance", "Drama"], "rating": 7.8, "year": 2005},
    "Parasite": {"genres": ["Drama", "Thriller", "Crime"], "rating": 8.5, "year": 2019},
    "Frozen": {"genres": ["Animation", "Adventure", "Comedy"], "rating": 7.4, "year": 2013},
    "Gladiator": {"genres": ["Action", "Drama", "Adventure"], "rating": 8.5, "year": 2000},
    "A Quiet Place": {"genres": ["Horror", "Thriller", "Sci-Fi"], "rating": 7.5, "year": 2018},
    "Forrest Gump": {"genres": ["Drama", "Romance"], "rating": 8.8, "year": 1994},
    "Spider-Man: Into the Spider-Verse": {"genres": ["Animation", "Action", "Adventure"], "rating": 8.4, "year": 2018},
}

VALID_GENRES = sorted({genre for movie in movies.values() for genre in movie["genres"]})


# ---------- Step 2: Get User Preferences ----------
def get_user_preferences():
    """
    Takes genre preferences and a minimum acceptable rating from the user.
    Returns a tuple: (list of genres, minimum rating).
    """
    print("Welcome to the AI Movie Recommendation System!")
    print("Available genres:", ", ".join(VALID_GENRES))

    user_input = input("\nEnter your favorite genres (comma separated): ")
    preferences = [genre.strip().title() for genre in user_input.split(",") if genre.strip()]

    rating_input = input("Enter minimum rating you'd accept (0-10, press Enter for no limit): ").strip()
    min_rating = float(rating_input) if rating_input else 0.0

    return preferences, min_rating


# ---------- Step 3: Calculate Similarity Score ----------
def calculate_similarity(user_genres, movie_genres):
    """
    Calculates how similar a movie's genres are to the user's preferred genres
    using set intersection (number of overlapping genres).
    """
    return len(set(user_genres).intersection(set(movie_genres)))


# ---------- Step 4: Generate Recommendations ----------
def recommend_movies(user_genres, min_rating, movie_dataset, top_n=5):
    """
    Matches user preferences against the dataset.
    Filters by minimum rating, scores by genre overlap,
    then sorts by (genre match score, rating) - both descending.
    """
    scored_movies = []

    for title, info in movie_dataset.items():
        genres = info["genres"]
        rating = info["rating"]
        year = info["year"]

        if rating < min_rating:
            continue  # skip movies below the user's minimum rating

        score = calculate_similarity(user_genres, genres)
        if score > 0:
            scored_movies.append((title, genres, rating, year, score))

    # Sort primarily by genre match score, then by rating (both descending)
    scored_movies.sort(key=lambda x: (x[4], x[2]), reverse=True)

    return scored_movies[:top_n]


# ---------- Step 5: Display Results ----------
def display_recommendations(recommendations):
    """
    Prints recommended movies with genres, rating, year, and match score.
    """
    if not recommendations:
        print("\nSorry, no matching movies found for your preferences.")
        return

    print("\nHere are your recommended movies:\n")
    print(f"{'#':<3}{'Title':<30}{'Genres':<30}{'Rating':<8}{'Year':<6}{'Match'}")
    print("-" * 80)
    for i, (title, genres, rating, year, score) in enumerate(recommendations, start=1):
        genre_text = ", ".join(genres)
        print(f"{i:<3}{title:<30}{genre_text:<30}{rating:<8}{year:<6}{score}")


# ---------- Step 6: Main Program ----------
def main():
    user_genres, min_rating = get_user_preferences()
    recommendations = recommend_movies(user_genres, min_rating, movies, top_n=5)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
