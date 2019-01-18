"""maxibonkata.developer

This module contains the Developer class implementation.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

class Developer:
    def __init__( self, name, maxibonsToGrab = 0 ):
        self.name = name
        self.maxibons_to_grab = max( 0, maxibonsToGrab )

    def name( self ):
        return self.name

    def maxibonsToGrab( self ):
        return self.maxibons_to_grab

    # Karumi's
    def pedro():
        return Developer("Pedro", 3)

    def fran():
        return Developer("Fran", 1)

    def davide():
        return Developer("Davide", 0)

    def sergio():
        return Developer("Sergio", 2)

    def jorge():
        return Developer("Jorge", 1)

    # TCK's
    def nuria():
        return Developer("Nuria", 3)

    def fausto():
        return Developer("Fausto", 2)

    def julia():
        return Developer("Julia",  0)

    def luismi():
        return Developer("Luismi", 3)

    def susana():
        return Developer("Susana", 2)

    def sahu():
        return Developer("Sahu", 1)

    def vero():
        return Developer("Vero", 3)

    def vito():
        return Developer("Vito", 3)
