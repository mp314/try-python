import try_transition

def test_transition_create():
    batman = try_transition.NarcolepticSuperhero("Batman")
    assert batman.state == 'asleep'

def test_transition_wake_up():
    batman = try_transition.NarcolepticSuperhero("Batman")
    batman.wake_up()
    assert batman.state == 'hanging out'

def test_transition_distress_call():
    batman = try_transition.NarcolepticSuperhero("Batman")
    batman.distress_call()
    batman.complete_mission()
    assert batman.kittens_rescued == 1