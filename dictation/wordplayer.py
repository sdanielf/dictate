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
import time

FNULL = open(os.devnull, 'w')


class WordPlayer():
    def __init__(self, args, checker=lambda w: None):
        self.paused = False
        self.text = args[1]
        self.args = args[2:] if len(args) > 2 else []
        self.current_word = ''
        self.checker = checker

        for word in self.text.split():
            while self.paused:
                check = self.checker()
                if check is not None:
                    check(self)
                    self.paused = not self.paused
            self.current_word = word
            print word
            self.speak(word)
            end_time = time.time() + len(word) / 2
            while time.time() < end_time:
                check = self.checker()
                if check is not None:
                    check(self)

    def print_all(self):
        print ' '.join(self.played_words)

    def speak(self, word):
        def wait_for_process(process):
            while process.poll() is None:
                check = self.checker()
                if check is not None:
                    check(self)

        espeak = subprocess.Popen(['espeak', word, '-s', '80',
                                   '--punct', '-w',
                                   '/tmp/dictation.wav'] + self.args,
                                  stdout=FNULL, stderr=FNULL)
        wait_for_process(espeak)
        gstreamer = subprocess.Popen(['gst-launch-1.0', 'playbin',
                                      'uri=file:///tmp/dictation.wav'],
                                     stdout=FNULL, stderr=FNULL)
        wait_for_process(gstreamer)
