from ...app import Kard
from ... import kard

class KardBeneficiaries:
    def __init__(self, kard: Kard):
        self.app = kard

    def getAll(self):
        query = "query androidListBeneficiaries { me { "\
                    "beneficiaries { bankLogo { url } bankName iban bic id surname fullName } "\
                "}}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('beneficiaries'):
            raise kard.exceptions.GraphQLException('Expected "me.beneficiaries" to be present. Got: ' + str(response))
        
        beneficiaries = []
        for beneficiary in response['me']['beneficiaries']:
            beneficiaries.append( beneficiary )

        return beneficiaries

    def get(self, beneficiaryId: str):
        _all = self.getAll()
        for beneficiary in _all:
            if beneficiary['id'] == beneficiaryId:
                return self.beneficiary._new(beneficiary.pop('id'), **beneficiary)

        raise kard.exceptions.BeneficiaryNotFoundError("Beneficiary %s not found" % beneficiaryId)
