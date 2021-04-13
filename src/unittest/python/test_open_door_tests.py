"""Tests para el método open door"""
import unittest

from secure_all import AccessManager, AccessManagementException


class MyTestCase(unittest.TestCase):
    """Clase de Tests para el método open door"""

    def test_open_door_good(self):
        """Test cuando se recibe un codigo existente y válido"""
        acs = AccessManager()
        codigo = "26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa97"
        self.assertEqual(True, acs.open_door(codigo))

    def test_open_door_good_exp_0(self):
        """Test cuando se recibe un codigo existente con la expiracion = 0"""
        acs = AccessManager()
        codigo = "26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa98"
        self.assertEqual(True, acs.open_door(codigo))

    def test_open_door_wrong_exp(self):
        """Test cuando se recibe un codigo existente pero con expiración incorrecta"""
        acs = AccessManager()
        with self.assertRaises(AccessManagementException) as res:
            acs.open_door("26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa99")
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_wrong_lenth(self):
        """Test cuando se recibe un codigo de longitud incorrecta"""
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().open_door("5445sfes64516rd5461")
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_not_string(self):
        """Test para cuando se recibe un codigo que no es un string"""
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().open_door(218)
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_not_in_store(self):
        """Test cuando se recibe un codigo no existente"""
        with self.assertRaises(AccessManagementException) as res:
            codigo = "jbk234123vbhj312vh312hvj132vhj13jbk234123vbhj312vh312hvj132vhj13"
            AccessManager().open_door(codigo)
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")
