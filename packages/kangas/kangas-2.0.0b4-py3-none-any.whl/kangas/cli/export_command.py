#!/usr/bin/env python
# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2022 Kangas Development Team      #
#    All rights reserved                             #
######################################################

import argparse
import sys

from .utils import Options

ADDITIONAL_ARGS = False


def get_parser_arguments(parser):
    parser.add_argument(
        "PATH",
        help=(
            "The source-specific path: workspace/project/exp, workspace/project, or workspace"
        ),
        type=str,
    )
    parser.add_argument(
        "NAME",
        help=("The name of the DataGrid to create"),
        type=str,
    )
    ## Add integrations here:
    parser.add_argument(
        "--comet",
        help="Use comet as the source",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--huggingface",
        help="Use huggingface as the source",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--options",
        metavar="KEY=VALUE",
        help="Pass the following KEY=VALUE pairs; for --huggingface: --options split=train streaming=True seed=42 samples=100 private=True push=False",
        nargs="+",
        default=[],
    )


def export_command(parsed_args, remaining=None):
    # Called via `kangas export ...`
    try:
        export_cli(parsed_args)
    except KeyboardInterrupt:
        print("Canceled by CONTROL+C")
    except Exception as exc:
        print("ERROR: " + str(exc))


def export_cli(parsed_args):
    # Include source-specific files here:
    from ..integrations.comet import export_from_comet
    from ..integrations.huggingface import export_from_huggingface

    options = Options(parsed_args.options)

    if parsed_args.comet:
        export_from_comet(path=parsed_args.PATH, name=parsed_args.NAME, options=options)
    elif parsed_args.huggingface:
        export_from_huggingface(
            path=parsed_args.PATH, name=parsed_args.NAME, options=options
        )
    else:
        raise Exception("You need to add a source: --comet OR --huggingface")


def main(args):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    get_parser_arguments(parser)
    parsed_args = parser.parse_args(args)
    export_command(parsed_args)


if __name__ == "__main__":
    # Called via `python -m kangas.cli.export_command ...`
    main(sys.argv[1:])
