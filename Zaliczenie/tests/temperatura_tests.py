import unittest

from ReportGenerator import ReportGenerator


class TestTemperatura(unittest.TestCase):

    def test_brak_logow(self):
        lines = []
        generator = ReportGenerator()
        result = generator.temperatura(lines)
        self.assertEqual(result, {"max": None, "min": None, "srednia": None})

    def test_jeden_log(self):
        lines = [
            "2023-01-01 23:00 90C"
        ]
        generator = ReportGenerator()
        result = generator.temperatura(lines)
        self.assertEqual(result, {"max": "90.0", "min": "90.0", "srednia": "90.0"})

    def test_wiele_logow(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C"
        ]
        generator = ReportGenerator()
        result = generator.temperatura(lines)
        self.assertEqual(result, {"max": "100.0", "min": "90.0", "srednia": "95.0"})

    def test_mieszane_logi(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10"
        ]
        generator = ReportGenerator()
        result = generator.temperatura(lines)
        self.assertEqual(result, {"max": "100.0", "min": "90.0", "srednia": "95.0"})


if __name__ == "__main__":
    unittest.main()
