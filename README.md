# NBA Player Stats Explorer 2026

An interactive NBA 2025/26 analytics app for exploring, comparing and visualizing player performance.

The project uses pandas to clean and aggregate game-level data, Streamlit for the interactive interface, and a small in-memory SQLite database for league ranking queries.

## Features

- Explore season averages for individual players
- Compare two players side by side
- Visualize game-by-game performance over time
- Switch between points, assists and rebounds in the performance chart
- Browse league rankings by points, assists, rebounds or minutes
- Paginated SQL rankings with a minimum-games filter

## Tech Stack

- Python
- pandas
- Streamlit
- SQLite / SQL
- Poetry
- Jupyter Notebook

## Data

The app works with game-level NBA player statistics from the 2025/26 season.

Data source: [NBA - PLAYER STATS - SEASON 25/26](https://www.kaggle.com/datasets/eduardopalmieri/nba-player-stats-season-2526/code) by Eduardo Palmieri on Kaggle.

The exploratory notebook in `notebooks/01_data_exploration.ipynb` was used to inspect missing values, validate shooting-percentage nulls, investigate game records and prepare the transformations later used by the app.

## How it works

The raw CSV is loaded and cleaned with pandas. Player-level averages and shooting percentages are then calculated from the game logs. The Streamlit app uses those aggregated statistics for player exploration and comparison, while the original game-level data is used for performance-history charts.

For league rankings, the aggregated player table is loaded into an in-memory SQLite database and queried with SQL using `ORDER BY`, `LIMIT` and `OFFSET`.

## Run locally

Install the dependencies with Poetry:

```bash
poetry install
```

Run the app:

```bash
poetry run streamlit run app.py
```

## Project Structure

```text
NBA-player-stats-explorer/
├── app.py
├── player.py
├── data/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── src/
│   └── data.py
├── pyproject.toml
└── poetry.lock
```

## Main analysis metrics

The app currently focuses on points, assists, rebounds, minutes played, games played and shooting percentages (FG%, 3P% and FT%).
