#!/usr/bin/env python3
# Begin /usr/bin/lsb_release

import sys
if sys.version_info < (3, 7):
  sys.exit("Python %s.%s or later is required.\n" %(3, 7))

import argparse, glob, itertools, lsbtools, os, re

# Set default values
config = {
  'LSB_VERSION'         : 'unavailable',
  'DISTRIB_ID'          : 'unavailable',
  'DISTRIB_DESCRIPTION' : 'unavailable',
  'DISTRIB_RELEASE'     : 'unavailable',
  'DISTRIB_CODENAME'    : 'unavailable',
}
printval = ''

# Process command line argurments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="Display the version of the LSB specification against which the distribution is compliant.", action="store_true")
parser.add_argument("-i", "--id", help="Display the string id of the distributor.", action="store_true")
parser.add_argument("-d", "--description", help="Display the single line text description of the distribution.", action="store_true")
parser.add_argument("-r", "--release", help="Display the release number of the distribution.", action="store_true")
parser.add_argument("-c", "--codename", help="Display the codename according to the distribution release.", action="store_true")
parser.add_argument("-a", "--all", help="Display all of the above information.", action="store_true")
parser.add_argument("-s", "--short", help="Display all of the above information in short output format.", action="store_true")
args = parser.parse_args()

if args.version:
  lv = 1
else:
  lv = 0

if args.id:
  li = 1
else:
  li =0

if args.description:
  ld = 1
else:
  ld = 0

if args.release:
  lr = 1
else:
  lr = 0

if args.codename:
  lc = 1
else:
  lc = 0

if args.all:
  lv = 1
  li = 1
  ld = 1
  lr = 1
  lc = 1

if args.short:
  ls = 1
else:
  ls = 0

if lv == 0 and li == 0 and ld == 0 and lr == 0 and lc == 0:
  lv = 1

# Read required configuration file
if not os.path.exists("/etc/lsb-release"):
  print("Required configuration file '/etc/lsb-relase' is not found. Exiting...", file=sys.stderr)
  sys.exit(1)

file = open("/etc/lsb-release", 'r')
content = file.read()
items = content.split('\n')
for pair in items:
  if pair != '':
    key,val = pair.split('=')
    config[key] = val.strip('\"')
file.close()

if lv == 1:
  if ls == 1:
    printval = printval + " " + config['LSB_VERSION']
  else:
    print("LSB Version:   ", config['LSB_VERSION'])

if li == 1:
  if ls == 1:
    printval = printval + " " + config['DISTRIB_ID']
  else:
    print("Distributor ID:", config['DISTRIB_ID'])

if ld == 1:
  if ls == 1:
    printval = printval + " " + config['DISTRIB_DESCRIPTION']
  else:
    print("Description:   ", config['DISTRIB_DESCRIPTION'])

if lr == 1:
  if ls == 1:
    printval = printval + " " + config['DISTRIB_RELEASE']
  else:
    print("Release:       ", config['DISTRIB_RELEASE'])

if lc == 1:
  if ls == 1:
    printval = printval + " " + config['DISTRIB_CODENAME']
  else:
    print("Codename:      ", config['DISTRIB_CODENAME'])

if ls == 1:
  print(printval.strip(" "))

