"""maxibonkata.karumihqs

This module contains the KarumiHQs class implementation.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

class KarumiHQs:
    MIN_MAXIBONS = 3
    MAX_MAXIBONS = 10

    def __init__( self, office_name = "KarumiHQs" ):
        self.maxibons_left = 10

    def maxibonsLeft( self ):
        return self.maxibons_left

    def openFridge( self, developer ):
        self.maxibons_left = max(0, self.maxibons_left - developer.maxibonsToGrab())
        if self.maxibons_left < KarumiHQs.MIN_MAXIBONS:
            self.maxibons_left = self.maxibons_left + KarumiHQs.MAX_MAXIBONS

        return self.maxibons_left
