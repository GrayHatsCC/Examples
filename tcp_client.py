#!/usr/bin/env python
from socket import getaddrinfo, socket, AF_UNSPEC, SOCK_STREAM
from sys import argv, exit

if len(argv) < 3:
    print('err: too few args')
    print('usage: {} host port'.format(argv[0]))
    exit(1)

s = None

for r in getaddrinfo(argv[1], int(argv[2]), AF_UNSPEC, SOCK_STREAM):
    af, socktype, proto, canonname, sockaddr = r

    try:
        s = socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue

    try:
        s.connect(sockaddr)
    except OSError as msg:
        s.close()
        s = None
        continue

    break

if s is None:
    print('could not open socket')
    exit(1)

s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received {}'.format(repr(data)))
