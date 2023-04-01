import os
import re
from datetime import datetime, timedelta


class ReportGenerator:

    def generuj_raport(self, lines):
        prawidlowe_logi, wadliwe_logi = self.wadliwe_logi(lines)
        procent_wadliwych_logow = self.procent_wadliwych_logow(lines, wadliwe_logi)
        czas_trwania_raportu = self.czas_trwania_raportu(prawidlowe_logi)
        temperatura = self.temperatura(prawidlowe_logi)
        liczba_okresow_przegrzania = self.liczba_okresow_przegrzania(prawidlowe_logi)
        najdluzszy_czas_przegrzania = self.najdluzszy_czas_przegrzania(prawidlowe_logi)
        problemy = self.problemy(procent_wadliwych_logow, temperatura["max"], najdluzszy_czas_przegrzania)

        return {
            "wadliwe_logi": wadliwe_logi,
            "procent_wadliwych_logow": procent_wadliwych_logow,
            "czas_trwania_raportu": czas_trwania_raportu,
            "temperatura": {
                "max": temperatura["max"],
                "min": temperatura["min"],
                "srednia": temperatura["srednia"]
            },
            "najdluzszy_czas_przegrzania": najdluzszy_czas_przegrzania,
            "liczba_okresow_przegrzania": liczba_okresow_przegrzania,
            "problemy": problemy
        }

    def read_log(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Plik '{path}' nie istnieje.")
        if not os.path.isfile(path):
            raise ValueError(f"Ścieżka '{path}' nie prowadzi do prawidłowego pliku.")
        with open(path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]

        return lines

    def wadliwe_logi(self, logi):
        prawidlowe_logi = []
        wadliwe_logi = []

        for log in logi:
            if re.fullmatch(r'\d{4}-[01]\d-[0-3]\d [0-2]\d:[0-5]\d [1-9]\d*(\.\d+)?C', log):
                prawidlowe_logi.append(log)
            else:
                wadliwe_logi.append(log)

        return prawidlowe_logi, wadliwe_logi

    def procent_wadliwych_logow(self, lines, wadliwe_logi):
        total_lines = len(lines)
        invalid_lines = len(wadliwe_logi)
        if total_lines == 0:
            return "100.0"
        else:
            return f"{invalid_lines / total_lines * 100:.1f}"

    def czas_trwania_raportu(self, prawidlowe_logi):
        time_format = "%Y-%m-%d %H:%M"
        valid_timestamps = []

        for line in prawidlowe_logi:
            try:
                date_str = line[:16]
                timestamp = datetime.strptime(date_str, time_format)
                valid_timestamps.append(timestamp)
            except ValueError:
                continue

        if len(valid_timestamps) < 2:
            return 0

        min_timestamp = min(valid_timestamps)
        max_timestamp = max(valid_timestamps)
        duration = max_timestamp - min_timestamp

        return int(duration.total_seconds() / 60)

    def temperatura(self, prawidlowe_logi):
        temperatures = []
        for line in prawidlowe_logi:
            try:
                temp_str = line.split()[-1][:-1]
                temp = float(temp_str)
                temperatures.append(temp)
            except (ValueError, IndexError):
                continue

        if not temperatures:
            return {"max": None, "min": None, "srednia": None}

        max_temp = max(temperatures)
        min_temp = min(temperatures)
        srednia_temp = sum(temperatures) / len(temperatures)

        return {
            "max": f"{max_temp:.1f}",
            "min": f"{min_temp:.1f}",
            "srednia": f"{srednia_temp:.1f}",
        }

    def najdluzszy_czas_przegrzania(self, prawidlowe_logi):
        time_format = "%Y-%m-%d %H:%M"
        valid_entries = []
        for line in prawidlowe_logi:
            try:
                date_str, temp_str = line[:16], line.split()[-1][:-1]
                timestamp = datetime.strptime(date_str, time_format)
                temp = float(temp_str)
                valid_entries.append((timestamp, temp))
            except (ValueError, IndexError):
                continue

        max_overheat_duration = timedelta(minutes=0)
        current_overheat_start = None

        for i, (timestamp, temp) in enumerate(valid_entries):
            if temp > 100:
                if current_overheat_start is None:
                    current_overheat_start = timestamp
            else:
                if current_overheat_start is not None:
                    overheat_duration = timestamp - current_overheat_start
                    if overheat_duration > max_overheat_duration:
                        max_overheat_duration = overheat_duration
                    current_overheat_start = None

        if current_overheat_start is not None:
            overheat_duration = valid_entries[-1][0] - current_overheat_start
            if overheat_duration > max_overheat_duration:
                max_overheat_duration = overheat_duration

        return int(max_overheat_duration.total_seconds() / 60)

    def liczba_okresow_przegrzania(self, prawidlowe_logi):
        valid_entries = []
        overheat_periods = 0
        overheat_in_progress = False

        for line in prawidlowe_logi:
            try:
                temp_str = line.split()[-1][:-1]
                temp = float(temp_str)
                valid_entries.append(temp)
            except (ValueError, IndexError):
                continue

        for temp in valid_entries:
            if temp > 100:
                if not overheat_in_progress:
                    overheat_periods += 1
                    overheat_in_progress = True
            else:
                overheat_in_progress = False

        return overheat_periods

    def problemy(self, procent_wadliwych_logow, max_temp, czas_przegrzania):
        problemy_dict = {
            "wysoki_poziom_zaklocen_EM": False,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
        }
        if float(procent_wadliwych_logow) > 10:
            problemy_dict["wysoki_poziom_zaklocen_EM"] = True

        if float(max_temp) > 100 and float(czas_przegrzania) > 10:
            problemy_dict["wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury"] = True

        return problemy_dict
