import requests
import json
from requests.auth import HTTPBasicAuth
import os

def get_user_data():
    url = "https://SUA API AQUI"
    username = "USERNAME"
    password = "PASSWORD"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        
        print("Resposta recebida com sucesso!")
        user_data = response.json()
        print("Dados do usuário:", user_data)
        
        return user_data

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None

def save_to_json(data, filename="data.json"):
    if data:
        # para aparecer onde ta sendo salvo o arquivo
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        print(f"Salvando arquivo em: {file_path}")
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dados salvos no arquivo {file_path}")
    else:
        print("Nenhum dado para salvar.")

user_data = get_user_data()

if user_data:
    save_to_json(user_data)
