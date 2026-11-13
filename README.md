# PROVA_TESTE

Projeto da prova prática. Ele pega os dados do tempo de uma API que roda no meu computador e mostra numa página feita com Streamlit.

Cidade usada: Jaraguá do Sul – SC (latitude -26.4851, longitude -49.0713).

## Arquivos

- `consumidor_api.py` – faz a requisição na API e pega os dados
- `frontend.py` – a tela feita com Streamlit
- `requirements.txt` – bibliotecas usadas

## Como instalar

1. Baixar o projeto:

```bash
git clone https://github.com/julianabcor/PROVA_TESTE.git
cd PROVA_TESTE
```

2. Instalar as bibliotecas (principais: `streamlit`, `requests` e `uvicorn`):

```bash
pip install -r requirements.txt
```

## Como rodar

1. Baixar a API do professor: https://github.com/jpsvalentim/api-meteorologica-offline
2. Em um terminal, dentro da pasta da API, ligar ela (o terminal tem que ficar aberto):

```bash
uvicorn app.main:app --reload
```

A API fica em http://127.0.0.1:8000 e a documentação em http://127.0.0.1:8000/docs

3. Em **outro terminal**, na pasta deste projeto, rodar a tela:

```bash
streamlit run frontend.py
```

## Sobre a API

- Endereço usado: `GET http://127.0.0.1:8000/v1/forecast?latitude=-26.4851&longitude=-49.0713`
- Retorna em JSON, dentro de `current`: temperatura (`temperature_2m`), umidade (`relative_humidity_2m`), sensação térmica (`apparent_temperature`) e horário (`time`). Também tem precipitação (`precipitation`) e vento (`wind_speed_10m`).
- Os nomes têm que ser escritos exatamente assim.
- Códigos: 200 deu certo, 400 parâmetro inválido, 404 não encontrado, 500 erro interno.

## Se der erro

- Erro de conexão: a API não está ligada. Conferir se o terminal do `uvicorn` está aberto.
