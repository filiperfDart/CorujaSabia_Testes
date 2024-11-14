
# Projeto de teste de performance, para sistema educacional CorujaSabia

Este projeto buscar implementar testes em python para analisar e testar a perfomance de um sistema educacional de aulas, o teste utiliza o framework Locust como principal recurso para execução dos testes.





## Rodando os testes

Para rodar os testes, é necessario ter instalados:

Python3.12 ou superior \
Poetry 1.8.4 ou superior
## Instalação

Processo de instalação utilizado:

```bash
  python -m pip install poetry==1.8.4  

```
    
## Execução dos testes

Para executar o teste, abra na pasta um prompt de comando e execute o codigo:

```bash
python -m poetry run locust --locustfile .\Login_Test.py --csv CorujaSabia_Test --logfile CorujaSabia_Log
```

Após executar acesse localhost:8089 e inicie os testes. \
No final da execução do teste será gerado na pasta do repositorio os arquivos CSV de erros e falhas e também o arquivo de log.
## Funcionalidades

- Temas dark e light
- Preview em tempo real
- Multiplataforma

