# Prova1

<video width="320" height="240" controls>
  <source src="vid.mp4" type="video/mp4">
  Seu navegador não suporta o elemento de vídeo.
</video>

## Instalação
Instale o Mosquitto e a biblioteca Paho do python.
``` 
sudo apt-get install mosquitto mosquitto-clients

pip install paho-mqtt
```

Agora configure o mosquitto para ser o broker.


Crie um arquivo mosquitto.conf e adicione essas 2 linhas de codigo

``` 
listener 1892
allow_anonymous true
```

## Rodando

Va para o diretorio onde se encontra os codigo, para isso, digite:

```
cd src
```
Agora: 

Voce precisa ter 3 terminais:

Um para inicializar o Broker.

```
mosquitto -c mosquitto.conf
```

Um para rodar o codigo `publisher` 


```
python3 publisher.py
```


E outro para rodar o `subscriber` 

```
python3 subscriber.py
```

## Sobre o Codigo

``` 
import paho.mqtt.client as mqtt  # Importa o módulo paho.mqtt.client para utilizar o MQTT
import time  # Importa o módulo time para trabalhar com tempo
import csv  # Importa o módulo csv para trabalhar com arquivos CSV
import json  # Importa o módulo json para trabalhar com dados no formato JSON

# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")  # Cria uma instância do cliente MQTT

# Conecta ao broker MQTT
client.connect("localhost", 1892, 60)  # Conecta ao broker MQTT na porta 1892

def publish_sensor_data():
    # Abre o arquivo CSV da pasta 'data_sensor'
    with open('data_sensor/sensor_data.csv', mode='r') as file:  # Abre o arquivo CSV em modo de leitura
        csv_reader = csv.DictReader(file)  # Cria um leitor de CSV usando o módulo csv.DictReader
        for row in csv_reader:  # Itera sobre cada linha do arquivo CSV
            # Para cada linha do CSV, cria um dicionário com os dados do sensor
            sensor_data = {
                "Sensor": row['Sensor'],
                "data": row['data'],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")  # Obtém o timestamp atual no formato especificado
            }
            
            client.publish("sensor/data", json.dumps(sensor_data))  # Publica os dados do sensor no tópico "sensor/data"
            print(f"Publicado: {sensor_data}")  # Imprime uma mensagem informando que os dados foram publicados
            time.sleep(3)  # Pausa por 3 segundos entre as publicações

try:
    publish_sensor_data()  # Chama a função para publicar os dados do sensor
except KeyboardInterrupt:
    print("Publicação encerrada")  # Imprime uma mensagem informando que a publicação foi encerrada devido a um KeyboardInterrupt
finally:
    client.disconnect()  # Desconecta do broker MQTT

```

Para gerar o csv, usei um site que gera csv's aleatorios. 
[Link do site para gerar](https://extendsclass.com/csv-generator.html).
