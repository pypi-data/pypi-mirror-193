from gamesdb_api.constantes import *

from typing import Union, List, Any
from bs4 import BeautifulSoup
import requests
from fuzzywuzzy import process


class GamesDB:

    def __init__(self):
        self.codigo_console = self.__get_consoles(URL_CONSOLES)

    def __get_consoles(self, url: str) -> dict[str, str]:

        """
        Este método acessa a página de consoles e retorna um dicionário contendo o identificador e o nome dos consoles.

        :param url: URL da página de consoles.
        :return: Dicionário com o nome do console como chave e o identificador do console como valor.
        """

        # Dicionário de saída
        consoles = {}
        # Fazendo a requisição da página
        response = requests.get(url)
        # Criando o objeto BeautifulSoup para parsear o código HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encontrando todas as tags <a> que tenham a classe 'grid-item' e armazenando-as na variável 'links'
        links = soup.find_all('a', class_='grid-item')
        # Para cada tag <a> na variável 'links'
        for link in links:
            # Removendo os espaços do início e fim e pegando o texto dentro da tag <a> (nome do console)
            text = link.text.strip()
            # Pegando o atributo 'href' da tag <a>
            href = link['href']
            # Extraindo apenas o identificador do console a partir do atributo 'href'
            id = href.replace('./platform.php?id=', '')
            # Adicionando o identificador do console como chave e o nome do console como valor no dicionário 'consoles'
            consoles[text] = id
        # Retornando o dicionário 'consoles'
        return consoles

    def get_game_by_id(self, number: Union[str, List[str]], mostrar_progresso=False) -> Union[
        List[TYPE_GAME], TYPE_GAME]:

        """

        Este método busca informações sobre jogos pelo seu identificador (ID). Ele aceita o ID do jogo como uma
        string única ou uma lista de IDs em formato de string. Retorna uma lista de dicionários, se foi buscado uma
        lista de ids, ou um dicionário contendo informações sobre cada jogo especificado como argumento. Se um jogo
        não for encontrado, será retornado um dicionário com o valor da (ID) para a chave 'not_found' para aquele
        jogo específico.

        :param number: identificador do jogo (‘string’) ou lista de identificadores de jogos.
        :param mostrar_progresso: Controla se as informações de progresso devem ser exibidas durante a execução do
        método. O padrão é False, o que significa que as informações de progresso não serão exibidas. Se definido
        como True, as informações de progresso serão exibidas.
        :return: dicionários ou lista de dicionários com informações sobre os jogos.

        """

        try:
            lista_games = []
            # Verifica se o argumento é uma string
            if isinstance(number, str):
                ids = [number]
            # Verifica se o argumento é uma lista
            elif isinstance(number, list):
                for x in number:
                    if not isinstance(x, str):
                        raise TypeError(f'Você passou como argumento {type(x)}, em uma lista '
                                        f'sendo que é esperado um {type(str())}.')
                ids = number
            # Caso o argumento não seja uma string ou uma lista, retorna erro
            else:
                raise TypeError(f'Você passou como argumento um {type(number)}, '
                                f'sendo que é esperado um {type(str())} ou um {type(list())}')
            # Contador para ser utilizado no for
            contador = 1
            # Para cada id passada como argumento chame o método para extrair os dados do jogo
            for i in ids:
                # Representação do progresso da extração de dados.
                if mostrar_progresso:
                    print(f'Extraindo informações: {contador} de {len(ids)}')
                # Adiciona os dados a lista games
                game_info = self.__scraping_game(i)
                # Adiciona o dicionário game_info à lista games caso for um jogo valido
                if game_info:
                    lista_games.append(game_info)
                # Se o valor de game-info for False adiciona o dicionario {"not_found": i}
                else:
                    lista_games.append({'not_found': i})
                contador += 1
            # Se só tem um jogo na lista, vai retornar somente um dict
            if len(lista_games) == 1:
                return lista_games[0]
            return lista_games
        except TypeError as e:
            print(e)
            return False

    def __scraping_game(self, number: str) -> TYPE_GAME:
        """
        Este método faz a raspagem de dados na página do jogo.

        :param number: Identificador do jogo.
        :return: Dicionário com informações sobre o jogo.
        """
        dict_game = {}
        # criando a url com a 'id' do jogo.
        url = URL_GAME_ID.replace('<id>', number)
        # Carregando a URL
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        # Caso o html apresente uma tag <legend> é porque o jogo não está disponível. Retornará False
        if html.find('legend'):
            return False
        # Extrair dados e armazenar na dict
        dict_game['id'] = number
        dict_game['game_title'] = html.find('h1').text
        dict_game['overview'] = html.find('p', class_='game-overview').text
        tag_p = html.find_all('p')

        for x in tag_p:
            if x.text.startswith('Genre(s): '):
                dict_game['genres'] = x.text.replace('Genre(s): ', '').split(' | ')
            elif x.text.startswith('ESRB Rating: '):
                dict_game['esrb_rating'] = x.text.replace('ESRB Rating: ', '')
            elif x.text.startswith('Trailer: '):
                dict_game['trailer'] = x.find('a')['href']
            elif x.text.startswith('Platform: '):
                dict_game['platform'] = x.text.replace('Platform: ', '')
            elif x.text.startswith('Region: '):
                dict_game['region'] = x.text.replace('Region: ', '')
            elif x.text.startswith('Developer(s): '):
                dict_game['developers'] = [y.strip() for y in x.text.replace('Developer(s): ', '').split(' | ')]
            elif x.text.startswith('Publishers(s): '):
                dict_game['publishers'] = [y.strip() for y in x.text.replace('Publishers(s): ', '').split(' | ')]
            elif x.text.startswith('ReleaseDate: '):
                dict_game['release_date'] = x.text.replace('ReleaseDate: ', '')
            elif x.text.startswith('Players: '):
                dict_game['players'] = x.text.replace('Players: ', '')
            elif x.text.startswith('Co-op: '):
                dict_game['coop'] = x.text.replace('Co-op: ', '')

        dict_game['cover'] = html.find('a', class_='fancybox-thumb')['href']
        dict_game['cover_thumb'] = html.find('a', class_='card-img-top')
        dict_game['fanarts'] = [x['href'] for x in html.find_all('a', attrs={'data-fancybox': 'fanarts'})]
        dict_game['screenshots'] = [x['href'] for x in html.find_all('a', attrs={'data-fancybox': 'screenshots'})]
        dict_game['clearlogos'] = [x['href'] for x in html.find_all('a', attrs={'data-fancybox': 'clearlogos'})]
        return dict_game

    def get_game_by_name(self, name: Union[str, List[str]], console: Union[str, int], system=''
                         , mostrar_progresso=False) -> List[dict]:
        """
        Este método busca informações sobre jogos pelo seu nome. Ele aceita o nome do jogo como uma string única ou
        uma lista de nomes em formato de string. Retorna uma lista de dicionários ou um dicionário contendo
        informações sobre cada jogo especificado como argumento. Se um jogo não for encontrado, será retornado um
        dicionário {"not_found": nome_do_jogo} para aquele jogo específico.

        :param name: Nome do jogo (string) ou lista de nomes de jogos.
        :param console: Nome do console ou identificador numérico do console.
        :param system: Região do jogo preferencial (ex: NTSC, PAL-M). Padrão é vazio.
        :param mostrar_progresso: Controla se as informações de progresso devem ser exibidas durante a execução do
        método. O padrão é False, o que significa que as informações de progresso não serão exibidas. Se definido
        como True, as informações de progresso serão exibidas.
        :return: dicionário ou lista de dicionários com informações sobre os jogos.
        """

        try:
            # Se `console` for inteiro, converte para string
            if isinstance(console, int):
                console = str(console)
            # Se `console` for string, busca o ID do console
            else:
                console = self.codigo_console[console]

            games = []
            # Prepara a variável de região
            sistema = " " + system
            # Verifica se `name` é string ou lista
            if isinstance(name, str):
                names = [name]
            elif isinstance(name, list):
                for x in name:
                    if not isinstance(x, str):
                        raise TypeError(f'Tipo inválido {type(x)} na lista. Era esperado {type(str())}.')
                names = name
            else:
                raise TypeError(f'Tipo inválido {type(name)}. Era esperado {type(str())} ou {type(list())}.')

            contador = 1
            # Para cada nome, busca informações sobre o jogo
            for i in names:
                # Representação do progresso da extração de dados.
                if mostrar_progresso:
                    print(f'Procurando {contador} de {len(names)} - {i}')
                name = self.__clear_name(i)
                url_search = URL_PESQUISA.replace('<search>', name.replace(' ', '+')).replace('<id>', console)
                resultados = self.__scraping_search(url_search)
                id = self.__busca(resultados, i + sistema)
                # Se o jogo não foi encontrado, adiciona {"not_found": nome_do_jogo} à lista
                if not id:
                    games.append({"not_found": i})
                # Senão, adiciona as informações do jogo à lista
                else:
                    games.append(self.__scraping_game(id))
                contador += 1
            # Se só tem um jogo na lista, vai retornar somente um dict
            if len(games) == 1:
                return games[0]
            return games
        except TypeError as e:
            print(e)
            return False

    def __scraping_search(self, url_search: str) -> dict[int, str]:
        saida = {}
        response = requests.get(url_search)
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for x in links:
            if x.get('href').startswith('./game.php?id='):
                saida[x['href'].replace('./game.php?id=', '')] = x.text.strip().split('\n')[0]

        return saida

    def __busca(self, resultados: dict[int, str], search: str) -> str:

        """
        Este método realiza uma busca para identificar o melhor resultado de um jogo conforme os resultados
        retornados pela pesquisa. Recebe um dicionário com identificadores e nomes de jogos resultantes da pesquisa,
        e o nome do jogo que está sendo procurado. Retorna o identificador do jogo encontrado como a opção provável.

        :param resultados: Dicionário com identificadores e nomes de jogos resultantes da pesquisa.
        :param search: Nome do jogo que está sendo procurado.
        :return: Identificador do jogo encontrado como a opção mais provável.
        """

        if len(resultados) == 0:
            return False
        saida = process.extractBests(search, resultados)[0][2]
        return saida

    def __clear_name(self, name: str) -> str:
        """
        Recebe uma string representando o nome de um jogo e retira os caracteres '-' e ','. Reordena o nome,
        por exemplo, de '7th Saga, The' para 'The 7th Saga'. Retorna uma string toda em minuscula e concatenada com o
        caracter '+'.

        :param name: Nome do jogo a ser processado.
        :return: Nome do jogo processado e formatado.
        """
        # Criando uma lista com as palavras presentes no nome do jogo
        saida = name.replace(' - ', ' ').split()
        # Verificando se alguma das palavras termina com ','
        # Se sim, a próxima palavra é removida da lista e inserida no início
        for x in saida:
            if x.endswith(','):
                indice = saida.index(x)
                saida[indice] = saida[indice].replace(',', '')
                saida.insert(0, saida.pop(indice + 1))

        # Juntando as palavras da lista com o caracter '+' e convertendo para minúsculo
        return '+'.join(saida).lower()

    def get_console_by_id(self, number: Union[int, str]) -> Union[dict[str, str], bool]:
        """
        Obtém informações de um console pelo ID. :param number: ID do console como inteiro ou string.
        :return: um dicionário contendo informações sobre o console, com chaves incluindo 'name',
        'overview' e 'developer'. Retorna False se for passado uma string que não é número.
        """
        number = str(number)
        # validar o número
        if not number.isdigit():
            return False
        console = self.__scraping_console(number)
        return console

    def __scraping_console(self, number: str) -> dict[str, str]:
        """
        Raspa informações de um console pelo ID.
        :param number: ID do console como uma string.
        :return: um dicionário contendo informações sobre o console, com chaves incluindo 'name',
        'overview' e 'developer'.
        """
        dict_game = {}
        # criando a url com a 'id' do jogo.
        url = URL_CONSOLE_ID.replace('<id>', number)
        # Carregando a URL
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        tag_p = html.find_all('p')
        dict_game['id'] = number
        dict_game['name'] = html.find('h1').text
        dict_game['overview'] = tag_p[0].text.strip()
        for x in tag_p:
            if x.text.startswith('Developer: '):
                dict_game['developer'] = x.text.replace('Developer: ', '')

        return dict_game

    def get_console_by_name(self, name: str) -> Union[dict[str, str], bool]:
        """
        Obtém informações sobre um console pelo nome.
        :param name: Nome do console como uma string.
        :return: um dicionário contendo informações sobre o console, com chaves incluindo 'name',
        'overview' e 'developer'. Retorna False se for passado uma string que não é número.
        """
        if not isinstance(name, str):
            return False
        try:
            id = self.codigo_console[name]
        except KeyError:
            return False

        return self.__scraping_console(id)

    def get_games_platform(self, number: int, mostrar_progresso=False) -> dict[str, str]:
        """
        Obtém informações sobre todos os jogos de um determinado console.

        :param number: id do jogo
        :param mostrar_progresso: mostrar com o print() um representação visual do andamento da tarefa.
        :return: Dicionario com id e nome dos jogos.
        """
        if not isinstance(number, int):
            return False

        dict_games = {}
        pagina = 1

        while True:
            url = URL_CONSOLE_GAMES.replace('<id>', str(number))
            response = requests.get(url.replace('<page>', str(pagina)))
            html = BeautifulSoup(response.text, 'html.parser')
            if html.find('h3'):
                break
            games = html.find_all('a')
            for game in games:
                if game['href'].startswith('./game.php?id='):
                    dict_games[game['href'].replace('./game.php?id=', '')] = game.text.strip().split('\n')[0]

            if mostrar_progresso:
                print(".", sep='', end='')

            pagina += 1

        return dict_games
