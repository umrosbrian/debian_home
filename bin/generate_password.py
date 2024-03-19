#!/usr/bin/env python3
 
"""Provide the number of characters as an argument.  This idea was lifted from https://docs.python.org/3/library/secrets.html#recipes-and-best-practices."""

import secrets
import string
import sys

length = int(sys.argv[1])
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
print(f"{''.join(secrets.choice(alphabet) for i in range(length))}")
