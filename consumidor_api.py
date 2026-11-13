import requests 

def obter_dados():

    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": "-26.4851",
        "longitude": "-49.0713"
    }

    resposta = requests.get(
    url,
    params=parametros,
    timeout=15
    )

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["current"]["temperature_2m"]
        umidade = dados["current"]["relative_humidity_2m"]
        sensacao = dados["current"]["apparent_temperature"]
        data = dados["current"]["time"]

        print(f"Temperatura do ar: {temperatura}°C")
        print(f"Umidade do ar: {umidade}%")
        print(f"Sensação térmica: {sensacao}°C")
        print(f"Data/hora: {data}")
        return dados

    else:
        print("Tente novamente.")


obter_dados()


