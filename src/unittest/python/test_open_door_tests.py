import unittest

from secure_all import AccessManager, AccessManagementException


class MyTestCase(unittest.TestCase):

    def test_open_door_good(self):
        acs = AccessManager()
        self.assertEqual(True, acs.open_door("26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa97"))

    def test_open_door_good_exp_0(self):
        acs = AccessManager()
        self.assertEqual(True, acs.open_door("26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa98"))

    def test_open_door_wrong_exp(self):
        acs = AccessManager()
        with self.assertRaises(AccessManagementException) as res:
            acs.open_door("26a5d2932358a872889c0df79a6a3f4983be03698b3a3601821721dc7cbfaa99")
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_wrong_lenth(self):
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().open_door("5445sfes64516rd5461")
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_not_string(self):
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().open_door(218)
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")

    def test_open_door_not_in_store(self):
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().open_door("jbk234123vbhj312vh312hvj132vhj13jbk234123vbhj312vh312hvj132vhj13")
        self.assertEqual(res.exception.message, "Clave no encontrada o expirada")
