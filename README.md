
# Prova Data Eng

Esse código simula um processo de aquisição, tratamento e processamento de dados. Definiu-se um banco fonte, um banco alvo, uma API e um processo de ETL.

## Pré-Requisitos
##### Instalar docker. (docker-engine);
##### Inicializar docker;

```bash
git clone https://github.com/matheusjtavares/Docker-Fast-API
```

## Rotas/ Portas Locais:
##### localhost:80 -> FastAPI
##### localhost:5432-> Banco Fonte
##### localhost:5433-> Banco Alvo
##### localhost:5000-> PgAdmin4 Web

## Containers / Serviços:
##### FastAPI - fastapi-app
##### Postgres Source - postgres-source-db
##### Postgres Target - postgres-target-db
##### PgAdmin4 Web - pgadmin-app
##### Python - python-app

## Passo a Passo - Execução
#### 1. Abra o CMD/bash no diretório raiz do repositório 
#### 2. Buildar docker-compose
```bash
docker-compose -f docker-compose.yml build
```
#### 2. Ativar serviços do docker-compose
```bash
docker-compose -f docker-compose.yml up -d
```
##### A criação do container irá configurar os bancos de dados de acordo com as configurações estabelecidas. O banco fonte é alimentado por dados aleatórios conforme o arquivo init_db.sql (de 2024-05-01 até 2024-05-10 23:59).
#### 3. Rodar Manualmente a criação do banco alvo
```bash
docker-compose run python-app python .code/etl/create_db.py
```
##### O banco alvo é criado durante a execução do código ./etl/create_db.py, que configura a database alvo e as tabelas de registro necessárias.

#### 4. Rodar Manualmente a aquisição de dados
```bash
docker-compose run python-app python .code/etl/etl_process.py
```
##### O arquivo etl_process.py contém a seguinte função:
```python
get_data_from_source_to_target(variables,start_date,end_date)
``` 
##### Caso deseje testar o processo para mais variáveis ou outros períodos, basta editar os parâmetros na execução da função e reexecutar todos os passos descritos.



