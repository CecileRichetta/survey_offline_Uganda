from otree.api import *

doc = """
Support for peace agreement provisions. 
"""

def treatment_other_check_g0_choices(player):
    import random
    shuffled = [
        (0, 'The person is a Northerner'),
        (1, 'The person is a Baganda living in Central Uganda'),
    ]
    fixed = [(998, "Don't know"), (999, 'Prefer not to say')]
    random.shuffle(shuffled)
    return shuffled + fixed

def treatment_other_check_g3_choices(player):
    import random
    shuffled = [(0, 'The LRA'), (1, 'The national army')]
    fixed = [(998, "Don't know"), (999, 'Prefer not to say')]
    random.shuffle(shuffled)
    return shuffled + fixed

class C(BaseConstants):
    NAME_IN_URL = 'app_9_ENG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PARTICIPATION_FEE = 10000
    # CHOICES
    CHOICE_PEACE_SUPPORT = [
        (0, "Not at all"), # Not at all
        (1, "Just a little"), # Just a little
        (2, "Somewhat"), # Somewhat
        (3, "A lot"), # A lot
        (4, "Completely"), # Completely
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]
    CHOICE_NGO_NAME = [
        (0, "1. GUSCO - an NGO working to promote peaceful solution to the conflict"),
        (1, "2. Waiting for Sam"),
        (2, "3. Waiting for Sam")
    ]
    HOPE_SCALE = [
        (0, "Very hopeless"), # Very hopeless
        (1, "Hopeless"), # Hopeless
        (2, "Neither hopeless nor hopeful"), # Neither hopeless nor hopeful
        (3, "Hopeful"), # Hopeful
        (4, "Very hopeful"), # Very hopeful
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    justice_provision_1 = models.IntegerField(
        label="9.1. Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of all previous fighters.",        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of all previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_2 = models.IntegerField(
        label="9.2. Regarding the conflict, please tell me how much do you support the following initiative: Amnesty for only low-rank fighters.",    # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of only low-rank previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_3 = models.IntegerField(
        label="9.3. Regarding the conflict, please tell me how much do you support the following initiative: Release of prisoners of war.",       # Regarding the conflict, please tell me how much do you support the following initiative: Release of prisoners of wars
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_4 = models.IntegerField(
        label="9.4. Regarding the conflict, please tell me how much do you support the following initiative: Reconciliation between the opposing sides.",        # Regarding the conflict, please tell me how much do you support the following initiative: Reconciliation between both sides
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_5 = models.IntegerField(
        label="9.5. Regarding the conflict, please tell me how much do you support the following initiative: Return of refugees of war.",       # Regarding the conflict, please tell me how much do you support the following initiative: Return of refugees of war
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_1 = models.IntegerField(
        label="9.6. Regarding the conflict, please tell me how much do you support the following initiative: Integration of all fighters in the national army.",        # Regarding the conflict, please tell me how much do you support the following initiative: Integration of all fighters in the national army
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_4 = models.IntegerField(
        label="9.7. Regarding the conflict, please tell me how much do you support the following initiative: Federalism. "
              "*Federalism is a mode of government that combines a central government with a regional level of sub-unit governments, "
              "while dividing the powers of governing between the two levels of governments.",        #  Regarding the conflict, please tell me how much do you support the following initiative: Federalism
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    ngo_binary = models.BooleanField(
        label="9.8. Do you want to give part of your participation fee? ",
        # 9.10. Do you want to give part of your participation fee?
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        blank=False
    )
    ngo_amount = models.IntegerField(
        label="9.9. If yes, how much?",
        max=10000,
        blank=True
    )
    ngo_name = models.IntegerField(
        label="9.10.To which NGO?",
        choices=C.CHOICE_NGO_NAME,
        widget=widgets.RadioSelect,
        blank=True
    )
    hope_check = models.IntegerField(
        label="9.11. How hopeful do you feel right now about the possibility of social reconciliation between former fighters and local communities in Northern Uganda?",        #
        choices= C.HOPE_SCALE,
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g3 = models.IntegerField(
        label="9.12.1. During the activities, you played with a Northerner and a former combatant. Which side do you think the other person was a combatant on? (Enumerator Note: Pse read options out loud)",
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g0 = models.IntegerField(
        label="9.12.2. During the activities in this survey and the last survey, you interacted with a partner. What is your guess: (Enumerator Note: Pse read options out loud)",
        blank=False,
        widget=widgets.RadioSelect
    )

# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
            'justice_provision_1',
            'justice_provision_2',
            'justice_provision_3',
            'justice_provision_4',
            'justice_provision_5',
            'military_provision_1',
            'territorial_provision_4'
        ]

class Page2(Page):
    form_model = 'player'
    form_fields = [
        'ngo_binary',
        'ngo_amount',
        'ngo_name'
    ]
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if player.ngo_binary==True and player.ngo_amount !=997:
            participant.participation_fee = C.PARTICIPATION_FEE - player.ngo_amount
        else:
            participant.participation_fee= C.PARTICIPATION_FEE
        participant.total_compensation = participant.participation_fee + participant.payoff_games
    def error_message(player, values):
        # If they want to donate (ngo_binary == True), they must specify amount and NGO
        if values['ngo_binary'] == True:
            if values.get('ngo_amount') is None:
                return 'Please indicate how much to give to the NGO'
            if values.get('ngo_name') is None:
                return 'Please choose an NGO to give to'


class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if player.session.config['name'] == "session_C4P_ENGLISH_w1":
            return ['hope_check']
        elif player.session.config['name'] == "session_C4P_ENGLISH_w2":
            if participant.treatment_other == 0:
                return [
                    'hope_check',
                    'treatment_other_check_g0'
                ]
            elif participant.treatment_other == 3:
                return [
                    'hope_check',
                    'treatment_other_check_g3'
                ]
            else:
                return ['hope_check']


page_sequence = [
    Page1,
    Page2,
    Page3
]
