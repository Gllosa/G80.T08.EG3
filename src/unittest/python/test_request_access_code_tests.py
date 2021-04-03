import unittest
from secure_all import AccessManager, AccessRequest


class MyTestCase(unittest.TestCase):
    def test_request_access_code_dni_valido(self):
        req = AccessRequest("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        self.assertEqual(codigo, codigo_esperado)


if __name__ == '__main__':
    unittest.main()
