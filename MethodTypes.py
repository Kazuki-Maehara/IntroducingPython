class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


if __name__ == "__main__":
    easy_a = A()
    breezy_a = A()
    wheezy_a = A()
    A.kids()

    A.count = 100
    print(A.count)
