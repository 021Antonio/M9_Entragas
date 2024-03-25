import os
import time
import csv
import json
from dotenv import load_dotenv
import paho.mqtt.client as paho
from paho import mqtt

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = int(os.getenv("PORT", 8883))  # Usa 8883 como padrão se PORT não estiver definido
topic = "my/test/topic"  # Assume que você deseja usar o mesmo tópico
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"CONNACK received with code {reason_code}")

def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Mid: {mid}")

# Configuração do cliente
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Publisher", protocol=paho.MQTTv5)
client.on_connect = on_connect
client.on_publish = on_publish

# Configurações de TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)  # Configuração da autenticação

# Conexão ao broker
client.connect(broker_address, port=port)

def publish_sensor_data():
    # Abrir o arquivo CSV
    with open('../data_sensor/sensor_data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Para cada linha do CSV, publicar os dados
            sensor_data = {
                "Sensor": row['Sensor'],
                "data": row['data'],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            client.publish(topic, json.dumps(sensor_data), qos=1)
            print(f"Publicado: {sensor_data}")
            time.sleep(5)  # Pausa entre publicações

try:
    client.loop_start()
    publish_sensor_data()
except KeyboardInterrupt:
    print("Publicação encerrada")
finally:
    client.disconnect()
    client.loop_stop()