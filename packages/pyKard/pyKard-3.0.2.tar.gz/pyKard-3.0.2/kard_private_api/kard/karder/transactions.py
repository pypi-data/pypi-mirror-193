from ...app import Kard
from ... import kard

class KardTransactions:
    def __init__(self, kard: Kard):
        self.app = kard

    def get(self, first: int=20, after: str=None, numberOfComments: int=3):
        query = "query androidTransactions($first: Int, $after: String, $numberOfComments: Int) { me { "\
                    "bankAccount { balance { value } } "\
                    "typedTransactions(first: $first, after: $after) { "\
                        "pageInfo { endCursor hasNextPage } "\
                        "nodes { "\
                            "__typename id title status visibility amount { value currency { symbol } } "\
                            "category { name color image { url } } user { id firstName lastName username } "\
                            "processedAt unreadCommentsCount lastCommentReadAt "\
                            "comments(first: $numberOfComments) { "\
                                "totalCount pageInfo { endCursor hasNextPage } "\
                                "nodes { id comment createdAt user { id nickname firstName lastName avatar { url } } } "\
                            "} "\
                            "...on P2pTransaction { triggeredBy { id firstName lastName username avatar { url } } reason } "\
                            "...on OutgoingWireTransferTransaction { "\
                                "beneficiary { bankLogo { url } bankName iban bic id surname fullName } reason "\
                            "} "\
                            "...on ClosingAccountTransaction { moneyAccount { ... Vault_VaultMiniParts } } "\
                            "...on CardTransaction { "\
                                "card { ... Card_CardParts } mobilePaymentProvider "\
                                "cashback { id status brandLogo brandName amount { value currency { symbol } } } "\
                            "} "\
                            "...on InternalTransferTransaction { moneyAccount { ... Vault_VaultMiniParts } } "\
                            "... on MoneyLinkTransaction { from message } "\
                            "... on TopupTransaction { sender { nickname member { id profile { firstName } } } message } "\
                            "... on RejectedTransaction { rejectionReason } "\
                            "... on CashbackTransaction { cashback { id status brandLogo brandName amount { value currency { symbol } } "\
                                "sourceTransaction { "\
                                    "id title image { id url } category { name color image { url } } "\
                                    "amount { value currency { symbol } } } "\
                                "} "\
                            "} "\
                            "...on AtmTransaction { card { ... Card_CardParts } } "\
                        "} "\
                    "} "\
                "}}\n\n"\
                "fragment Vault_VaultMiniParts on Vault { name color emoji { name unicode }}\n\n"\
                "fragment Card_CardParts on Card { "\
                    "__typename id activatedAt customText name visibleNumber blocked expirationAt "\
                    "scheme ... on PhysicalCard { "\
                        "atm contactless swipe online design reorderExpiredFees { value currency { isoCode } } "\
                        "orderedAt orderDelayed isMain isSoonExpired estimatedCraftingDate estimatedDeliveryDate "\
                    "}"\
                "}"
        variables = {
            'first': first,
            'after': after,
            'numberOfComments': numberOfComments
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('typedTransactions'):
            raise kard.exceptions.GraphQLException('Expected "me.typedTransactions" to be present. Got: ' + str(response))
        
        return response['me']['typedTransactions']

    def getAll(self):
        transactions = []
        lastPageInfo = {}

        x = self.get()
        transactions += x['nodes']
        lastPageInfo = x['pageInfo']

        while lastPageInfo['hasNextPage']:
            x = self.get(after=lastPageInfo['endCursor'])
            transactions += x['nodes']
            lastPageInfo = x['pageInfo']

        return transactions

