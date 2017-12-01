#!/usr/bin/env python
import socket as z
import sys

s = None

for r in z.getaddrinfo(None, int(sys.argv[1]), z.AF_UNSPEC, z.SOCK_DGRAM, 0, z.AI_PASSIVE):
	af, socktype, proto, canonname, sa = r

	try:
		s = z.socket(af, socktype, proto)
	except OSError as msg:
		s = None
		continue

	try:
		s.bind(sa)
	except OSError as msg:
		s.close()
		s = None
		continue

	break

if s is None:
	print('Could Not Open Socket')
	sys.exit(1)

while True:
	(data, addr) = s.recvfrom(1024)

	if not data:
		break

	s.sendto(data, addr)
