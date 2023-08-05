#!/usr/bin/env python3
"""
The is the command-line interface to **yace**.

TODO
====

* Discover 'adhoc' targets, e.g. targets available in the
  current-workding-directory
* Discover targets via packages under the namespace 'yace.targets.{NAME}`

"""
import argparse
import logging as log
import sys
from pathlib import Path

from yace import __version__ as version
from yace.compiler import Compiler
from yace.parser import c_to_yace
from yace.idl.formater import do_format


def parse_args():
    """Parse command-line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filepath",
        nargs="+",
        type=Path,
        help="Path to Yace File or C Header",
    )
    parser.add_argument(
        "--target",
        nargs="+",
        choices=[target.NAME for target in Compiler.TARGETS],
        default=[target.NAME for target in Compiler.TARGETS][0],
        help="Targets",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Path to output directory, for emitted code / artifacts",
    )
    parser.add_argument(
        "--log-level",
        "-l",
        action="append_const",
        const=1,
        default=[],
        help="Increase log-level.",
    )

    parser.add_argument(
        "--c-to-yace",
        action="store_true",
        help="Treat filepath as C Header and use it to emit a Yace-file, then exit",
    )
    parser.add_argument(
        "--lint",
        action="store_true",
        help="Parse and check the given Yace-files, then exit",
    )
    parser.add_argument(
        "--format",
        action="store_true",
        help="Format the given Yace-file, then exit",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version}",
    )

    return parser.parse_args()


def main():
    """Emit enums, structs, and pretty-printer functions for them"""

    ok = False
    try:
        args = parse_args()
        args.filepath = [filepath.resolve() for filepath in args.filepath]

        levels = [log.ERROR, log.INFO, log.DEBUG]
        log.basicConfig(
            format="%(levelname)s:%(module)s:%(funcName)s(): %(message)s",
            level=levels[min(sum(args.log_level), len(levels) - 1)],
        )

        if args.format:  # Yace-file formater
            return sys.exit(do_format(args.filepath))

        if args.c_to_yace:  # C to Yace-file Compiler
            return sys.exit(c_to_yace(args.filepath, args.output))

        yace = Compiler(
            args.target, args.output
        )  # Yace-file linter and/or Yace-file Compiler
        ok = all(
            [
                yace.process(path, ["parse", "lint"] if args.lint else Compiler.STAGES)
                for path in args.filepath
            ]
        )
    except Exception as exc:
        log.error("Unhandled Exception: message(%s)", exc)
        log.error("Unhandled Exception: increase log-level (-ll) for trace")
        log.error("Unhandled Exception(%s)", exc, exc_info=True)

    return sys.exit(0 if ok else 1)
