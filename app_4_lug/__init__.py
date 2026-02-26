from otree.api import *


doc = """
Treatment hope
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_4_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    IMAGE_UNHRC = 'imgs/HRC_logo.png'
    # CONSTANTS
    BINARY_ANSWER = [
        (1, 'Yes'),  # Yes
        (0, 'No'), # No
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]
    HOPE_READ = [
        (0, "Yes"), #
        (1, 'No')
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    hope_recall = models.IntegerField(
        label="4.1. Wali owulidde essuubi nti okusonyiwagana mu bantu wakati wa balwanyi n'abantu ababulijjo, mu mbeera yeby'emirembe mu mambuka, binavaamu ebirungi? Bambi twala akaseera wefumitirize ku kinno. ",
        # Have you ever felt hopeful that the social reconciliation between former fighters and local communities, in the context of the peace process in the North, will be successful? Please take a moment to reflect on this.
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    hope_reason = models.LongStringField(
        label="4.2. Bwoba olina kyowulidde muggwe, Bambi tubulire mu sentensi 1 ku 2",
        # If you have ever had such a feeling, please tell us about it in 1-2 sentences.
        blank=False
    )
    hope_read = models.IntegerField(
        label="For the enumerator: was the person attentive during the readout?",
        # For the enumerator: did you the person read the text autonomously?
        choices=C.HOPE_READ,
        widget=widgets.RadioSelect,
        blank=False
    )

# PAGES
class Page1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_LUGANDA_w1":
            return [
                'hope_recall',
                'hope_reason',
                'hope_read'
            ]
        else:
            return []
    def is_displayed(player):
        participant = player.participant
        return participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_LUGANDA_w1"

page_sequence = [
    Page1
]
