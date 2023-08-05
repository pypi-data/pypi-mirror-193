from ...app import Kard
from ... import kard

class KardFamily:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidFamily { me { family { ... Family_FamilyParts } }}\n\n"\
    		"fragment Topup_TopupCardParts on TopupCard { "\
                "id name expirationDate default last4 providerSourceId providerPaymentId"\
            "}\n\n"\
			"fragment Topup_RecurringParts on RecurringPayment { "\
                "id active amount { value currency { symbol isoCode } }"\
                "child { id } firstPayment nextPayment cancelledAt topupCard { ... Topup_TopupCardParts }"\
            "}\n\n"\
			"fragment Card_CardParts on Card { __typename id activatedAt customText name visibleNumber blocked scheme"\
                "... on PhysicalCard { atm contactless swipe online design orderedAt }"\
            "}\n\n"\
			"fragment Me_KycParts on Kyc { required deadline globalStatus fundsOrigin { status value rejectionReason }"\
                " identityVerification { status url rejectionReason score } proofOfAddress {"\
                    " status files { contentType url ... on Image { width height } } rejectionReason "\
                "} canStart lastRejectedIdentityVerification { status url rejectionReason score} nbOfRejectedIdentityVerifications"\
            "}\n\n"\
			"fragment Me_SubscriptionParts on Subscription { id status cancelledAt cancellationReason nextBilling { "\
                "date amount { value currency { isoCode name symbol symbolFirst } } } plan {"\
                    " __typename id periodUnit name providerId price { value } }"\
            "}\n\n"\
			"fragment Family_MeParts on Me { id type createdAt profile { avatar { url } firstName lastName username age "\
                "birthday placeOfBirth shippingAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } "\
                "homeAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } } card { id } "\
                "canOrderCard cardBeingSetup { __typename id customText name ... on PhysicalCard { design } } "\
                "outgoingRecurringPayments { ... Topup_RecurringParts } incomingRecurringPayment { ... Topup_RecurringParts } "\
                "cards { nodes { ... Card_CardParts } } email claimId canOrderCard phoneNumber bankAccount { "\
                    "id iban bic user { firstName lastName } balance { value currency { symbol isoCode } } lockedTransactions } "\
                "topupCards { ... Topup_TopupCardParts } kyc { ... Me_KycParts } subscription { ... Me_SubscriptionParts } "\
                "onboardingDone savingsAmount { value } topupIncentiveActivated noPhoneNumber currentSpendings { "\
                    "monthlyPos { value } weeklyPos { value } weeklyAtm { value } monthlyAtm { value } "\
                "} transactionLimits { id amount { value currency { symbol } } recurrence transactionType }"\
            "}\n\n"\
			"fragment Family_FamilyParts on Family { memberships { status primary type nickname member { ... Family_MeParts } }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('family', {}):
            raise kard.exceptions.GraphQLException('Expected "me.family" to be present. Got: ' + str(response))

        return response

    def getMembers(self):
        query = "query androidFamily { me { family { ... Family_FamilyParts } }}\n\n"\
            "fragment Family_MeParts on Me { id type createdAt profile { avatar { url } firstName lastName username age "\
                "birthday placeOfBirth shippingAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } "\
                "homeAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } } "\
                "email claimId phoneNumber "\
            "}\n\n"\
			"fragment Family_FamilyParts on Family { memberships { status primary type nickname member { ... Family_MeParts } }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('family', {}):
            raise kard.exceptions.GraphQLException('Expected "me.family" to be present. Got: ' + str(response))

        return response

    def getSiblings(self):
        members = self.getMembers()
        siblings = []
        for member in members['me']['family']['memberships']:
            if member['member']['id'] != self.app.details.id:
                if member['type'] != 'PARENT':
                    siblings.append(member)

        return siblings

    def getParents(self):
        members = self.getMembers()
        parents = []
        for member in members['me']['family']['memberships']:
            if member['member']['id'] != self.app.details.id:
                if member['type'] == 'PARENT':
                    parents.append(member)

        return parents

    def getChildren(self):
        # Siblings are anyone but parents, so if user is a parent, siblings returned are in fact children
        return self.getSiblings()
