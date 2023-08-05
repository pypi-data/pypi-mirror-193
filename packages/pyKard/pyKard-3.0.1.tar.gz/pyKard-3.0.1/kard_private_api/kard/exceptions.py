class InvalidPasscodeError(Exception):
    pass

class InvalidOTPError(Exception):
    pass

class InvalidPhoneNumberError(Exception):
    pass

class GraphQLException(Exception):
    pass

class CardNotFoundException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class InvalidValueException(Exception):
    pass

class VaultNotFoundException(Exception):
    pass

class ContactNotFoundError(Exception):
    pass

class BeneficiaryNotFoundError(Exception):
    pass

class WireTransferInvalidAmount(Exception):
    pass
