import csv
file = open('number19.csv', 'r', newline='')
reader = csv.DictReader(file, delimiter=',')
next(reader)
writefile = open('number19_python_diagram_adaption.csv', 'w', newline='')
writer = csv.DictWriter(writefile, fieldnames=['date', 'type', 'value'])
writer.writeheader()
for row in reader:
    writer.writerow({'date': row['<DATE>'], 'type': 'open', 'value': row['<OPEN>']})
    writer.writerow({'date': row['<DATE>'], 'type': 'high', 'value': row['<HIGH>']})
    writer.writerow({'date': row['<DATE>'], 'type': 'low', 'value': row['<LOW>']})
    writer.writerow({'date': row['<DATE>'], 'type': 'close', 'value': row['<CLOSE>']})