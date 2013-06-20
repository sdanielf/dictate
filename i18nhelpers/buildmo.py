#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

import sys
import os

podir = sys.argv[1]
localedir = sys.argv[2]
module = sys.argv[3]

for path, names, filenames in os.walk(podir):
    for f in filenames:
        if f.endswith('.po'):
            lang = f[:-3]
            src = os.path.join(path, f)
            dest_path = os.path.join(localedir, lang, 'LC_MESSAGES')
            dest = os.path.join(dest_path, '.'.join([module, 'mo']))
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            if not os.path.exists(dest):
                print 'Building %s at %s' % (src, dest)
                os.system('msgfmt %s -o %s' % (src, dest))
            else:
                src_mtime = os.stat(src)[8]
                dest_mtime = os.stat(dest)[8]
                if src_mtime > dest_mtime:
                    print 'Building %s at %s' % (src, dest)
                    os.system('msgfmt %s -o %s' % (src, dest))
