teamname_to_chi = {
    "Hawks": "老鷹",
    "Celtics": "賽爾提克",
    "Nets": "籃網",
    "Hornets": "黃蜂",
    "Bulls": "公牛",
    "Cavaliers": "騎士",
    "Mavericks": "獨行俠",
    "Nuggets": "金塊",
    "Pistons": "活塞",
    "Warriors": "勇士",
    "Rockets": "火箭",
    "Pacers": "溜馬",
    "Clippers": "快艇",
    "Lakers": "湖人",
    "Grizzlies": "灰熊",
    "Heat": "熱火",
    "Bucks": "公鹿",
    "Timberwolves": "灰狼",
    "Pelicans": "鵜鶘",
    "Knicks": "尼克",
    "Thunder": "雷霆",
    "Magic": "魔術",
    "76ers": "76人",
    "Suns": "太陽",
    "Blazers": "拓荒者",
    "Kings": "國王",
    "Spurs": "馬刺",
    "Raptors": "暴龍",
    "Jazz": "爵士",
    "Wizards": "巫師",
}

# url resource: https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos/
teamname_to_pictureurl = {
    "Hawks": "https://content.sportslogos.net/logos/6/220/full/8190_atlanta_hawks-primary-2021.png",
    "Celtics": "https://content.sportslogos.net/logos/6/213/full/boston_celtics_logo_primary_19977628.png",
    "Nets": "https://content.sportslogos.net/logos/6/3786/full/brooklyn_nets_logo_primary_20135043.png",
    "Hornets": "https://content.sportslogos.net/logos/6/5120/full/1926_charlotte__hornets_-primary-2015.png",
    "Bulls": "https://content.sportslogos.net/logos/6/221/full/chicago_bulls_logo_primary_19672598.png",
    "Cavaliers": "https://content.sportslogos.net/logos/6/222/full/cleveland_cavaliers_logo_primary_2023_sportslogosnet-5369.png",
    "Mavericks": "https://content.sportslogos.net/logos/6/228/full/3463_dallas_mavericks-primary-2018.png",
    "Nuggets": "https://content.sportslogos.net/logos/6/229/full/8926_denver_nuggets-primary-2019.png",
    "Pistons": "https://content.sportslogos.net/logos/6/223/full/detroit_pistons_logo_primary_20185710.png",
    "Warriors": "https://content.sportslogos.net/logos/6/235/full/3152_golden_state_warriors-primary-2020.png",
    "Rockets": "https://content.sportslogos.net/logos/6/230/full/6830_houston_rockets-primary-2020.png",
    "Pacers": "https://content.sportslogos.net/logos/6/224/full/4812_indiana_pacers-primary-2018.png",
    "Clippers": "https://content.sportslogos.net/logos/6/236/full/los_angeles_clippers_logo_primary_2019_sportslogosnet-3776.png",
    "Lakers": "https://content.sportslogos.net/logos/6/237/full/los_angeles_lakers_logo_primary_2024_sportslogosnet-7324.png",
    "Grizzlies": "https://content.sportslogos.net/logos/6/231/full/4373_memphis_grizzlies-primary-2019.png",
    "Heat": "https://content.sportslogos.net/logos/6/214/full/burm5gh2wvjti3xhei5h16k8e.gif",
    "Bucks": "https://content.sportslogos.net/logos/6/225/full/milwaukee_bucks_logo_primary_20165763.png",
    "Timberwolves": "https://content.sportslogos.net/logos/6/232/full/9669_minnesota_timberwolves-primary-2018.png",
    "Pelicans": "https://content.sportslogos.net/logos/6/4962/full/new_orleans_pelicans_logo_primary_2024_sportslogosnet-9292.png",
    "Knicks": "https://content.sportslogos.net/logos/6/216/full/new_york_knicks_logo_primary_2024_sportslogosnet-7170.png",
    "Thunder": "https://content.sportslogos.net/logos/6/2687/full/khmovcnezy06c3nm05ccn0oj2.png",
    "Magic": "https://content.sportslogos.net/logos/6/217/full/orlando_magic_logo_primary_20117178.png",
    "76ers": "https://content.sportslogos.net/logos/6/218/full/7034_philadelphia_76ers-primary-2016.png",
    "Suns": "https://content.sportslogos.net/logos/6/238/full/phoenix_suns_logo_primary_20143696.png",
    "Blazers": "https://content.sportslogos.net/logos/6/239/full/9725_portland_trail_blazers-primary-2018.png",
    "Kings": "https://content.sportslogos.net/logos/6/240/full/4043_sacramento_kings-primary-2017.png",
    "Spurs": "https://content.sportslogos.net/logos/6/233/full/2547_san_antonio_spurs-primary-2018.png",
    "Raptors": "https://content.sportslogos.net/logos/6/227/full/7024_toronto_raptors-primary-2021.png",
    "Jazz": "https://content.sportslogos.net/logos/6/234/full/utah_jazz_logo_primary_2023_sportslogosnet-8513.png",
    "Wizards": "https://content.sportslogos.net/logos/6/219/full/5671_washington_wizards-primary-2016.png",
}

chi_to_teamname = {v: k for k, v in teamname_to_chi.items()}


def getChiname(teamName):
    """
    Get the Chinese name of a team based on its English name.

    Parameters:
    - teamName (str): The English name of the NBA team.

    Returns:
    - str: The Chinese name of the NBA team.
    """
    Chi_teamname = teamname_to_chi[teamName]
    return Chi_teamname


def getEngname(teamName):
    """
    Get the English name of a team based on its Chinese name.

    Parameters:
    - teamName (str): The Chinese name of the NBA team.

    Returns:
    - str or None: The English name of the NBA team, or None if not found.
    """
    Eng_teamname = chi_to_teamname.get(teamName)
    return Eng_teamname


# get teamname picture
def getUrl(teamName):
    """
    Get the URL of the team's logo based on its English name.

    Parameters:
    - teamName (str): The English name of the NBA team.

    Returns:
    - str: The URL of the team's logo.
    """
    url = teamname_to_pictureurl[teamName]
    return url
