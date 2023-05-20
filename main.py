#!/usr/bin/env python3

import sys
from commands.deletexml import deleteXmlFiles

args = sys.argv

if len(args) < 2:
    print("Please pass a command")
    exit(1)

command = args[1]

match command:
    case 'delete-xml':
        deleteXmlFiles(args)
                    
    case _:
        print("Unknown command")
        exit(1)
