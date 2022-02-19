import try_transition

def test_transition_create():
    batman = try_transition.NarcolepticSuperhero("Batman")
    assert batman.state == 'asleep'