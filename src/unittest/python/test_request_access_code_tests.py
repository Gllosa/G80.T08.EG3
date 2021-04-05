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

    def test_request_access_code_dni_letra_incorrecta(self):
        datosPersona = ("41694463D", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "DNI no válido")

    def test_request_acccess_code_dni_solo_letras(self):
        datosPersona = ("FEUYYDWYV", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "DNI no válido")

    def test_rquest_access_code_dni_letra_minuscula(self):
        datosPersona = ("41694463v", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_guest(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_resident(self):
        datosPersona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 0)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_access_type_invalid(self):
        datosPersona = ("41694463V", "Jose Lopez", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Access type no válido")

    def test_request_access_code_name_ok(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_name_empty_string(self):
        datosPersona = ("41694463V", "", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Nombre no válido")

    def test_request_access_code_no_blank_space(self):
        datosPersona = ("41694463V", "JoseLopez", "Owner", "jllopez@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Nombre no válido")

    def test_request_access_code_email_ok(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 5)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_email_no_at(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopezinf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_domain(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@infuc3mes", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_text_between_at_and_domain(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_email_no_text_before_at(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "@inf.uc3m.es", 5)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Email no válido")

    def test_request_access_code_validity_ok_top_limit(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 15)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_ok_boottom_limit(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 2)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_ok_extra_limit(self):
        datosPersona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 0)
        req = AccessRequest(*datosPersona)
        codigo_esperado = req.access_code
        codigo = AccessManager().request_access_code(*datosPersona)
        self.assertEqual(codigo, codigo_esperado)

    def test_request_access_code_validity_number_out_of_range(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", 21)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_not_a_number(self):
        datosPersona = ("41694463V", "Jose Lopez", "Guest", "jllopez@inf.uc3m.es", "SIEMPRE")
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Número de días no válido")

    def test_request_access_code_validity_resident_days_not_0(self):
        datosPersona = ("41694463V", "Jose Lopez", "Resident", "jllopez@inf.uc3m.es", 13)
        with self.assertRaises(AccessManagementException) as res:
            AccessManager().request_access_code(*datosPersona)
        self.assertEqual(res.exception.message, "Número de días no válido")


if __name__ == '__main__':
    unittest.main()
