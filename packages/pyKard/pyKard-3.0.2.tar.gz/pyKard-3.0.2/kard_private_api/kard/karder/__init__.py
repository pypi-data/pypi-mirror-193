from . import bankAccount
from . import beneficiaries
from . import beneficiary
from . import cards
from . import cashback
from . import contacts
from . import details
from . import family
from . import kyc
from . import notifications
from . import offers
from . import subscription
from . import transactions
from . import topupCards
from . import topupCard
from . import vaults
from . import vault

def setup(kard):
    kard.bankAccount = bankAccount.KardBank(kard)
    kard.beneficiaries = beneficiaries.KardBeneficiaries(kard)
    kard.beneficiaries.beneficiary = beneficiary.KardBeneficiary(kard)
    kard.cards = cards.KardCards(kard)
    kard.cashback = cashback.KardCashback(kard)
    kard.cashback.offers = offers.KardOffers(kard)
    kard.contacts = contacts.KardContacts(kard)
    kard.details = details.KardAccount(kard)
    kard.family = family.KardFamily(kard)
    kard.kyc = kyc.KardKYC(kard)
    kard.notifications = notifications.KardNotifications(kard)
    kard.subscription = subscription.KardSubscription(kard)
    kard.transactions = transactions.KardTransactions(kard)
    kard.topupCards = topupCards.KardTopupCards(kard)
    kard.topupCards.topupCard = topupCard.KardTopupCard(kard)
    kard.vaults = vaults.KardVaults(kard)
    kard.vaults.vault = vault.KardVault(kard)

    return kard
