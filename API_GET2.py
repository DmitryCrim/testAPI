import requests


class test_new_joke():
    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус-код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили новую шутку")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = 'utf-8'
        print(result.text)

        """проверяем значения ключей (категория)"""
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Категория верна")

        """проверяем значения ключей (value)"""
        check_info_value = check.get("value")
        print(check_info_value)

        """проверяем проверяем есть ли в value значение Chuck - проверяем значение поля"""

        name = "Chuck"
        if name in check_info_value:
            print("Chuck присутствует")
        else:
            print("Chuck отсутствует")


            """*** выбираем категорию  шутки"""

    def test_create_new_random_categories_joke_(self):
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Статус-код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили новую шутку")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = 'utf-8'
        print(result.text)

        """проверяем значения ключей (категория)"""
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верна")
        #
        # """проверяем значения ключей (value)"""
        # check_info_value = check.get("value")
        # print(check_info_value)
        #
        # """проверяем проверяем есть ли в value значение Chuck - проверяем значение поля"""
        #
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Chuck отсутствует")





sport_joke = test_new_joke()
sport_joke.test_create_new_random_categories_joke_()
