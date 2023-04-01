import unittest

from ReportGenerator import ReportGenerator


class TestLiczbaOkresowPrzegrzania(unittest.TestCase):

    def test_brak_logow(self):
        lines = []
        generator = ReportGenerator()
        result = generator.liczba_okresow_przegrzania(lines)
        self.assertEqual(result, 0)

    def test_brak_przegrzania(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:10 95C",
            "2023-01-01 23:20 100C"
        ]
        generator = ReportGenerator()
        result = generator.liczba_okresow_przegrzania(lines)
        self.assertEqual(result, 0)

    def test_jedno_przegrzanie(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:10 105C",
            "2023-01-01 23:20 100C"
        ]
        generator = ReportGenerator()
        result = generator.liczba_okresow_przegrzania(lines)
        self.assertEqual(result, 1)

    def test_wiele_przegrzan(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:10 105C",
            "2023-01-01 23:20 110C",
            "2023-01-01 23:30 100C",
            "2023-01-01 23:40 110C",
            "2023-01-01 23:50 115C",
            "2023-01-02 00:00 100C"
        ]
        generator = ReportGenerator()
        result = generator.liczba_okresow_przegrzania(lines)
        self.assertEqual(result, 2)

    def test_mieszane_logi(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:10 105C",
            "2023-01-01 23:20 110C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-01 23:30 100C",
            "2023-01-01 23:40 110C",
            "2023-01-01 23:50 115C",
            "2023-01-02 00:10"
        ]
        generator = ReportGenerator()
        result = generator.liczba_okresow_przegrzania(lines)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
