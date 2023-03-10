import csv

readfile = open('SPFB.RTS-12.18_180901_181231.csv', 'r', newline='')
reader = csv.DictReader(readfile, delimiter=',')
fieldnames = next(reader).keys()
writefile = open('number19.csv', 'w', newline='')
writer = csv.DictWriter(writefile, fieldnames=fieldnames)
writer.writeheader()
for row in reader:
    if row['<DATE>'][:2] == '19':
        writer.writerow(row)