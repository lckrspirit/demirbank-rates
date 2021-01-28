#!/bin/python3

import requests
import urllib3
import argparse

from bs4 import BeautifulSoup

url = "https://demirbank.kg/en-us"
temp = '/tmp'
arg = argparse.ArgumentParser()

def get_page():
    with open(f"{temp}/rate.html", "wb") as page:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page.write(requests.get(url, verify=False).content)


def rates_parse(val):
    with open(f"{temp}/rate.html", "rb") as html:
        soap = BeautifulSoup(html, 'html.parser', from_encoding="iso-8859-1")
        result = soap.findAll('td')
        if val == 'BUY':
            print(float(result[18].get_text()))
        elif val == 'SELL':
            print(float(result[19].get_text()))


if __name__ == '__main__':
    arg.add_argument('-b', '--buy', action='store_const', const='BUY')
    arg.add_argument('-s', '--sell', action='store_const', const='SELL')
    get_page()
    if arg.parse_args().buy is not None:
        rates_parse(arg.parse_args().buy)
    elif arg.parse_args().sell is not None:
        rates_parse(arg.parse_args().sell)
    else:
        pass
