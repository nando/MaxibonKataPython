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
import generators as gnrt

def calculate_maxibons_left( initial_maxibons, developers ):
    if not isinstance( developers, tuple ):
        developers = [ developers ]

    maxibons_left = initial_maxibons
    for developer in developers:
        maxibons_left = max( maxibons_left - developer.maxibonsToGrab(), 0 )

    if maxibons_left < KarumiHQs.MIN_MAXIBONS:
      return maxibons_left + KarumiHQs.MAX_MAXIBONS
    else:
      return maxibons_left

def test_should_start_the_day_with_10_maxibons():
    office = KarumiHQs()
    assert office.maxibonsLeft() == 10

@given( gnrt.developers )
def test_should_always_has_more_than_two_maxibons_in_the_fridge( developer ):
    office = KarumiHQs()
    office.openFridge( developer )
    assert office.maxibonsLeft() >= 2

@given( gnrt.hungry_developers )
def test_should_buy_10_more_maxibons_if_there_are_less_than_3_in_the_fridge( developer ):
    office = KarumiHQs()
    initial_maxibons = office.maxibonsLeft()
    office.openFridge( developer )
    expected_maxibons = calculate_maxibons_left( initial_maxibons,
                                                 developer )
    assert office.maxibonsLeft() == expected_maxibons

@given( gnrt.hungry_developers )
def test_should_request_10_more_maxibons_using_the_chat_if_there_are_less_than_3_in_the_fridge( developer ):
    chat = Chat()
    office = KarumiHQs( chat )
    office.openFridge( developer )
    assert office.chat.messageSent == f"Hi guys, I'm {developer.name}. We need more maxibons!"

@given ( gnrt.not_so_hungry_developers )
def test_should_never_request_more_maxibons_to_the_team_using_the_chat_if_there_are_more_than_2_in_the_fridge( developer ):
    chat = Chat()
    office = KarumiHQs( chat )
    office.openFridge( developer )
    assert office.chat.messageSent is None

@given ( gnrt.karumies_group )
def test_should_always_has_more_than_two_maxibons_in_the_fridge_even_if_some_karumies_grab_maxibons_in_group( developers ):
    office = KarumiHQs()
    office.openFridge( developers )
    assert office.maxibonsLeft() > 2

@given ( gnrt.developers_group )
def test_should_buy_10_more_maxibons_if_there_are_less_than_2_in_the_fridge_when_grabbing_maxibons_in_group( developers ):
    office = KarumiHQs()
    initial_maxibons = office.maxibonsLeft()
    office.openFridge( developers )
    expected_maxibons = calculate_maxibons_left( initial_maxibons,
                                                 developers )
    assert office.maxibonsLeft() == expected_maxibons
