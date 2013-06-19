from distutils.core import setup

from distutils.command.build import build
from distutils.core import Command

import os
srcdir = os.path.dirname(os.path.abspath(__file__))
docdir = os.path.join(srcdir, 'doc')
mandir = os.path.join(docdir, 'man')

class build_manpage(Command):
    description = 'Generate man page.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
            pass

    def run(self):
        os.system('sphinx-build -b man %s %s' % (docdir, mandir))
        if os.path.exists('%s/dictate.1.gz' % mandir):
            os.remove('%s/dictate.1.gz' % mandir)
        os.system('gzip %s/*.1' % mandir)

build.sub_commands.append(('build_manpage', None))

manfiles = [os.path.join(mandir, 'dictate.1.gz')]

setup(name='dictate',
      version='0.1',
      description='Command-line dictation utility.',
      author='Daniel Francis',
      author_email='francis@sugarlabs.org',
      license='GPLv3',
      url='https://github.com/sdanielf/dictate/',
      packages=['dictation'],
      scripts=['dictate'],
      data_files=[('/usr/share/man/man1/', manfiles)],
      cmdclass={'build_manpage': build_manpage},
      long_description="""Dictation is an eSpeak-based dictation utility.
It reads a text slowly, allowing users to write it. Also can pause the
dictation, spell difficult words and identify punctuation marks.""",
      classifiers=['Development Status :: 1 - Planning',
                   'Environment :: Console',
                   'Intended Audience :: Education',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Operating System :: POSIX',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Education',
                   'Topic :: Multimedia :: Sound/Audio :: Speech',
                   'Topic :: Utilities']
)
