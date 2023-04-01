import unittest

from ReportGenerator import ReportGenerator


class TestWadliweLogi(unittest.TestCase):

    def test_prawidlowe_logi(self):
        logi = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C",
            "2023-01-02 00:10 95.5C",
            "2023-01-02 00:10 5C",
            "2023-01-02 00:10 5.5C"
        ]
        generator = ReportGenerator()

        prawidlowe, wadliwe = generator.wadliwe_logi(logi)
        self.assertEqual(len(prawidlowe), 6)

    def test_wadliwe_logi(self):
        logi = [
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10",
            "2023-01-02 00:10 -95,5C",
            '2023-01-02 00:15 -78C',
            "2023-01-02 00:10C",
            "2023-01-02 00:10 C",
        ]
        generator = ReportGenerator()

        prawidlowe, wadliwe = generator.wadliwe_logi(logi)

        self.assertEqual(len(wadliwe), 6)

    def test_mieszane_logi(self):
        logi = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10"
        ]

        generator = ReportGenerator()
        prawidlowe, wadliwe = generator.wadliwe_logi(logi)
        self.assertEqual(len(prawidlowe), 3)
        self.assertEqual(len(wadliwe), 2)


if __name__ == "__main__":
    unittest.main()
