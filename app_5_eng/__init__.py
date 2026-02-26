from otree.api import *
import csv
import random


doc = """
Ultimatum Game Experiment App.
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_5_ENG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # GAME ELEMENTS
    TOKEN_VALUE = 2500
    TOKEN_ENDOWMENT = 4
    CHOICES_UG_PROPOSER = [
        (0, "I won't give any tokens to my partner, but I'll keep all 4 for myself."),
        (1, 'I want to give 1 token to my partner and keep 3 for myself.'),
        (2, 'I want to give 2 tokens to my partner and keep 2 for myself.'),
        (3, "I want to give 3 tokens to my partner and keep 1 for myself."),
        (4, "I want to give 4 tokens to my partner and keep none for myself.")
    ]
    CHOICES_UG_RECEIVER = [
        (0, 'I accept that I receive nothing, and the other person keeps all 4 tokens.'),
        (1, 'I accept the offer if the other person sends me 1 token and they keep 3 tokens.'),
        (2, 'I accept the offer if the other person sends me 2 tokens and they keep 2 tokens.'),
        (3, 'I accept the offer if the other person sends me 3 tokens and they keep 1 token.'),
        (4, 'I accept the offer if the other person sends me 4 tokens and they keep nothing.')
    ]
    # INSTRUCTIONS TEMPLATES
    TEMPLATE_INSTRUCTIONS_ULTIMATUM_PROPOSER = '_static/texts_ENGLISH/instr_ultimatum_proposer.html'
    TEMPLATE_INSTRUCTIONS_ULTIMATUM_RECEIVER = '_static/texts_ENGLISH/instr_ultimatum_receiver.html'
    TEMPLATE_INSTRUCTIONS_PG = '_static/texts_ENGLISH/instr_pg.html'
    # IMAGES TEMPLATES
    IMAGE_UG_INSTR = 'imgs/diagram_UG.png'
    IMAGE_UG_EXAMPLE1 = 'imgs/diagram_UG_example1.png'
    IMAGE_UG_EXAMPLE2 = 'imgs/diagram_UG_example2.png'




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # COMPREHENSION CHECKS SUM
    ultimatum_correct_answers = models.IntegerField()
    ultimatum_redo_questions = models.BooleanField(
        label="5.3. Some of your answers in the previous questions were not correct. I want to give you the opportunity to listen once more to the full instructions, and answer the questions. Do you want to listen the instructions and answer once again the questions?",        #  Some of your answers in the previous questions were not correct. I want to give you the opportunity to listen
        #  once more to the full instructions, and answer the questions. Do you want to listen the instructions and answer once again the questions?
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=False)
    # PROPOSER comprehension checks
    ug_proposer_cc1 = models.IntegerField(
        label="5.1.1. I have no choice but to give tokens to the receiver.",
        #  I have no choice but to give tokens to the receiver.
        choices=[
            (0, 'True'), # True
            (1, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    ug_proposer_cc2 = models.IntegerField(
        label="5.1.2. The receiver can refuse my offer.",
        # The receiver can refuse my offer.
        choices=[
            (1, 'True'), # True
            (0, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    ug_proposer_cc3 = models.IntegerField(
        label="5.1.3. The receiver is fake.",
        # The receiver is fake.
        choices=[
            (0, 'True'), # True
            (1, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    # RESPONDER COMPREHENSION CHECKS
    ug_receiver_cc1 = models.IntegerField(
        label="5.2.1.  The proposer has no choice but to send me tokens.",
        # The proposer has no choice but to send me tokens.
        choices=[
            (0, 'True'), # True
            (1, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    ug_receiver_cc2 = models.IntegerField(
        label="5.2.2. If the minimum of tokens that I want is smaller than what the proposer offers, I get the tokens. ",
        # If the minimum of tokens that I want is smaller than what the proposer offers, I get the tokens.
        choices=[
            (1, 'True'), # True
            (0, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    ug_receiver_cc3 = models.IntegerField(
        label="5.2.3. The proposer is fake.",
        # The proposer is fake.
        choices=[
            (0, 'True'), # True
            (1, 'False') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    # CHOICES IN UG
    decision_proposer = models.IntegerField(
        label="",
        # How much do you offer to the other person and how much do you keep?
        choices=C.CHOICES_UG_PROPOSER,
        blank=False,
        widget=widgets.RadioSelect
    )
    decision_receiver = models.IntegerField(
        label="",
        # How much do you want the other person to send you?
        choices=C.CHOICES_UG_RECEIVER,
        blank=False,
        widget=widgets.RadioSelect
    )


# FUNCTIONS
def extract_games_and_payoffs_pilot(p):
    # Read CSV manually
    with open("_static/data_internal/payoffs/games_pilot.csv", newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Convert numeric fields
    for row in rows:
        row['group'] = int(row['group'])
        row['etv'] = int(row['etv'])
        row['side_ultimatum'] = int(row['side_ultimatum'])
        row['decision_UG'] = float(row['decision_UG'])
        row['decision_PG'] = float(row['decision_PG'])

    participant = p.participant

    # Pre-filter based on treatment_other
    def filter_df(rows, treatment):
        if treatment == 0:
            return rows
        elif treatment == 1:
            return [r for r in rows if r['group'] == 0]
        elif treatment == 2:
            return [r for r in rows if r['group'] == 1]
        elif treatment == 3:
            return [r for r in rows if r['group'] == 0 and r['etv'] == 1]
        elif treatment == 4:
            return [r for r in rows if r['group'] == 1 and r['etv'] == 1]
        return rows

    source = filter_df(rows, participant.treatment_other)

    # Define candidates based on side_ultimatum
    if participant.side_ultimatum == 0:
        ug_candidates = [r for r in source if r['side_ultimatum'] == 1]
        pg_candidates = source
    else:
        ug_candidates = [r for r in source if r['side_ultimatum'] == 0]
        pg_candidates = source

    # Helper to safely sample
    def safe_sample(candidates, column):
        if len(candidates) > 1:
            return random.choice(candidates)[column]
        elif len(candidates) == 1:
            return candidates[0][column]
        else:
            return None

    participant.other_UG_decision = safe_sample(ug_candidates, 'decision_UG')
    participant.other_PG_decision = safe_sample(pg_candidates, 'decision_PG')


def correct_answers_ultimatum(player):
    participant = player.participant
    if participant.side_ultimatum == 0:
        cc1 = player.field_maybe_none('ug_proposer_cc1')
        cc2 = player.field_maybe_none('ug_proposer_cc2')
        cc3 = player.field_maybe_none('ug_proposer_cc3')
        if None in (cc1, cc2, cc3):
            player.ultimatum_correct_answers = 0
        else:
            player.ultimatum_correct_answers = cc1 + cc2 + cc3
    else:
        cc1 = player.field_maybe_none('ug_receiver_cc1')
        cc2 = player.field_maybe_none('ug_receiver_cc2')
        cc3 = player.field_maybe_none('ug_receiver_cc3')
        if None in (cc1, cc2, cc3):
            player.ultimatum_correct_answers = 0
        else:
            player.ultimatum_correct_answers = cc1 + cc2 + cc3


def payoff_UG(participant):
    if participant.side_ultimatum == 0:
        if participant.decision_UG >= participant.other_UG_decision:
            participant.payoff_UG = C.TOKEN_ENDOWMENT - participant.decision_UG
        else:
            participant.payoff_UG = 0
    else:
        if participant.decision_UG <= participant.other_UG_decision:
            participant.payoff_UG = participant.other_UG_decision
        else:
            participant.payoff_UG = 0

# PAGES
class Page1(Page):
    pass
    @staticmethod
    def before_next_page(player, timeout_happened):
        extract_games_and_payoffs_pilot(player)
        participant = player.participant
        print(participant.other_UG_decision)
        print(participant.other_PG_decision)


class Page2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.side_ultimatum == 0:
            return [
                'ug_proposer_cc1',
                'ug_proposer_cc2',
                'ug_proposer_cc3'
            ]
        elif participant.side_ultimatum == 1:
            return [
                'ug_receiver_cc1',
                'ug_receiver_cc2',
                'ug_receiver_cc3'
            ]
        else:
            return []
    def before_next_page(player, timeout_happened):
        correct_answers_ultimatum(player)


class Page3(Page):
    form_model = 'player'
    form_fields = ['ultimatum_redo_questions']

    @staticmethod
    def is_displayed(player):
        return player.field_maybe_none('ultimatum_correct_answers') < 3

class Page4(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.side_ultimatum == 0:
            return [
                'ug_proposer_cc1',
                'ug_proposer_cc2',
                'ug_proposer_cc3'
            ]
        elif participant.side_ultimatum == 1:
            return [
                'ug_receiver_cc1',
                'ug_receiver_cc2',
                'ug_receiver_cc3'
            ]
        else:
            return []
    def before_next_page(player, timeout_happened):
        correct_answers_ultimatum(player)
    def is_displayed(player):
        return player.ultimatum_correct_answers < 3 and player.ultimatum_redo_questions


class Page5_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.side_ultimatum==0:
            return [
                'decision_proposer'
            ]
        else:
            pass
    def is_displayed(player):
        participant = player.participant
        return participant.side_ultimatum==0
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.decision_UG = player.decision_proposer
        payoff_UG(participant)


class Page5_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.side_ultimatum == 1:
            return [
                'decision_receiver'
            ]
        else:
            pass
    def is_displayed(player):
        participant = player.participant
        return participant.side_ultimatum == 1
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.decision_UG = player.decision_receiver
        payoff_UG(participant)


class Page6(Page):
    pass

page_sequence = [
    Page1, # Introduction wave 1
    Page2, # Instructions + questions
    Page3, # Ask to re-do
    Page4, # Re-do instructions + questions
    Page5_1, # Decision proposer
    Page5_2 # Decision receiver
#    Page6 # Payoff calculation
]
