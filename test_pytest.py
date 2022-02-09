import try_pytest # The code to test

def test_increment():
    assert try_pytest.increment(3) == 4

def test_decrement():
    assert try_pytest.decrement(3) == 4