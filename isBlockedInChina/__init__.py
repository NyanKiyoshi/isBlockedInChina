try:
    import httplib
except ImportError:
    import http.client as httplib

from urllib import urlencode
from lxml.html import fromstring


class NoResultsFound(Exception):
    pass


class IsBlockedInChina(object):
    DOMAIN_NAME = 'www.blockedinchina.net'
    TIMEOUT = 25
    RESULT_EXPR = '//div[@id="results"]//table'

    # the table from the blockedinchina.net's response is pretty ugly, to avoid a row containing a text "tweet"
    # or anything, we remove the last row
    GET_FROM_TABLE_FROM = -1

    def __init__(self):
        self.connection = httplib.HTTPConnection(self.DOMAIN_NAME, timeout=self.TIMEOUT)
        self._document = None
        self.results = None

    def test(self, url):
        self.connection.request('GET', '/?' + urlencode({'siteurl': url}))
        response = self.connection.getresponse()
        if response.status != 200:
            raise Exception
        self._document = fromstring(response.read())
        self.connection.close()
        self._parse()
        return self.results

    def _parse(self):
        table = self._document.xpath(self.RESULT_EXPR)
        try:
            rows = table[0].findall('tr')
        except IndexError:
            raise NoResultsFound
        self.results = [
            [children.text_content() for children in row.getchildren()] for row in rows[:self.GET_FROM_TABLE_FROM]
        ]

    def get_results(self):
        return self.results

if __name__ == '__main__':
    from sys import version_info
    from pprint import pprint
    _input = [input, raw_input][version_info.major == 2]
    is_blocked = IsBlockedInChina()
    pprint(is_blocked.test(_input('Domain: ')))
