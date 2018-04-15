#!/usr/bin/env python
#
# Copyright (C) 2018 The GrayHats Cybersecurity Club
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
from socket import getaddrinfo, socket, AF_UNSPEC, SOCK_STREAM
from sys import argv, exit

if len(argv) != 3:
    print('err: needs two arguments')
    print('usage: {} host port'.format(argv[0]))
    exit(1)

s = None

for r in getaddrinfo(argv[1], int(argv[2]), AF_UNSPEC, SOCK_STREAM):
    af, socktype, proto, canonname, sockaddr = r

    try:
        s = socket(af, socktype, proto)
    except:
        s = None
        continue

    try:
        s.connect(sockaddr)
    except:
        s.close()
        s = None
        continue

    break

if s is None:
    print('err: failed to connect to {} on port {}'.format(argv[1], argv[2]))
    exit(1)

s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('received "{}" back from server'.format(data.decode("utf-8")))
