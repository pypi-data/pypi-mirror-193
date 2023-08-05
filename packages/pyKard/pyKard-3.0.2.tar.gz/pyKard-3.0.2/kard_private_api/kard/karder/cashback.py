from ...app import Kard
from ... import kard

class KardCashback:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Transaction_TransactionCashbackParts on Transaction { "\
                "id title amount { value currency { symbol } } image { id url } processedAt category { name color image { url } }"\
                " ... on CashbackTransaction { cashback { status brandLogo brandName sourceTransaction { "\
                    "id title image { id url } category { name color image { url } } amount { value currency { symbol } } } } }"\
            "}\n\n"\
            "fragment Me_MeParts on Me { "\
                "cashbackEnabled cashbackWallet { "\
                    "id balance { value currency { symbol isoCode } } "\
                    "amountEarned { value currency { symbol isoCode } } "\
                    "transactions(first: 10, order: CREATED, direction: DESC) { "\
                        "pageInfo { endCursor hasNextPage } "\
                        "nodes { ... Transaction_TransactionCashbackParts } "\
                    "} "\
                "}"\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackWallet'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackWallet" to be present. Got: ' + str(response))

        return response['me']

    @property
    def walletId(self):
        return self.getWalletId()

    @property
    def isEnabled(self):
        return self.isEnabled()

    @property
    def balance(self):
        return self.getBalance()
    
    @property
    def amountEarned(self):
        return self.getAmountEarned()
    
    @property
    def totalEarned(self):
        return self.amountEarned
    
    @property
    def earned(self):
        return self.amountEarned

    @property
    def transactions(self):
        return self.getTransactions()

    def getWalletId(self):
        query = "query androidMe { me { cashbackWallet { id } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackWallet', {}).get('id'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackWallet.id" to be present. Got: ' + str(response))
        
        return response['me']['cashbackWallet']['id']

    def isEnabled(self):
        query = "query androidMe { me { cashbackEnabled } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackEnabled'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackEnabled" to be present. Got: ' + str(response))
        
        return response['me']['cashbackEnabled']

    def getBalance(self):
        query = "query androidMe { me { cashbackWallet { balance { value currency { symbol isoCode } } } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackWallet', {}).get('balance'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackWallet.balance" to be present. Got: ' + str(response))
        
        return response['me']['cashbackWallet']['balance']

    def getAmountEarned(self):
        query = "query androidMe { me { cashbackWallet { amountEarned { value currency { symbol isoCode } } } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackWallet', {}).get('amountEarned'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackWallet.amountEarned" to be present. Got: ' + str(response))
        
        return response['me']['cashbackWallet']['amountEarned']

    def getTransactions(self, first: int=20, after: str=None):
        query = "query androidCashbackTransactions($first: Int, $after: String) { "\
                "me { "\
                    "cashbackWallet { "\
                        "transactions(first: $first, after: $after, order: CREATED, direction: DESC) { "\
                            "pageInfo { endCursor hasNextPage } nodes { ... Transaction_TransactionCashbackParts } "\
                        "} "\
                    "} "\
                "}"\
            "}\n\n"\
            "fragment Transaction_TransactionCashbackParts on Transaction { "\
                "id title amount { value currency { symbol } } image { id url } processedAt "\
                "category { name color image { url } } ... on CashbackTransaction { "\
                    "cashback { "\
                        "status brandLogo brandName sourceTransaction { "\
                            "id title image { id url } category { name color image { url } } amount { value currency { symbol } } "\
                        "} "\
                    "} "\
                "}"\
            "}"
        variables = {
            "first": 10,
            "after": None
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cashbackWallet', {}).get('transactions'):
            raise kard.exceptions.GraphQLException('Expected "me.cashbackWallet.transactions" to be present. Got: ' + str(response))

        return response['me']['cashbackWallet']['transactions']
    
    # def getAllTransactions(self):
    #     transactions = self.getTransactions()
    #     nodes = transactions['nodes']

    #     while transactions['pageInfo']['hasNextPage']:
    #         transactions = self.getTransactions(after=transactions['pageInfo']['endCursor'])
    #         nodes += transactions['nodes']

    #         # page won't change..

    #     return nodes

    def cashout(self, amount: float, currency: str='EUR'):
        query = "mutation androidTransferMoney($sourceId: ID, $destinationId: ID!,$amount: AmountInput!) { "\
                    "transferMoney(input: {sourceId: $sourceId, destinationId: $destinationId, amount: $amount}) { "\
                        "errors { message path } "\
                    "}"\
                "}"
        variables = {
            "amount": {
                "value": amount,
                "currency": currency
            },
            "sourceId": self.walletId,
            "destinationId": self.app.bankAccount.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('transferMoney') or response.get('transferMoney', {}).get('errors'):
            errors = response.get('errors', [])
            errors += response.get('transferMoney', {}).get('errors', [])

            for error in errors:
                if error['message'] == "Source doesn't have enough funds":
                    raise kard.exceptions.InsufficientFundsException('Insufficient funds')
                elif error['message'].startswith("Variable $amount of type AmountInput! was provided invalid value"):
                    raise kard.exceptions.InvalidValueException(error['message'])

            raise kard.exceptions.GraphQLException('Expected "transferMoney" to be present. Got: ' + str(response))

        return response['transferMoney']

    def transferBalance(self, amount: float, currency: str='EUR'):
        return self.cashout(amount=amount, currency=currency)

    def cashoutAll(self, maximum: float=None):
        if not maximum:
            maximum = self.balance['value']
        else:
            maximum = min(maximum, self.balance['value'])

        return self.cashout(amount=maximum)

    def transferAllBalance(self, maximum: float=None):
        return self.cashoutAll(maximum=maximum)
