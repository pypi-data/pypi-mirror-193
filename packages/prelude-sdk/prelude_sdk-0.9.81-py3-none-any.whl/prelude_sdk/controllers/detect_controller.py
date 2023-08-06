import requests

from prelude_sdk.models.account import verify_credentials


class DetectController:

    def __init__(self, account):
        self.account = account

    @verify_credentials
    def register_endpoint(self, name, tags):
        """ Register (or re-register) an endpoint to your account """
        params = dict(id=name, tags=tags)
        res = requests.post(f'{self.account.hq}/detect/endpoint', headers=self.account.headers, json=params)
        if res.status_code == 200:
            return res.text
        raise Exception(res.text)

    @verify_credentials
    def delete_endpoint(self, ident: str):
        """ Delete an endpoint from your account """
        params = dict(id=ident)
        res = requests.delete(f'{self.account.hq}/detect/endpoint', headers=self.account.headers, json=params)
        if res.status_code != 200:
            raise Exception(res.text)

    @verify_credentials
    def list_endpoints(self):
        """ List all endpoints on your account """
        res = requests.get(f'{self.account.hq}/detect/endpoint', headers=self.account.headers)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)
    
    @verify_credentials
    def describe_activity(self, filters: dict, view: str = 'logs'):
        """ Get report for an Account """
        params = dict(view=view, **filters)
        res = requests.get(f'{self.account.hq}/detect/activity', headers=self.account.headers, params=params)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)

    @verify_credentials
    def print_queue(self):
        res = requests.get(f'{self.account.hq}/detect/queue', headers=self.account.headers)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)

    @verify_credentials
    def enable_test(self, ident: str, run_code: int, tags: str):
        """ Enable a test so endpoints will start running it """
        res = requests.post(
            url=f'{self.account.hq}/detect/queue/{ident}',
            headers=self.account.headers,
            json=dict(code=run_code, tags=tags)
        )
        if res.status_code != 200:
            raise Exception(res.text)

    @verify_credentials
    def disable_test(self, ident):
        """ Disable a test so endpoints will stop running it """
        res = requests.delete(f'{self.account.hq}/detect/queue/{ident}', headers=self.account.headers)
        if res.status_code != 200:
            raise Exception(res.text)
    
    @verify_credentials
    def search(self, identifier: str):
        """ Search the NVD for a keyword """
        params = dict(identifier=identifier)
        res = requests.get(f'{self.account.hq}/detect/search', headers=self.account.headers, params=params)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)

    @verify_credentials
    def social_stats(self, ident: str, days: int = 30):
        """ Pull social statistics for a specific test """
        params = dict(days=days)
        res = requests.get(f'{self.account.hq}/detect/{ident}/social', headers=self.account.headers, params=params)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)

    @verify_credentials
    def recommendations(self):
        """ List all security recommendations for your account """
        res = requests.get(f'{self.account.hq}/detect/recommendations', headers=self.account.headers)
        if res.status_code == 200:
            return res.json()
        raise Exception(res.text)

    @verify_credentials
    def create_recommendation(self, title: str, description: str):
        """ Create a new security recommendation """
        params = dict(title=title, description=description)
        res = requests.post(f'{self.account.hq}/detect/recommendations', headers=self.account.headers, json=params)
        if res.status_code != 200:
            raise Exception(res.text)
