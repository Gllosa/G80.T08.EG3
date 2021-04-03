"""Module """
from secure_all import AccessRequest, AccessManagementException


class AccessManager:
    """Class for providing the methods for managing the access to a building"""

    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""
        str_number_dni = dni[0:-1]
        # Comprobar que el dni tiene 8 numeros seguidos de una letra
        if len(str_number_dni) != 8:
            return False
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in str_number_dni:
            if int(char) not in numbers:
                return False
        letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                   "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        index = int(str_number_dni) % 23
        return letters[index] == dni[-1].upper()

    @staticmethod
    def check_name(name):
        if len(name) > 0:
            for letra in name:
                if letra == " ":
                    return True
        raise AccessManagementException("Nombre no válido")

    @staticmethod
    def check_access_type(access_type):
        if access_type == "Guest" or access_type == "Resident":
            return True
        raise AccessManagementException("Access type no válido")

    @staticmethod
    def check_email(email):
        try:
            nombre, dominio = email.split("@")
        except ValueError:
            raise AccessManagementException("Email no válido")
        if len(dominio) > 0 and len(nombre) > 0:
            if "." in dominio:
                return True
        raise AccessManagementException("Email no válido")

    @staticmethod
    def check_validity(val, acc_type):
        if (acc_type == "Guest" and 15 >= val >= 2) or (acc_type == "Resident" and val == 0):
            return True
        raise AccessManagementException("Número de días no válido")

    def request_access_code(self, id_document, full_name, access_type, email_address, validity):
        self.check_name(full_name)
        self.check_access_type(access_type)
        self.check_email(email_address)
        self.check_validity(validity, access_type)
        if self.validate_dni(id_document):
            req = AccessRequest(id_document, full_name, access_type, email_address, validity)
            return req.access_code
        raise AccessManagementException("DNI no válido")
