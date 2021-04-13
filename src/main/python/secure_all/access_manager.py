"""Module """

import json
import pathlib
import os
import secure_all

from secure_all import AccessRequest, AccessManagementException
from datetime import datetime


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
        try:
            with open(path) as solicitudes:
                for sol in solicitudes:
                    datos = json.loads(sol)
                    return datos == solicitud.__dict__
        except FileNotFoundError:
            return False

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
                    raise AccessManagementException("ERROR, typo en clave \"AccessCode\"")
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
        try:
            with open(input_file) as solicitud:
                datos = json.load(solicitud)
                path = pathlib.Path(__file__).parent.parent.parent.parent
                path = path.joinpath("almacen/solicitudes.json")
                with open(path) as solicitudes:
                    for sol in solicitudes:
                        datos_en_base = json.loads(sol)
                        lista = []
                        for index in datos_en_base:
                            lista.append(datos_en_base[index])
                        my_request = AccessRequest(lista)
                        if isinstance(datos_en_base["_AccessRequest__email_address"], list):
                            if len(datos["NotificationMail"]) == len(datos_en_base["_AccessRequest__email_address"]):
                                if datos["NotificationMail"] == datos_en_base["_AccessRequest__email_address"]:
                                    if datos["DNI"] == datos_en_base["_AccessRequest__id_document"]:
                                        if datos["AccessCode"] == my_request.access_code:
                                            return datos_en_base
                                        raise AccessManagementException("ERROR, AccesCode incorrecto")
                        elif datos["NotificationMail"][0] == datos_en_base["_AccessRequest__email_address"]:
                            if len(datos["NotificationMail"]) == 1:
                                if datos["DNI"] == datos_en_base["_AccessRequest__id_document"]:
                                    if datos["AccessCode"] == my_request.access_code:
                                        return datos_en_base
                                    raise AccessManagementException("ERROR, AccesCode incorrecto")
        except FileNotFoundError:
            raise AccessManagementException("ERROR, la solicitud no esta en la base de datos")
        raise AccessManagementException("ERROR, la solicitud no esta en la base de datos")

    def get_access_key(self, input_file):
        """segun la peticion de acceso devuelve
        una clave hash 256 y guarda en claves los parametros de la clave"""
        datos_en_base = self.get_solicitud_from_acces_code(input_file)
        with open(input_file) as solicitud:
            datos = json.load(solicitud)
            my_key = secure_all.AccessKey(datos["DNI"], datos["AccessCode"], datos["NotificationMail"],
                                          datos_en_base["_AccessRequest__validity"])
            path = pathlib.Path(__file__).parent.parent.parent.parent
            path = path.joinpath("almacen/claves.json")
            with open(path, "a+") as claves:
                diccionario_llave = my_key.__dict__
                diccionario_llave["_AccessKey__key"] = my_key.key
                cadena = json.dumps(diccionario_llave)
                claves.write(cadena)
                claves.write("\n")
            return my_key.key

    @staticmethod
    def open_door(key):
        if not isinstance(key, str) or len(key) != 64:
            raise AccessManagementException("Clave no encontrada o expirada")

        path_origen = pathlib.Path(__file__).parent.parent.parent.parent
        path_claves = path_origen.joinpath("almacen/claves.json")

        with open(path_claves) as claves:
            for clave in claves:
                diccionario_clave = json.loads(clave)
                time_stamp = datetime.timestamp(datetime.utcnow())
                if diccionario_clave["_AccessKey__key"] == key \
                        and (diccionario_clave["_AccessKey__expiration_date"] > time_stamp
                             or diccionario_clave["_AccessKey__expiration_date"] == 0):
                    # Registrar la marca de tiempo y la clave
                    data = {"key": key, "time_stamp": time_stamp}
                    with open(path_origen.joinpath("almacen/llavesValidas.json"), "a+") as llaves_validas:
                        cadena = json.dumps(data)
                        llaves_validas.write(cadena)
                        llaves_validas.write("\n")
                    return True

            raise AccessManagementException("Clave no encontrada o expirada")
