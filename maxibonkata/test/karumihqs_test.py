"""maxibonkata.test.karumihqstest

This module contains property tests for maxibonkata.karumihqs KarumiHQs class.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

import pytest

from hypothesis import given
from hypothesis import strategies as st

from karumihqs import KarumiHQs

@given( office_name = st.just( "Madrid KarumiHQs" ))
def test_should_start_the_day_with_10_maxibons( office_name ):
    office = KarumiHQs( office_name )
    assert office.maxibonsLeft() == 10
