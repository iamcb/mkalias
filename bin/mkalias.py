#!/usr/bin/env python3
import os

from mkalias import mkalias

mkalias.parse_args()

args = mkalias.parse_args()

source = os.path.abspath(args.source)
destination = os.path.abspath(args.destination)

mkalias.check_path(source, destination)

mkalias.create_alias(source, destination)

if args.alias_name:
    mkalias.rename_alias(source, destination, args.alias_name)
