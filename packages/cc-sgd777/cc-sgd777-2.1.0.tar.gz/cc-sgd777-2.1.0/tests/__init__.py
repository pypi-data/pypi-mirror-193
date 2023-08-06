from dotenv import load_dotenv

load_dotenv()

import logging
import os
import sys
import unittest
import requests
from urllib.parse import urlparse

from bookmaker.platforms.sgd777 import Sgd777Client, AuthenticationError

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def save_html(r: requests.Response, **kwargs):
    if r.status_code != 200:
        return

    uri = urlparse(r.url)
    path = uri.path.lstrip('/')

    if r.headers.get('Content-Type') == 'text/html; charset=utf-8':
        with open(BASE_DIR + '/test_html/{}_{}.html'.format(r.request.method, path), 'w', encoding='utf8') as f:
            f.write(r.text)


class ApiTest(unittest.TestCase):
    def setUp(self) -> None:

        self.client = Sgd777Client({
            'username': os.environ['TEST_USERNAME'],
            'password': os.environ['TEST_PASSWORD'],
        })

        self.from_date = os.environ['TEST_FROM_DATE']
        self.to_date = os.environ['TEST_TO_DATE']

    def tearDown(self) -> None:
        self.client.close()

    @staticmethod
    def read(filepath):
        with open(BASE_DIR + '/test_html/' + filepath, encoding='utf8') as f:
            return f.read()

    def test_parser(self):
        self.assertEqual(self.client.get_name(self.read('GET_header.aspx.html')), '5evre6')

    def test_basic(self):
        # print(self.client.login_init_token)
        # self.assertEqual('uwa51', self.client.root)
        # self.assertEqual(self.client.get_timestamp('2022-03-07'), 1646625600000)
        # self.client.hooks['response'].append(save_html)
        # self.client.debug_captcha = True
        # print(os.getenv('CAPTCHA_API'))
        self.assertEqual(self.client.root, '5evre6')

    def test_api(self):
        wl = self.client.win_lose(self.from_date, self.to_date)
        for i in wl:
            print(i)

    def test_login_error(self):
        client = Sgd777Client({'username': 'testasfasf', 'password': 'test@ajsfh'})
        with self.assertRaises(AuthenticationError):
            client.login()
