#!/usr/bin/python
# Author: Gines Sanchez
# Email: gsccordoba@gmail.com
# Github: Gsanch

import sys
import json
def parseLine(template, line):
    new_CSV_line=""
    for fields in template:
        try:
            new_CSV_line = new_CSV_line + line[template[fields][0]:template[fields][1]] + ","
        except IndexError:
            new_CSV_line = new_CSV_line + line[template[fields][0]:template[fields][0]] + ","
        except:
            print("Error reading field " + fields)
            print("Line length is " + str(len(line)))
    new_CSV_line = new_CSV_line[:-1]
    new_CSV_line = new_CSV_line + '\n'
    return new_CSV_line

print ("ASCII DATASET TO CSV GENERATOR")
if len(sys.argv) < 3:
    print ("Usage: ascii2CSV.py template origin destination")
    exit()
else:
    print ("Starting conversion from template: " + sys.argv[1])
    with open(sys.argv[1], "r") as template_file:
         template_data = json.load(template_file)

header_line = ""
for header in template_data:
    header_line = header_line + header + ","
header_line = header_line[:-1]
print ("Using the following headers: " + header_line)

with open(sys.argv[2]) as origin:
    print ("Reading origin file: " + sys.argv[2])
    with open(sys.argv[3], "w") as destination:
        destination.write(header_line)
        destination.write('\n')
        print ("Writing in file: " + sys.argv[3])
        for line in origin:
            destination.write(parseLine(template_data, line))
print("Conversion is OK.")
