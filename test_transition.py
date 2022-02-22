#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Transitions testing """

import pytest
import try_transition



def test_transition_create():
    ''' Test init '''
    batman = try_transition.NarcolepticSuperhero("Batman")
    assert batman.state == 'asleep' # pylint: disable=no-member

def test_transition_wake_up():
    ''' Test wake_up transition '''
    batman = try_transition.NarcolepticSuperhero("Batman")
    batman.wake_up() # pylint: disable=no-member
    assert batman.state == 'hanging out' # pylint: disable=no-member

def test_transition_distress_call():
    ''' Test distress_call transition '''
    batman = try_transition.NarcolepticSuperhero("Batman")
    batman.distress_call() # pylint: disable=no-member
    batman.complete_mission() # pylint: disable=no-member
    assert batman.kittens_rescued == 1

def test_transition_clean_up():
    ''' Test clean_up transition '''
    batman = try_transition.NarcolepticSuperhero("Batman")
    #with pytest.raises(Exception) as e_info:
    with pytest.raises(Exception):
        batman.clean_up() # pylint: disable=no-member
   