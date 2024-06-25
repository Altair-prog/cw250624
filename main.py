from src.saver import JSONSaver
from src.api import HeadHunterAPI, AREAS  # Импортируем AREAS из src.api
from src.models import Vacancy
import sys
import requests


def user_interaction():
    query = input("Введите поисковый запрос: ")
    count = int(input("Введите количество вакансий: "))  # Вводим количество вакансий, которое хотим получить
    city = input("Введите название города (или оставьте пустым для поиска по всей России): ")

    # Используем API для получения вакансий
    api = HeadHunterAPI()
    try:
        if city.strip() and city in AREAS:  # Проверяем, был ли введен город и он содержится в словаре AREAS
            vacancies_data = api.get_vacancies(query, count, city=city)
        else:
            vacancies_data = api.get_vacancies(query, count)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса к API: {e}")
        sys.exit(1)

    # Преобразуем данные вакансий из словарей в объекты Vacancy
    vacancies = []
    for vacancy_data in vacancies_data:
        # Извлекаем нужные данные из словаря
        title = vacancy_data.get('name', 'Не указано')
        url = vacancy_data.get('url', '')
        salary = vacancy_data.get('salary', None)
        description = vacancy_data.get('description', '')

        # Создаем объект Vacancy и добавляем его в список
        vacancy = Vacancy(title, url, salary, description)
        vacancies.append(vacancy)

    # Сохраняем вакансии в JSON файл
    json_saver = JSONSaver('vacancies.json')
    for vacancy in vacancies:
        json_saver.add_vacancy(vacancy)
    json_saver.save_vacancies()  # Сохраняем вакансии после добавления всех данных
    print(f"Вакансии успешно сохранены в файл {json_saver.filename}")


if __name__ == "__main__":
    user_interaction()
