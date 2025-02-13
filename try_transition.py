#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transitions"""

import random
from transitions import Machine


class NarcolepticSuperhero(object):
    '''Transitionclass'''

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def __init__(self, name):

        # No anonymous superheroes on my watch! Every narcoleptic superhero gets
        # a name. Any name at all. SleepyMan. SlumberGirl. You get the idea.
        self.name = name

        # What have we accomplished today?
        self.kittens_rescued = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='asleep')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # At some point, every superhero must rise and shine.
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')

        # Superheroes need to keep in shape.
        self.machine.add_transition('work_out', 'hanging out', 'hungry')

        # Those calories won't replenish themselves!
        self.machine.add_transition('eat', 'hungry', 'hanging out')

        # Superheroes are always on call. ALWAYS. But they're not always
        # dressed in work-appropriate clothing.
        self.machine.add_transition('distress_call', '*', 'saving the world',
                         before='change_into_super_secret_costume')

        # When they get off work, they're all sweaty and disgusting. But before
        # they do anything else, they have to meticulously log their latest
        # escapades. Because the legal department says so.
        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty',
                         after='update_journal')

        # Sweat is a disorder that can be remedied with water.
        # Unless you've had a particularly long day, in which case... bed time!
        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')

        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        self.machine.add_transition('nap', '*', 'asleep')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    @property
    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        '''Testing things'''
        print("Beauty, eh?")



def main():
    '''Batman doing stuff'''
    batman = NarcolepticSuperhero("Batman")
    print(batman.state) # pylint: disable=no-member

    batman.wake_up() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member

    batman.nap() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member

    #batman.clean_up()
    #MachineError: "Can't trigger event clean_up from state asleep!"

    batman.wake_up() # pylint: disable=no-member
    batman.work_out() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member

    # Batman still hasn't done anything useful...
    print(batman.kittens_rescued)


    # We now take you live to the scene of a horrific kitten entreement...
    batman.distress_call() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member

    # Back to the crib.
    batman.complete_mission() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member

    batman.clean_up() # pylint: disable=no-member
    print(batman.state) # pylint: disable=no-member


    # Another productive day, Alfred.
    print(batman.kittens_rescued)


if __name__ == "__main__":
    main()
