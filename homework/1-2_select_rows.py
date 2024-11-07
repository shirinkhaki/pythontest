"""
    homework 1.2 select_rows.py --write CSV rows with selected rows based on value

    Author: Shirin Khaki
    Last Revised:   10/14/2024
"""


import argparse
import os
import sys
import csv

parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                 description='writes selected rows based on value from source csv to target csv file')

parser.add_argument('--source', required=True)
parser.add_argument('--target', required=True)
parser.add_argument('--column', required=True)
parser.add_argument('--value', required=True)

args = parser.parse_args()


fh = open(args.source)
wfh = open(args.target, 'w', newline='')

reader = csv.reader(fh)
writer = csv.writer(wfh)

header = next(reader)
writer.writerow(header)

header_index = header.index(args.column)

for row in reader:
    if row[header_index] == args.value:
        writer.writerow(row)

fh.close()
wfh.close()