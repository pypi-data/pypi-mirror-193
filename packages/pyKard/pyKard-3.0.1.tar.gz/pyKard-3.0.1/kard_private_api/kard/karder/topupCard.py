from ...app import Kard
from ... import kard

class KardTopupCard:
    def __init__(self, kard: Kard):
        self.app = kard

    def _new(self, cardId: str, **kwargs):
        card = KardTopupCard(self.app)
        card._setId(cardId)

        card._name = kwargs.get('name')
        card._expirationDate = kwargs.get('expirationDate')
        card._default = kwargs.get('default')
        card._last4 = kwargs.get('last4')
        card._providerSourceId = kwargs.get('providerSourceId')
        card._providerPaymentId = kwargs.get('providerPaymentId')

        return card

    def _setId(self, cardId: str):
        self._id = cardId
    
    def _getId(self):
        return self._id

    @property
    def id(self):
        return self._getId()

    @property
    def name(self):
        return self._name
    
    @property
    def expirationDate(self):
        return self._expirationDate
    
    @property
    def isDefault(self):
        return self._default
    
    @property
    def last4(self):
        return self._last4
    
    @property
    def providerSourceId(self):
        return self._providerSourceId
    
    @property
    def providerPaymentId(self):
        return self._providerPaymentId
    

    def forget(self):
        query = "mutation androidForgetTopupCard($topupCardId: ID!) { "\
                    "forgetTopupCard(input: { topupCardId: $topupCardId }) { "\
                        "errors { path message } "\
                    "}"\
                "}"
        variables = {
            "id": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('forgetTopupCard'):
            raise kard.exceptions.GraphQLException('Expected "forgetTopupCard" to be present. Got: ' + str(response))

        return response['forgetTopupCard']

    def delete(self):
        return self.forget()

    def setDefault(self):
        query = "mutation androidUpdateTopupCard($topupCardId: ID!) { "\
                    "updateTopupCard(input: {topupCardId: $topupCardId, attributes: {default: true}}) { "\
                        "errors { message path } "\
                    "}"\
                "}"
        variables = {
            "topupCardId": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateTopupCard'):
            raise kard.exceptions.GraphQLException('Expected "updateTopupCard" to be present. Got: ' + str(response))

        if response['updateTopupCard'].get('errors'):
            raise kard.exceptions.GraphQLException('Expected "updateTopupCard.errors" to be empty. Got: ' + str(response))

        return True

    def makeDefault(self):
        return self.setDefault()

