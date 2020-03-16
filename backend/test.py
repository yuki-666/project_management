# coding: utf-8
import requests
import json
import numpy as np
import pandas as pd
import os

base_url = 'http://127.0.0.1:7777'
route = '/homepage/search'

if __name__ == "__main__":
    url = base_url + route

    # post
    d = {'id': '-1', 'name': '1'}
    r = requests.post(url, data=d)

    # get
    # r = requests.get(url + '?page=0&&size=10')

    print(r.content)
    print(r.text)
