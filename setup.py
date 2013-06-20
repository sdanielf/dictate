from distutils.core import setup

from distutils.command.build import build
from distutils.core import Command

import os
srcdir = os.path.dirname(os.path.abspath(__file__))
docdir = os.path.join(srcdir, 'doc')
docgettextdir = os.path.join(docdir, 'gettext')
mandir = os.path.join(docdir, 'man')

class build_manpage(Command):
    description = 'Generate man pages.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
            pass

    def run(self):
        for i in os.listdir(docgettextdir) + ['man1.1']:
            name, ext = i.split('.')
            if ext != 'pot' and name:
                build_dir = os.path.join(mandir, name)
                if not os.path.exists(build_dir):
                    os.makedirs(build_dir)
                langopt = ('-Dlanguage=%s' % name) if name != 'man1' else ''
                print 'Generating %s/dictate.1.gz' % build_dir
                os.system('sphinx-build -b man %s %s %s' %\
                          (langopt, docdir, build_dir))
                if os.path.exists('%s/dictate.1.gz' % build_dir):
                    os.remove('%s/dictate.1.gz' % build_dir)
                os.system('gzip %s/*.1' % build_dir)


from distutils.command.install_data import install_data as _install_data

import os

class build_trans(Command):
    description = 'Compile .po files into .mo files'
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        srcdir = os.path.join(os.path.abspath(os.curdir))
        translations = [(os.path.join(srcdir, 'po'),
                         os.path.join(srcdir, 'locale'), 'dictate'),
                        (os.path.join(srcdir, 'doc', 'gettext'),
                         os.path.join(srcdir, 'doc', 'locale'), 'index')]
        for po_dir, locale_dir, module in translations:
            os.system('%s/i18nhelpers/buildmo.py %s %s %s' %\
                        (srcdir, po_dir, locale_dir, module))

build.sub_commands.append(('build_trans', None))
build.sub_commands.append(('build_manpage', None))

class install_data(_install_data):
    def run(self):
        self.data_files = [] if self.data_files == None else self.data_files
        self.append_mo('%s/locale/' % srcdir)
        self.install_man('doc/man')
        print 'Data files are', self.data_files
        _install_data.run(self)

    def append_mo(self, directory):
        for lang in os.listdir(directory):
            lang_dir = os.path.join('share', 'locale', lang,
                                    'LC_MESSAGES')
            lang_file = os.path.join('locale', lang, 'LC_MESSAGES',
                                        'dictate.mo')
            self.data_files.append((lang_dir, [lang_file]))

    def install_man(self, directory):
        for i in os.listdir(directory):
            path = os.path.join(directory, i)
            if os.path.isdir(path) and i != '.doctrees':
                install_path = os.path.join('share', 'man', i, 'man1')
                if i == 'man1':
                    install_path = os.path.join('share', 'man', 'man1')
                files = []
                for filename in os.listdir(path):
                    if filename.split('.')[-1] == 'gz':
                        files.append(os.path.join(path, filename))
                self.data_files.append((install_path, files))

build.sub_commands.append(('install_data', None))

setup(name='dictate',
      version='0.1',
      description='Command-line dictation utility.',
      author='Daniel Francis',
      author_email='francis@sugarlabs.org',
      license='GPLv3',
      url='https://github.com/sdanielf/dictate/',
      packages=['dictation'],
      scripts=['dictate'],
      cmdclass={'build_manpage': build_manpage,
                'build_trans': build_trans,
                'install_data': install_data},
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
