import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)


class Tiny():
    def __str__(self):
        return 'tiny'


obj1 = Tiny()
print(type(obj1))

print(obj1)

pickled = pickle.dumps(obj1)
print(pickled)

obj2 = pickle.loads(pickled)
print(type(obj2))
print(obj2)
