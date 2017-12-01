#!/usr/bin/env python
import requests as r
import sys

print(r.get(sys.argv[1]).text)
