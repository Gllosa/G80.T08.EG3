"""Contains the class Access Key"""
from datetime import datetime
import hashlib

class AccessKey():
    """Class representing the key for accessing the building"""

    def __init__(self, dni, access_code, notification_emails, validity):
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__id_document = dni
        self.__access_code = access_code
        self.__notification_emails = notification_emails
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if validity == 0:
            self.__expiration_date = 0
        else:
            #timestamp is represneted in seconds.microseconds
            #validity must be expressed in senconds to be added to the timestap
            self.__expiration_date = self.__issued_at + (validity * 24 * 60 *60)

    def __signature_string(self):
        """Composes the string to be used for generating the key"""
        return "{alg:"+self.__alg+",typ:"+self.__type+",accesscode:"+self.__access_code+",issuedate:"+self.__issued_at+",expirationdate:"+self.__expiration_date+"}"

    @property
    def id_document( self ):
        """Property that represents the dni of the visitor"""
        return self.__id_document

    @id_document.setter
    def id_document( self, value ):
        self.__id_document = value

    @property
    def access_code(self):
        """Property that represents the access_code of the visitor"""
        return self.__access_code
    @access_code.setter
    def access_code(self, value):
        self.__access_code = value

    @property
    def notification_emails(self):
        """Property that represents the access_code of the visitor"""
        return self.__notification_emails

    @notification_emails.setter
    def notification_emails(self, value ):
        self.__notification_emails = value

    @property
    def key(self):
        """Returns the sha256 signature"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at( self, value ):
        self.__issued_at = value
