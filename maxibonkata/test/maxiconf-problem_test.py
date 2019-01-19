"""
This file contains the test to let us enjoy an AWESOME conf. wo melted Maxibons. :D

:copyright: 2019 The Cocktail Experience

:license: Apache License. See LICENSE.txt file for further details.
"""

from karumihqs import KarumiHQs
from developer import Developer

from hypothesis import note, settings
from hypothesis.strategies import integers
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant

class MaxiconfProblem( RuleBasedStateMachine ):
    melted_maxibons = 0
    awesome_conf = False
    maxiconf_venue = KarumiHQs()
    audience = [[ Developer.pedro(),  { "grabbings": 0 } ],
                [ Developer.fran(),   { "grabbings": 0 } ],
                [ Developer.davide(), { "grabbings": 0 } ],
                [ Developer.sergio(), { "grabbings": 0 } ],
                [ Developer.jorge(),  { "grabbings": 0 } ],
                [ Developer.nuria(),  { "grabbings": 0 } ],
                [ Developer.fausto(), { "grabbings": 0 } ],
                [ Developer.julia(),  { "grabbings": 0 } ],
                [ Developer.luismi(), { "grabbings": 0 } ],
                [ Developer.susana(), { "grabbings": 0 } ],
                [ Developer.sahu(),   { "grabbings": 0 } ],
                [ Developer.vero(),   { "grabbings": 0 } ],
                [ Developer.vito(),   { "grabbings": 0 } ]]

    grabbings = []

    @rule()
    def pedro( self ) :
        self.developer_grabs( "Pedro" )

    @rule()
    def fran( self ):
        self.developer_grabs( "Fran" )

    @rule()
    def davide( self ):
        self.developer_grabs( "Davide" )

    @rule()
    def sergio( self ):
        self.developer_grabs( "Sergio" )

    @rule()
    def jorge( self ):
        self.developer_grabs( "Jorge" )

    # TCK's
    @rule()
    def nuria( self ):
        self.developer_grabs( "Nuria" )

    @rule()
    def fausto( self ):
        self.developer_grabs( "Fausto" )

    @rule()
    def julia( self ):
        self.developer_grabs( "Julia" )

    @rule()
    def luismi( self ):
        self.developer_grabs( "Luismi" )

    @rule()
    def susana( self ):
        self.developer_grabs( "Susana" )

    @rule()
    def sahu( self ):
        self.developer_grabs( "Sahu" )

    @rule()
    def vero( self ):
        self.developer_grabs( "Vero" )

    @rule()
    def vito( self ):
        self.developer_grabs( "Vito" )

    def developer_grabs( self, developer_name ):
        data = next(dev for dev in self.audience if dev[0].name == developer_name)
        developer, developer_data, grabbings = data[0], data[1], data[1]["grabbings"]
        # print(f"IN developer_grabs() with {developer.name} ({grabbings} grabbings...)")
        if grabbings == 0:
            print(f"With {self.maxiconf_venue.maxibonsLeft()} maxibons {developer.name} is grabbing {developer.maxibonsToGrab()}...")
            self.grabbings.append( developer )
            self.maxiconf_venue.openFridge( developer )
            developer_data["grabbings"] = 1

        if self.completed():
            print("Maxiconf completed delivering {m} melted maxibons.".format(
                m = self.maxiconf_venue.meltedMaxibons() ))
            self.melted_maxibons = self.maxiconf_venue.meltedMaxibons()
            self.awesome_conf = self.melted_maxibons < 2
            if not( self.awesome_conf ):
                for dev in self.audience:
                    dev[1]["grabbings"] = 0
                self.maxiconf_venue.init_counters()

    def completed( self ):
        return len( self.grabbings ) == len( self.audience )

    @invariant()
    def lots_of_maxibons_always_melt_in_our_confs(self):
        if self.awesome_conf:
            if self.melted_maxibons > 0:
                note("We've delivered ONLY {m} MELTED maxibon/s! :__)".format(
                    m = self.melted_maxibons ))
            else:
                note("AWESOME!! NO MELTED_MAXIBONS DELIVERED!!")

        assert not( self.awesome_conf )

with settings(max_examples=2000):
    MaxiconfProblemTest = MaxiconfProblem.TestCase
