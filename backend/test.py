# coding: utf-8
import requests
import json
import numpy as np
import pandas as pd
import os

base_url = 'http://127.0.0.1:7777/api'

def test_login():
    route = '/homepage/login'
    url = base_url + route

    # post
    d = {'username': '卡桑', 'password': '000111'}
    r = requests.post(url, data=d)

    print(r.content)
    print(r.text)

def test_project():
    route = '/homepage/search'
    url = base_url + route

    # post
    d = {'keyword': '0'}
    r = requests.post(url, data=d)

    # get
    # r = requests.get(url + '?uid=0017')

    print(r.content)
    print(r.text)

if __name__ == "__main__":
    test_project()
