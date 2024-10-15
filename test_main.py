import os
import unittest

class TestDownloadScript(unittest.TestCase):
    def test_downloads_directory(self):
        # Define o diretório esperado
        expected_dir = os.path.join(os.path.expanduser("."), "downloads")
        
        # Cria o diretório, se não existir
        if not os.path.exists(expected_dir):
            os.makedirs(expected_dir)
        
        # Verifica se o diretório foi criado com sucesso
        self.assertTrue(os.path.isdir(expected_dir), "O diretório de downloads não foi configurado corretamente.")

if __name__ == '__main__':
    unittest.main()
