"""maxibonkata.test.generators

This module contains data generators for MaxibonKata property tests.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

from hypothesis import given
from hypothesis import strategies as st

from hypothesis.strategies import characters, text, integers, builds
from hypothesis import given
from unicodedata import category

from maxibonkata.developer import Developer

developer_names = text(
    characters( max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size = 3 ).map(lambda s: s.strip()).filter(lambda s: len(s) > 0)
maxibons_to_grab = integers()

developers = builds( Developer, name = developer_names,
                                maxibonsToGrab = maxibons_to_grab )
