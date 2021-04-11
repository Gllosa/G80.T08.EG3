"""Module """
import json
import pathlib
import os

from secure_all import AccessRequest, AccessManagementException
from datetime import datetime
import secure_all.access_key

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
            try:
                if int(char) not in numbers:
                    return False
            except ValueError:
                return False
        letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                   "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        index = int(str_number_dni) % 23
        return letters[index] == dni[-1].upper()

    @staticmethod
    def check_name(name):
        """Comprobar el formato correcto del nombre"""
        if len(name) > 0:
            for letra in name:
                if letra == " ":
                    return True
        raise AccessManagementException("Nombre no válido")

    @staticmethod
    def check_access_type(access_type):
        """Comprobar el formato correcto del tipo de acceso"""
        if access_type in ("Guest", "Resident"):
            return True
        raise AccessManagementException("Access type no válido")

    @staticmethod
    def check_email(email):
        """Comprobar el formato correcto del email"""
        try:
            nombre, dominio = email.split("@")
        except ValueError:
            raise AccessManagementException("Email no válido") from None
        if len(dominio) > 0 and len(nombre) > 0:
            if "." in dominio:
                try:
                    texto = dominio.split(".")
                except ValueError:
                    raise AccessManagementException("Email no válido") from None
                nada = False
                for i in texto:
                    if len(i) == 0:
                        nada = True
                if not nada:
                    return True
        raise AccessManagementException("Email no válido")

    @staticmethod
    def check_validity(val, acc_type):
        """Comprobar el formato correcto del numero de días de validez"""
        if not isinstance(val, int):
            raise AccessManagementException("Número de días no válido")
        if (acc_type == "Guest" and 15 >= val >= 2) or (acc_type == "Resident" and val == 0):
            return True
        raise AccessManagementException("Número de días no válido")

    def request_access_code(self, datos_persona):
        """Método para obtener un código de acceso"""
        self.check_name(datos_persona[1])
        self.check_access_type(datos_persona[2])
        self.check_email(datos_persona[3])
        self.check_validity(datos_persona[4], datos_persona[2])
        if not self.validate_dni(datos_persona[0]):
            raise AccessManagementException("DNI no válido")
        req = AccessRequest(datos_persona)
        if not self.request_in_json(req):
            self.save_request(req)
            return req.access_code
        raise AccessManagementException("Solicitud ya realizada")

    @staticmethod
    def save_request(solicitud):
        """Guardar una solicitud en el almacen"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("almacen/solicitudes.json")
        with open(path, "a+") as solicitudes:
            cadena = json.dumps(solicitud.__dict__)
            solicitudes.write(cadena)
            solicitudes.write("\n")

    @staticmethod
    def request_in_json(solicitud):
        """Comprobar si una peticion ya esta en el almacen"""
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("almacen/solicitudes.json")
        with open(path) as solicitudes:
            for sol in solicitudes:
                datos = json.loads(sol)
                return datos == solicitud.__dict__

    def check_json_request(self, input_file):
        """Comprueba que no haya errores en la solicitud json"""
        try:
            with open(input_file) as solicitud:
                datos = json.load(solicitud)
                llaves = []

                for key in datos:
                    llaves.append(key)
                if len(llaves) > 3:
                    raise AccessManagementException("ERROR, demasiados parametros")
                if len(llaves) < 3:
                    raise AccessManagementException("ERROR, menos de tres parametros")
                if llaves[0] != "AccessCode":
                    raise AccessManagementException("ERROR, typo en clave \"AccesCode\"")
                if llaves[1] != "DNI":
                    raise AccessManagementException("ERROR, typo en clave \"DNI\"")
                if llaves[2] != "NotificationMail":
                    raise AccessManagementException("ERROR, typo en clave \"NotificationMail\"")
                if not self.validate_dni(datos["DNI"]):
                    raise AccessManagementException("ERROR, typo en DNI")
                emails = datos["NotificationMail"]
                if not isinstance(emails, list):
                    raise AccessManagementException("ERROR DE SINTAXIS EN ARCHIVO")
                if len(emails) > 5:
                    raise AccessManagementException("ERROR, demasiados emails")
                if len(emails) == 0:
                    raise AccessManagementException("ERROR, cero emails")
                for email in emails:
                    self.check_email(email)
        except ValueError:
            raise AccessManagementException("ERROR DE SINTAXIS EN ARCHIVO")


    def get_solicitud_from_acces_code(self, input_file):
        """return los datos en la base de datos de solicitudes
         correspondientes a la clave de acceso
         si existen y si el codigo de acceso es correcto"""
        self.check_json_request(input_file)
        with open(input_file) as solicitud:
            datos = json.load(solicitud)
            path = pathlib.Path(__file__).parent.parent.parent.parent
            path = path.joinpath("almacen/solicitudes.json")
            with open(path) as solicitudes:
                for sol in solicitudes:
                    datos_en_base = json.loads(sol)
                    my_request = AccessRequest(datos_en_base)
                    if datos["NotificationMail"] == datos_en_base["_AccessRequest__email_address"]:
                        if datos["DNI"] == datos_en_base["_AccessRequest__id_document"]:
                            if datos["AccesCode"] == my_request.access_code:
                                return datos_en_base
                            raise AccessManagementException("ERROR, AccesCode incorrecto")
                    raise AccessManagementException("ERROR, la solicitud no esta en la base de datos")

    def get_access_key(self, input_file):
        """segun la peticion de acceso devuelve
        una clave hash 256 y guarda en claves los parametros de la clave"""
        datos_en_base = self.get_solicitud_from_acces_code(input_file)
        with open(input_file) as solicitud:
            datos = json.load(solicitud)
            my_key = AccessKey(datos["DNI"], datos["AccesCode"], datos["NotificationMail"],
                              datos_en_base["_AccessRequest__validity"])
            path = pathlib.Path(__file__).parent.parent.parent.parent
            path = path.joinpath("almacen/claves.json")
            with open(path, "a+") as claves:
                cadena = json.dumps(claves.__dict__)
                claves.write(cadena)
                claves.write("\n")
            return my_key.key







    def open_door(self, key):
        path = pathlib.Path(__file__).parent.parent.parent.parent
        path = path.joinpath("jsons_e2")
        archivos = [path.joinpath(file) for file in os.listdir(path)]
        for archivo in archivos:
            try:
                llave = self.get_access_key(archivo)
                if llave == key:
                    # Registrar la marca de tiempo y la clave
                    path = pathlib.Path(__file__).parent.parent.parent.parent
                    path = path.joinpath("almacen/llavesValidas.json")
                    time_stamp = datetime.timestamp(datetime.utcnow())
                    data = {"key": key, "time_stamp": time_stamp}
                    json.dump(data, path)
                    return True
            except AccessManagementException:
                continue
        return False
