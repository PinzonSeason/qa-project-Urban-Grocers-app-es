import configuration
import data
import sender_stand_request

def get_kit_body(name):
    return {"name": name}

def prueba(numero_de_prueba, status):
    kit_body = get_kit_body(data.valores_prueba[numero_de_prueba])
    response = sender_stand_request.post_new_client_kit(kit_body=kit_body, auth_token=token)
    assert response.status_code == status


def test_positive_assert_1():
    prueba(1, 201)

def test_positive_assert_2():
    prueba(2, 201)

def test_positive_assert_3():
    prueba(3, 201)

def test_positive_assert_4():
    prueba(4, 201)

def test_positive_assert_5():
    prueba(5, 201)

def test_positive_assert_6():
    prueba(6, 201)

def test_positive_assert_7():
    prueba(7, 201)

def test_positive_assert_8():
    prueba(8, 201)

def test_positive_assert_9():
    prueba(9, 201)

#-------------------------------------------------------------#

def test_negative_assert_400_1():
    prueba(1, 400)

def test_negative_assert_400_2():
    prueba(2, 400)

def test_negative_assert_400_3():
    prueba(3, 400)

def test_negative_assert_400_4():
    prueba(4, 400)

def test_negative_assert_400_5():
    prueba(5, 400)

def test_negative_assert_400_6():
    prueba(6, 400)

def test_negative_assert_400_7():
    prueba(7, 400)

def test_negative_assert_400_8():
    prueba(8, 400)

def test_negative_assert_400_9():
    prueba(9, 400)


token = sender_stand_request.get_new_user_token()
url = configuration.URL + configuration.CREATE_KIT
