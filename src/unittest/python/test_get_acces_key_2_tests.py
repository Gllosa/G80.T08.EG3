"""Tests para probar el metodo get_acces_key"""
import unittest
import pathlib
from secure_all import AccessManager, AccessManagementException


class MyTestCase(unittest.TestCase):
    """Clase para probar get_acces_key"""

    def test_sintaxis_no_nombre_dato1(self):
        """Nodo 13 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n21.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato1_igual_dup(self):
        """Nodo 14 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n22.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_igual_dato1(self):
        """Nodo 14 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n23.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato1_atb_dup(self):
        """Nodo 15 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n24.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato1_atb_elim(self):
        """Nodo 15 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n25.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_coma_typo(self):
        """Nodo 16 modificiado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n26.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato2_nombre_elim(self):
        """Nodo 17 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n27.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato2_nombre_dup(self):
        """Nodo 17 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n28.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato2_valor_elim(self):
        """Nodo 19 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n29.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato2_valor_dup(self):
        """Nodo 19 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n30.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato3_nombre_elim(self):
        """Nodo 21 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n31.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato3_nombre_dup(self):
        """Nodo 21 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n32.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato3_valor_elim(self):
        """Nodo 23 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n33.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato3_valor_dup(self):
        """Nodo 23 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n34.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_comilla_elim(self):
        """Nodo 24 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n35.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_comilla_dup(self):
        """Nodo 24 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n36.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_str_nombre1_elim(self):
        """Nodo 25 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n37.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR, typo en clave \"AccesCode\"")

    def test_sintaxis_str_nombre1_dup(self):
        """Nodo 25 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n38.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR, typo en clave \"AccesCode\"")

    def test_sintaxis_str_valor1_elim(self):
        """Nodo 29 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n39.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR --")

    def test_sintaxis_str_valor1_dup(self):
        """Nodo 29 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n40.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR --")


if __name__ == '__main__':
    unittest.main()
