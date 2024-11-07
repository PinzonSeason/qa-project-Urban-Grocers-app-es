import configuration
import data
import sender_stand_request


def get_kit_body(name=None):
    # Si no se pasa un nombre, devolvemos un diccionario vacío
    kit_body = {}
    if name:
        kit_body["name"] = name
    return kit_body


def post_new_client_kit(numero_de_prueba, status):
    # Obtener el token de usuario antes de crear el kit
    token = sender_stand_request.get_new_user_token()

    # Obtener el cuerpo de la solicitud
    kit_body = get_kit_body(data.valores_prueba[numero_de_prueba])

    # En la prueba 8, el cuerpo debe estar vacío, eliminamos el nombre si existe
    if numero_de_prueba == 8:
        kit_body.pop("name", None)  # Eliminar el parámetro 'name' si existe

    # Enviar la solicitud y obtener la respuesta
    response = sender_stand_request.post_new_client_kit(kit_body=kit_body, auth_token=token)

    # Realizar la aserción sobre el código de estado
    print(f"Prueba {numero_de_prueba} - Esperado: {status}, Obtenido: {response.status_code}")

    assert response.status_code == status
    if status == 201:
        assert response.json().get('name') == kit_body.get('name', None)
    if status == 400:
        print("Respuesta completa (400): ", response.json())


# -------------------------------------------------------------#

# Pruebas positivas (esperado: código 201)
def test_create_kit_1_letter_in_name_get_success_response():
    """Prueba que crea un kit con un solo carácter en el nombre y obtiene una respuesta 201"""
    post_new_client_kit(1, 201)

def test_create_kit_64_letters_in_name_get_success_response():
    """Prueba que crea un kit con 64 caracteres en el nombre y obtiene una respuesta 201"""
    post_new_client_kit(2, 201)

def test_create_kit_empty_name_get_success_response():
    """Prueba que crea un kit con nombre vacío y obtiene una respuesta 201"""
    post_new_client_kit(3, 201)

def test_create_kit_name_with_255_chars_get_success_response():
    """Prueba que crea un kit con nombre de 255 caracteres y obtiene una respuesta 201"""
    post_new_client_kit(4, 201)

def test_create_kit_name_with_special_characters_get_success_response():
    """Prueba que crea un kit con caracteres especiales en el nombre y obtiene una respuesta 201"""
    post_new_client_kit(5, 201)


# -------------------------------------------------------------#

# Pruebas negativas (esperado: código 400)
def test_create_kit_with_spaces_in_name_get_bad_response():
    """Prueba que crea un kit con espacios en el nombre y obtiene una respuesta 400"""
    post_new_client_kit(6, 400)

def test_create_kit_with_numbers_in_name_get_bad_response():
    """Prueba que crea un kit con números en el nombre y obtiene una respuesta 400"""
    post_new_client_kit(7, 400)

def test_create_kit_with_invalid_type_in_name_get_bad_response():
    """Prueba que crea un kit con un tipo no válido en el nombre y obtiene una respuesta 400"""
    post_new_client_kit(8, 400)

def test_create_kit_with_integer_name_get_bad_response():
    """Prueba que crea un kit con un número entero como nombre y obtiene una respuesta 400"""
    post_new_client_kit(9, 400)


# -------------------------------------------------------------#

# Definir la URL (no es necesario modificar esto en este bloque de pruebas)
url = configuration.URL + configuration.CREATE_KIT
