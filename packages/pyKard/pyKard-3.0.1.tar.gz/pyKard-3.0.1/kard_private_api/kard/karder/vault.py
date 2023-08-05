from ...app import Kard
from ... import kard

class KardVault:
    def __init__(self, kard: Kard):
        self.app = kard

    def _new(self, vaultId: str):
        vault = KardVault(self.app)
        vault._setId(vaultId)
        return vault

    def _setId(self, vaultId: str):
        self._id = vaultId

    def _getId(self):
        return self._id


    def getCompleteData(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { "\
            "id name color emoji { name unicode } goal { value currency { symbol isoCode } } "\
            "balance { value currency { symbol isoCode } }"\
        "} }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault'):
            raise kard.exceptions.GraphQLException('Expected "vault" to be present. Got: ' + str(response))

        return response['vault']

    @property
    def id(self):
        return self._getId()

    @property
    def name(self):
        return self.getName()

    @property
    def balance(self):
        return self.getBalance()
    
    @property
    def goal(self):
        return self.getGoal()
    
    @property
    def emoji(self):
        return self.getEmoji()
    
    @property
    def color(self):
        return self.getColor()
    
    @property
    def colour(self):
        return self.color


    def getName(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { name } }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('name'):
            raise kard.exceptions.GraphQLException('Expected "vault.name" to be present. Got: ' + str(response))

        return response['vault']['name']

    def getBalance(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { balance { value currency { symbol isoCode } } } }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('balance'):
            raise kard.exceptions.GraphQLException('Expected "vault.balance" to be present. Got: ' + str(response))

        return response['vault']['balance']

    def getGoal(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { goal { value currency { symbol isoCode } } } }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('goal'):
            raise kard.exceptions.GraphQLException('Expected "vault.goal" to be present. Got: ' + str(response))

        return response['vault']['goal']
    
    def getEmoji(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { emoji { name unicode } } }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('emoji'):
            raise kard.exceptions.GraphQLException('Expected "vault.emoji" to be present. Got: ' + str(response))

        return response['vault']['emoji']

    def getColor(self):
        query = "query getVault($vaultId: ID!) { vault(vaultId: $vaultId) { color } }"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('color'):
            raise kard.exceptions.GraphQLException('Expected "vault.color" to be present. Got: ' + str(response))

        return response['vault']['color']
    
    def getColour(self):
        return self.getColor()

    def getTransactions(self, first: int=10, after: str=None, numberOfComments: int=3):
        query = "query androidGetVaultTransactions($vaultId: ID!, $first: Int, $after: String, $numberOfComments: Int) { "\
                    "vault(vaultId: $vaultId) { id transactions(first: $first, after: $after) { "\
                        "pageInfo { endCursor hasNextPage } nodes { ... Transaction_TransactionParts } "\
                    "} }"\
                "}\n\n"\
                "fragment Transaction_TransactionParts on Transaction { "\
                    "__typename id title status address image { id url } visibility amount { value currency { symbol } } "\
                    "category { name color image { url } } processedAt unreadCommentsCount lastCommentReadAt "\
                    "comments(first: $numberOfComments) { "\
                        "totalCount pageInfo { endCursor hasNextPage } "\
                            "nodes { id comment createdAt user { id nickname firstName lastName avatar { url } } } "\
                    "} quickAnswers { message } user { id firstName lastName username avatar { url } } "\
                "}"
        variables = {
            "vaultId": self._getId(),
            "first": first,
            "after": after,
            "numberOfComments": numberOfComments
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('vault', {}).get('transactions'):
            raise kard.exceptions.GraphQLException('Expected "vault.transactions" to be present. Got: ' + str(response))
        
        return response['vault']['transactions']


    def setName(self, name: str):
        query = "mutation androidUpdateVault($vaultId: ID!, $name: Name) { "\
                "updateVault(input: {vaultId: $vaultId, name: $name}) { "\
                    "errors { message path } vault { id name } "\
                "}"\
            "}"
        variables = {
            "vaultId": self.id,
            "name": name
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateVault', {}).get('vault'):
            raise kard.exceptions.GraphQLException('Expected "updateVault.vault" to be present. Got: ' + str(response))
        
        return response['updateVault']

    def setEmoji(self, emoji: str):
        valid_emojies = ["🎁", "🎈", "🛍", "💰", "😈", "🎓", "🏝", "🎫", "🎸", "✈️", "👟", "📱", "🎮", "🛴", "🛵"]

        query = "mutation androidUpdateVault($vaultId: ID!, $emoji: EmojiInput) { "\
                "updateVault(input: {vaultId: $vaultId, emoji: $emoji}) { "\
                    "errors { message path } vault { id emoji { name unicode } } "\
                "}"\
            "}"
        variables = {
            "vaultId": self.id,
            "emoji": emoji
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateVault', {}).get('vault'):
            raise kard.exceptions.GraphQLException('Expected "updateVault.vault" to be present. Got: ' + str(response))
        
        return response['updateVault']

    def setColor(self, color: str):
        official_colors = {
            "purpleblack": "#1f193f",    "grey":"#75818c",
            "purplelight": "#bd3fdd",    "yellow":"#ffca10",
            "purpledark": "#9850ff",     "pink":"#f943b1",
            "black": "#1b1d20",          "green":"#3ce977",
            "orange":"#ff9455",          "red": "#ff5f7c",
            "cyan":"#15e4da",            "blue": "#35c4ff"
        } # Any hexadecimal code will work though! (Must provide in #xxxxxx format)
          
        if color in official_colors:
            color = official_colors[color]

        query = "mutation androidUpdateVault($vaultId: ID!, $color: HexadecimalColorCode) { "\
                "updateVault(input: {vaultId: $vaultId, color: $color}) { "\
                    "errors { message path } vault { id color } "\
                "}"\
            "}"
        variables = {
            "vaultId": self.id,
            "color": color
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateVault', {}).get('vault'):
            raise kard.exceptions.GraphQLException('Expected "updateVault.vault" to be present. Got: ' + str(response))
        
        return response['updateVault']

    def setColour(self, colour: str):
        return self.setColor(colour)


    def topup(self, amount: float, currency: str="EUR"):
        query = "mutation androidTransferMoney($sourceId: ID, $destinationId: ID!,$amount: AmountInput!) { "\
                    "transferMoney(input: {sourceId: $sourceId, destinationId: $destinationId, amount: $amount}) { "\
                        "errors { message path } "\
                    "}"\
                "}"
        variables = {
            "destinationId": self.id,
            "sourceId": self.app.bankAccount.id,
            "amount": {
                "value": amount,
                "currency": currency
            }
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('transferMoney'):
            raise kard.exceptions.GraphQLException('Expected "transferMoney" to be present. Got: ' + str(response))
        
        return response['transferMoney']

    def withdraw(self, amount: float, currency: str="EUR"):
        query = "mutation androidTransferMoney($sourceId: ID, $destinationId: ID!,$amount: AmountInput!) { "\
                    "transferMoney(input: {sourceId: $sourceId, destinationId: $destinationId, amount: $amount}) { "\
                        "errors { message path } "\
                    "}"\
                "}"
        variables = {
            "destinationId": self.app.bankAccount.id,
            "sourceId": self.id,
            "amount": {
                "value": amount,
                "currency": currency
            }
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('transferMoney'):
            raise kard.exceptions.GraphQLException('Expected "transferMoney" to be present. Got: ' + str(response))
        
        return response['transferMoney']

    def delete(self):
        query = "mutation androidCloseVault($vaultId: ID!) { closeVault(input: {vaultId: $vaultId}) { "\
                    "errors { message path } }"\
                "}"
        variables = {
            "vaultId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('closeVault'):
            raise kard.exceptions.GraphQLException('Expected "closeVault" to be present. Got: ' + str(response))
        
        return response['closeVault']

