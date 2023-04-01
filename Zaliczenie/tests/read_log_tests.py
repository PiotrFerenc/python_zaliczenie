import unittest
from unittest.mock import mock_open, patch

from ReportGenerator import ReportGenerator


class TestRaportGenerator(unittest.TestCase):
    def test_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            ReportGenerator().read_log("non_existing_file.txt")

    def test_invalid_path(self):
        with patch("os.path.exists", return_value=True):
            with patch("os.path.isfile", return_value=False):
                with self.assertRaises(ValueError):
                    ReportGenerator().read_log("invalid_path")

    def test_read_log(self):
        self.log_data = (
            "2023-01-01 23:00 90C"
            "2023-01-01 23:50 100C"
            "2023-x1-01 23:5x 10xC"
            "2023-01-02 00:10"
        )
        with patch("builtins.open", mock_open(read_data=self.log_data)):
            with patch("os.path.exists", return_value=True):
                with patch("os.path.isfile", return_value=True):
                    generator = ReportGenerator()
                    self.assertEqual(generator.read_log("mocked_file.txt"), self.log_data.splitlines(True))


if __name__ == "__main__":
    unittest.main()
