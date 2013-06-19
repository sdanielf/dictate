Welcome to Dictate's documentation!
===================================

Command-line usage
------------------

The **first** argument must be the text to speak.

See an example::

        $ dictate "Hello world. This is a short text to be dictated."

If you need to load the text from a file, you can type::

        $ dictate "`/path/to/file.txt`"

Other arguments are given to the espeak command, so the languaje can be set::

        $ dictate "Hola Mundo. Este es un ejemplo corto para dictar." -ves

See `eSpeak Usage <http://espeak.sourceforge.net/commands.html>`_.

A short help message can be shown by typing::

        $ dictate --help

Runtime options
---------------

Once the program is running, some keys can be used to control the dictation.
The keys are displayed when the program starts. The most important are:

* ``q`` to stop the dictation.
* ``spacebar`` to pause the dictation until ``enter`` is pressed.
* ``s`` to spell the current word.
