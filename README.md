# NBA stats 🏀
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

O NBA stats é um script que extrai informações dos jogos da nba e esse projeto foi criado para poder consolidar estudos relacionados a extração de dados em Pyhton.

O script acessa o site [Basketball Reference](https://www.basketball-reference.com) e extrai as informações de todos os jogos da temporada selecionada e são armazenadas utilizando dataframes.

# Instaciando a classe
Primeiramante para instanciar a classe é preciso informar o codigo do time, a data de inicio, e a data final.
```bash
# Instancia da classe
StatsNBA(team, start_year, end_year)

# team -> codigo do time
# start_year -> ano inicial
# end_year -> ano final, por padrão, se não colocar ano, ele é 2023
```
⚠ Cada time possui um código próprio, para saber o código do time escolhido, você deverá acessar o site [Basketball Reference](https://www.basketball-reference.com/teams) e entrar na página do time desejado, o codigo estará na url. 

👇Veja o exemplo para o time do Cleveland Cavaliers👇

https://www.basketball-reference.com/teams/CLE

Onde "CLE" é o código do time.

## Métodos e atributos
### init
O método __init__ possui alguns atributos padrões como:
team, start_year, end_year e columns
```bash
# Exemplo:
#Instanciando a classe para o time do Cleveland Cavaliers
cavs = StatsNBA('CLE', 2021, 2023)

cavs.team
# retorno: 'CLE'

cavs.start_year
# retorno: 2021

cavs.end_year
# retorno: 2023

cavs.columns
# retorno: ['G','Date','Start (ET)','#','##','Out Home','Opponent', 'W\L', 'OT','Tm','Opp','W','L','Streak','Notes']
```
### get_stats()
Utilizamos o método get_stats() para obtermos as estatisticas do time.

Após instanciarmos a classe usamos:
```bash
cavs.get_stats()
# O retorno vem como um dataframe do pandas.
```

### Exemplo das estatisticas armazenadas
![Exemplo das estatisticas armazenadas](https://github.com/venntim/assets/blob/db4402e60a74ada8275109c6cc3e7b5d12b4b642/NBAstats/NBAstats-Saida.png)
### Legenda da tabela
- G -> Número do jogo na temporada;
- Date -> Data do jogo;
- Start (ET) -> Horário de início, quando possui;
- Out Home -> Jogos fora de casa;
- Opponent -> Time adversário;
- W\L -> Vitória ou Derrota;
- OT -> Prorrogação;
- Tm -> Pontos do time escolhido;
- Opp -> Pontos do time adversário;
- W -> Quantidade de vitorias na temporada;
- L -> Quantidade de derrotas na temporada;
- Streaks -> Sequência de vitorias(W) ou derrotas(L);


# Tecnologias utilizadas
- Requests 2.31.0
- bs4 4.12.2
- Pandas 2.0.3
- Numpy 1.24.3
- Time
- Random

# Usando o Script

## No git bash
```bash
# clonar repositório
git clone https://github.com/venntim/NBAstats-WebScraping.git
```
## No pyhton
```bash
# importando as bibliotecas
import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from NBAstats import StatsNBA

# criando instância da classe StatsNBA
cavs = StatsNBA("CLE", 1971, 2023)

# chamando o método para extrair as estatísticas
estatisticas = cavs.get_stats()

# armazenando as estatisticas em um arquivo CSV
estatisticas.to_csv('dataset_StatsNBA.csv')
```

# Autor

Victor Hugo Valério Barros

[https://www.linkedin.com/in/victorh-vbarros/](https://www.linkedin.com/in/victorh-vbarros/)
