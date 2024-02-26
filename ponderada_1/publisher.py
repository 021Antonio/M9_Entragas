import paho.mqtt.client as mqtt
import time
import csv
import json

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conecte ao broker
client.connect("localhost", 1892, 60)

def publish_sensor_data():
    # Abrir o arquivo CSV da pasta 'data_sensor'
    with open('data_sensor/sensor_data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Para cada linha do CSV, publicar os dados
            sensor_data = {
                "Sensor": row['Sensor'],
                "data": row['data'],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            client.publish("sensor/data", json.dumps(sensor_data))
            print(f"Publicado: {sensor_data}")
            time.sleep(5)  # Pausa entre publicações

try:
    publish_sensor_data()
except KeyboardInterrupt:
    print("Publicação encerrada")
finally:
    client.disconnect()
