"""Tests para probar el metodo get_acces_key"""
import unittest
import pathlib
from secure_all import AccessManager, AccessManagementException



class MyTestCase(unittest.TestCase):
    """Clase para probar get_acces_key"""

    def test_sintaxis_str_nombre2_elim(self):
        """Nodo 32 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n41.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre2_dup(self):
        """Nodo 32 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n42.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_valor2_elim(self):
        """Nodo 36 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n43.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_valor2_sup(self):
        """Nodo 36 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n44.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre3_elim(self):
        """Nodo 39 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n45.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre3_dup(self):
        """Nodo 39 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n46.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_abierto_elim(self):
        """Nodo 42 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n47.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_abierto_dup(self):
        """Nodo 42 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n48.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_emails_elim(self):
        """Nodo 43 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n49.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_emails_coma_elim(self):
        """Nodo 43 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n50.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_cerrado_elim(self):
        """Nodo 44 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n51.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_corchete_cerrado_dup(self):
        """Nodo 44 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n52.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_email_elim(self):
        """Nodo 64 elimimado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n53.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_email_dup(self):
        """Nodo 62 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n54.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_comilla_typo(self):
        """Nodo 45 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n55.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre1_typo(self):
        """Nodo 46 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n56.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_valor1_typo(self):
        """Nodo 49 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n57.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre2_typo(self):
        """Nodo 52 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n58.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_valor2_typo(self):
        """Nodo 55 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n59.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre3_typo(self):
        """Nodo 58 modificado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2/sintaxis_n60.json")
        with open(path) as solicitud:
            with self.assertRaises(AccessManagementException) as res:
                AccessManager().get_access_key(solicitud)
            self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")


if __name__ == '__main__':
    unittest.main()
