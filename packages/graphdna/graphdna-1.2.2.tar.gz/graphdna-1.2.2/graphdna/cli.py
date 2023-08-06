"""Managing the CLI flow."""

import argparse
import sys
from typing import List, Optional

from graphdna.dna import detect_engine


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse the arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-u',
        '--url',
        dest='url',
        type=str,
        help='The URL of the GraphQL endpoint.',
    )
    parser.add_argument(
        '-H',
        '--header',
        metavar='<header>',
        dest='headers',
        action='append',
        default=[],
    )

    return parser.parse_args(args)


def validate_args(args: argparse.Namespace) -> None:
    """Validate arguments namespace.

    Throw:
        ValueError: If the arguments are invalid.
    """

    if not args.url:
        raise ValueError('The URL is required.')


def cli(argv: Optional[List[str]] = None) -> None:
    """CLI entry point."""

    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)
    validate_args(args)

    headers = {}
    for h in args.headers:
        key, value = h.split(': ', 1)
        headers[key] = value

    detect_engine(args.url, headers=headers)
