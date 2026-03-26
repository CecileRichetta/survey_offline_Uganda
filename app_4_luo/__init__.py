from otree.api import *


doc = """
Treatment hope
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_4_LUO'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    IMAGE_UNHRC = 'imgs/HRC_logo.png'
    # CONSTANTS
    BINARY_ANSWER = [
        (1, "Yes"),  # Yes
        (0, "No"), # No
        (998, "Don't know"),  # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    text_check = models.IntegerField(
        label="4.1. Lukwan nyo lukwed maggi dong gumoko look ma lube is dwoggo pa kuc I Kumalo me lobo Uganda?"
              "",
        # For the enumerator: did you the person read the text autonomously?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    hope_recall = models.IntegerField(
        label="4.2. Manaka tika ibedo ki gen ni mato oput ikin lulweny macon ki dano me kin gang ikit man mekelo kuc "
              "ikumalo ni obi nyako nyige? Timber ikwany kare man me lwodo ikom lok man.",
        # Have you ever felt hopeful that the social reconciliation between former fighters and local communities, in the context of the peace process in the North, will be successful? Please take a moment to reflect on this.
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    hope_reason = models.LongStringField(
        label="4.3. Kace ma naka ibedo ki cwiny macalo man, timber iwaci wa  ikine me nyik lok 1 onyo 2.",
        # If you have ever had such a feeling, please tell us about it in 1-2 sentences.
        blank=True
    )

# PAGES
class Page1_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant #
        if participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_LUO_w1":
            return [
                'text_check',
                'hope_recall',
                'hope_reason'
            ]
        else:
            return []
    def is_displayed(player):
        participant = player.participant
        return participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_LUO_w1"


class Page1_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant #
        if participant.treatment_hope == 0 and player.session.config['name'] == "session_C4P_LUO_w1":
            return [
                'text_check'
            ]
        else:
            return []
    def is_displayed(player):
        participant = player.participant
        return participant.treatment_hope == 0 and player.session.config['name'] == "session_C4P_LUO_w1"


page_sequence = [
    Page1_1,
    Page1_2
]