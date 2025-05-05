# API Kit Tests

Este proyecto contiene un conjunto de pruebas automatizadas para la API de creación de kits, verificando la funcionalidad de la solicitud de nuevos kits. Utiliza `pytest` para la ejecución de pruebas y está diseñado para asegurar que la API maneje correctamente diferentes escenarios de entrada.

## Pruebas para el Parámetro `name` al Crear un Kit de Usuario/a

### Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes:

- `pytest`
- `requests`

Puedes instalarlos utilizando `pip`:

```bash
pip install pytest requests
```

## Ejecución de Pruebas

Para ejecutar todas las pruebas, usa el siguiente comando en la terminal:

```bash
pytest create_kit_name_kit_test.py
```

Este comando ejecutará todas las pruebas definidas en el archivo `create_kit_name_kit_test.py`.

## Descripción de las Pruebas

Este conjunto de pruebas verifica el comportamiento del parámetro `name` al crear un kit de usuario/a a través de la API.

Las pruebas cubren los siguientes escenarios:

- **Valores válidos**: Prueba de diferentes valores que cumplen con los requisitos de longitud y formato.
- **Valores válidos con longitud límite**: Verificación de nombres que alcanzan el límite máximo de longitud permitido.
- **Valores inválidos**: Se prueba con nombres que contienen caracteres no permitidos, como caracteres especiales o números.
- **Valores con longitud mayor o menor a la permitida**: Pruebas para nombres demasiado largos o demasiado cortos.
- **Ausencia del parámetro `name`**: Verificación de la respuesta cuando el parámetro `name` no se incluye en la solicitud.

## Resultados Esperados

Cada prueba debe retornar un código de estado HTTP adecuado, dependiendo del resultado esperado:

- **Códigos de éxito (por ejemplo, 200 o 201)** para nombres válidos.
- **Códigos de error (por ejemplo, 400 o 422)** para valores inválidos o casos en los que faltan parámetros.

Asegúrate de revisar los resultados después de ejecutar las pruebas para validar que el comportamiento de la API es el esperado.

## Características

- Pruebas positivas para la creación de kits con nombres válidos.
- Pruebas negativas para manejar errores de entrada, como nombres con espacios, números o tipos inválidos.
- Verificación de respuestas de la API, incluyendo códigos de estado y mensajes de error.

## Estructura del Código

El código está organizado en varios módulos:

- **`configuracion.py`**: Contiene las configuraciones necesarias, como la URL base y las rutas de la API.
- **`create_kit_name_kit_test.py`**: Contiene las pruebas automatizadas para la creación de kits, incluyendo pruebas positivas y negativas.
- **`data.py`**: Proporciona datos de prueba y configuraciones necesarias para las pruebas, incluyendo encabezados y el cuerpo de la solicitud para crear kits.
- **`sender_stand_request.py`**: Maneja las solicitudes a la API, incluyendo la creación de usuarios y la gestión de kits.

## Programas Recomendados

Para ejecutar el código de manera adecuada, se recomienda tener instalados los siguientes programas:

- **Python**: Asegúrate de tener Python 3.x instalado en tu máquina.
- **Postman**: Para realizar pruebas manuales de la API.
- **Visual Studio Code** o cualquier otro editor de código: Para editar y gestionar el código fuente.
- **Git**: Para clonar el repositorio y gestionar el control de versiones.

## Información Adicional

Si encuentras errores o tienes sugerencias para mejorar las pruebas, por favor abre un **issue** en este repositorio.

## Información del Autor

- **Nombre**: Eduardo Reyna Hernández  
- **Cohorte**: 19
