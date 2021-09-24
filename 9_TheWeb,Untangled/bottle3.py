from bottle import route, run


@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing


run(host='localhost', port=8000)
