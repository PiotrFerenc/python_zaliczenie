import unittest

from ReportGenerator import ReportGenerator


class TestProblemy(unittest.TestCase):

    def test_brak_problemy(self):
        procent_wadliwych_logow = 5.0
        max_temp = 90.0
        czas_przegrzania = 5
        generator = ReportGenerator()
        result = generator.problemy(procent_wadliwych_logow, max_temp, czas_przegrzania)
        self.assertEqual(result, {"wysoki_poziom_zaklocen_EM": False,
                                  "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False})

    def test_wysoki_poziom_zaklocen(self):
        procent_wadliwych_logow = 15.0
        max_temp = 90.0
        czas_przegrzania = 5
        generator = ReportGenerator()
        result = generator.problemy(procent_wadliwych_logow, max_temp, czas_przegrzania)
        self.assertEqual(result, {"wysoki_poziom_zaklocen_EM": True,
                                  "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False})

    def test_wysokie_ryzyko_uszkodzenia_silnika(self):
        procent_wadliwych_logow = 5.0
        max_temp = 110.0
        czas_przegrzania = 15
        generator = ReportGenerator()
        result = generator.problemy(procent_wadliwych_logow, max_temp, czas_przegrzania)
        self.assertEqual(result, {"wysoki_poziom_zaklocen_EM": False,
                                  "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": True})

    def test_wszystkie_problemy(self):
        procent_wadliwych_logow = 20.0
        max_temp = 120.0
        czas_przegrzania = 30
        generator = ReportGenerator()
        result = generator.problemy(procent_wadliwych_logow, max_temp, czas_przegrzania)
        self.assertEqual(result, {"wysoki_poziom_zaklocen_EM": True,
                                  "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": True})


if __name__ == "__main__":
    unittest.main()
