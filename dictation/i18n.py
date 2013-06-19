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

import gettext
import sys
import os

LOCALE_DOMAIN = 'dictation'

moduledir = os.path.dirname(__file__)
if moduledir.startswith(sys.prefix):
    LOCALE_DIR = os.path.join(sys.prefix, 'share', 'locale')
else:
    LOCALE_DIR = os.path.join('/'.join(moduledir.split('/')[:-1]), 'locale')

gettext.bindtextdomain(LOCALE_DOMAIN, LOCALE_DIR)
gettext.textdomain(LOCALE_DOMAIN)
gettext.install(LOCALE_DOMAIN)
