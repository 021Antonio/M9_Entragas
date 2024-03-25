# Ponderada 1

# Simulação de Comunicação MQTT com Sensor de Umidade

Este repositório foi criado com o propósito de demonstrar a comunicação de dados entre sensores e um servidor utilizando a tecnologia MQTT. 

<video width="320" height="240" controls>
  <source src="./img/ponderada1.mp4" type="video/mp4">
  Seu navegador não suporta o elemento de vídeo.
</video>

## Instalação e Requisitos
Para realizar a instalação, é necessário ter instalado o Python e o [Eclipse Mosquitto](https://mosquitto.org) (para simulação de um Broker MQTT). Em seguida, é preciso instalar a biblioteca Paho MQTT para Python utilizando o seguinte comando no terminal:

``` 
sudo apt-get install mosquitto mosquitto-clients

pip install paho-mqtt
```

Para a crição do broker, criei um arquivo chamado  `mosquitto.conf` e dentro adicione as seguintes linhas de codigo. 

``` 
listener 1892
allow_anonymous true
```

O `listener 1892` representa a porta que era ser util8izada, no meu caso, a porta 1891 deu erro e para resolver, apenas precisou mudar para 1892.


## Inicialização 

Para operar o sistema completo do projeto, serão necessários três terminais, cada um executando um componente diferente:
1. **Broker MQTT (Mosquitto)**
2. **Subscriber (subscriber.py)**
3. **Publisher (publisher.py)**

Inicialize o Broker MQTT com o comando:

```
mosquitto -c mosquitto.conf
```

Agora, inicie os arquivos de `publisher` e `subscriber` em 2 terminais diferentes utilizando o comando:

```
python3 publisher.py
python3 subscriber.py
```


Com essa configuração, as mensagens começarão a ser publicadas pelo Publisher e inscritas no tópico `sensor/humidity_1` (neste exemplo, o nome atribuído ao sensor). Os dados enviados podem ser modificados através do arquivo .csv localizado na pasta **sensor_data**. Este arquivo permite a inclusão de novos dados e sensores conforme necessário.
