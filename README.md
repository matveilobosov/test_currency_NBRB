# Currency Rates Microservice

Этот микросервис предоставляет API для получения курсов валют с сайта Национального банка Республики Беларусь (НБ РБ).

## Функциональность

Микросервис имеет два конечных точки (endpoint):

1. **Получение курсов валют за выбранную дату**
    - **URL**: `/api/rates`
    - **Метод**: `GET`
    - **Параметры запроса**:
        - `date` (обязательный): Дата в формате `YYYY-MM-DD`.
    - **Формат ответа**:
        ```json
        {
            "Cur_Abbreviation": "USD",
            "Cur_Scale": 1,
            "Cur_Name": "Доллар США",
            "Cur_OfficialRate": 2.5469
        }
        ```
    - **Заголовок ответа**:
        - `X-CRC32`: Контрольная сумма CRC32 тела ответа.

2. **Получение курса конкретной валюты за выбранную дату**
    - **URL**: `/api/rate`
    - **Метод**: `GET`
    - **Параметры запроса**:
        - `date` (обязательный): Дата в формате `YYYY-MM-DD`.
        - `code` (обязательный): Код валюты (например, 840 для USD).
    - **Формат ответа**:
        ```json
        {
            "Cur_ID": 145,
            "Date": "2024-05-01T00:00:00",
            "Cur_Abbreviation": "USD",
            "Cur_Scale": 1,
            "Cur_Name": "Доллар США",
            "Cur_OfficialRate": 2.5469
        }
        ```
    - **Заголовок ответа**:
        - `X-CRC32`: Контрольная сумма CRC32 тела ответа.

## Инструкция по запуску

### Требования

- Python 3.6 и выше
- `pip` (пакетный менеджер Python)

### Установка

1. Клонируйте репозиторий или скачайте файлы проекта.
    ```bash
    git clone https://github.com/yourusername/currency-rates-microservice.git
    cd currency-rates-microservice
    ```

2. Создайте и активируйте виртуальное окружение (опционально, но рекомендуется).
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
    ```

3. Установите зависимости.
    ```bash
    pip install -r requirements.txt
    ```

### Запуск

1. Запустите приложение Flask.
    ```bash
    python app.py
    ```

2. Микросервис будет доступен по адресу `http://127.0.0.1:5000`.

### Примеры запросов

#### Получение курсов валют за выбранную дату

- **Запрос**:
    ```http
    GET /api/rates?date=2024-05-01 HTTP/1.1
    Host: 127.0.0.1:5000
    ```

- **Ответ**:
    ```json
    [
        {
            "Cur_Abbreviation": "USD",
            "Cur_Scale": 1,
            "Cur_Name": "Доллар США",
            "Cur_OfficialRate": 2.5469
        },
        {
            "Cur_Abbreviation": "EUR",
            "Cur_Scale": 1,
            "Cur_Name": "Евро",
            "Cur_OfficialRate": 3.0567
        }
    ]
    ```

#### Получение курса конкретной валюты за выбранную дату

- **Запрос**:
    ```http
    GET /api/rate?date=2024-05-01&code=840 HTTP/1.1
    Host: 127.0.0.1:5000
    ```

- **Ответ**:
    ```json
    {
        "Cur_ID": 145,
        "Date": "2024-05-01T00:00:00",
        "Cur_Abbreviation": "USD",
        "Cur_Scale": 1,
        "Cur_Name": "Доллар США",
        "Cur_OfficialRate": 2.5469
    }
    ```

## Логирование

Микросервис использует стандартное логирование Python для записи важных событий и ошибок. Логи можно найти в консоли, где запущен сервис.

## Автор

- [Matvei Lobosov](https://github.com/matveilobosov)

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).
