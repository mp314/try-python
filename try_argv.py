#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command line args.

Usage:
    python3 try-argv.py
"""

import sys

def main():
    '''Print number of command line arguments + list arguments'''
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    print("Done.")

if __name__ == "__main__":
    main()
