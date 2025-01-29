#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import json
import sys
import io
import requests
from bs4 import BeautifulSoup
import sqlite3
from contextlib import closing
import datetime


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


cgitb.enable()
form=cgi.FieldStorage()
num1=form.getvalue("sent2")
num2=form.getvalue("sent3")
num_add=int(num1) + int(num2)

print("Content-type: text/html\n")

print(num_add)
