#!/usr/bin/env python
import socket as z
import sys
s = None

for r in z.getaddrinfo(sys.argv[1], int(sys.argv[2]), z.AF_UNSPEC, z.SOCK_STREAM):
    af, socktype, proto, canonname, sa = r

    try:
        s = z.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue

    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue

    break

if s is None:
    print('could not open socket')
    sys.exit(1)

s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
