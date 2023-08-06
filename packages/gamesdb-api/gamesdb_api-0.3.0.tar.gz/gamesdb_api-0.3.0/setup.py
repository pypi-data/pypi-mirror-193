from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as r:
    long_description = r.read()

setup(
    name='gamesdb_api',
    version='0.3.0',
    description='Um pacote Python para extrair informações de jogos do site TheGamesDB.net.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bruno Rodrigues',
    author_email='email@bruno.gs',
    license='MIT',
    project_urls={'GitHub': 'https://github.com/rc-bruno/gamesdb_api'},
    install_requires=['beautifulsoup4==4.11.2',
                      'fuzzywuzzy==0.18.0',
                      'Levenshtein==0.20.9',
                      'python-Levenshtein==0.20.9',
                      'requests==2.28.2',
                      'soupsieve==2.4']
    ,
    packages=['gamesdb_api'],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
                 'Natural Language :: Portuguese (Brazilian)',
                 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9',
                 'Topic :: Software Development :: Libraries', 'Topic :: Utilities']
)
