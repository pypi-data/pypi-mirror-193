from ...app import Kard
from ... import kard

class KardSubscription:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
				"fragment Me_MeParts on Me { subscription {"\
                    "id status cancelledAt cancellationReason nextBilling { date amount { value } } "\
                    "plan { __typename id periodUnit name providerId price { value } } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('subscription'):
            raise kard.exceptions.GraphQLException('Expected "me.subscription" to be present. Got: ' + str(response))

        return response['me']['subscription']

    @property
    def id(self):
        return self.getId()

    @property
    def isActive(self):
        status = self.getStatus()
        return status == 'ACTIVE'

    @property
    def nextBillingDate(self):
        return self.getNextBilling()['date']
    
    @property
    def nextBillingAmount(self):
        nextBilling = self.getNextBilling()
        if nextBilling['amount']:
            return nextBilling['amount']['value']
        return None # Should return None or 0?

    @property
    def planName(self):
        return self.getPlan()['name']

    @property
    def planId(self):
        return self.getPlan()['id']
    
    @property
    def planPrice(self):
        return self.getPlan()['price']['value']

    @property
    def price(self):
        return self.planPrice

    @property
    def isPaidMonthly(self):
        period = self.getPlan()['periodUnit']
        return period == 'MONTH'

    @property
    def isPaidYearly(self):
        period = self.getPlan()['periodUnit']
        return period == 'YEAR'


    def getId(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
                "fragment Me_MeParts on Me { subscription { id } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('subscription', {}).get('id'):
            raise kard.exceptions.GraphQLException('Expected "me.subscription.id" to be present. Got: ' + str(response))

        return response['me']['subscription']['id']

    def getStatus(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
                "fragment Me_MeParts on Me { subscription { status } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('subscription', {}).get('status'):
            raise kard.exceptions.GraphQLException('Expected "me.subscription.status" to be present. Got: ' + str(response))

        return response['me']['subscription']['status']

    def getNextBilling(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
                "fragment Me_MeParts on Me { subscription { nextBilling { date amount { value } } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('subscription', {}).get('nextBilling'):
            raise kard.exceptions.GraphQLException('Expected "me.subscription.nextBilling" to be present. Got: ' + str(response))

        return response['me']['subscription']['nextBilling']
	
    def getPlan(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
                "fragment Me_MeParts on Me { subscription { plan { __typename id periodUnit name providerId price { value } } } }"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('subscription', {}).get('plan'):
            raise kard.exceptions.GraphQLException('Expected "me.subscription.plan" to be present. Got: ' + str(response))

        return response['me']['subscription']['plan']

