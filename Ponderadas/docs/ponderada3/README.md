# Sistema de Comunicação de Dados de Sensores com MQTT

Este repositório contém um sistema de comunicação baseado em MQTT para dados de sensores, utilizando Python e a biblioteca Paho MQTT. O sistema é composto por duas partes: um publisher que envia os dados dos sensores e um subscriber que ouve e recebe esses dados.

[Video de Demostração](https://www.loom.com/embed/1474f994f6de44949373365f8c43db40?sid=9318fd06-2fd1-482d-b907-171160e88065)

## Visão Geral do Sistema

O **publisher** lê os dados dos sensores de um arquivo CSV e os publica em um tópico MQTT especificado.

O **subscriber** ouve o mesmo tópico MQTT e exibe os dados dos sensores recebidos.

Ambos, publisher e subscriber, estão configurados para se conectar a um broker MQTT hospedado em `b2d33a9f975547e0b35739621effd029.s1.eu.hivemq.cloud`.

## Pré-requisitos

- Python 3.x
- Biblioteca Paho MQTT
- Acesso a um broker MQTT

## Instalação e Configuração

1. Clone o repositório para a sua máquina local.
2. Instale as dependências necessárias com `pip install paho-mqtt python-dotenv`.
3. Crie um arquivo `.env` na raiz do diretório do projeto com as seguintes variáveis:

``` 
HIVE_USER=SeuUsuarioHiveMQ
HIVE_PSWD=SuaSenhaHiveMQ
BROKER_ADDR=EnderecoDoSeuBroker
```

Substitua `SeuUsuarioHiveMQ`, `SuaSenhaHiveMQ` e `EnderecoDoSeuBroker` pelos seus dados reais.

## Execução do Sistema

### Iniciando o publisher

Execute o comando:

```
python3 src/code/publisher.py
```

Isso iniciará a leitura dos dados do arquivo `data_sensor/sensor_data.csv` e a publicação dos dados de sensores no tópico `my/test/topic`.

### Iniciando o subscriber

Execute o comando:

``` 
python3 src/code/subscriber.py
```


Isso se inscreverá no tópico `my/test/topic` e exibirá quaisquer dados de sensores recebidos.

## Estrutura do Projeto

- `src/`: Contém o código-fonte para o publisher e subscriber.
- `data_sensor/`: Contém o arquivo CSV com dados de sensores a serem publicados.
- `.env`: Arquivo para armazenar variáveis de ambiente como o endereço do broker e credenciais.
- `.gitignore`: Especifica arquivos que devem ser intencionalmente não rastreados pelo Git.

## Observações

Certifique-se de que seu broker MQTT esteja em execução e acessível no endereço especificado no seu arquivo `.env`. O broker MQTT utilizado para este projeto é o HiveMQ Cloud, mas o sistema pode ser adaptado para usar outro broker MQTT se necessário.

