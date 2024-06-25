import unittest
import os
import sys
import pathlib
from src.saver import JSONSaver
from src.models import Vacancy


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.json_saver = JSONSaver('test_vacancies.json')

    def tearDown(self):
        if os.path.exists(self.json_saver.file_path):
            os.remove(self.json_saver.file_path)

    def test_add_vacancy(self):
        vacancy = Vacancy('Test Vacancy', 'http://test-url.com', '100000-150000 руб.', 'Test description')
        self.json_saver.add_vacancy(vacancy)
        self.json_saver.save_vacancies()
        vacancies = self.json_saver.get_vacancies()
        self.assertEqual(len(vacancies), 1)

    def test_delete_vacancy(self):
        vacancy = Vacancy('Test Vacancy', 'http://test-url.com', '100000-150000 руб.', 'Test description')
        self.json_saver.add_vacancy(vacancy)
        self.json_saver.save_vacancies()
        self.json_saver.delete_vacancy(vacancy)
        self.json_saver.save_vacancies()
        vacancies = self.json_saver.get_vacancies()
        self.assertEqual(len(vacancies), 0)

    def test_add_and_get_vacancy(self):
        vacancy = Vacancy('Test Vacancy', 'http://test-url.com', '100000-150000 руб.', 'Test description')
        self.json_saver.add_vacancy(vacancy)
        self.json_saver.save_vacancies()
        vacancies = self.json_saver.get_vacancies()
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], 'Test Vacancy')


if __name__ == '__main__':
    # Запускаем тесты и выводим сообщение о успешном завершении
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestJSONSaver)
    result = unittest.TextTestRunner().run(suite)

    # Проверяем результаты тестов и выводим сообщение
    if result.wasSuccessful():
        print(f"The tests were completed successfully. {result.testsRun} tests passed.")
    else:
        print("Some tests failed.")
