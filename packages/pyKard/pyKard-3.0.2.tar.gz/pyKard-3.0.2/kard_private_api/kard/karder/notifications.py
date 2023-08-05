from ...app import Kard
from ... import kard

class KardNotifications:
    def __init__(self, kard: Kard):
        self.app = kard


    def getCompleteData(self):
        query = "query androidGetActivityItems { activityItems { "\
                    "id onClickUrl title body icon isRead isDone createdAt device modal "\
                        "{ title body buttonTitle onClickUrl kardy withCelebration } "\
                "}}"
        variables = {}
        extensions = {}

        response = self.app.graphql.request(query, variables, extensions)
        if not response.get('activityItems'):
            raise kard.exceptions.GraphQLException('Expected "activityItems" to be present. Got: ' + str(response))

        return response['activityItems']
