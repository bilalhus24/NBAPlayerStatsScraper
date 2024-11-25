from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
from collections import OrderedDict
import re
app = Flask(__name__)

PLAYER_BASE_URL = 'https://www.basketball-reference.com/players/'

def scrape_player_stats_by_name(player_name):
    try:
        parts = player_name.split()
        if len(parts) < 2:
            return {"error": "Invalid player name format. Please use full name (e.g., 'LeBron James')"}

        last_name = parts[-1].lower()
        first_name = parts[0].lower()
        first_letter = last_name[0]
        player_url = f"{PLAYER_BASE_URL}{first_letter}/{last_name[:5]}{first_name[:2]}01.html"

        response = requests.get(player_url)
        if response.status_code != 200:
            return {"error": f"Player not found. URL attempted: {player_url}"}
        soup = BeautifulSoup(response.content, 'html.parser')

        stats_div = soup.find('div', class_='stats_pullout')
        if not stats_div:
            return {"error": "Stats summary not found for the player."}

        # Initialize an empty list to hold stats in the parsed order
        ordered_stats = []

        # Extract each section (p1, p2, p3) in order
        stat_sections = stats_div.find_all('div', class_=['p1', 'p2', 'p3'], recursive=False)
        for section in stat_sections:
            stat_items = section.find_all('div', recursive=False)
            for item in stat_items:
                label_element = item.find('span', class_='poptip')
                values = item.find_all('p')

                if label_element and len(values) == 2:
                    # Extract the clean label name without additional description
                    label = label_element['data-tip']
                    label = re.sub(r"<[^>]*>", "", label).split("<br")[0].strip()  # Remove tags and split extra text

                    season_value = values[0].get_text(strip=True)
                    career_value = values[1].get_text(strip=True)
                    ordered_stats.append({"label": label, "season": season_value, "career": career_value})

        return {
            "stats": ordered_stats
        }

    except Exception as e:
        print(f"Error occurred while fetching stats by name: {e}")
        return {"error": "An error occurred while fetching player stats by name."}

def scrape_player_stats_by_name_and_year(player_name, year):
    try:
        parts = player_name.split()

        last_name = parts[-1].lower()
        first_name = parts[0].lower()
        first_letter = last_name[0]
        player_url = f"{PLAYER_BASE_URL}{first_letter}/{last_name[:5]}{first_name[:2]}01/splits/{year}"

        response = requests.get(player_url)

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id='splits')
        if not table:
            return {"error": "Splits stats table not found on the page."}

        headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

        first_data_row = table.find('tbody').find('tr')
        if not first_data_row:
            return {"error": "No data rows found in the table."}
        data = [td.get_text(strip=True) for td in first_data_row.find_all(['th', 'td'])]

        data = [value for value in data if value][1:]  # Remove "Total" and the first entry
        headers = [header for header in headers if header]
        headers = headers[6:]  # Remove unnecessary headers (5th and 6th)

        in_each = [17, 4, 4, 4]  # Totals, Shooting, Advanced, Per Game
        categories = ["Totals", "Shooting", "Advanced", "Per Game"]

        stats_dict = OrderedDict()
        data_index = 0
        for i, category in enumerate(categories):
            group_size = in_each[i]
            stats_dict[category] = OrderedDict(
                (headers[data_index + j], data[data_index + j]) for j in range(group_size)
            )
            data_index += group_size

        return OrderedDict({
            "stats": OrderedDict({
                "stats": stats_dict
            })
        })

    except Exception as e:
        print(f"Error: {e}")
        return {"error": "An error occurred while fetching player stats by name and year."}


@app.route('/player-splits-stats', methods=['GET'])
def get_player_splits_stats():
    player_name = request.args.get('player', None)
    year = request.args.get('year', None)

    if not player_name:
        return jsonify({"error": "Player name must be specified"}), 400

    # Determine which scraping function to use based on provided parameters
    if year:
        stats = scrape_player_stats_by_name_and_year(player_name.lower(), year)
    else:
        stats = scrape_player_stats_by_name(player_name.lower())

    if not stats:
        return jsonify({"error": "Player or stats not found"}), 404
    if not year:
        year = "Current Year"
    return jsonify({"player": player_name,
                    "year": year,
                    "stats": stats})


# Main function to run the API
if __name__ == '__main__':
    app.run(debug=True)
