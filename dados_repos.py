import requests
import pandas as pd

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'seutokengithub'
        self.headers = {'Authorization' : 'Bearer seutokengithub',
           'X-GitHub-Api-Version': '2022-11-28'}

    
    def list_repositorios(self):
        repos_list = []
        for page_num in range(1,20):
            try:
                    url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                    response = requests.get(url, headers=self.headers)
                    repos_list.append(response.json())

            except:
                repos_list.append(None)

        return repos_list


    def nomes_repos(self, repos_list):
            
        repos_name = []
        for page in repos_list:
            for repo  in page:
                try:
                    repos_name.append(repo['name'])
                except:
                    pass
        return repos_name
       
    

    def nomes_linguagens(self, repos_list):
        repos_linguage = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_linguage.append(repo['language'])
                except:
                    pass
        
        return repos_linguage     

    def cria_df_linguagem(self):
        repositorios = self.list_repositorios()
        names = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_names'] = names
        dados['linguagens'] = linguagens

        return dados

    
    
amz_repos = DadosRepositorios('amzn')
ling_amz_usadas = amz_repos.cria_df_linguagem()
        # print(ling_amz_usadas)

netflix_repos = DadosRepositorios('netflix')
ling_netflix_usadas = netflix_repos.cria_df_linguagem()
        # print(ling_netflix_usadas)

spotify_repos = DadosRepositorios('spotify')
ling_spotify_usadas = spotify_repos.cria_df_linguagem()
        # print(ling_spotify_usadas)

        # Salvando dados
ling_amz_usadas.to_csv('dados/ling_rep_amz.csv')

ling_netflix_usadas.to_csv('dados/ling_rep_netiflix.csv')

ling_spotify_usadas.to_csv('dados/ling_rep_spotify.csv')



    
