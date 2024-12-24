# pySide6-door

![](https://i.imgur.com/sS6bYnB.png)

Control de puerta usando Arduino, Python y MongoDB

## Librerías necesarias

- sys, os, random, time, ssl
- smtplib
- dotenv
- email
- pymata4
- pymongo
- PySide6

```bash
pip install -r requirements.txt
```

# Requisitos

1. [FirmataExpress](https://mryslab.github.io/pymata4/firmata_express/#installation-instructions)
2. Crear un archivo `.env` con la información del servicio de email [usado ](https://docs.python.org/3/library/email.examples.html)
 ```env
FROM=correo-origen@example.com
TO=correo-destino@example.com
SSL_HOST=smtp.host-de-correo.com
SSL_PORT=puerto-de-correo
PASSWORD=contraseña
```

## Características

- Uso de pymata4 para controlar el selenoide de una puerta con códigos de acceso enviados por email.
- Almacenamiento del historial de accesos en una base de datos local con MongoDB.

### En proceso

> [!TIP]
>
> - Enviar notificaciones de acceso por email.
> - Uso de una base de datos en la nube.
> - Agregar el circuito electronico del proyecto.
