def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="{0}", name="{1}", value2="{2}"'.format(value, name, value2))


if __name__ == '__main__':
    unicode_test('A')

    unicode_test('$')

    unicode_test('\u00a2')

    unicode_test('\u2603')

    unicode_test('\u00e9')

    place = 'caf\u00e9'
    print(place)
    place = '\N{LATIN SMALL LETTER E WITH ACUTE}'
    print(place)

    u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'

    drink = 'Gew' + u_umlaut + 'rztraminer'
    print('Now I can finally have my', drink, 'in a', place)

    print(len('$'))
    print(len('\U0001f47b'))
