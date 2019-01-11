"""maxibonkata.karumihqs

This module contains the KarumiHQs class implementation.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

from chat import Chat

class KarumiHQs:
    MIN_MAXIBONS = 3
    MAX_MAXIBONS = 10

    def __init__( self, chat = None ):
        self.chat = chat
        self.maxibons_left = 10

    def maxibonsLeft( self ):
        return self.maxibons_left

    def chat( self ):
        return self.chat

    def openFridge( self, developer ):
        self.maxibons_left = max(0, self.maxibons_left - developer.maxibonsToGrab())
        if self.maxibons_left < KarumiHQs.MIN_MAXIBONS:
            self._notify_we_should_buy_maxibons( developer )
            self._buy_maxibons()

        return self.maxibons_left

    # private
    def _notify_we_should_buy_maxibons( self, developer ):
        if( isinstance( self.chat, Chat )):
            self.chat.sendMessage( f"Hi guys, I'm {developer.name}. We need more maxibons!" )

    def _buy_maxibons( self ):
        self.maxibons_left = self.maxibons_left + KarumiHQs.MAX_MAXIBONS
