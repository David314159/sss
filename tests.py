import unittest
from enum import Enum, auto
from random import randint
from typing import Callable, Any

from positions.directions import Direction
from entities.player import Player


class NumChange(Enum):
    """Represents a change in a numeric value."""
    INCREASE = auto()
    DECREASE = auto()
    STAY = auto()


class SSSTest(unittest.TestCase):

    def assertChanges(self,
                      change_things: Callable[[], Any],
                      get_things: Callable[[], list[int]],
                      expected_net_changes: list[int],
                      messages: list[str]):
        """
        Asserts that a function changes certain integer variables a certain amount.
        :param Callable[[], Any] change_things: The function to be tested. Makes relevant changes when called with no args.
        :param Callable[[], Any] get_things: A function that takes no args and returns a list of ints,
            which are the values of the things to be changed.
        :param list[int] expected_net_changes: A list representing the expected net changes to the things
            after calling change_things()
        :param list[str] messages: A list of messages to be sent if the corresponding thing is not changed properly.
        """
        things_before_change = get_things()
        change_things()
        things_after_change = get_things()
        for (thing_before_change, thing_after_change, expected_net_change, message) \
                in zip(things_before_change, things_after_change, expected_net_changes, messages):
            self.assertEqual(thing_after_change, thing_before_change + expected_net_change, message)

