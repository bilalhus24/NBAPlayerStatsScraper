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

## Endpoints

### 1. Fetch Player Stats by Year

**URL**: `GET /player-splits-stats`

**Query Parameters**:
- `player` (required): Full name of the player (e.g., `LeBron James`).
- `year` (required): Season year (e.g., `2024`).

**Example Request**: `GET http://127.0.0.1:5000/player-splits-stats?player=LeBron%20James&year=2024`

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

