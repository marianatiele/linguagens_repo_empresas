import requests
import base64
from dados_repos import DadosRepositorios

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.headers = {
            'Authorization' : 'Bearer seutokengithub',
           'X-GitHub-Api-Version': '2022-11-28'
           
        }
    


    def cria_repos(self, name_repo):

        data = {
            'name':name_repo,
            'description':'Dados dos repositórios de algumas empresas',
            'private':False

        }

        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)
        print('STATUS CODE repositório: ', response.status_code)

    

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Fazendo o upload do arquivo
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"

        data = {
            'message':'Add um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')


# Enviando os arquivos 
novo_repo = ManipulaRepositorios('marianatiele')

nome_repo = 'linguagens_repo_empresas'

novo_repo.cria_repos(nome_repo)

novo_repo.add_arquivo(nome_repo, 'ling_rep_amz.csv', 'dados/ling_rep_amz.csv')

novo_repo.add_arquivo(nome_repo, 'ling_rep_netiflix.csv', 'dados/ling_rep_netiflix.csv')

novo_repo.add_arquivo(nome_repo, 'ling_rep_spotify.csv', 'dados/ling_rep_spotify.csv')