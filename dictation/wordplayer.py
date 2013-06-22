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

import time

from dictation import config
from dictation import espeak


class WordPlayer():
    def __init__(self, text, console):
        self.paused = False
        self.text = text
        self.args = config.get_espeak_options()
        self.current_word = ''
        self.console = console
        self.tbw = config.get_tbw()
        self.language = config.get_language()
        self.speed = config.get_speed()

        for word in self.text.split():
            while self.paused:
                if self.check_keys():
                    self.paused = not self.paused
            self.current_word = word
            self.console.print_word(word)
            self.speak(word)
            end_time = time.time() + len(word) * self.tbw
            while time.time() < end_time:
                self.check_keys()

    def speak(self, word):
        espeak.espeak(word, self.language, self.speed, self.args,
                      self.check_keys)

    def check_keys(self):
        check = self.console.check_keys()
        if check is not None:
            check(self)
            return True
        return False
