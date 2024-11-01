"""
    homework 1.1 select_columns.py --write CSV rows with selected columns

    Author: Shirin Khaki
    Last Revised:   10/14/2024
"""

import argparse
import os
import sys
import csv

parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                 description='writes selected columns from source csv to target csv file')

parser.add_argument('--source', required=True)
parser.add_argument('--target', required=True)
parser.add_argument('--columns', required=True, nargs='+')

args = parser.parse_args()


fh = open(args.source)
wfh = open(args.target, 'w', newline='')

dreader = csv.DictReader(fh)
dwriter = csv.DictWriter(wfh, args.columns)

dwriter.writeheader()


for row in dreader:
    rowdict = {}
    for column in args.columns:
        rowdict[column] = row[column]
    dwriter.writerow(rowdict)

fh.close()
wfh.close()