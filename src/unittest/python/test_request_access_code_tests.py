import unittest
from secure_all import AccessManager, AccessRequest, AccessManagementException


class MyTestCase(unittest.TestCase):
    def test_request_access_code_dni_valido(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_dni_solo_numeros(self):
        datosPersona = ("41694463", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "DNI no válido")


if __name__ == '__main__':
    unittest.main()
