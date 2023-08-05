from ...app import Kard
from ... import kard

class KardBank:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "id iban bic user { firstName lastName } balance { value currency { symbol isoCode } } "\
                    "lockedTransactions createdAt"\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount" to be present. Got: ' + str(response))

        return response['me']['bankAccount']

    @property
    def id(self):
        return self.getId()
    
    @property
    def iban(self):
        return self.getIBAN()
    
    @property
    def bic(self):
        return self.getBIC()
    
    @property
    def user(self):
        return self.getUser()

    @property
    def owner(self):
        return self.user
    
    @property
    def balance(self):
        return self.getBalance()

    def getId(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "id "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('id'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.id" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['id']

    def getIBAN(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "iban "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('iban'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.iban" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['iban']
    
    def getIban(self):
        return self.getIBAN()

    def getBIC(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "bic "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('bic'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.bic" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['bic']

    def getBic(self):
        return self.getBIC()

    def getUser(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "user { firstName lastName } "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('user'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.user" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['user']

    def getOwner(self):
        return self.getUser()

    def getBalance(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "balance { value currency { symbol isoCode } } "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('balance'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.balance" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['balance']
    
    def getLockedTransactions(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "lockedTransactions "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('lockedTransactions'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.lockedTransactions" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['lockedTransactions']
    
    def getCreatedAt(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Me_MeParts on Me { "\
                "bankAccount { "\
                    "createdAt "\
                "} "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('bankAccount', {}).get('createdAt'):
            raise kard.exceptions.GraphQLException('Expected "me.bankAccount.createdAt" to be present. Got: ' + str(response))
        
        return response['me']['bankAccount']['createdAt']


    def sendMoneyToUser(self, userId: str, amount: float, currency: str='EUR', reason: str=''):
        query = "mutation androidSendMoney($input: SendMoneyInput!) { sendMoney(input: $input) { errors { path message } } }"
        variables = {
            "input": {
                "internalUsersIds": [userId],
                "externalUsers": [],
                "amount": {"value": amount, "currency": currency},
                "reason": reason
            }
		}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('sendMoney'):
            raise kard.exceptions.GraphQLException('Expected "sendMoney" to be present. Got: ' + str(response))
        
        if response['sendMoney'].get('errors'):
            raise kard.exceptions.GraphQLException('Expected "sendMoney.errors" to be empty. Got: ' + str(response))

        return True

