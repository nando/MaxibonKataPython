"""maxibonkata.test.generators

This module contains data generators for MaxibonKata property tests.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

from hypothesis import given
from hypothesis import strategies as st

from hypothesis.strategies import characters, text, integers, builds, tuples
from hypothesis import given
from unicodedata import category

from maxibonkata.developer import Developer

developer_names = text(
    characters( max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size = 3 ).map(lambda s: s.strip()).filter(lambda s: len(s) > 0)

developers = builds( Developer,
                     name = developer_names,
                     maxibonsToGrab = integers() )

hungry_developers = builds( Developer,
                            name = developer_names,
                            maxibonsToGrab = integers( 8 ) ) # min_value

not_so_hungry_developers = builds( Developer,
                                   name = developer_names,
                                   maxibonsToGrab = integers( 0, 2 ) ) # min, max

karumi_developers = builds( Developer,
                   name = developer_names,
                   maxibonsToGrab = integers( 0, 3 ) )

karumies_group = tuples( karumi_developers, karumi_developers, karumi_developers )
