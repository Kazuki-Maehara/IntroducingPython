n = 42
f = 7.03
s = 'string cheese'

print('{} {} {}'.format(n, f, s))

print('{2} {0} {1}'.format(n, f, s))

print('{s} {f} {n}'.format(n=n, f=f, s=s))

d = dict(n=n, f=f, s=s)

print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))

print('{0:d} {1:f} {2:s}'.format(n, f, s))

print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))

print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

print('{0:!^20s}'.format('BIG SLE'))
