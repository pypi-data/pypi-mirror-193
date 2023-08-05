from ...app import Kard
from ... import kard

class KardBeneficiary:
    def __init__(self, kard: Kard):
        self.app = kard

    def _new(self, beneficiaryId: str, **kwargs):
        beneficiary = KardBeneficiary(self.app)
        beneficiary._setId(beneficiaryId)

        beneficiary._name = kwargs.get('fullName')
        beneficiary._bankName = kwargs.get('bankName')
        beneficiary._bankLogo = kwargs.get('bankLogo')
        beneficiary._bankSurname = kwargs.get('surname')
        beneficiary._iban = kwargs.get('iban')
        beneficiary._bic = kwargs.get('bic')
        beneficiary.deleted = False

        return beneficiary

    def _setId(self, beneficiaryId: str):
        self._id = beneficiaryId

    def _getId(self):
        return self._id

    @property
    def id(self):
        return self._getId()
    
    @property
    def name(self):
        return self._name

    @property
    def bankName(self):
        return self._bankName

    @property
    def bankSurname(self):
        return self._bankSurname
    
    @property
    def bankLogo(self):
        return self._bankLogo

    @property
    def iban(self):
        return self._iban
    
    @property
    def bic(self):
        return self._bic


    def setBeneficiaryName(self, name: str):
        return self.editBeneficiary(name, self.bankSurname, self.iban, self.bic)

    def setBeneficiaryBankName(self, bankName: str):
        return self.editBeneficiary(self.name, bankName, self.iban, self.bic)
    
    def setBeneficiaryIban(self, iban: str):
        return self.editBeneficiary(self.name, self.bankSurname, iban, self.bic)
    
    def setBeneficiaryBic(self, bic: str):
        return self.editBeneficiary(self.name, self.bankSurname, self.iban, bic)

    def editBeneficiary(self, name: str, bankName: str, iban: str, bic: str):
        query = "mutation androidUpdateBeneficiary("\
                    "$iban: FrenchIban!, $bic: Bic!, $displayName: BankInfoDisplayName!, "\
                    "$surname: String, $beneficiary_id: ID!"\
                ") { "\
                        "updateBeneficiary(input: { "\
                            "beneficiaryInfo: { iban: $iban, bic: $bic, displayName: $displayName, surname: $surname }, "\
                            "beneficiaryId: $beneficiary_id "\
                        "}) { "\
                            "errors { message path extensions { code } } "\
                        "}"\
                    "}"
        variables = {
            "iban": iban,
            "surname": bankName,
            "beneficiary_id": self.id,
            "bic": bic,
            "displayName": name
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('updateBeneficiary'):
            raise kard.exceptions.GraphQLException('Expected "updateBeneficiary" to be present. Got: ' + str(response))
        
        if response['updateBeneficiary'].get('errors'):
            for error in response['updateBeneficiary']['errors']:
                if error['message'] == 'Variable $bic of type Bic! was provided invalid value':
                    raise ValueError('Invalid BIC %s provided' % bic)
                elif error['message'] == 'Variable $iban of type FrenchIban! was provided invalid value':
                    raise ValueError('Invalid IBAN %s provided' % iban)
                elif error['message'] == 'Variable $surname of type String was provided invalid value':
                    raise TypeError('Invalid surname %s provided. Must be of type str' % bankName)
        
            raise kard.exceptions.GraphQLException('Expected "updateBeneficiary.errors" to be empty. Got: ' + str(response))

        self._name = name
        self._bankName = bankName
        self._bankSurname = bankName
        self._iban = iban
        self._bic = bic

        return True

    def delete(self):
        query = "mutation androidDeleteBeneficiary($beneficiary_id: ID!) { "\
                    "deleteBeneficiary(input: { beneficiaryId: $beneficiary_id }) { "\
                        "errors { message path } "\
                    "}"\
                "}"
        variables = {
            "beneficiary_id": self.id
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('deleteBeneficiary'):
            raise kard.exceptions.GraphQLException('Expected "deleteBeneficiary" to be present. Got: ' + str(response))
        
        if response['deleteBeneficiary'].get('errors'):
            raise kard.exceptions.GraphQLException('Expected "deleteBeneficiary.errors" to be empty. Got: ' + str(response))
        
        self.deleted = True
        return True

    def sendWireTransfer(self, amount: float, currency: str='EUR', reason: str=''):
        query = "mutation androidSendWireTransfer($amount: AmountInput!, $id: ID! $reason: WireTransferReason!) { "\
                    "sendWireTransfer(input: {beneficiaryId: $id, amount: $amount, reason: $reason}) { "\
                        "errors { message path extensions { code }} "\
                    "}"\
                "}"
        variables = {
            "amount": {
                "value": amount,
                "currency": currency
            },
            "id": self.id,
            "reason": reason
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('sendWireTransfer'):
            raise kard.exceptions.GraphQLException('Expected "sendWireTransfer" to be present. Got: ' + str(response))

        if response['sendWireTransfer'].get('errors'):
            for error in response['sendWireTransfer']['errors']:
                errCode = error.get('extensions', {}).get('code')
                if errCode == 'INSUFFICIENT_BALANCE':
                    raise kard.exceptions.InsufficientFundsException('Insufficient funds to send wire transfer')
                elif errCode == 'AMOUNT_TOO_SMALL':
                    raise kard.exceptions.WireTransferInvalidAmount(error['message'])

            raise kard.exceptions.GraphQLException('Expected "sendWireTransfer.errors" to be empty. Got: ' + str(response))

        return True

    def sendMoney(self, **kwargs):
        return self.sendWireTransfer(**kwargs)

    def transfer(self, **kwargs):
        return self.sendWireTransfer(**kwargs)
