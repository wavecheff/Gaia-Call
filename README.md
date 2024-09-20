# 🌍 GAIA CALL 🌍

**GAIA CALL** es una herramienta de seguridad diseñada para enviar mensajes SMS y realizar llamadas de manera masiva, simulando ataques de denegación de servicio (DoS) a través de mensajes o llamadas. Inspirado en Quack Toolkit, está optimizado para operar en España y es fácil de usar desde terminales macOS.

## 🛠 Características

- Envío masivo de SMS (50-100 por ataque).
- Llamadas automáticas con mensajes predefinidos.
- Sin necesidad de proveedores como Twilio.
- Fácil uso desde la terminal.

## 🚀 Instalación

### Requisitos

- **Python 3.8 o superior**
- Librería `requests`

### Pasos

1. Clona el repositorio:

   ```bash
   git clone https://github.com/wavecheff/Gaia-Call.git
   ```

2. Navega al directorio:

   ```bash
   cd Gaia-Call
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Uso

Para enviar SMS o realizar llamadas masivas, utiliza el siguiente comando:

### Enviar SMS

```bash
python3 gaia_call.py --target <número_destino> --message "Mensaje a enviar" --count 50
```

### Realizar una llamada

```bash
python3 gaia_call.py --target <número_destino> --message "Mensaje de llamada"
```

### Ejemplo

```bash
python3 gaia_call.py --target +34612345678 --message "Prueba" --count 50
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

