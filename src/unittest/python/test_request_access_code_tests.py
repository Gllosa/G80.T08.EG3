"""Test para probar request_access_code"""
import unittest
from secure_all import AccessManager, AccessRequest, AccessManagementException


class MyTestCase(unittest.TestCase):
    """ Clase para probar request_access_code"""

    def test_request_access_code_dni_valido(self):
        """DNI correcto"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 7)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_dni_solo_numeros(self):
        """DNI sin letra"""
        datos_persona = ("41694463", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "DNI no válido")

    def test_request_access_code_dni_letra_incorrecta(self):
        """DNI con una letra que no sigue el algortimo"""
        datos_persona = ("41694463D", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "DNI no válido")

    def test_request_acccess_code_dni_solo_letras(self):
        """DNI con solo letras"""
        datos_persona = ("FEUYYDWYV", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "DNI no válido")

    def test_rquest_access_code_dni_letra_minuscula(self):
        """DNI sigue siendo válido aunque la letra sea minuscula"""
        datos_persona = ("41694463v", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_guest(self):
        """AccessType es Guest"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 6)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_resident(self):
        """AccessType es Resident"""
        datos_persona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 0)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_invalid(self):
        """AccessType distitno de Guest o Resident"""
        datos_persona = ("41694463V", "Jose Lopez", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Access type no válido")

    def test_request_access_code_name_ok(self):
        """Nombre formato correcto"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 10)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_name_empty_string(self):
        """Nombre con un string vacio"""
        datos_persona = ("41694463V", "", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Nombre no válido")

    def test_request_access_code_name_no_blank_space(self):
        """Nombre sin un espacio, es decir, no hay apellido"""
        datos_persona = ("41694463V", "JoseLopez", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Nombre no válido")

    def test_request_access_code_email_ok(self):
        """Email correcto"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 8)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_email_no_at(self):
        """Email sin la @"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopezinf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_domain(self):
        """Email sin el dominio (.es, .com, etc)"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@infuc3mes", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_text_between_at_and_domain(self):
        """Sin texto entre la @ y el dominio"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_text_before_at(self):
        """Sin texto antes de la @"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(datos_persona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_validity_ok_top_limit(self):
        """Limite superior validity"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 15)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_ok_bottom_limit(self):
        """Limite inferior del validity"""
        datos_persona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 2)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_ok_extra_limit(self):
        """Límite extra del validity cuando el AccessType es Resident"""
        datos_persona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 0)
        req = AccessRequest(datos_persona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(datos_persona)
        self.assertEqual(codigo, codigo_esperado)


if __name__ == '__main__':
    unittest.main()
