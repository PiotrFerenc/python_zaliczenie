import unittest

from ReportGenerator import ReportGenerator


class TestProcentWadliwychLogow(unittest.TestCase):

    def test_brak_logow(self):
        lines = []
        wadliwe_logi = []
        generator = ReportGenerator()
        result = generator.procent_wadliwych_logow(lines, wadliwe_logi)
        self.assertEqual(result, "100.0")

    def test_brak_wadliwych_logow(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C"
        ]
        wadliwe_logi = []
        generator = ReportGenerator()
        result = generator.procent_wadliwych_logow(lines, wadliwe_logi)
        self.assertEqual(result, "0.0")

    def test_tylko_wadliwe_logi(self):
        lines = [
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10"
        ]
        wadliwe_logi = lines
        generator = ReportGenerator()
        result = generator.procent_wadliwych_logow(lines, wadliwe_logi)
        self.assertEqual(result, "100.0")

    def test_mieszane_logi(self):
        lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10"
        ]
        wadliwe_logi = [
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10"
        ]
        generator = ReportGenerator()
        result = generator.procent_wadliwych_logow(lines, wadliwe_logi)
        self.assertEqual(result, "40.0")


if __name__ == "__main__":
    unittest.main()
