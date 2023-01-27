#!python
# -*- coding: utf-8 -*-

from sys import version
from os import path
from time import time
import requests
import csv
import json
import yaml
from headers import HEADERS

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


def csv_to_dict(filename="PIRC.csv"):
    """Convert the contents of a CSV file into a Python dictionary

    Args:
        filename (str, optional): CSV file name. Defaults to "PIRC.csv".

    Returns:
        data: Python dictionary
    """
    data = {}

    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for i, row in enumerate(csv_reader):
            data[i+1] = row
    
    return data


def dict_to_yaml(dict, filename="output.yaml"):
    """Convert a Python dictionary to a YAML file

    Args:
        dict (dict): Dictionary to convert
        filename (str, optional): Output file name. Defaults to "output.yaml".
    """
    with open(filename, "w") as file:
        yaml.dump(dict, file, default_flow_style=False)


def dict_to_json(dict, filename="output.json"):
    """Convert a Python dictionary to a JSON file

    Args:
        dict (dict): Dictionary to convert
        filename (str, optional): Output file name. Defaults to "output.json".
    """
    with open(filename, "w") as file:
        json.dump(dict, file, indent=4)


def main():
    """

    :return:
    """
    if boold:
        print("Main")

    url = "https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true"
    r = requests.get(url, headers=HEADERS)

    open("PIRC.csv", "wb").write(r.content)

    csv_dict = csv_to_dict("PIRC.csv")

    print("CSV to Dictionary")
    print(csv_dict)

    print("\nTranslation and creation of YAML file...")
    dict_to_yaml(csv_dict)
    print("Dictionary converted and saved in YAML file")

    print("\nTranslation and creation of JSON file...")
    dict_to_json(csv_dict)
    print("Dictionary converted and saved in JSON file")


if __name__ == '__main__':
    if boold:
        msg = "".join(["Execution ", programname, " with Python ", version])
        print(msg)
        msg = "".join(["Author: ", __author__, " Version: ", __version__])
        print(msg)

    t1 = time()
    main()
    t2 = time()

    if boold:
        msg = "".join(["Executed in ", str(t2 - t1), " seconds"])
        print(msg)
