"""Tests para probar el metodo get_acces_key"""
import unittest
import pathlib
from secure_all import AccessManager, AccessManagementException


class MyTestCase(unittest.TestCase):
    """ Clase para probar get_acces_key"""
    def test_sintaxis_6_emails(self):
        """6 correos em el JSON"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n1.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR, demasiados emails")

    def test_sintaxis_all_repeated(self):
        """Nodo 1 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n2.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_json_vacio(self):
        """Nodo 1 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n3.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_doble_llave_inicial(self):
        """Nodo 2 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n4.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_llave_inicial(self):
        """Nodo 2 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n5.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_all_datos_repetidos(self):
        """Nodo 3 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n6.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_datos(self):
        """Nodo 3 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n7.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR, menos de tres parametros")

    def test_sintaxis_llave_final_duplicada(self):
        """Nodo 4 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n8.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_llave_final(self):
        """Nodo 4 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n9.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_llave_inicial_typo(self):
        """Nodo 5 modificiado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n10.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_llave_final_typo(self):
        """Nodo 12 modificiado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n11.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato1_repetido(self):
        """Nodo 6 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n12.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_dato1(self):
        """Nodo 6 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n13.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_doble_coma(self):
        """Nodo 7 suplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n14.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_coma(self):
        """Nodo 7 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n15.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_dato2(self):
        """Nodo 8 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n16.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato2_duplicado(self):
        """Nodo 8 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n17.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_dato3_duplicado(self):
        """Nodo 11 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n18.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_no_dato3(self):
        """Nodo 11 eliminado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n19.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")

    def test_sintaxis_nombre_dato1_dup(self):
        """Nodo 13 duplicado"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("src/jsons_e2/sintaxis_n20.json")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().get_access_key(path)
        self.assertEqual(res.exception.message, "ERROR DE SINTAXIS EN ARCHIVO")


if __name__ == '__main__':
    unittest.main()
