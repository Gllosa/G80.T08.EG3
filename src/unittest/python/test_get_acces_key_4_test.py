"""Tests para probar el metodo get_acces_key"""
import unittest
import pathlib
from secure_all import AccessManager, AccessManagementException



class MyTestCase(unittest.TestCase):
    """Clase para probar get_acces_key"""

    def test_sintaxis_corchete_abierto_typo(self):
        """Nodo 60 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n61.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_cerrado_typo(self):
        """Nodo 65 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n62.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_email_typo(self):
        """Nodo 67 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n63.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")


if __name__ == '__main__':
    unittest.main()
