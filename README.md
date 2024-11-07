# Pruebas para el Parámetro `name` al Crear un Kit de Usuario/a

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes:

- `pytest`
- `requests`

Puedes instalar estos paquetes utilizando `pip`: pip install pytest requests

## Ejecución de Pruebas

Para ejecutar todas las pruebas, usa el siguiente comando en la terminal: `pytest create_kit_name_kit_test.py`

Este comando ejecutará todas las pruebas definidas en el archivo `create_kit_name_kit_test.py`.

## Descripción de las Pruebas

Este conjunto de pruebas verifica el comportamiento del parámetro `name` al crear un kit de usuario/a a través de la API [nombre de la API/endpoint].

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

## Información Adicional

Si encuentras errores o tienes sugerencias para mejorar las pruebas, por favor abre un **issue** en este repositorio.

## Información del Autor

- **Nombre**: Eduardo Reyna Hernández
- **Cohorte**: 15