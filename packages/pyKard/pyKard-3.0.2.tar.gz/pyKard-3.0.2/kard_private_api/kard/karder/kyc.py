from ...app import Kard
from ... import kard

class KardKYC:
    def __init__(self, kard: Kard):
        self.app = kard

    
    def getCompleteData(self):
        query = "query androidKyc { me { kyc { ... Me_KycParts } }}\n\n"\
                "fragment Me_KycParts on Kyc { "\
                    "required deadline globalStatus fundsOrigin { status value rejectionReason } "\
                    "identityVerification { status url rejectionReason score } "\
                    "proofOfAddress { status files { contentType url ... on Image { width height } } rejectionReason } "\
                    "canStart lastRejectedIdentityVerification { status url rejectionReason score} nbOfRejectedIdentityVerifications"\
                "}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('kyc', {}):
            raise kard.exceptions.GraphQLException('Expected "me.kyc" to be present. Got: ' + str(response))

        return response['me']['kyc']

    @property
    def isCompleted(self):
        return self.getCompletedStatus() == 'APPROVED'

    @property
    def deadline(self):
        return self.getDeadline()

    @property
    def fundsOrigin(self):
        return self.getFundsOrigin()

    @property
    def proofsOfAddress(self):
        return self.getProofsOfAddress()


    def getCompletedStatus(self):
        query = "query androidKyc { me { kyc { globalStatus } }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('kyc', {}):
            raise kard.exceptions.GraphQLException('Expected "me.kyc" to be present. Got: ' + str(response))

        return response['me']['kyc']['globalStatus']

    def getDeadline(self):
        query = "query androidKyc { me { kyc { deadline } }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('kyc', {}):
            raise kard.exceptions.GraphQLException('Expected "me.kyc" to be present. Got: ' + str(response))

        return response['me']['kyc']['deadline']

    def getFundsOrigin(self):
        query = "query androidKyc { me { kyc { fundsOrigin { status value rejectionReason } }}}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('kyc', {}):
            raise kard.exceptions.GraphQLException('Expected "me.kyc" to be present. Got: ' + str(response))

        return response['me']['kyc']['fundsOrigin']['value']

    def getProofsOfAddress(self):
        query = "query androidKyc { me { kyc { "\
                    "proofOfAddress { status files { contentType url ... on Image { width height } } rejectionReason } "\
                "}}}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('kyc', {}):
            raise kard.exceptions.GraphQLException('Expected "me.kyc" to be present. Got: ' + str(response))

        return response['me']['kyc']['proofOfAddress']['files']

