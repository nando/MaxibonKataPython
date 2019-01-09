"""maxibonkata.test.developertest

This module contains property tests for maxibonkata.developer Developer class.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

import pytest

from hypothesis import given
from hypothesis.strategies import integers, text

from developer import Developer

@given( text(), integers() )
def test_should_always_grab_a_positive_number_of_maxibons( name, mtg ):
    developer = Developer( name, mtg )
    assert developer.maxibonsToGrab() >= 0