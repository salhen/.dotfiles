#!/usr/bin/env python3
import i3ipc
import argparse
import os
import code

parser=argparse.ArgumentParser()
parser.add_argument('-w', help = 'Switch [string] workspace.')
parser.add_argument('-c', help = 'Look for such a window.')
parser.add_argument('-i', help = 'Look for such a window.')
parser.add_argument('-x', help = 'Execute this command if [WM_CLASS] is not found')
args = parser.parse_args()

if args.w is None:
  os.system('notify-send "You need to provide a workspace using the -w option."')
  exit(1)

i3 = i3ipc.Connection()

i3.command('workspace ' + args.w)

if args.c is None or args.x is None:
  exit(0)

tree = i3.get_tree()
found = False

for instance in tree.find_classed(args.c):
  if instance.workspace().name == args.w:
    if not args.i or args.i == instance.window_instance:
      found = True
      break

if found is False:
  os.system(args.x + " &")

subprocess.call('i3-msg "workspace back_and_forth"', shell=True)
