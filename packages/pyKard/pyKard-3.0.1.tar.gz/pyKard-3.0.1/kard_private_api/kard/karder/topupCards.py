from ...app import Kard
from ... import kard

import requests

class KardTopupCards:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidListTopupCard { me { topupCards { ... Topup_TopupCardParts } }}\n\n"\
                "fragment Topup_TopupCardParts on TopupCard { id name expirationDate default last4 providerSourceId providerPaymentId}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('topupCards'):
            raise kard.exceptions.GraphQLException('Expected "me.topupCards" to be present. Got: ' + str(response))

        return response['me']['topupCards']

    def getAll(self):
        return self.getCompleteData()

    def get(self, cardId: str):
        cards = self.getAll()
        for card in cards:
            if card['id'] == cardId:
                return card
        
        raise kard.exceptions.CardNotFoundException('Card %s not found' % cardId)

    def getDefault(self):
        cards = self.getAll()
        for card in cards:
            if card['default']:
                return card
        
        raise kard.exceptions.CardNotFoundException('No default card found')
    

    def add(self, digits: str, exp_month: str, exp_year: str, cvv: str):
        # Step 1: Create a token
        r = requests.post(
            'https://api.checkout.com/tokens',
            json={
                'type': 'card',
                'number': digits,
                'expiry_month': exp_month,
                'expiry_year': exp_year,
                'cvv': cvv
            },
            headers={
                'authorization': 'INVESTIGATE IF THIS IS PRIVATE, IF SO, HOW IS IT OBTAINED'
            }
        )
        if r.status_code != 201:
            raise ValueError('Failed to create token: %s: %s' % (r.status_code, r.text))
        
        # Step 2: Add the token to Kard
        query = "mutation androidAddTopupCard($token: String!, $failureUrl: String, $successUrl: String) { "\
                    "addTopupCard(input: {token: $token, failureUrl: $failureUrl, successUrl: $successUrl}) { "\
                        "paymentId secureFormUrl errors { message path } "\
                    "}"\
                "}"
        variables = {
            "token": r.json()['token'],
            "failureUrl": "https://eu.kard.app/3ds/failure",
            "successUrl": "https://eu.kard.app/3ds/success"
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('addTopupCard'):
            raise kard.exceptions.GraphQLException('Expected "addTopupCard" to be present. Got: ' + str(response))
        
        if response['addTopupCard']['errors']:
            raise kard.exceptions.GraphQLException('Expected "addTopupCard.errors" to be empty. Got: ' + str(response))
        
        # Step 3: Return 3D secure form url
        return response['addTopupCard']['secureFormUrl']

        #~ TODO!

        
