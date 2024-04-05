https://www.loom.com/share/0850158c538f4c8d9c4d5880ded8b244?sid=ca820a8f-4b0f-432e-932b-06ee81f01774


# Sistema de Comunicação MQTT para Dados de Sensores

Este projeto implementa um sistema de comunicação MQTT para a publicação e inscrição de dados de sensores. Consiste em dois componentes principais: um `publisher` que envia dados de sensores, e um `subscriber` que recebe e armazena esses dados em um banco de dados SQLite.

## Estrutura do Projeto

- `docs/`: Arquivos relacionados à documentação.
- `images/`: Recursos de imagens.
- `src/`: Código fonte do projeto.
    - `code/`: Contém os scripts Python para o publisher e subscriber.
    - `data_sensor/`: Arquivos CSV com dados de sensores a serem publicados.
- `metabase-data/`: Arquivos de banco de dados para armazenar dados subscribers.
- `venv/`: Ambiente virtual para as dependências do projeto.
- `.env`: Variáveis de ambiente para configuração do broker MQTT.
- `.gitignore`: Especifica arquivos não rastreados que devem ser ignorados.

## publisher

O script `publisher.py` é responsável por ler os dados de sensores de um arquivo CSV e publicá-los em um tópico MQTT especificado. Ele usa as variáveis de ambiente definidas no arquivo `.env` para configurar a conexão com o broker MQTT e autenticação.

## subscriber

O `subscriber.py` inscreve-se no tópico MQTT configurado e, ao receber dados, insere-os em uma tabela no banco de dados SQLite. O script também configura a tabela do banco de dados caso ela ainda não exista.

## Configuração e Execução

Antes de executar os scripts, instale as dependências e configure o ambiente virtual conforme necessário. Além disso, certifique-se de configurar corretamente o arquivo `.env` com os detalhes do seu broker MQTT.

Para executar o publisher, navegue até a pasta `src/code` e execute:

```bash
python publisher.py
```
Para iniciar o subscriber, em um terminal separado, execute:

```bash
python subscriber.py
```
## Requisitos

- Python 3
- Paho-MQTT
- SQLite3


Lembre-se de ajustar as instruções de configuração e execução conforme necessário para seu ambiente específico e adicionar o nome da licença correta no final.
Para melhor informação, [Clique Aqui!](https://github.com/021Antonio/M9_Entragas/tree/main/Ponderadas/docs/ponderada3)

