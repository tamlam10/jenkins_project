import io
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Tamer Lammam!")

    def test_greet_another_name(self):
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins from Tamer Lammam!")

    def test_script_output(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            runpy.run_path(str(Path(__file__).resolve().parents[1] / "app.py"),
                           run_name="__main__")
        self.assertEqual(output.getvalue(),
                         "Hello, World from Tamer Lammam!\n")


if __name__ == "__main__":
    unittest.main()
