```markdown
# GAIA CALL

**GAIA CALL** es una herramienta enfocada en el envío masivo de mensajes SMS y llamadas, diseñada para simular un ataque de denegación de servicio (DoS) a través de mensajes. Este proyecto se basa en la estructura de Quack Toolkit, pero optimizado para trabajar en España, con una capacidad de envío entre 50 a 100 SMS por ataque.

## Características

- Envío masivo de SMS (50-100 por ataque).
- Soporte para llamadas automáticas con mensajes predefinidos.
- Optimizado para funcionar sin registro en proveedores externos (ej. Twilio).
- Herramienta ligera y fácil de usar desde la terminal de macOS.

## Instalación

### Requisitos

- **Python 3.8 o superior**
- Bibliotecas necesarias (instaladas a través de `pip`):
    - `requests`

### Pasos de instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/wavecheff/Gaia-Call.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd Gaia-Call
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar **GAIA CALL** y enviar SMS, usa el siguiente comando en la terminal:

```bash
python3 gaia_call.py --target <número_destino> --message "Mensaje a enviar" --count 50
```

- `--target`: Número de teléfono de destino en formato internacional (+34 para España).
- `--message`: El mensaje que deseas enviar.
- `--count`: Número de mensajes SMS a enviar.

### Ejemplo

```bash
python3 gaia_call.py --target +34612345678 --message "Hola, este es un mensaje de prueba" --count 50
```

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu mejora o corrección:

    ```bash
    git checkout -b mi-nueva-rama
    ```

3. Realiza tus cambios y haz commit:

    ```bash
    git commit -m "Descripción de los cambios"
    ```

4. Envía tu rama al repositorio remoto:

    ```bash
    git push origin mi-nueva-rama
    ```

5. Crea una Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo `LICENSE`.

```
