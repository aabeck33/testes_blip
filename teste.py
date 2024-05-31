'''
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fuzz.ratio("This is my first sentence","This is my first sentence.")
'''
'''
import base64

message = "Ws#$%678"
message = 'Was#a$b%e6c7k8'
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)
'''
'''
# import the Fernet class
from cryptography.fernet import Fernet

# generate key
#key = Fernet.generate_key()
key = b'rw1uw5ATUnw-vEloPtQczkdBqLfL84oSFD5ga2rjjBE='
f = Fernet(key)
print(key)
enc = f.encrypt(b"test_password")
print(enc)
enc = b'gAAAAABi7UatqisTTsVj43lS4k9ofpiqBIcZ1INvG1ugOMaOdchfKjSr0-aGEKzPh0iNQvypDBDgAKm1BXehB2kQ1eLf39iOMg=='
dec = f.decrypt(enc)
print(dec)


#b'gAAAAABi7UY2Wae_QFPKWRwSutXiq6_mB7H6nfimyTV3EwlC6p7dZ2JEhY7s0PoOzaDknIo9g5Cvze2CVQ2qcbKsW3AWrZezLg=='
#b'gAAAAABi7UZcxMdrw2ZeE5jWv6c8EyWQap0A54GLyE4ntJ-PSWon6DhJwVY9TpYWhpCxYeFeVSpsW4__9N8dbPd402HNLjdCOQ=='
#b'gAAAAABi7UatqisTTsVj43lS4k9ofpiqBIcZ1INvG1ugOMaOdchfKjSr0-aGEKzPh0iNQvypDBDgAKm1BXehB2kQ1eLf39iOMg=='
#b'gAAAAABi7UbI3MaW35hysKNvr2BkMCCIFzhFvm412of6B6z2fRY5on7F5QCors26vjCESYKVT69EKPc3udT_hG5PzI6GqdGl8w=='
'''

import requests

# URL da API da Take Blip
api_url = "https://msging.net/commands"

# Substitua 'seu_token' pelo token real fornecido pela Take Blip
headers = {
    "Authorization": "Bearer cm90ZWFkb3I2MTk5NjkxOTc0NTpsMGhSSDJJQllVMjAweFRDN3lRVA==",
    "Content-Type": "application/json"
}

# Dados a serem enviados (se necessário)
payload = {
        'id': '1',
        'method': 'get',
        'uri': '/ping'
    }

# Realiza a chamada à API usando o método adequado (GET, POST, etc.)
response = requests.get(api_url, headers=headers, params=payload)

# Verifica se a chamada foi bem-sucedida (código de status 200)
if response.status_code == 200:
    print("Chamada bem-sucedida!")
    print("Resposta da API:", response.json())
else:
    print(f"Erro na chamada à API. Código de status: {response.status_code}")
    print("Resposta da API:", response.text)
