from ...app import Kard
from ... import kard

import requests

class KardCards:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Card_CardParts on Card { __typename id activatedAt customText name visibleNumber blocked expirationAt "\
                "scheme ... on PhysicalCard { atm contactless swipe online design reorderExpiredFees { value currency { isoCode } } "\
                    "orderedAt orderDelayed isMain isSoonExpired estimatedCraftingDate estimatedDeliveryDate "\
                "}"\
            "}\n\n"\
            "fragment Me_MeParts on Me { "\
                "card { id } cardBeingSetup { __typename id customText name ... on PhysicalCard { design } } "\
                "cards { nodes { ... Card_CardParts } } "\
            "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('cards', {}).get('nodes'):
            raise kard.exceptions.GraphQLException('Expected "me.cards.nodes" to be present. Got: ' + str(response))

        return response['me']['cards']['nodes']

    def getCard(self, cardId: str):
        for card in self.getCards():
            if card['id'] == cardId:
                return card

        raise kard.exceptions.CardNotFoundException('Card "%s" not found' % cardId)

    def getCards(self):
        return self.getCompleteData()

    def getPhysicalCards(self):
        return [card for card in self.getCards() if card['__typename'] == 'PhysicalCard']

    def getVirtualCards(self):
        return [card for card in self.getCards() if card['__typename'] == 'VirtualCard']

    def getPIN(self, cardId: str):
        query = "query androidUrlToGetPin($cardId: ID!) { urlToGetPin(cardId: $cardId) { ip url }}"
        variables = {
            "cardId": cardId
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('urlToGetPin', {}).get('url'):
            raise kard.exceptions.GraphQLException('Expected "urlToGetPin.url" to be present. Got: ' + str(response))

        response = requests.request(
            'GET',
            response['urlToGetPin']['url'],
            headers={
                "Authorization": "Bearer " + self.app.settings.getAccessToken(),
                "VendorIdentifier": self.app.settings.getVendorIdentifier()
            }
        )
        if response.status_code != 200 or not response.json().get('card_pin'):
            raise kard.exceptions.GraphQLException('Expected "card_pin" to be present. Got: ' + str(response.content))
        
        return response.json()['card_pin']

    def getPin(self, cardId: str):
        return self.getPIN(cardId)

    def getDigits(self, cardId: str):
        query = "query androidUrlToGetPan($cardId: ID!) { urlToGetPan(cardId: $cardId) { ip url }}"
        variables = {
            "cardId": cardId
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('urlToGetPan', {}).get('url'):
            raise kard.exceptions.GraphQLException('Expected "urlToGetPan.url" to be present. Got: ' + str(response))
        
        response = requests.request(
            'GET',
            response['urlToGetPan']['url'],
            headers={
                "Authorization": "Bearer " + self.app.settings.getAccessToken(),
                "VendorIdentifier": self.app.settings.getVendorIdentifier()
            }
        )
        if response.status_code != 200 or not response.json().get('card_pan'):
            raise kard.exceptions.GraphQLException('Expected "card_pan" to be present. Got: ' + str(response.content))
        
        return response.json()

    def getNumbers(self, cardId: str):
        return self.getDigits(cardId)

    def getDetails(self, cardId: str):
        return self.getDigits(cardId)

    def getAvailableBackgroundCustomizations(self):
        query = "query androidCardCustomizationBackgrounds { cardCustomizationBackgrounds { id name image { url } }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('cardCustomizationBackgrounds'):
            raise kard.exceptions.GraphQLException('Expected "cardCustomizationBackgrounds" to be present. Got: ' + str(response))

        return response['cardCustomizationBackgrounds']


    def update(self, cardId: str, attributes: dict):
        query = "mutation androidUpdateCard($input: UpdateCardInput!) { "\
                    "updateCard(input: $input) { card { ... Card_CardParts } errors { path message} }}\n\n"\
                "fragment Card_CardParts on Card { "\
                    "__typename id activatedAt customText name visibleNumber blocked expirationAt "\
                    "scheme ... on PhysicalCard { atm contactless swipe online design reorderExpiredFees { value currency { isoCode } } "\
                    "orderedAt orderDelayed isMain isSoonExpired estimatedCraftingDate estimatedDeliveryDate "\
                "}"\
            "}"
        variables = {
            "input": {
                "cardId": cardId,
                "attributes": attributes
            }
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateCard', {}).get('card'):
            raise kard.exceptions.GraphQLException('Expected "updateCard.card" to be present. Got: ' + str(response))

        return response['updateCard']['card']

    def block(self, cardId: str):
        return self.update(cardId, {"blocked": True})
    
    def unblock(self, cardId: str):
        return self.update(cardId, {"blocked": False})
