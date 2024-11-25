# NBA Player Stats Scraper

A Flask-based API that scrapes basketball player statistics from [Basketball Reference](https://www.basketball-reference.com/) and provides them in JSON format.

## Features

- Retrieve general player stats.
- Fetch player stats by year and category.
- Maintains data structure order for readability.

## Prerequisites

- Python 3.7+
- `pip` package manager

## Installation

1. Clone the repository: `git clone https://github.com/bilalhus24/NBAPlayerStatsScraper`
2. Navigate to the project directory: `cd NBAPlayerStatsScraper`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Start the Flask application: `python app.py`
2. The API will be available at: `http://127.0.0.1:5000/`
3. Can run code to fetch player by current year(passing only player's name as a parameter) or for a specific year(passing player's name and ending year[ex: for 2023-2024 season, pass in 2024])

## Endpoints

### 1. Fetch Player Stats by Year

**URL**: `GET /player-splits-stats`

**Query Parameters**:
- `player` (required): Full name of the player (e.g., `LeBron James`).
- `year` (required): Season year (e.g., `2024`).

**Example Request**: `GET http://127.0.0.1:5000/player-splits-stats?player=Lebron%20James'

**Example Response**:
```json
{
    "player": "Lebron James",
    "stats": {
        "stats": [
            {
                "career": "1508",
                "label": "Games",
                "season": "16"
            },
            {
                "career": "27.1",
                "label": "Points",
                "season": "23.6"
            },
            {
                "career": "7.5",
                "label": "Total Rebounds",
                "season": "8.1"
            },
            {
                "career": "7.4",
                "label": "Assists",
                "season": "9.1"
            },
            {
                "career": "50.6",
                "label": "Field Goal Percentage",
                "season": "51.1"
            },
            {
                "career": "34.9",
                "label": "3-Point Field Goal Percentage",
                "season": "42.2"
            },
            {
                "career": "73.6",
                "label": "Free Throw Percentage",
                "season": "73.8"
            },
            {
                "career": "54.8",
                "label": "Effective Field Goal PercentageThis statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.",
                "season": "58.1"
            },
            {
                "career": "27.0",
                "label": "Player Efficiency RatingA measure of per-minute production standardized such that the league average is 15.",
                "season": "22.3"
            },
            {
                "career": "265.3",
                "label": "Win SharesAn estimate of the number of wins contributed by a player.",
                "season": "1.6"
            }
        ]
    },
    "year": "Current Year"
}
```

**Example Request**: `GET http://127.0.0.1:5000/player-splits-stats?player=LeBron%20James&year=2022`

**Example Response**:
```json
{
    "player": "LeBron James",
    "year": "2024",
    "stats": {
        "stats": {
            "Totals": {
                "G": "71",
                "GS": "71",
                "MP": "2504",
                "FG": "685",
                "FGA": "1269",
                "3P": "149",
                "3PA": "363",
                "FT": "303",
                "FTA": "404",
                "ORB": "61",
                "TRB": "518",
                "AST": "589",
                "STL": "89",
                "BLK": "38",
                "TOV": "245",
                "PF": "78",
                "PTS": "1822"
            },
            "Shooting": {
                "FG%": ".540",
                "3P%": ".410",
                "FT%": ".750",
                "TS%": ".630"
            },
            "Advanced": {
                "USG%": "29.4",
                "ORtg": "120",
                "DRtg": "115",
                "+/-": "+4.2"
            },
            "Per Game": {
                "MP": "35.3",
                "PTS": "25.7",
                "TRB": "7.3",
                "AST": "8.3"
            }
        }
    }
}
```

   **Screenshots**:

   
   ![Screenshot 2024-11-24 155319](https://github.com/user-attachments/assets/981c7050-c05d-4f0a-93ce-b5baff357787)
   ![Screenshot 2024-11-24 155434](https://github.com/user-attachments/assets/f7b803f2-e7f5-4aa7-b32d-22bf95fdeacf)

   ![Screenshot 2024-11-24 155356](https://github.com/user-attachments/assets/fc23210b-c2ba-4731-9e62-6108a4819cae)
   ![Screenshot 2024-11-24 155421](https://github.com/user-attachments/assets/013e0beb-9702-4d61-9b11-1ebbbb42c484)
