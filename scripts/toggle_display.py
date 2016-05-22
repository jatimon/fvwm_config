#!/usr/bin/env python

LAPTOP = 'eDP1'
CMD = 'xrandr'
OFF = 'off'

import subprocess
import re

def get_display():
    pattern = re.compile('^(\S+) connected (.*)\(')   
    displays = subprocess.check_output([CMD], stderr=subprocess.STDOUT)
    for line in displays.splitlines():
        display = pattern.match(line)
        if display:
            do_toggle(display)

def do_toggle(display):
    output, mode = display.groups()
    print('Toggling Display: {}'.format(output))
    if mode:
        print('Setting mode to: {}'.format(mode))
        set_xrandr(output, mode)
    else:
        print('Disabling display on: {}'.format(output))
        set_xrandr(output, OFF)

def set_xrandr(o, m):
    if m == OFF:
        mode = ['--off']
    else:
        mode = ['--mode', m]
    result = subprocess.check_output(
        [CMD, '--output', o] + mode, stderr=subprocess.STDOUT
    )
    print(result)

get_display()
