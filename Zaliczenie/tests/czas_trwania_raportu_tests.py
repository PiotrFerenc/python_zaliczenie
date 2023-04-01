import unittest

from ReportGenerator import ReportGenerator


class TestCzasTrwaniaRaportu(unittest.TestCase):

    def test_brak_logow(self):
        lines = []
        generator = ReportGenerator()
        result = generator.czas_trwania_raportu(lines)
        self.assertEqual(result, 0)

    def test_jeden_log(self):
        lines = [
            "2023-01-01 23:00 90C"
        ]
        generator = ReportGenerator()
        result = generator.czas_trwania_raportu(lines)
        self.assertEqual(result, 0)

    def test_dwa_logi(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C"
        ]
        generator = ReportGenerator()
        result = generator.czas_trwania_raportu(lines)
        self.assertEqual(result, 50)

    def test_wiele_logow(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C"
        ]
        generator = ReportGenerator()
        result = generator.czas_trwania_raportu(lines)
        self.assertEqual(result, 70)


if __name__ == "__main__":
    unittest.main()
