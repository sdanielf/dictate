# Copyright (C) 2013 S. Daniel Francis <francis@sugarlabs.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import os
import subprocess
import re


def voices():
    out = {}
    result = subprocess.Popen(["espeak", "--voices"],
        stdout=subprocess.PIPE).communicate()[0]

    for line in result.split('\n'):
        m = re.match(r'\s*\d+\s+([\w-]+)\s+([MF])\s+([\w_-]+)\s+(.+)', line)
        if not m:
            continue
        language, gender, name, stuff = m.groups()
        if stuff.startswith('mb/'):  # or \
                #name in ('en-rhotic','english_rp','english_wmids'):
            # these voices don't produce sound
            continue
        out[language] = name

    return out

espeak_voices = voices()
FNULL = open(os.devnull, 'w')


def run_command(command, function=lambda: None):
    """Runs a command and runs a function until the command returns a value"""
    command = subprocess.Popen(command, stdout=FNULL, stderr=FNULL)
    while command.poll() is None:
        function()
    return command

def espeak(word, language, speed, args, checker):
    output_file = '/tmp/dictation.wav'
    run_command(['espeak', word, '-v', language, '-s', speed, '--punct', '-w',
                 output_file] + args, checker)
    run_command(['gst-launch-1.0', 'playbin', 'uri=file://%s' % output_file],
                checker)
