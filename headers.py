#!python
# -*- coding: utf-8 -*-

from sys import version
from os import path
from time import time

__author__ = "Pietro Foroni"
__copyright__ = "Copyright 2022"
__credits__ = ["Pietro Foroni", "Guido van Rossum"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Pietro Foroni"
__email__ = "19039@studenti.marconiverona.edu.it"
__status__ = "Development"

boold = False    # True in debug (development) mode. False in production
programname = path.basename(__file__)
filename = programname


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Accept": "text/html,text/csv",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close"}
