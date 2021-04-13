"""Test para probar request_access_code"""
import unittest
from secure_all import AccessManager, AccessRequest, AccessManagementException


class MyTestCase(unittest.TestCase):
    """ Clase para probar request_access_code"""

    def test_request_access_code_validity_not_a_number(self):
        """Validity no es un número"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", "SIEMPRE")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_resident_days_not_0(self):
        """El AccessType es Resient y la validity no es 0"""
        datos_persona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 13)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_below_bottom_limit(self):
        """Límite por debajo del inferior"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 1)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_above_bottom_limit(self):
        """Límite por encima del inferior"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 3)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_above_top_limit(self):
        """Limite por encima del superior"""
        datos_persona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 16)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_below_top_limit(self):
        """Límite por debajo del superior"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 14)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)
