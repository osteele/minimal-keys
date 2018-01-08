"Compute the minimal keys for a collection of strings or sequences."

__version__ = "0.1.0"

import re


def minimal_keys(keys, *, key=None, split=r'(\w+)'):
    """Compute the minimal keys for a collection of string.

    Parameters
    ----------
    items : [str]
        A sequence of keys.
    key: function
        A function of one argument that normalizes substrings before they are
        tested for equality.
    split: str
        A regular expression string that is used to split the string into
        the substrings that are candidates for removal. It should capture
        characters that should be included in the resulting minimal keys.

    Returns
    -------
    str
        A sequence of keys.

    Examples
    --------
        >>> minimal_keys(['assignments/alice/hw1.txt', 'assignments/bob/hw1.txt'])
        ['alice', 'bob']
        >>> minimal_keys(['alice/assignments/hw1.txt', 'bob/assignments/hw1.txt'])
        ['alice', 'bob']

    Use ``key`` to normalize components before comparing them:
        >>> minimal_keys(['assignments/alice.txt', 'Assignments/bob.txt'])
        ['assignments/alice', 'Assignments/bob']
        >>> minimal_keys(['assignments/alice.txt', 'Assignments/bob.txt'], key=str.upper)
        ['alice', 'bob']

    Use ``split`` to specify the boundaries for common substring removal:
        >>> minimal_keys(['assignments/alice_smith.txt', 'assignments/alice_jones.txt'])
        ['alice_smith', 'alice_jones']
        >>> minimal_keys(['assignments/alice_smith.txt', 'assignments/alice_jones.txt'], \
                         split=r'([a-z]+)')
        ['smith', 'jones']
    """
    splitter = re.compile(split).split
    keys = list(map(splitter, keys))
    keys = minimal_seq_keys(keys, key)
    return list(map(''.join, keys))


def minimal_seq_keys(keys, key=None):
    """Compute the minimal keys for a collection of sequences.

    Parameters
    ----------
    items : [seq]
        A sequence of keys. Each key is itself a sequence.
    key: function
        A function of one argument that normalizes substrings before they are
        tested for equality.

    Returns
    -------
    seq
        A sequence of keys.
    """
    key = key or (lambda k: k)

    def trim(keys, ix, s0, s1):
        "Return a list k[s0:s1] if all the k[ix] are equivalent under key."
        while all(keys) and len(set(key(k[ix]) for k in keys)) == 1:
            keys = [k[s0:s1] for k in keys]
        return keys
    keys = trim(keys, 0, 1, None)
    keys = trim(keys, -1, None, -1)
    if any(not k for k in keys):
        raise Exception("duplicate keys")
    return keys
