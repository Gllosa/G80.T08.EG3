"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime


class AccessRequest:
    """Class representing the access request"""

    def __init__(self, datosPersona):
        self.__id_document = datosPersona[0]
        self.__full_name = datosPersona[1]
        self.__visitor_type = datosPersona[2]
        self.__email_address = datosPersona[3]
        self.__validity = datosPersona[4]
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)
        # self.__time_stamp = 0

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def full_name(self):
        """Property representing the name and the surname of
        the person who request access to the building"""
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def visitor_type(self):
        """Property representing the type of visitor: Resident or Guest"""
        return self.__visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self.__visitor_type = value

    @property
    def email_address(self):
        """Property representing the requester's email address"""
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def id_document(self):
        """Property representing the requester's DNI"""
        return self.__id_document

    @id_document.setter
    def id_document(self, value):
        """Setter de id_document para el AccessRequest"""
        self.__id_document = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def access_code(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()
