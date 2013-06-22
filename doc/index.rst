Dictate's documentation
=======================

Command-line usage
------------------

The text to speak is given as an argument.

See an example::

        $ dictate "Hello world. This is a short text to be dictated."

If you want to load the text from a file, you can use the file path as
the argument::

        $ dictate /path/to/file.txt

The language can be set through adding the argument ``-l``::

        $ dictate -l es "Hola Mundo. Este es un ejemplo corto para dictar."

To see the list of available voices, type ``espeak --voices``.

The speed of espeak can be controlled with the argument ``-s`` and the time
between words (TBW) can be controlled with the argument ``-t``::

        $ dictate -s 300 -t 0 "How can a clam cram in a clean cream can?"

With ``-e``, some arguments can be given directly to the espeak command, in
the following example the amplitude is set::

        $ dictate -e "-a 50" "Hello World."

See `eSpeak Usage <http://espeak.sourceforge.net/commands.html>`_.

A short help message can be shown by typing::

        $ dictate --help

Configuring default behavior
----------------------------

Dictate reads the default preferences from the file ``~/.dictate``. All those
settings can be overwritten with command-line arguments.

If you want to set Dictate's language to Spanish by default, you can modify
the language line::

        language = es

Runtime options
---------------

Once the program is running, some keys can be used to control the dictation.
The keys are displayed when the program starts. The most important are:

* ``q`` to stop the dictation.
* ``spacebar`` to pause the dictation until the ``spacebar`` is pressed again.
* ``s`` to spell the current word.
