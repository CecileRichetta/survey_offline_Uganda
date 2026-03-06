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
    NAME_IN_URL = 'app_9_LUO'
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
    HOPE_SCALE_EN = [
        (0, "Very hopeless"), # Very hopeless
        (1, "Hopeless"), # Hopeless
        (2, "Neither hopeless nor hopeful"), # Neither hopeless nor hopeful
        (3, "Hopeful"), # Hopeful
        (4, "Very hopeful"), # Very hopeful
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]
    HOPE_SCALE = [
        (0, "Apeke ki gen matwal"), # Very hopeless
        (1, "Apeke ki gen"), # Hopeless
        (2, "Apeke ki gen onyo atye ki gen"), # Neither hopeless nor hopeful
        (3, "Atye ki gen"), # Hopeful
        (4, "Atye ki gen matek"), # Very hopeful
        (998, "Pe angeyo"), # Don't know
        (999, "Ayero pe me lok") # Prefer not to say
    ]
    OTHER_GROUP = [
        (0, "The LRA"),
        (1, "The national army"),
        (998, "Don't know"),
        (999, "Prefer not to say")
    ]
    OTHER_GROUP_CONTROL = [
        (0, "Baganda"),
        (1, "Northerner"),
        (998, "Don't know"),
        (999, "Prefer not to say")
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    justice_provision_1 = models.IntegerField(
        label="9.1. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man: Timo kica bot lulweny macon weng",
        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of all previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_2 = models.IntegerField(
        label="9.2. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man: Timo kica bot lulweny ma rwom gi obedo lapiny",
        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of only low-rank previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_3 = models.IntegerField(
        label="9.3. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man:  Gonyo mabuc me lweny weng",
        # Regarding the conflict, please tell me how much do you support the following initiative: Release of prisoners of wars
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_4 = models.IntegerField(
        label="9.4. Madok i kom lweny, timber iwaca rwom mene ma icwako kwede tic man: Ribo wat i kin  opojicon (jo ma gin pe yer i kom tam)",
        # Regarding the conflict, please tell me how much do you support the following initiative: Reconciliation between both sides
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_5 = models.IntegerField(
        label="9.5. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man: Dwoko cen oring ayela me lweny",
        # Regarding the conflict, please tell me how much do you support the following initiative: Return of refugees of war
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_1 = models.IntegerField(
        label="9.6. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man: Ribo ki keto lulweny weng me doko lumony pa gamente",
        # Regarding the conflict, please tell me how much do you support the following initiative: Integration of all fighters in the national army
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_4 = models.IntegerField(
        label="9.7. Madok ikom lweny, timber iwaca rwom mene ma icwako kwede tic man: Bedo ki gamente ma poko loc ikin gamente ma malo ki gamente ma piny dok weko gi lone pi ken gi."
              "*Federalism is a mode of government that combines a central government with a regional level of sub-unit governments, "
              "while dividing the powers of governing between the two levels of governments.",
        #  Regarding the conflict, please tell me how much do you support the following initiative: Federalism
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    ngo_binary = models.BooleanField(
        label="9.8. Imito miyo but cente me bedo i tic atima ma megi?",
        # 9.10. Do you want to give part of your participation fee?
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        blank=False
    )
    ngo_amount = models.IntegerField(
        label="9.9. Kace iyer, imiyo marom mene?",
        max=10000,
        blank=True
    )
    ngo_name = models.IntegerField(
        label="9.10. Bot dul ma pe jenge ikom gamente mene?",
        choices=C.CHOICE_NGO_NAME,
        widget=widgets.RadioSelect,
        blank=True
    )
    hope_check = models.IntegerField(
        label="9.12. Itye ki gen marom mene kombedi ni mato oput romo time ikin lulweny macon ki lwak me kin gang itung kumalo me Uganda?",
        # How hopeful do you feel right now about the possibility of a peace process bewteen the central Thai government and armed groups in the Deep South?
        choices= C.HOPE_SCALE,
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g3 = models.IntegerField(
        label="9.12.1. TRANSLATION",
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g0 = models.IntegerField(
        label="9.12.3. TRANSLATION",
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
        if player.session.config['name'] == "session_C4P_LUO_w1":
            return ['hope_check']
        elif player.session.config['name'] == "session_C4P_LUO_w2":
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
