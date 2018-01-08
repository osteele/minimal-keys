Minimal Keys
============

|PyPI version| |License| |Supported Python|

Compute the minimal keys for a collection of strings or sequences. This is
intended for use in presenting data in a user interface.

For example, the minimal keys of ``["assignments/alice/hw1.txt",
"assignments/bob/hw1.txt"]`` are ``["alice", "bob"]``.

The minimal keys of ``["alice/assignments/hw1.txt", "bob/assignments/hw1.txt"]``
are also ``["alice", "bob"]``.

Finally, the minimal keys of ``["assignments/alice.txt",
"assignments/bob.txt"]`` are—wait for it—``["alice", "bob"]``.

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

    $ pip install minimal-keys

Usage
-----

.. code:: python

    >>> from minimalkeys import minimalkeys
    >>> minimal_keys(["assignments/alice/hw1.txt", "assignments/bob/hw1.txt"])
    ['alice', 'bob']


License
-------

MIT

.. |PyPI version| image:: https://img.shields.io/pypi/v/minimal-keys.svg
    :target: https://pypi.python.org/pypi/minimal-keys
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/minimal-keys.svg
    :target: https://pypi.python.org/pypi/minimal-keys
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/minimal-keys.svg
    :target: https://pypi.python.org/pypi/minimal-keys
    :alt: Supported Python Versions

.. _superkey: https://en.wikipedia.org/wiki/Superkey
