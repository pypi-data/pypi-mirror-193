from ...app import Kard
from ... import kard

class KardContact:
    def __init__(self, kard: Kard):
        self.app = kard

    def _new(self, contactId: str, **kwargs):
        contact = KardContact(self.app)
        contact._setId(contactId)

        contact._type = kwargs.get('type')
        contact._status = kwargs.get('status')
        contact._hasBankAccount = kwargs.get('hasBankAccount')
        contact._firstName = kwargs.get('firstName')
        contact._lastName = kwargs.get('lastName')
        contact._username = kwargs.get('username')
        contact._avatar = kwargs.get('avatar')

        return contact

    def _setId(self, contactId: str):
        self._id = contactId
    
    def _getId(self):
        return self._id
    
        
