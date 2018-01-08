from minimalkeys import minimal_keys


def test_minimal_keys():
    assert minimal_keys(['assignments/alice/hw1.txt', 'assignments/bob/hw1.txt']) == ['alice', 'bob']
    assert minimal_keys(['alice/assignments/hw1.txt', 'bob/assignments/hw1.txt']) == ['alice', 'bob']
    assert minimal_keys(['assignments/alice.txt', 'assignments/bob.txt']) == ['alice', 'bob']


def test_minimal_keys_key():
    assert minimal_keys(['assignments/alice.txt', 'Assignments/bob.txt']) == ['assignments/alice', 'Assignments/bob']
    assert minimal_keys(['assignments/alice.txt', 'Assignments/bob.txt'], key=str.upper) == ['alice', 'bob']


def test_minimal_keys_splitter():
    assert minimal_keys(['assignments/alice.txt', 'assignments/arnold.txt']) == ['alice', 'arnold']
    assert minimal_keys(['assignments/alice_smith.txt', 'assignments/alice_jones.txt']
                        ) == ['alice_smith', 'alice_jones']
    assert (minimal_keys(['assignments/alice_smith.txt', 'assignments/alice_jones.txt'],
                         split=r'([a-z]+)') == ['smith', 'jones'])


def test_minimal_keys_key_option():
    assert minimal_keys(['assignments/alice.txt', 'Assignments/bob.txt'], key=str.upper) == ['alice', 'bob']
