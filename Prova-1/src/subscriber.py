import paho.mqtt.client as mqtt
import json

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    sensor_data = json.loads(message.payload)
    print(f"Dados do Sensor Recebidos: {sensor_data}")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conectado com código de resultado {reason_code}")
    client.subscribe("sensor/data")

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1892, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()