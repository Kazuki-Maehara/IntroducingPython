class Duck1():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


if __name__ == '__main__':
    fowl = Duck1('Howard')
    print(fowl.name)

    fowl.get_name()

    fowl.name = 'Daffy'
    print(fowl.name)

    fowl_2 = Duck2('Howard')
    print(fowl_2.name)

    fowl_2.name = 'Donald'
    print(fowl_2.name)
