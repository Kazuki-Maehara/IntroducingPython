import csv

villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']
]

with open('villains', 'wt') as fout:  # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)


with open('villains', 'rt') as fin:  # context manager
    cin = csv.reader(fin)
    villainsForPrint = [row for row in cin]  # This uses a list comprehension

print(villainsForPrint)

print('')

with open('villains', 'rt') as fin:  # context manager
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villainsForPrint = [row for row in cin]  # This uses a list comprehension

print(villains)
