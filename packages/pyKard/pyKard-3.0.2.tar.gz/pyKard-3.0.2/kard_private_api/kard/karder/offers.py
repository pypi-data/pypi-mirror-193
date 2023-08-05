from ...app import Kard
from ... import kard

class KardOffers:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidOffers { "\
            "cashbackOffers { "\
                "name url cashbackRate channel description legalTerms isConsumed maxPerUser brand { name logoUrl description } "\
                "minAmount maxAmount pictureUrl startDate endDate "\
            "} "\
        "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('cashbackOffers'):
            raise kard.exceptions.GraphQLException('Expected "cashbackOffers" to be present. Got: ' + str(response))

        return response['cashbackOffers']

    def get(self):
        return self.getCompleteData()