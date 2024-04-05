import os
from dotenv import load_dotenv
import paho.mqtt.client as paho
from paho import mqtt
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = int(os.getenv("PORT", 8883))  
topic = "my/test/topic"  
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

# Conexão com o MongoDB
mongo_user = os.getenv('MONGO_USER')
mongo_password = os.getenv('MONGO_PASSWORD')
uri = f"mongodb+srv://{mongo_user}:{mongo_password}@prova2.vopbq5y.mongodb.net/?retryWrites=true&w=majority&appName=Prova2"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['nome_do_banco_de_dados']  
metabase_collection = db['metabase']

# Verifica se a coleção existe e cria se não existir
if 'metabase' not in db.list_collection_names():
    db.create_collection('metabase')

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    sensor_data = json.loads(message.payload.decode('utf-8'))
    print(f"Dados do Sensor Recebidos: {sensor_data}")

    # Insere os dados recebidos no MongoDB
    metabase_collection.insert_one({'Sensor': sensor_data['Sensor'], 'data': sensor_data['data']})

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conectado com código de resultado {reason_code}")
    # Subscreve no tópico após conectar
    client.subscribe(topic, qos=1)

# Instanciação do cliente MQTT
client_mqtt = paho.Client(paho.CallbackAPIVersion.VERSION2, "Subscriber", protocol=paho.MQTTv5)
client_mqtt.on_connect = on_connect
client_mqtt.on_message = on_message

# Configurações de TLS
client_mqtt.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client_mqtt.username_pw_set(username, password)  # Configuração da autenticação

# Conexão ao broker
client_mqtt.connect(broker_address, port=port)

# Loop de espera por mensagens
client_mqtt.loop_forever()