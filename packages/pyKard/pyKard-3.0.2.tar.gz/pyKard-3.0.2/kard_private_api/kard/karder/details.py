from ...app import Kard
from ... import kard

class KardAccount:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidMe { me { ... Me_MeParts }}\n\n"\
            "fragment Card_CardParts on Card { __typename id activatedAt customText name visibleNumber blocked expirationAt "\
                "scheme ... on PhysicalCard { atm contactless swipe online design reorderExpiredFees { value currency { isoCode } } "\
                    "orderedAt orderDelayed isMain isSoonExpired estimatedCraftingDate estimatedDeliveryDate "\
                "}"\
            "}\n\n"\
            "fragment Topup_TopupCardParts on TopupCard { "\
                "id name expirationDate default last4 providerSourceId providerPaymentId"\
            "}\n\n"\
            "fragment Me_SubscriptionParts on Subscription { "\
                "id status cancelledAt cancellationReason maxChildren maxParents hasInsurance promotionalCreditBalance { "\
                    "value currency { isoCode name symbol symbolFirst } "\
                "} nextBilling { date amount { value currency { isoCode name symbol symbolFirst } } } "\
                    "plan { __typename id periodUnit name providerId price { value } }"\
            "}\n\n"\
            "fragment Topup_RecurringParts on RecurringPayment { "\
                "id active amount { value currency { symbol isoCode } } child { id } firstPayment nextPayment cancelledAt "\
                    "topupCard { ... Topup_TopupCardParts }"\
                "}\n\n"\
            "fragment Me_TopupRequestParts on TopupRequest { "\
                "id amount { value currency { symbol isoCode } } reason accepted cancelled declined createdAt "\
                    "requestee { id nickname firstName lastName avatar { url } } "\
                    "requester { id nickname firstName lastName avatar { url } }"\
            "}\n\n"\
            "fragment Transaction_TransactionCashbackParts on Transaction { "\
                "id title amount { value currency { symbol } } image { id url } processedAt category { name color image { url } }"\
                " ... on CashbackTransaction { cashback { status brandLogo brandName sourceTransaction { "\
                    "id title image { id url } category { name color image { url } } amount { value currency { symbol } } } } }"\
            "}\n\n"\
            "fragment Me_MeParts on Me { "\
                "id modirumId type intercomHashes { android } teenOnboardingFlow parentOnboardingFlow canFinishOnboarding "\
                    "profile { avatar { url } firstName lastName username age birthday placeOfBirth "\
                        "shippingAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } "\
                        "homeAddress { firstName lastName street line1 line2 zipcode city state country fullAddress } "\
                    "} email emailConfirmed unconfirmedEmail phoneNumber referralCode referralUrl "\
                    "bankAccount { id iban bic user { firstName lastName } balance { value currency { symbol isoCode } } "\
                        "lockedTransactions createdAt "\
                    "} card { id } cardBeingSetup { __typename id customText name ... on PhysicalCard { design } } "\
                    "cards { nodes { ... Card_CardParts } } earnings { value currency { symbol isoCode } } onboardingDone "\
                    "passcodeSet pendingDebts { amount { value currency { symbol isoCode } } id "\
                        "owner { avatar { url } firstName id lastName username } reason } "\
                    "topupCards { ... Topup_TopupCardParts } subscription { ... Me_SubscriptionParts } "\
                    "outgoingRecurringPayments { ... Topup_RecurringParts } incomingRecurringPayment { ... Topup_RecurringParts } "\
                    "fundsOrigin canOrderCard externalAuthenticationProviders { id type uniqueId } claimId cardTransactionsCount "\
                    "topupRequestsFromChildren { ... Me_TopupRequestParts } topupRequestsToParent { ... Me_TopupRequestParts } "\
                    "savingsAmount { value } createdAt cashbackEnabled cashbackWallet { "\
                        "id balance { value currency { symbol isoCode } } "\
                        "amountEarned { value currency { symbol isoCode } } "\
                        "transactions(first: 10, order: CREATED, direction: DESC) { "\
                            "pageInfo { endCursor hasNextPage } "\
                            "nodes { ... Transaction_TransactionCashbackParts } "\
                        "} "\
                    "} invitedByOther topupIncentiveActivated unreadActivityItemsCount noPhoneNumber allowedToAddChild "\
                    "modirumEnabled currentSpendings { "\
                        "monthlyPos { value } weeklyPos { value } weeklyAtm { value } monthlyAtm { value } "\
                    "} legalSpendingLimits { monthlyPos { value } weeklyPos { value } weeklyAtm { value } monthlyAtm { value } } "\
                    "transactionLimits { id amount { value currency { symbol } } recurrence transactionType } "\
                    "transactionAuthorizations { authorizationType isAuthorized } "\
                    "familyRewardAmount { value currency { isoCode } } familyRewardActivated offboardingReasonValidatedAt "\
                    "wireTransfersMinAmount { value currency { isoCode symbol } } family { accountsClosedAt } "\
                    "teenPaysForKardEnabled confirmedAdult canVoteForFeatures"\
            "}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me'):
            raise kard.exceptions.GraphQLException('Expected "me" to be present. Got: {}'.format(request))

        return request['me']

    @property
    def id(self):
        return self.getId()

    @property
    def firstName(self):
        return self.getFirstName()

    @property
    def lastName(self):
        return self.getLastName()

    @property
    def email(self):
        return self.getEmail()

    @property
    def phoneNumber(self):
        return self.getPhoneNumber()

    @property
    def referralCode(self):
        return self.getReferralCode()
    
    @property
    def referralUrl(self):
        return self.getReferralUrl()
    
    @property
    def avatar(self):
        return self.getAvatar()

    @property
    def age(self):
        return self.getAge()

    @property
    def birthday(self):
        return self.getBirthday()

    @property
    def birthDate(self):
        return self.getBirthday()

    @property
    def placeOfBirth(self):
        return self.getPlaceOfBirth()

    @property
    def birthPlace(self):
        return self.getPlaceOfBirth()

    @property
    def shippingAddress(self):
        return self.getShippingAddress()

    @property
    def homeAddress(self):
        return self.getHomeAddress()


    def getId(self):
        query = "query androidMe { me { id }}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('id'):
            raise kard.exceptions.GraphQLException('Expected "me.id" to be present. Got: {}'.format(request))

        return request['me']['id']

    def getFirstName(self):
        query = "query androidMe { me { profile { firstName }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('firstName'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.firstName" to be present. Got: {}'.format(request))

        return request['me']['profile']['firstName']

    def getLastName(self):
        query = "query androidMe { me { profile { lastName }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('lastName'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.lastName" to be present. Got: {}'.format(request))

        return request['me']['profile']['lastName']

    def getEmail(self):
        query = "query androidMe { me { email }}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('email'):
            raise kard.exceptions.GraphQLException('Expected "me.email" to be present. Got: {}'.format(request))

        return request['me']['email']
    
    def getPhoneNumber(self):
        query = "query androidMe { me { phoneNumber }}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('phoneNumber'):
            raise kard.exceptions.GraphQLException('Expected "me.phoneNumber" to be present. Got: {}'.format(request))

        return request['me']['phoneNumber']
    
    def getReferralCode(self):
        query = "query androidMe { me { referralCode }}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('referralCode'):
            raise kard.exceptions.GraphQLException('Expected "me.referralCode" to be present. Got: {}'.format(request))

        return request['me']['referralCode']
    
    def getReferralUrl(self):
        query = "query androidMe { me { referralUrl }}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('referralUrl'):
            raise kard.exceptions.GraphQLException('Expected "me.referralUrl" to be present. Got: {}'.format(request))

        return request['me']['referralUrl']
    
    def getAvatar(self):
        query = "query androidMe { me { avatar { url }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('avatar', {}).get('url'):
            raise kard.exceptions.GraphQLException('Expected "me.avatar.url" to be present. Got: {}'.format(request))

        return request['me']['avatar']['url']
    
    def getAge(self):
        query = "query androidMe { me { profile { age }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('age'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.age" to be present. Got: {}'.format(request))

        return request['me']['profile']['age']

    def getBirthday(self):
        query = "query androidMe { me { profile { birthday }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('birthday'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.birthday" to be present. Got: {}'.format(request))

        return request['me']['profile']['birthday']
    
    def getPlaceOfBirth(self):
        query = "query androidMe { me { profile { placeOfBirth }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('placeOfBirth'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.placeOfBirth" to be present. Got: {}'.format(request))

        return request['me']['profile']['placeOfBirth']
    
    def getShippingAddress(self):
        query = "query androidMe { me { profile { shippingAddress { street line1 line2 city state zipcode country fullAddress } }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('shippingAddress'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.shippingAddress" to be present. Got: {}'.format(request))

        return request['me']['profile']['shippingAddress']
    
    def getHomeAddress(self):
        query = "query androidMe { me { profile { homeAddress { street line1 line2 city state zipcode country fullAddress } }}}"
        variables = {}
        extensions = {}

        request = self.app.graphql.request(query, variables, extensions)
        if not request.get('me', {}).get('profile', {}).get('homeAddress'):
            raise kard.exceptions.GraphQLException('Expected "me.profile.homeAddress" to be present. Got: {}'.format(request))

        return request['me']['profile']['homeAddress']

