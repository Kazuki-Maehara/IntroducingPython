def dump(func):
    "Print input arguments and output valuw(s)"
    def wrapped(*args, **kwargs):
        print("Function name: %s" % func.__name__)
        print("input arguments: %s" % ' '.join(map(str, args)))
        print("Input keyword arguments %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return wrapped
