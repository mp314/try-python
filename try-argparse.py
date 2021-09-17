#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do something with argparse.

See:
- https://realpython.com/command-line-interfaces-python-argparse/
- https://docs.python.org/3/library/argparse.html
"""

from os import environ
import sys
import argparse

def init_argparse() -> argparse.ArgumentParser:
    """Create an argument parser, print usage etc.
    """
    # Create the parser
    _parser = argparse.ArgumentParser(
        description = "Does something with command line arguments."
    )
    _parser.add_argument('Positional_arg_1',
        metavar = 'POSITIONAL_ARG_1',
        type = str,
        help = 'Documentation for mandatory argument')
    _parser.add_argument('-m',
        '--modifier',
        action = 'store_true',
        help = 'Documentation for optional argument without value')
    _parser.add_argument('-o',
        '--option',
        metavar = 'OPTIONAL_ARG_O',
        type = str,
        help = 'Documentation for optional argument with value')
    return _parser

def main():
    # parse command line
    parser = init_argparse()
    args = parser.parse_args()
    print(f"POSITIONAL_ARG_1 = '{args.Positional_arg_1}'")
    print(f"OPTIONAL_ARG_O = '{args.option}'")
    print(f"modifier = '{args.modifier}'")
    print(f"Done.")

if __name__ == '__main__':
    # execute only if run as a script
    main()
