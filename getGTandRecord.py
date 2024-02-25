import requests
from bs4 import BeautifulSoup
import json
from getDetail import getUrl, getEngname

def getNextGame(gameDate, teamname):
    """
    Get the details of the next game for a specific team on a given date.

    Parameters:
    - gameDate (datetime.date): The date of the game.
    - teamname (str): The name of the team.

    Returns:
    - dict or None: A dictionary containing details of the next game, or None if no game is found for the team.
    """
    try:
        # Send a web request
        url = f"https://tw-nba.udn.com/nba/schedule_boxscore/{gameDate}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract game details
        result_list = []

        for card in soup.find_all('div', class_='card'):
            during = card.find('span', class_='during').get_text(strip=True)

            team_info_dict = {}
            for i, team in enumerate(card.find_all('div', class_='team'), 1):
                team_name = team.find('span', class_='team_name').get_text(strip=True)
                team_score = team.find('span', class_='team_score').get_text(strip=True)
                team_info_dict[f'team{i}_name'] = team_name
                team_info_dict[f'team{i}_score'] = team_score

            result_dict = {'during': during, **team_info_dict}
            result_list.append(result_dict)

        # Check if the team has a game
        for game in result_list:
            team1name = game['team1_name']
            team2name = game['team2_name']
            twoTeamName = [team1name, team2name]
            team1score = game['team1_score']
            team2score = game['team2_score']
            gameStart = game['during']

            if teamname not in twoTeamName:
                continue
            else:
                # Load JSON template for no game or not started
                with open('json/NoGameOrNotStarted.json', 'r', encoding='utf-8') as file:
                    noGame_bubble = json.load(file)

                # Update bubble content with game details
                noGame_bubble['body']['contents'][0]['contents'][0]['contents'][0]['text'] = team1name
                noGame_bubble['body']['contents'][0]['contents'][0]['contents'][1]['url'] = getUrl(getEngname(team1name))
                noGame_bubble['body']['contents'][0]['contents'][0]['contents'][2]['text'] = team1score
                noGame_bubble['body']['contents'][0]['contents'][1]['contents'][2]['text'] = gameStart
                noGame_bubble['body']['contents'][0]['contents'][1]['contents'][3]['text'] = gameDate.strftime('%m-%d')
                noGame_bubble['body']['contents'][0]['contents'][2]['contents'][0]['contents'][0]['text'] = team2name
                noGame_bubble['body']['contents'][0]['contents'][2]['contents'][0]['contents'][1]['url'] = getUrl(getEngname(team2name))
                noGame_bubble['body']['contents'][0]['contents'][2]['contents'][0]['contents'][2]['text'] = team2score

                return noGame_bubble

        return None

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
