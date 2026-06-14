# Project 3: AI Recommendation Logic System

## Decode Labs – AI Internship

## Goal
Create a recommendation system that suggests movies to a user based on
their genre preferences and minimum rating requirement, using similarity
matching logic.

## How It Works
1. **User Input** – The user enters their favorite genres (e.g., Action, Comedy, Romance) and an optional minimum rating (0–10).
2. **Filtering** – Movies below the minimum rating are removed from consideration.
3. **Similarity Matching** – Each remaining movie is compared against the
   user's preferred genres using set intersection (genre overlap count).
4. **Recommendation** – Movies are sorted by genre match score (highest first),
   then by rating, and the top 5 results are displayed in a table.

## Key Concepts Used
- Logic building
- Set/pattern matching
- Filtering and multi-key sorting
- Recommendation system fundamentals (content-based filtering)

## Technologies
- Python (no external libraries required)

## Dataset
25 movies, each with:
- Title
- Genres (list)
- IMDb-style rating
- Release year

## How to Run

### Locally
```bash
python recommendation.py
```

### Google Colab
1. Open a new notebook on [Google Colab](https://colab.research.google.com)
2. Paste the entire code from `recommendation.py` into a cell
3. Run the cell (Shift + Enter)
4. When prompted, type your favorite genres (comma separated) and press Enter
5. Optionally enter a minimum rating, or press Enter to skip

## Example Run
```
Enter your favorite genres (comma separated): Action, Sci-Fi, Adventure
Enter minimum rating you'd accept (0-10, press Enter for no limit): 8

Here are your recommended movies:

#  Title                         Genres                        Rating  Year  Match
--------------------------------------------------------------------------------
1  Avengers: Endgame             Action, Sci-Fi, Adventure     8.4     2019  3
2  Mad Max: Fury Road            Action, Adventure, Sci-Fi     8.1     2015  3
3  Inception                     Action, Sci-Fi, Thriller      8.8     2010  2
4  The Matrix                    Action, Sci-Fi                8.7     1999  2
5  Interstellar                  Sci-Fi, Drama, Adventure      8.6     2014  2
```

## Future Improvements
- Add a larger movie dataset (e.g., from a CSV file or API)
- Use user ratings/history for collaborative filtering
- Add actor/director-based recommendations
- Build a simple web interface using Streamlit
