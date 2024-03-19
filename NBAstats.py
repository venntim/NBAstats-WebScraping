import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint

class StatsNBA():
    def __init__(self, team, start_year, end_year = 2023):
        self.team = team
        self.start_year = int(start_year)
        self.end_year = int(end_year)
        self.columns = ['G','Date','Start (ET)','#','##','Out Home','Opponent', 'W\L', 'OT','Tm','Opp','W','L','Streak','Notes']

    def get_HTML(self, year):
        url = f'https://www.basketball-reference.com/teams/{self.team}/{year}_games.html'
        r = get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        return soup
    

    def get_stats(self):
        

        # Criando dataframes
        df_data = pd.DataFrame(columns=self.columns)
        df_StatsNBA = pd.DataFrame(columns=self.columns) 

        rows = []
        count_index = 1
        count_year = self.start_year

        while count_year <= self.end_year:

            html = self.get_HTML(count_year)
            games = html.find_all('tr')
        
            try:
                for game in games[1:]:

                    # Verificando se a coluna [G] é um numero
                    if game.findAll('th')[0].get_text().isnumeric():
                            
                            # Armazenando o numero do jogo e fazendo append na lista de linhas 
                            numGame = game.findAll('th')[0].get_text()
                            rows.append(numGame)

                            for infoJogo in game.findAll('td'):
                                rows.append(infoJogo.get_text())

                            # adicionando os dados no datafreme
                            df_data[self.columns] = [rows]
                            df_StatsNBA = pd.concat([df_StatsNBA, df_data])
                            rows.clear()
            except:
                rows.clear()
                for game in games[1:]:


                    # Verificando se a coluna [G] é um numero
                    if game.findAll('th')[0].get_text().isnumeric():
                            
                            # Armazenando o numero do jogo e fazendo append na lista de linhas 
                            numGame = game.findAll('th')[0].get_text()
                            rows.append(numGame)

                            # for para percorrer a tabela que contem as estatisticas e armazenando na lista de linhas    
                            for infoJogo in game.findAll('td'):
                            
                                if count_index == 2:
                                    
                                    rows.append(np.NaN)
                                    rows.append(infoJogo.get_text())
                                        
                                    count_index+=1
                            
                                else:
                                    rows.append(infoJogo.get_text())
                                    count_index+=1

                            count_index = 1

                            # Adicionando as Linhas no DataFrame
                            df_data[self.columns] = [rows]
                            df_StatsNBA = pd.concat([df_StatsNBA, df_data])
                            rows.clear()
            
            count_year += 1
            sleep(randint(1, 5))
        
        df_StatsNBA.drop(['##', '#', 'Notes'], axis=1, inplace=True)
        
        return df_StatsNBA