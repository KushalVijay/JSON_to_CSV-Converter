import csv
import json

infile = open(filename.json,"r",encoding="utf8")


outfile = open(output_filename.csv,"w")

writer =  csv.writer(outfile)


for row in json.loads(infile.read()):
    writer.writerow(row)
