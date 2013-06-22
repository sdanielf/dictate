#!/bin/bash
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

PYFILES="dictate dictation/*.py"

# Generate main pot
xgettext --language=Python --keyword=_ --output=po/dictation.pot \
    --copyright-holder="Daniel Francis" --package-name="Dictate" \
    --package-version=0.2 --msgid-bugs-address="francis@sugarlabs.org" \
    $PYFILES "`i18nhelpers/getmodulepath.py argparse`"
sed -i 's/SOME DESCRIPTIVE TITLE/Dictate Translations/g' po/dictation.pot
sed -i 's/PACKAGE/Dictate/g' po/dictation.pot
sed -i 's/(C) YEAR/(C) 2013/g' po/dictation.pot
sed -i 's/CHARSET/UTF-8/g' po/dictation.pot

# Generate Sphinx pot
sphinx-build -b gettext doc doc/gettext

# Merge main po files
for file in po/*.po; do
    msgmerge $file po/dictation.pot -o $file
done

# Merge Sphinx po files
for file in doc/gettext/*.po; do
    msgmerge $file doc/gettext/index.pot -o $file
done
