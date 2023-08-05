import requests

class GraphQL:
    def __init__(self, host: str, path: str, vendorIdentifier: str):
        self.host = host
        self.path = path
        self.url = 'https://' + self.host + self.path

        self.s = requests.Session()
        self.s.headers.update({
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'en',
            'Content-Type': 'application/json',
            'Host': self.host,
            'User-Agent': 'okhttp/4.9.3',
            'vendorIdentifier': vendorIdentifier,
        })

    def setVendorIdentifier(self, vendorIdentifier: str):
        self.s.headers.update({
            'vendorIdentifier': vendorIdentifier,
        })

    def setAccessToken(self, accessToken: str):
        self.s.headers.update({
            'Authorization': 'Bearer ' + accessToken,
        })


    def request(self, query, variables: dict={}, extensions: dict={}):
        response = self.s.post(
            self.url,
            json={
                'query': query,
                'variables': variables,
                'extensions': extensions
            }
        )
        if response.status_code == 200:
            r = response.json()
            if r.get('data'):
                return r['data']
            return r
        else:
            raise Exception('Query failed to run by returning code of {}.\nQuery: {}\nResponse: {}'.format(response.status_code, query, response.content))