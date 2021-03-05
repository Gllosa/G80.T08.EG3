"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime

class AccessRequest:
    """Class representing the access request"""
    def __init__( self, id_document, full_name, access_type, email_address, validity ):
        self.__id_document = id_document
        self.__full_name = full_name
        self.__visitor_type = access_type
        self.__email_address = email_address
        self.__validity = validity
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def full_name( self ):
        """Property representing the name and the surname of
        the person who request access to the building"""
        return self.__full_name
    @full_name.setter
    def full_name( self, value ):
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
    def id_document( self ):
        """Property representing the requester's DNI"""
        return self.__id_document
    @id_document.setter
    def id_document( self, value ):
        self.__id_document = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def access_code(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()
