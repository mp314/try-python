#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test pytest module"""

import try_pytest # The code to test


def test_increment():
    ''' Test Increment '''
    assert try_pytest.increment(3) == 4

# FAIL
# def test_decrement():
#    ''' Test Decrement '''
#    assert try_pytest.decrement(3) == 4
    