# NBA stats 🏀
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

O NBA stats é um script que extrai informações dos jogos da nba e esse projeto foi criado para poder consolidar estudos relacionados a extração de dados em Pyhton.

O script acessa o site [Basketball Reference](https://www.basketball-reference.com) e extrai as informações de todos os jogos da temporada selecionada e são armazenadas utilizando dataframes.

## Exemplo das estatisticas armazenadas
![Exemplo das estatisticas armazenadas](https://github.com/venntim/assets/blob/main/exemplo-estatistica.png)

## Legenda da tabela
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
- Requests
- bs4
- Pandas
- Numpy
- Time
- Random

# Autor

Victor Hugo Valério Barros

[https://www.linkedin.com/in/victorh-vbarros/](https://www.linkedin.com/in/victorh-vbarros/)
