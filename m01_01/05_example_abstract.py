from abc import ABCMeta, abstractmethod


class StreamABC(metaclass=ABCMeta):
    @abstractmethod
    def read(self, max_buffer=100):
        pass

    @abstractmethod
    def write(self, data, encoding):
        pass


class SocketStream(StreamABC):
    def read(self, max_buffer=100):
        print('read from socket')

    def write(self, data, encoding):
        print('write to socket')

    def init_socket(self):
        pass


class HTTPStream(StreamABC):
    def read(self, max_buffer=100):
        print('read from http')

    def write(self, data, encoding):
        print('write to http')

    def init_http_protocol(self):
        pass


sk = SocketStream()
nt = HTTPStream()


def serialize(stream: StreamABC):
    if not isinstance(stream, StreamABC):
        raise TypeError('Is not stream!')
    return stream


serialize(sk)
serialize(nt)
# serialize('Hello world!')
