"""maxibonkata.developer

This module contains the Developer class implementation.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

class Developer:
    def __init__( self, name, maxibonsToGrab = 0 ):
        self.name = name
        self.maxibons_to_grab = max( 0, maxibonsToGrab )

    def maxibonsToGrab( self ):
        return self.maxibons_to_grab
