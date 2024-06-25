from typing import Optional

class Vacancy:
    def __init__(self, title: str, url: str, salary: Optional[str], description: str):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def get_salary_value(self) -> int:
        if self.salary is None or not isinstance(self.salary, str):
            return 0

        if self.salary.lower() == 'не указана':
            return 0

        salary_range = self.salary.split('-')
        if len(salary_range) > 0:
            try:
                return int(salary_range[0].replace(' ', ''))
            except ValueError:
                return 0
        return 0

    def __repr__(self) -> str:
        return f"Vacancy(title={self.title}, url={self.url}, salary={self.salary}, description={self.description})"
