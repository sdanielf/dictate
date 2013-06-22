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
from gettext import gettext as _
import ConfigParser
from dictation.espeak import espeak_voices

configpath = os.path.join(os.environ['HOME'], '.dictate')
espeak_args = _('Options given to espeak. (See "espeak --help")')

settings = {'tbw': ('-t', '--tbw', 'TWB', None,
                    _('Time Between Words (Word length * TBW)'), '0.5'),
            'espeak_options': ('-e', '--espeak_options', 'ARGS', None,
                                espeak_args, ''),
            'language': ('-l', '--language', 'LANG', espeak_voices,
                         _('Language voice to speak'), 'default'),
            'speed': ('-s', '--speed', 'SPEED', None,
                      _('Speed in words per minute. From 80 to 450'), 80)}
options = {}

if not os.path.exists(configpath):
    config = ConfigParser.RawConfigParser()
    config.add_section('Dictation')
    for setting in settings:
        config.set('Dictation', setting, settings[setting][-1])
    configfile = open(configpath, 'w')
    config.write(configfile)
    configfile.close()

config = ConfigParser.RawConfigParser()
config.read(configpath)
for i in settings:
    try:
        options[i] = config.get('Dictation', i)
    except:
        options[i] = settings[i][-1]


def get_tbw():
    try:
        return float(options['tbw'])
    except:
        return float(settings['tbw'][-1])

def get_espeak_options():
    try:
        return options['espeak_options'].split()
    except:
        return settings['espeak_options'][-1].split()

def get_language():
    language = options['language']
    if language in espeak_voices:
        return language
    else:
        return settings['language'][-1]

def get_speed():
    try:
        speed = int(options['speed'])
        if speed >= 80 and speed <= 450:
            return options['speed']
        else:
            raise Exception
    except:
        return settings['speed'][-1]
