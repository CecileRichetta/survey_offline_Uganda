from otree.api import *
import random

doc = """
Economics questions
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_10_ENG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # CHOICES IN VARIABLES
    BINARY_ANSWER = [
        (1, 'Yes'), # Yes
        (0, 'No'),  # No
        (998, "Don't know"), # don't know
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    ETHNIC_COMP = [
        (0, "Same ethnic group as me"), # Same ethnic group as me
        (1, "A different ethnic group than me"), # A different ethnic group than me
        (2, "Mixed: Some are from the same ethnic group as me, others not"), # Mixed: Some are from the same ethnic group as me, others not
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    ECONOMIC_STATUS_1 = [
        (0, 'Very'), #
        (1, 'Fairly bad'), #
        (2, 'Neither bad nor good'), # Neither disagree or agree
        (3, 'Fairly good'), # Agree
        (4, 'Good'), # Completely agree
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # SOCIO-DEM VARIABLES
    asset_1 = models.IntegerField(
        label="10.1. May I know if you have the following: Motorcycle in working conditions",
        # Do you have the following at home: motorcycle
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    asset_2 = models.IntegerField(
        label="10.2. May I know if you have the following: Bicycle in working conditions",
        # Do you have the following at home: bicycle
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    asset_3 = models.IntegerField(
        label="10.3. May I know if you have the following in your home: Cows and Goats",
        # Do you have the following at home: cows or goats
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    ethnic_composition = models.IntegerField(
        label="10.4. To which ethnic groups do you think the majority of the people in your village / your neighborhood belong?",
        #
        choices=C.ETHNIC_COMP,
        widget=widgets.RadioSelect,
        blank=False
    )
    eco_status_1 = models.IntegerField(
        label="10.5. In general, how would you describe your own present living conditions?", # In general, how would you describe your own present living conditions?
        widget=widgets.RadioSelect,
        choices=C.ECONOMIC_STATUS_1,
        blank=False
    )
    eco_status_2 = models.IntegerField(
        label="10.6. Adding up your sources of income, what is your household's gross monthly income (before deducting taxes, social security contributions and other expenses)?",
        # Adding up your sources of income, what is your household's gross monthly income (before deducting taxes, social security contributions and other expenses)?
        blank=True
    )

# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'asset_1',
        'asset_2',
        'asset_3',
        'ethnic_composition',
        'eco_status_1',
        'eco_status_2'
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_ENGLISH_w1"

page_sequence = [
    Page1 # socio-demographics
]
