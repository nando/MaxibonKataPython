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

    def pedro():
        return { "name": "Pedro",
                 "maxibons_to_grab": 3 }

    def fran():
        return { "name": "Fran",
                 "maxibons_to_grab": 1 }

    def davide():
        return { "name": "Davide",
                 "maxibons_to_grab": 0 }

    def sergio():
        return { "name": "Sergio",
                 "maxibons_to_grab": 2 }

    def jorge():
        return { "name": "jorge",
                 "maxibons_to_grab": 1 }
