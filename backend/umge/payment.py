from django.conf import settings

import requests
import json


'''
    Paystack as gateway
'''


class PaymentAPI:

    DEBUG = True

    RECIEVE_ENDPOINT = 'https://api.paystack.co/transaction/initialize/'
    VERIFY_ENDPOINT = 'https://api.paystack.co/transaction/verify/'

    HEADERS = {
        'Cache-Control': 'no-cache'
    }

    def __init__(self, *args, **kwargs):

        '''
        api secret key
        '''

        with open(settings.BASE_DIR.joinpath('config.json')) as config:
            CONFIG = json.load(config)

        if self.DEBUG:
            SECRET_KEY = 'TEST_SECRET_KEY'
            PUBLIC_KEY = 'TEST_PUBLIC_KEY'
        else:
            SECRET_KEY = 'LIVE_SECRET_KEY'
            PUBLIC_KEY = 'LIVE_PUBLIC_KEY'

        self.SECRET_KEY = CONFIG[SECRET_KEY]
        self.PUBLIC_KEY = CONFIG[PUBLIC_KEY]

        '''
        set authorization header
        '''

        self.HEADERS['Authorization'] = f'Bearer {self.SECRET_KEY}'

    def send_request_post(self, *args, **kwargs):
        kwargs = {
            **{
                'headers': self.HEADERS
            },
            **kwargs
        }

        request = requests.post(*args, **kwargs)

        return request

    def send_request_get(self, *args, **kwargs):
        kwargs = {
            **{
                'headers': self.HEADERS
            },
            **kwargs
        }

        request = requests.get(*args, **kwargs)

        return request

    def verify(self, reference):
        response = self.send_request_get(
            url=f'{self.VERIFY_ENDPOINT}{reference}'
        )
        return response.json()

    def recieve(self, email, amount):
        payload = {
            'email': email,
            'amount': amount
        }

        response = self.send_request_post(
            url=self.RECIEVE_ENDPOINT,
            data=payload
        )

        return response.json()

    def transfer(self, *args, **kwargs):
        pass
