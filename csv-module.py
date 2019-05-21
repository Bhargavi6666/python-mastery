import csv

fmtparams = ''
csvfile = ('./_data/test.csv')
# csv.reader(csvfile, dialect='excel', **fmtparams)

with open('./_data/eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

csv.writer('./_data/eggs.csv', dialect='excel', **fmtparams)

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['It\'s more spaaaam!'])
    spamwriter.writerow(['Spam', 'Spam', 'Wonderful Spam'])

# csv.register_dialect(name, dialect, **fmtparams)
# csv.unregister_dialect(name)
# csv.get_dialect(name)
# csv.list_dialects()
# csv.field_size_limit([new_limit])
# csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwargs)