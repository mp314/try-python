#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command line args.

Usage:
    python3 try-argv.py
"""

import sys

def main():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    print(f"Done.")

if __name__ == "__main__":
    main()
