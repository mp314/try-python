#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command line args with Click.

See:
- https://click.palletsprojects.com/

Usage:
    python3 try-cli.py --help
    python3 try-cli.py --count 3 Nimi
"""

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello() # pylint: disable=no-value-for-parameter
