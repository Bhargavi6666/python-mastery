import csv

# fmtparams = ''
csvfile = ('./_data/test.csv')
# csv.reader(csvfile, dialect='excel', **fmtparams)

# with open('./_data/eggs.csv') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# csv.writer('./_data/eggs.csv', dialect='excel', **fmtparams)

# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['It\'s more spaaaam!'])
#     spamwriter.writerow(['Spam', 'Spam', 'Wonderful Spam'])

# csv.register_dialect(name, dialect, **fmtparams)
# csv.unregister_dialect(name)
# csv.get_dialect(name)
# csv.list_dialects()
# csv.field_size_limit([new_limit])
# csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwargs)

# DictWriter usage example
with open('./_data/test.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Joe', 'last_name': 'Slick'})
    writer.writerow({'first_name': 'Jack', 'last_name': 'Silver'})

# DictReader example
with open('./_data/test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

# Classes
# csv.Dialect()
# csv.excel()
# csv.excel_tab()
# csv.unix_dialect()

# Determine the dialect of a CSV file
# sniffer = csv.Sniffer()
# sniffer.sniff(csvfile, delimiters=None)
# sniffer.has_header(csvfile)
