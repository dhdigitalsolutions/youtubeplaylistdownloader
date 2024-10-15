import os
import unittest

class TestDownloadScript(unittest.TestCase):
    def test_downloads_directory(self):
        expected_dir = os.path.join(os.path.expanduser("."), "downloads")
        self.assertTrue(os.path.isdir(expected_dir), "O diretório de downloads não foi configurado corretamente.")

if __name__ == '__main__':
    unittest.main()
