import unittest

from ReportGenerator import ReportGenerator


class TestGenerujRaport(unittest.TestCase):
    def test_generuj_raport(self):
        mocked_lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-01-02 00:10 95C"
        ]

        expected_output = {
            "wadliwe_logi": [],
            "procent_wadliwych_logow": "0.0",
            "czas_trwania_raportu": 70,
            "temperatura": {
                "max": "100.0",
                "min": "90.0",
                "srednia": "95.0"
            },
            "najdluzszy_czas_przegrzania": 0,
            "liczba_okresow_przegrzania": 0,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": False,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
            }
        }

        generator = ReportGenerator()
        result = generator.generuj_raport(mocked_lines)
        self.assertEqual(result, expected_output)

    def test_generuj_raport_z_wadliwymi_logami(self):
        mocked_lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 100C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10 95C",
            "2023-01-02 00:10"
        ]

        expected_output = {
            "wadliwe_logi": [
                "2023-x1-01 23:5x 10xC",
                "2023-01-02 00:10"
            ],
            "procent_wadliwych_logow": "40.0",
            "czas_trwania_raportu": 70,
            "temperatura": {
                "max": "100.0",
                "min": "90.0",
                "srednia": "95.0"
            },
            "najdluzszy_czas_przegrzania": 0,
            "liczba_okresow_przegrzania": 0,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": True,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
            }
        }

        generator = ReportGenerator()
        result = generator.generuj_raport(mocked_lines)
        self.assertEqual(result, expected_output)

    def test_generuj_raport_z_wadliwymi_logami(self):
        mocked_lines = [
            "2023-01-01 23:00 90C",
            "2023-01-01 23:50 110C",
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:10 95C",
            "2023-01-02 00:15 -78C",
            "2023-01-02 00:20 100.3C",
            "2023-01-02 00:40 115.3C",
            "2023-01-02 00:50 100.1C",
            "2023-01-02 01:00 106C",
            "2023-01-02 01:10"
        ]

        expected_output = {
            "wadliwe_logi": [
                "2023-x1-01 23:5x 10xC",
                "2023-01-02 00:15 -78C",
                "2023-01-02 01:10"
            ],
            "procent_wadliwych_logow": "30.0",
            "czas_trwania_raportu": 120,
            "temperatura": {
                "max": "115.3",
                "min": "90.0",
                "srednia": "102.4"
            },
            "najdluzszy_czas_przegrzania": 40,
            "liczba_okresow_przegrzania": 2,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": True,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": True
            }
        }

        generator = ReportGenerator()
        result = generator.generuj_raport(mocked_lines)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
