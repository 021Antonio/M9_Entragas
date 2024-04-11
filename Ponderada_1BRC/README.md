# Nome do Projeto

Este repositório contém um script Python desenvolvido para gerar e processar um grande volume de medições de temperatura para diversas estações meteorológicas. Dada a natureza desafiadora do problema, com um arquivo de dados contendo 1 bilhão de registros, foram empregadas técnicas específicas para lidar com a geração e processamento eficiente desses dados.

## Estrutura de Arquivos

Aqui está uma descrição da estrutura de arquivos e pastas no projeto:

- `src/`: Pasta que contém o código fonte.
- `venv/`: Ambiente virtual Python onde as dependências são instaladas.
- `.gitignore`: Arquivo que especifica arquivos não rastreados pelo Git.
- `calculateAveragePolars.py`: Este arquivo contém a lógica para calcular médias usando a biblioteca Polars.
- `createMeasurements.py`: Script para criar medições de temperatura simuladas e salvá-las em `measurements.txt`.
- `measurements.txt`: Arquivo gerado pelo `createMeasurements.py`, contendo medições de temperatura.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.
- `resultados.txt`: Arquivo que armazena o resultado da análise de dados.
- `stations_data.py`: Arquivo que contém os dados das estações meteorológicas utilizadas para a geração de medições.
- `README.md`: Este arquivo, que contém informações e instruções sobre o projeto.

## Configuração do Ambiente

Para configurar o ambiente e instalar todas as dependências necessárias, siga estes passos:

1. Certifique-se de ter o Python instalado na sua máquina.
2. (Opcional) Crie e ative um ambiente virtual:

```sh
python -m venv venv
source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
```

3. Instale as dependências:

```sh
pip install -r requirements.txt
```

## Executando o Projeto

Para executar o script principal e gerar os resultados, use o comando abaixo. 

```sh
python createMeasurements.py
```

Os resultados serão salvos no arquivo resultados.txt na pasta raiz do projeto.

Para ver os resultados salvos, utilize o comando abaixo e veja o arquivo `resultados.txt` que será gerado. 

```sh
python src/calculateAveragePolars.py
```

# Desafio de Processamento de Grandes Volumes de Dados de Temperatura

## Estrutura do Código

O script `createMeasurements.py` utiliza a biblioteca `polars`, que é otimizada para operações de alto desempenho em grandes conjuntos de dados. Além disso, faz uso de funcionalidades da biblioteca `numpy` para geração de números aleatórios e operações matemáticas avançadas.

## Técnicas Utilizadas

### Geração de Dados Aleatórios

Utilizando a classe `default_rng` da `numpy`, geramos números aleatórios que simulam medições de temperatura. Isso garante que, mesmo sendo aleatórios, os dados sejam reproduzíveis, o que é essencial para testes e validação.

### Processamento em Lotes

Para lidar com a escrita eficiente de 1 bilhão de registros, o script divide o processo em lotes. Essa abordagem permite que o script mantenha um baixo consumo de memória e evite sobrecarregar o sistema, o que seria um risco se tentasse processar todos os registros de uma só vez.

### Parâmetros Customizáveis

O script aceita argumentos de linha de comando para customização do nome do arquivo de saída e a quantidade de registros a serem criados, oferecendo flexibilidade para diferentes necessidades de geração de dados.

### Progresso da Execução

A barra de progresso fornecida pela biblioteca `tqdm` oferece feedback visual em tempo real durante a criação dos dados, melhorando a experiência do usuário ao executar o script para grandes quantidades de dados.

# Análise de Dados de Temperatura

## Técnicas e Bibliotecas Utilizadas

### Polars

A biblioteca `polars` é utilizada para lidar eficientemente com a leitura e o agrupamento dos dados. Esta biblioteca é conhecida por sua alta performance com grandes conjuntos de dados, tornando-a ideal para os requisitos deste projeto.

### Lazy Evaluation

O método `scan_csv` da biblioteca `polars` utiliza avaliação preguiçosa (lazy evaluation) para escanear o arquivo de dados sem carregá-lo inteiramente na memória. Isso permite processar arquivos que são maiores do que a memória disponível.

### Agrupamento e Agregação

Os dados são agrupados por nome da estação meteorológica, e as funções de agregação são aplicadas para calcular as estatísticas mínimas, médias e máximas para as medições de cada estação.

### Ordenação

Os resultados agregados são ordenados pelo nome da estação meteorológica para facilitar a leitura e a localização das informações.

### Escrita em Arquivo

O script então escreve os resultados em um arquivo chamado `resultados.txt`, onde cada linha contém o nome da estação e suas respectivas estatísticas de temperatura, separadas por igual e barras (por exemplo, `Hamburg=12.0/23.1/34.2`).


## Nota

Este script assume que o arquivo de medições de temperatura está no formato correto, como especificado no desafio de processamento de dados.