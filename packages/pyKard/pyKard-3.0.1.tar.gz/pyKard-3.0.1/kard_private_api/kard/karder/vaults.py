from ...app import Kard
from ... import kard

class KardVaults:
    def __init__(self, kard: Kard):
        self.app = kard

    def getCompleteData(self):
        query = "query androidListVault { "\
                    "me { vaults { ... Vault_VaultParts } }"\
                "}\n\n"\
                "fragment Vault_VaultParts on Vault { id name color emoji { name unicode } goal { value } balance { value }}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('me', {}).get('vaults') and not isinstance(response['me']['vaults'], list):
            raise kard.exceptions.GraphQLException('Expected "me.vaults" to be present. Got: ' + str(response))

        return response['me']['vaults']

    def getVaults(self, asObject: bool=True):
        vaults = self.getCompleteData()
        if not asObject:
            return vaults

        vaultsObj = []

        for vault in vaults:
            vaultsObj.append(self.getVault(vault['id']))

        return vaultsObj

    def getVault(self, vaultId: str):
        for vault in self.getVaults(asObject=False):
            if vault['id'] == vaultId:
                return self.vault._new(vaultId)

        raise kard.exceptions.VaultNotFoundException("Vault %s not found" % vaultId)


    def createVault(self, name: str, goal: float, currency: str='EUR'):
        query = "mutation androidCreateVault($goal: AmountInput!, $name: Name!) { "\
                    "createVault(input: {goal: $goal, name: $name}) { "\
                        "errors { message path } vault { id } "\
                    "}"\
                "}"
        variables = {
            "name": name,
            "goal": {
                "value": goal,
                "currency": currency
            }
        }
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('createVault', {}).get('vault', {}).get('id'):
            raise kard.exceptions.GraphQLException('Expected "createVault.vault.id" to be present. Got: ' + str(response))

        return self.getVault(response['createVault']['vault']['id'])

    def deleteVault(self, vaultId: str):
        vault = self.getVault(vaultId)
        return vault.delete()
