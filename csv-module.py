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

# # DictWriter usage example
# with open('./_data/test.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'John', 'last_name': 'Smith'})
#     writer.writerow({'first_name': 'Joe', 'last_name': 'Slick'})
#     writer.writerow({'first_name': 'Jack', 'last_name': 'Silver'})

# # DictReader example
# with open('./_data/test.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# Classes
# csv.Dialect()
# csv.excel()
# csv.excel_tab()
# csv.unix_dialect()

# Determine the dialect of a CSV file
# sniffer = csv.Sniffer()
# sniffer.sniff(csvfile, delimiters=None)
# sniffer.has_header(csvfile)

# print(csv.Dialect.escapechar)
# print(csv.Dialect.doublequote)
# print(csv.Dialect.delimiter)
# print(csv.Dialect.escapechar)

# DIALECT OBJECTS (Subclass of Dialect Class)
# sniffer = csv.Sniffer()
# dialect = sniffer.sniff(csvfile)
# print(dialect)
# print('delimiter:', dialect.delimiter)
# print('doublequote:', dialect.doublequote)
# print('escapechar:', dialect.escapechar)
# print('lineterminator:', ascii(dialect.lineterminator))
# print('quotechar:', dialect.quotechar)
# print('skipinitialspace:', dialect.skipinitialspace)
# print('mro:', dialect.mro())

# # READER OBJECTS
# with open(csvfile, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     print(reader.__next__())
#     print(reader.__next__())
#     print(reader.__next__())
#     print(reader.dialect)
#     print(reader.line_num)
#     print(reader.fieldnames)

# # CONSTANTS
# print(csv.QUOTE_ALL) # Wrap all fields in quotes
# print(csv.QUOTE_MINIMAL) # Only wrap fields in quotes if they require it
# print(csv.QUOTE_NONNUMERIC) # Quote all non-numeric fields.
# print(csv.QUOTE_NONE) # Never Quote fields.
# print(csv.Error)

# Writing a file with csv.writer method
with open('./_data/test2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Field 1', 'Field 2'])
    writer.writerow(['Value 1', 'Value 2'])


# Writing a file with csv.DictWriter
with open('./_data/test3.csv', 'w', newline='') as csvfile:
    fieldnames = ['Field 1', 'Field 2', 'Field 3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Field 1': 'Value 1'})
    writer.writerow({'Field 1': 'Value 1', 'Field 2': 'Value 2'})

    rows = [
        {'Field 1': 'Value 1', 'Field 2': 'Value 2', 'Field 3': 'Value 3'},
        {'Field 1': 'Value 1', 'Field 2': 'Value 2', 'Field 3': 'Value 3'},
        {'Field 1': 'Value 1', 'Field 2': 'Value 2', 'Field 3': 'Value 3'},
        {'Field 1': 2.00, 'Field 2': 1/2, 'Field 3': 2000},
    ]

    writer.writerows(rows)
    print(writer)

# Reading a file with csv.DictReader
with open('./_data/test3.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.line_num)
    print(reader.fieldnames)
    while (True):
        try:
            print(reader.__next__())
        except StopIteration:
            break
    print(reader.dialect)

# Short writer example (takes a list of lists, if passed a list of dicts, will write the keys as the values.)
with open('./_data/test4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read an alternate format
with open('./_data/test4.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

# REGISTERING A NEW DIALECT
with open('./_data/passwd', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=':')
    writer.writerows([
        ['username', 'password'],
        ['user1', 'raspberry'],
        ['user2', 'football']
    ])


csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('./_data/passwd', newline='') as file:
    reader = csv.reader(file, 'unixpwd')
    for row in reader:
        print(row)

# READING WITH ERROR HANDLING
import sys
filename = './_data/test.csv'
with open(filename, newline='') as file:
    reader = csv.reader(file)
    try:
        for row in reader:
            print(row)
    except csv.Error as err:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, err))

for attr in dir(csv):
    print(attr)


print(csv.excel)
print(csv.excel_tab)
print(csv.field_size_limit())
print(csv.list_dialects())