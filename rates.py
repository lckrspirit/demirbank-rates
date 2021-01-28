#!/bin/python3

import requests
import urllib3

from bs4 import BeautifulSoup

url = "https://demirbank.kg/en-us"
temp = '/tmp/'

def get_page():
    with open(f"{temp}/rate.html", "wb") as page:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page.write(requests.get(url, verify=False).content)
    return True

def rates_parse():
    with open(f"{temp}/rate.html", "rb") as html:
        soap = BeautifulSoup(html, 'html.parser', from_encoding="iso-8859-1")
        result = soap.findAll('td')
        print(result[18].get_text(), result[19].get_text())


if __name__ == '__main__':
    if get_page():
        rates_parse()
