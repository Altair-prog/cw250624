import json
from pathlib import Path
from project_folder.src.models import Vacancy

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def save_vacancies(self, vacancies):
        data = []
        for vacancy in vacancies:
            vacancy_data = {
                "title": vacancy.title,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "description": vacancy.description
            }
            data.append(vacancy_data)

        file_path = Path(__file__).parent.parent / 'data' / self.filename  # Путь к файлу vacancies.json
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Пример использования
    vacancies = [
        Vacancy("Тестировщик", "https://hh.ru/vacancy/123456", None, "Описание вакансии 1"),
        Vacancy("Разработчик", "https://hh.ru/vacancy/789012", "100000 - 150000 руб.", "Описание вакансии 2")
    ]
    saver = JSONSaver('vacancies.json')
    saver.save_vacancies(vacancies)
