import csv


villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Klebb', 'last': 'Rosa'},
    {'first': 'Big', 'last': 'Mister'},
    {'first': 'Goldfinger', 'last': 'Auric'},
    {'first': 'Blofeld', 'last': 'Ernst'}
]

with open('villainsWithHeader', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

with open('villainsWithHeader', 'rt') as fin:
    cin = csv.DictReader(fin)
    villainsForPrint = [row for row in cin]

print(villainsForPrint)
