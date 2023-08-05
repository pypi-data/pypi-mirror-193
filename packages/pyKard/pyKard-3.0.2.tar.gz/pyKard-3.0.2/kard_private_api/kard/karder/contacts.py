from ...app import Kard
from ... import kard

class KardContacts:
    def __init__(self, kard: Kard):
        self.app = kard


    def getCompleteData(self):
        query = "query androidListContacts { me { contacts(kardersOnly: true) { "\
                    "identifier status user { __typename avatar { url } hasBankAccount id firstName lastName username } "\
                "} }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('contacts'):
            raise kard.exceptions.GraphQLException('Expected "me.contacts" to be present. Got: ' + str(response))

        return response['me']['contacts']

    def getAll(self):
        return self.getCompleteData()
    
    def get(self, identifier: str|int):
        cId = str(identifier)

        for contact in self.getAll():
            if contact['identifier'] == cId:
                return contact

        raise kard.exceptions.ContactNotFoundError("Contact %s not found" % cId)

    def getAllParents(self):
        contacts = []
        for contact in self.getAll():
            if contact['user']['__typename'] == 'ParentUser':
                contacts.append(contact)
        
        return contacts

    def getAllAdults(self):
        contacts = []
        for contact in self.getAll():
            if contact['user']['__typename'] == 'AdultUser':
                contacts.append(contact)
        
        return contacts

    def getAllTeens(self):
        contacts = []
        for contact in self.getAll():
            if contact['user']['__typename'] == 'TeenUser':
                contacts.append(contact)
        
        return contacts
