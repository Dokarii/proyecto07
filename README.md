import requests

def obtener_tasa_cambio():
    url = "https://api.exchangerate-api.com/v4/latest/COP"
    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"].get("USD", None)
    except Exception as e:
        print("Error al obtener la tasa de cambio:", e)
        return None

def convertir_cop_a_usd(cop):
    tasa = obtener_tasa_cambio()
    if tasa:
        return round(cop * tasa, 2)
    else:
        return "No se pudo obtener la tasa de cambio"

if __name__ == "__main__":
    cop = float(input("Ingrese la cantidad en COP: "))
    usd = convertir_cop_a_usd(cop)
    print(f"{cop} COP equivalen a {usd} USD")


////////////////////////////////////////////////////////////////
PS C:\Users\desarrollo\proyecto07> .\env\Scripts\activate
(env) PS C:\Users\desarrollo\proyecto07> pip install requests
