import requests
from abc import ABC, abstractmethod

AREAS = {
    'Москва': '113',  # Пример числового идентификатора для Москвы
    'Санкт-Петербург': '2',  # Пример числового идентификатора для Санкт-Петербурга
    # Добавьте другие города по аналогии, если необходимо
}


class JobPlatformAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query: str, count: int, city: str = None) -> list:
        pass


class HeadHunterAPI(JobPlatformAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str, count: int, city: str = None) -> list:
        params = {
            'text': query,
            'per_page': count
        }
        if city and city in AREAS:
            params['area'] = AREAS[city]  # Используем числовой идентификатор для указания города

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()['items']
