# Импорт настроек из модуля/файла configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# POST-ЗАПРОСЫ
# Функция для отправки POST-запроса, на создание Заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.orders_body)
print(response.status_code)
print(response.json())

# Функция для отправки GET-запроса, на получение заказа по его номеру/треку
def get_order_within_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        params={"t": track_number})
