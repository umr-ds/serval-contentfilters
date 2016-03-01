#!/usr/bin/env python
import sys

with open(sys.argv[1]) as file:
    for line in file:
        if "hello" in line: sys.exit(0)

sys.exit(1)
