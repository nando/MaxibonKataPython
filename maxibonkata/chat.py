"""maxibonkata.chat

This module contains the Chat class implementation.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

class Chat:
    def __init__( self ):
        self.messageSent = ""

    def messageSent( self ):
        return self.messageSent

    def sendMessage( self, message ):
        self.messageSent = message
