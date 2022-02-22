#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""python module which can be run as a script too.

Usage:
import mypackage

mypackage.mymodule.print_helloworld("Foo Bar")
"""

def get_name() -> str:
    """Return 'a name'"""
    return "a name"

def print_helloworld(name: str):
    """Print a message for someone.

    :param name: who to hello.
    """
    print("hello", name)

def run():
    """Called when run as a script."""
    print_helloworld(get_name())
