"""Tests para probar el metodo get_acces_key"""
import unittest
import pathlib
from secure_all import AccessManager, AccessManagementException, AccessKey


class MyTestCase(unittest.TestCase):
    """Clase para probar get_acces_key"""

    def test_sintaxis_corchete_abierto_typo(self):
        """Nodo 60 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n61.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_cerrado_typo(self):
        """Nodo 65 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n62.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_email_typo(self):
        """Nodo 67 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n63.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_valido_1(self):
        """Todo correcto con un email,
            en access_request timestamp = 0
            y en acces_key issued_at = 0"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/valido_n1.json")
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        codigo_de_acceso = AccessManager().request_access_code(datos_persona)
        codigo_esperado = AccessKey("41694463V", codigo_de_acceso, "jllopez@inf.uc3m.es", 5).key
        codigo = AccessManager().get_access_key(path)
        self.assertEqual(codigo_esperado, codigo)

    def test_valido_2(self):
        """Todo correcto con cinco emails,
                en access_request timestamp = 0
                y en acces_key issued_at = 0"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/valido_n2.json")
        datos_persona = ("52058792V", "Jose Carrasco", "Guest", "jllopez@inf.uc3m.es", 5)
        codigo_de_acceso = AccessManager().request_access_code(datos_persona)
        print(codigo_de_acceso)
        codigo_esperado = AccessKey("52058792V", codigo_de_acceso, ["jllopez@inf.uc3m.es","jllopezz@inf.uc3m.es",
                         "jllopezzz@inf.uc3m.es","jllopezzzz@inf.uc3m.es","jllopezzzzz@inf.uc3m.es"], 5).key
        codigo = AccessManager().get_access_key(path)
        self.assertEqual(codigo_esperado, codigo)

if __name__ == '__main__':
    unittest.main()
