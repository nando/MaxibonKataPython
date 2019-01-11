"""maxibonkata.test.karumihqstest

This module contains property tests for maxibonkata.karumihqs KarumiHQs class.

:copyright: 2019, Karumi & The Cocktail

:license: Apache License. See LICENSE.txt file for further details.
"""

import pytest

from hypothesis import given
from hypothesis import strategies as st

from karumihqs import KarumiHQs
from chat import Chat
from generators import developers, hungry_developers

def calculate_maxibons_left( initial_maxibons, developer ):
    maxibons_left = max( initial_maxibons - developer.maxibonsToGrab(), 0 )
    if maxibons_left < KarumiHQs.MIN_MAXIBONS:
      return maxibons_left + KarumiHQs.MAX_MAXIBONS
    else:
      return maxibons_left

def test_should_start_the_day_with_10_maxibons():
    office = KarumiHQs()
    assert office.maxibonsLeft() == 10

@given( developers )
def test_should_always_has_more_than_two_maxibons_in_the_fridge( developer ):
    office = KarumiHQs()
    office.openFridge( developer )
    assert office.maxibonsLeft() >= 2

@given( hungry_developers )
def test_should_buy_10_more_maxibons_if_there_are_less_than_3_in_the_fridge( developer ):
    office = KarumiHQs()
    initial_maxibons = office.maxibonsLeft()
    office.openFridge( developer )
    expected_maxibons = calculate_maxibons_left( initial_maxibons,
                                                 developer )
    assert office.maxibonsLeft() == expected_maxibons

@given( hungry_developers )
def test_should_request_10_more_maxibons_using_the_chat_if_there_are_less_than_3_in_the_fridge( developer ):
    chat = Chat()
    office = KarumiHQs( chat )
    office.openFridge( developer )
    assert office.chat.messageSent == f"Hi guys, I'm {developer.name}. We need more maxibons!"
