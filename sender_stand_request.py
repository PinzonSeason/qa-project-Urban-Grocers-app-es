import configuration
import requests
import data


def get_new_user_token():
    headers = data.headers
    url = configuration.URL + configuration.CREATE_USER_PATH
    body = data.user_body
    response =  requests.post(url, headers=headers, json=body)
    # Revisar que el usuario se haya creado y regresar el token
    token = None
    if response.status_code == 404:
        print("Error al crear usuario, revise la URL del servidor en configuration.py")
    elif response.status_code == 201:
        print("Usuario creado con exito")
        token = response.json()["authToken"]
    else:
        print("Usuario no creado", response)
    return token

def post_new_client_kit(kit_body, auth_token):
    url = configuration.URL + configuration.CREATE_KIT
    headers = data.headers
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(url, headers=headers, json=kit_body)
    return response

