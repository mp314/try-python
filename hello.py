#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""helloworld level snippets."""

import requests

def main():
    ''' Print HELLO WORLD and other stuff '''
    msg = "Hello World"
    print(msg)
    msg = msg.capitalize()

    # HTTP GET
    print(requests.__version__)
    resp = requests.get("https://sixty-north.com/c/t.txt")
    print(resp.text)

    print("Done.")


if __name__ == "__main__":
    # running as script, this is the main() for this package
    main()
    