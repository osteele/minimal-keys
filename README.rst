Minimal Keys
============

|PyPI version| |Doc Status| |License| |Supported Python|

Compute the minimal unique keys for a collection of strings or sequences.

This is intended for use in presenting data in a user interface. For example,
the ``nbcollate`` command-line interface from the nbcollate_ package uses it to
guess student names from notebook filenames, for use in the creation of the
collated Jupyter notebook.

The minimal keys from ``["assignments/alice/hw1.txt",
"assignments/bob/hw1.txt"]`` are ``["alice", "bob"]``, because the input strings
share the common prefix ``"assignments/"`` and the common suffix ``".txt"``.

The minimal keys from ``["alice/assignments/hw1.txt", "bob/assignments/hw1.txt"]``
are also ``["alice", "bob"]``, because the input strings
share the common suffix ``"/assignments/hw1.txt"``.

Finally, the minimal keys from ``["assignments/alice.txt",
"assignments/bob.txt"]`` are—wait for it—``["alice", "bob"]``.

There are options to ignore case, and to split the strings at different
boundaries. (The default is split to on words, so that ``["alice", "adam"]`` is
not abbreviated to ``["lice", "dam"]``.)

This is the same basic idea as a database superkey_, except that the actual
minimal unique keys are returned, instead of the attributes that select these
keys.

The current implementation trims only the beginnings and ends of sequences,
because this is all that I've needed so far. I have in my head a more
sophisticated implementation that uses `difflib`, but it is too long to fit in
the header of this README.

Install
-------

.. code:: bash

    $ pip install minimalkeys

Usage
-----

.. code:: python

    >>> from minimalkeys import minimal_keys
    >>> minimal_keys(["assignments/alice/hw1.txt", "assignments/bob/hw1.txt"])
    ['alice', 'bob']


License
-------

MIT

.. |PyPI version| image:: https://img.shields.io/pypi/v/minimalkeys.svg
    :target: https://pypi.python.org/pypi/minimalkeys
    :alt: Latest PyPI Version
.. |Doc Status| image:: https://readthedocs.org/projects/minimal-keys/badge/?version=latest
    :target: http://minimal-keys.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |License| image:: https://img.shields.io/pypi/l/minimal-keys.svg
    :target: https://pypi.python.org/pypi/minimal-keys
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/minimal-keys.svg
    :target: https://pypi.python.org/pypi/minimal-keys
    :alt: Supported Python Versions

.. _superkey: https://en.wikipedia.org/wiki/Superkey
.. _nbcollate: https://github.com/osteele/nbcollate