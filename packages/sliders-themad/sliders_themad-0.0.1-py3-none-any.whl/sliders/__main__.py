import os
import sys
import argparse

# Argparse

parser = argparse.ArgumentParser(prog='sliders', description='Python IDE for non-GUI users')
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

# Initialization

if args.verbose == True:
    print("Initializing IDE...")

from .cmd import CmdParser
from .settings import Config

config = Config()
cmdP = CmdParser(config)

cmd = ""
while cmd != "exit":
    try:
        cmd = input(config.settings["cmdline"])
        args = cmd.split(" ")
        config = cmdP.parse(cmd, args)
    except KeyboardInterrupt:
        print("\n\nExiting...")
        cmd = "exit"
