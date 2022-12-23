import requests


class test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовая url
        post_resource = "/maps/api/place/add/json"  # ресурс метода post
        key = "?key=qaclick123"  # параметры для всех запросов
        post_url = base_url + post_resource + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print("Статус-код: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Мы получили новую локацию")
        else:
            print("Провал!!! Запрос ошибочный")
        result_post.encoding = 'utf-8'
        print(result_post.text)
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код-ответа: " + check_info_post)
        assert check_info_post == "OK"
        print('Статус ответа верен')
        place_id = check_post.get("place_id")
        print("Id-адрес локации равен: " + place_id)

        """Проверяем создание новой локации"""
        # place_id = "5555"
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус-код: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка создание новой локации")
        else:
            print("Провал!!! Запрос ошибочный. Локация не создалась!!!")

            """Изменяем новую локацию"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print("Статус-код: " + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Успешно!!! Проверка обновления локации")
        else:
            print("Провал!!! Запрос ошибочный. Локация не обновилась!!!")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Сообщение: " + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Сообщение верно")

        """Проверка измения новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус-код: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка измения новой локации")
        else:
            print("Провал!!! Запрос ошибочный. Локация не изменилась!!!")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Сообщение: " + check_address_info)
        assert check_address_info == "100 Lenina street, RU"
        print("Адрес верный")

        """удаление новой локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": "4c4452fa0570dcc0f763b0253cac9aa6"
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print("Статус-код: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("Успешно!!! Удаление новой локации")
        else:
            print("Провал!!! Запрос ошибочный. Локация не удалилась!!!")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение: " + check_status_info)
        assert check_address_info == "OK"
        print("Адрес верный")



new_place = test_new_location()
new_place.test_create_new_location()
