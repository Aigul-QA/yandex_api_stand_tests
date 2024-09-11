# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = 'https://6a93ec05-1174-42c8-93a9-df1192bb062e.serverhub.praktikum-services.ru'

# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"
DOC_PATH = "/docs/"

LOG_MAIN_PATH = "/api/logs/main/"

USERS_TABLE_PATH = "/api/db/resources/user_model.csv"

CREATE_USER_PATH = "/api/v1/users/"

PRODUCTS_KITS_PATH = "/api/v1/products/kits/"