"""maxibonkata.test.developertest

This module contains property tests for maxibonkata.developer Developer class.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

import pytest

from hypothesis import given
from hypothesis.strategies import integers, text, sampled_from

from developer import Developer

@given( text() )
def test_assign_the_name_of_the_developer_in_construction( name ):
    developer = Developer( name )
    assert developer.name == name

@given( text(), integers() )
def test_should_always_grab_a_positive_number_of_maxibons( name, mtg ):
    developer = Developer( name, mtg )
    assert developer.maxibonsToGrab() >= 0

@given( sampled_from([
    ( Developer.pedro, 3 ),
    ( Developer.fran, 1 ),
    ( Developer.davide, 0 ),
    ( Developer.sergio, 2 ),
    ( Developer.jorge, 1 )
]) )
def test_assign_the_number_of_maxibons_specified_to_every_developer( tuple ):
    developer = tuple[0]
    maxibons_to_grab = tuple[1]
    assert developer()["maxibons_to_grab"] == maxibons_to_grab
