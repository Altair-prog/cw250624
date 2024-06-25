import json
from pathlib import Path
from .models import Vacancy  # Импортируем модель Vacancy

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = Path(__file__).parent.parent / 'data' / self.filename  # Путь к файлу vacancies.json
        self.data = []

    def add_vacancy(self, vacancy):
        self.data.append({
            "title": vacancy.title,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description
        })

    def delete_vacancy(self, vacancy):
        self.data = [v for v in self.data if v["title"] != vacancy.title]

    def save_vacancies(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def _load_vacancies(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def get_vacancies(self):
        return self.data
