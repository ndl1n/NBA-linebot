import json
from datetime import datetime
from nba_api.live.nba.endpoints import scoreboard
from getDetail import getUrl, getChiname
from getGTandRecord import getNextGame
import datetime 

def get_Info(teamName):
    """
    Retrieve information for the specified basketball team's current game.

    Parameters:
    - teamName (str): The Chinese name of the team used to look up its game information.

    Returns:
    - dict: If specfic game is found today, returns a dictionary containing game score board and lead player.
            If specfic game isn't found today, returns a dictionary containing details of the next game.

    """
    
    # Today's Score Board
    daily_scoreboard = scoreboard.ScoreBoard()

    # Convert json string to Python dictionary
    total_data_json = daily_scoreboard.get_json()
    total_data = json.loads(total_data_json)
    scoreboard_info = total_data['scoreboard']
    
    # 從scoreboard中找到符合teamName的game
    NBA_games = scoreboard_info['games']
    NBA_game=""
    for game in NBA_games:
        NBA_homeTeamChiName = getChiname(game['homeTeam']['teamName'])
        NBA_awayTeamChiName = getChiname(game['awayTeam']['teamName'])
        twoteamChiName = [NBA_homeTeamChiName, NBA_awayTeamChiName]
        if(teamName in twoteamChiName and teamName != 'unknown'):
            NBA_game = game
            break
    else:
        # 在台灣的比賽時間(與NBA gameDate相差一天)
        NBA_gameDate_intW = datetime.date.today()
        # 今天無比賽，找到下一次比賽時間
        for i in range(1, 9):
            nextGameDate_intW = NBA_gameDate_intW + datetime.timedelta(days=i)
            getResult = getNextGame(nextGameDate_intW, teamName)
            if not (getResult is None):
                return getResult
            
    # Game profile    
    period_in_game = NBA_game['period']
    gameleaders_in_game = NBA_game['gameLeaders']

    # hometeam - info
    NBA_homeTeam = NBA_game['homeTeam']
    hometeam_name = NBA_homeTeam['teamName']
    hometeam_wins = NBA_homeTeam['wins']
    hometeam_losses = NBA_homeTeam['losses']
    hometeam_score = NBA_homeTeam['score']

    # hometeam - score detail
    hometeam_periods = NBA_homeTeam['periods']
    Hometeam_period_score = []
    for i in range(period_in_game):
        Hometeam_period_score.append(hometeam_periods[i]['score'])

    # hometeam - gameleader
    homeleader = gameleaders_in_game['homeLeaders']
    homeleader_name = homeleader['name']
    homeleader_jerseyNum = homeleader['jerseyNum']
    homeleader_points = homeleader['points']
    homeleader_rebounds = homeleader['rebounds']
    homeleader_assists = homeleader['assists']

    # awayteam - info
    NBA_awayTeam = NBA_game['awayTeam']   
    awayteam_Name = NBA_awayTeam['teamName']
    awayteam_wins = NBA_awayTeam['wins']
    awayteam_losses = NBA_awayTeam['losses']
    awayteam_score = NBA_awayTeam['score']

    # awayteam - score detail
    awayteam_periods = NBA_awayTeam['periods']
    Awayteam_period_score = []
    for i in range(period_in_game):
        Awayteam_period_score.append(awayteam_periods[i]['score'])

    # awayteam - gameleader
    awayleader = gameleaders_in_game['awayLeaders']
    awayleader_name = awayleader['name']
    awayleader_jerseyNum = awayleader['jerseyNum']
    awayleader_points = awayleader['points']
    awayleader_rebounds = awayleader['rebounds']
    awayleader_assists = awayleader['assists']

    # bubble condition expression 
    if(period_in_game == 5):
        game_bubble = json.load(open('json/OvertimeGame1.json','r',encoding='utf-8'))
    elif(period_in_game == 6):
        game_bubble = json.load(open('json/OvertimeGame2.json','r',encoding='utf-8'))
    elif(period_in_game == 7):
        game_bubble = json.load(open('json/OvertimeGame3.json','r',encoding='utf-8'))
    else:
        game_bubble = json.load(open('json/RegularGame.json','r',encoding='utf-8'))
    
    # Set AwayTeam Bubble
    Away_logo_url = getUrl(awayteam_Name)
    game_bubble['body']['contents'][0]['contents'][0]['contents'][1]['url'] = Away_logo_url
    game_bubble['body']['contents'][0]['contents'][0]['contents'][2]['text'] = '{} - {}'.format(awayteam_wins, awayteam_losses)

    # Set Total Score
    game_bubble['body']['contents'][0]['contents'][1]['contents'][2]['text'] = str(awayteam_score)
    game_bubble['body']['contents'][0]['contents'][2]['contents'][2]['text'] = str(hometeam_score)

    # Set HomeTeam Bubble
    Home_logo_url = getUrl(hometeam_name)
    game_bubble['body']['contents'][0]['contents'][3]['contents'][0]['contents'][1]['url'] = Home_logo_url
    game_bubble['body']['contents'][0]['contents'][3]['contents'][0]['contents'][2]['text'] = '{} - {}'.format(hometeam_wins, hometeam_losses)

    # Set the quarter score
    for i in range(period_in_game):
        game_bubble['body']['contents'][2]['contents'][i+1]['contents'][1]['text'] = str(Awayteam_period_score[i])
        game_bubble['body']['contents'][2]['contents'][i+1]['contents'][2]['text'] = str(Hometeam_period_score[i])

    # Set Name
    Chiname_away = getChiname(awayteam_Name)
    Chiname_home = getChiname(hometeam_name)
    game_bubble['body']['contents'][0]['contents'][0]['contents'][0]['text'] = Chiname_away
    game_bubble['body']['contents'][0]['contents'][3]['contents'][0]['contents'][0]['text'] = Chiname_home
    game_bubble['body']['contents'][2]['contents'][0]['contents'][1]['text'] = Chiname_away
    game_bubble['body']['contents'][2]['contents'][0]['contents'][2]['text'] = Chiname_home
    game_bubble['body']['contents'][4]['contents'][1]['contents'][0]['text'] = '{}({})'.format(Chiname_away, awayleader_jerseyNum)
    game_bubble['body']['contents'][4]['contents'][2]['contents'][0]['text'] = '{}({})'.format(Chiname_home, homeleader_jerseyNum)

    # Set awayteam best player
    game_bubble['body']['contents'][4]['contents'][1]['contents'][1]['text'] = awayleader_name
    game_bubble['body']['contents'][4]['contents'][1]['contents'][2]['text'] = str(awayleader_points)
    game_bubble['body']['contents'][4]['contents'][1]['contents'][3]['text'] = str(awayleader_rebounds)
    game_bubble['body']['contents'][4]['contents'][1]['contents'][4]['text'] = str(awayleader_assists)


    # Set hometeam best player
    game_bubble['body']['contents'][4]['contents'][2]['contents'][1]['text'] = homeleader_name
    game_bubble['body']['contents'][4]['contents'][2]['contents'][2]['text'] = str(homeleader_points)
    game_bubble['body']['contents'][4]['contents'][2]['contents'][3]['text'] = str(homeleader_rebounds)
    game_bubble['body']['contents'][4]['contents'][2]['contents'][4]['text'] = str(homeleader_assists)

    return game_bubble