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
from socket import getaddrinfo, socket, AF_UNSPEC, SOCK_STREAM, AI_PASSIVE
from sys import argv, exit

if len(argv) != 2:
    print('err: needs one argument')
    print('usage: {} port'.format(argv[0]))
    exit(1)

s = None

for r in getaddrinfo(None, int(argv[1]), AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):
    af, socktype, proto, canonname, sockaddr = r

    try:
        s = socket(af, socktype, proto)
    except:
        s = None
        continue
	
    try:
        s.bind(sockaddr)
        s.listen(1)
    except:
        s.close()
        s = None
        continue
	
    break

if s is None:
    print('err: failed to listen on port {}'.format(argv[1]))
    exit(1)

while True:
    conn, addr = s.accept()

    try:
        ip, port = addr
    except ValueError:
        ip, port, flow, scope = addr

    print('new connection from {} on port {}'.format(ip, port))

    while True:
        data = conn.recv(1024)

        if not data:
            break

        print('recieved "{}" from client'.format(str(data)))
        conn.send(data)

    print('connection from {} has been closed'.format(ip))
    conn.close()
