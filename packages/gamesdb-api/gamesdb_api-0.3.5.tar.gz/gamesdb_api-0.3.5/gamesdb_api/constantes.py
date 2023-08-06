from typing import Union, List, Dict
URL_PESQUISA = 'https://thegamesdb.net/search.php?name=<search>&platform_id%5B%5D=<id>'
URL_GAME_ID = 'https://thegamesdb.net/game.php?id=<id>'
URL_CONSOLES = 'https://thegamesdb.net/list_platforms.php'
URL_CONSOLE_ID = "https://thegamesdb.net/platform.php?id=<id>"
URL_CONSOLE_GAMES = 'https://thegamesdb.net/list_games.php?platform_id=<id>&page=<page>'
TYPE_GAME = Dict[str, Union[str, Union[List[str], str]]]

