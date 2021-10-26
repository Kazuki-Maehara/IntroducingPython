from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('Client', str(data, 'utf-8'))
        if data.startswith(b'Knock knock'):
            response = b"Who's there?"
        else:
            response = data + b" who?"
        print('Server:', str(response, 'utf-8'))
        self.transport.write(response)


class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()


if __name__ == "__main__":
    reactor.listenTCP(8000, KnockFactory())
    reactor.run()
