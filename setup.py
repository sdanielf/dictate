from distutils.core import setup

setup(name='dictate',
      version='0.1',
      description='Command-line dictation utility.',
      author='Daniel Francis',
      author_email='francis@sugarlabs.org',
      license='GPLv3',
      url='https://github.com/sdanielf/dictate/',
      packages=['dictation'],
      scripts=['dictate'],
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
