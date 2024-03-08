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
    with open('./data/temperatura_data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # Para cada linha do CSV, publicar os dados
            sensor_data = {
                "id": row['id'],
                "type": row['tipo'],
                "temperature": row['temperatura'],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),

            }
            
            if int(sensor_data['temperature']) < -15:
                print("Temperatura muito alta para o normal")
            elif int(sensor_data['temperature']) > -25:
                print("Temperatura muito baixa para o normal")
            else:
                print("Temperatura dentro da faixa normal")


            client.publish("sensor/data", json.dumps(sensor_data))
            
            print(f'Lj {sensor_data["id"]} | {sensor_data["type"]} | {sensor_data["temperature"]}')
            print("----------------------")
            time.sleep(3)  # Pausa entre publicações

            

try:
    publish_sensor_data()
except KeyboardInterrupt:
    print("Publicação encerrada")
finally:
    client.disconnect()
