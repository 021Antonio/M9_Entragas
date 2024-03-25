import os
from dotenv import load_dotenv
import paho.mqtt.client as paho
from paho import mqtt
import json

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = int(os.getenv("PORT", 8883))  # Usa 8883 como padrão se PORT não estiver definido
topic = "my/test/topic"  # Mudar conforme necessário
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    sensor_data = json.loads(message.payload.decode('utf-8'))
    print(f"Dados do Sensor Recebidos: {sensor_data}")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conectado com código de resultado {reason_code}")
    # Subscreve no tópico após conectar
    client.subscribe(topic, qos=1)

# Instanciação do cliente
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Subscriber", protocol=paho.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

# Configurações de TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)  # Configuração da autenticação

# Conexão ao broker
client.connect(broker_address, port=port)

# Loop de espera por mensagens
client.loop_forever()