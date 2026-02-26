from otree.api import *

doc = """
Support for peace agreement provisions. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_9_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PARTICIPATION_FEE = 10000
    # CHOICES
    CHOICE_PEACE_SUPPORT = [
        (0, "Not at all"),  # Not at all
        (1, "Just a little"),  # Just a little
        (2, "Somewhat"),  # Somewhat
        (3, "A lot"),  # A lot
        (4, "Completely"),  # Completely
        (998, "Don't know"),  # Don't know
        (999, "Prefer not to say")  # Prefer not to say
    ]
    CHOICE_NGO_NAME = [
        (0, "1. GUSCO - an NGO working to promote peaceful solution to the conflict"),
        (1, "2. Habitat International - an NGO working to improve access to housing for the poor"),
        (2, "3. World Vision International - an NGO working to help children and vulnerable communities."),
        (997, "Not applicable")
    ]
    HOPE_SCALE_EN = [
        (0, "Very hopeless"),  # Very hopeless
        (1, "Hopeless"),  # Hopeless
        (2, "Neither hopeless nor hopeful"),  # Neither hopeless nor hopeful
        (3, "Hopeful"),  # Hopeful
        (4, "Very hopeful"),  # Very hopeful
        (998, "Don't know"),  # Don't know
        (999, "Prefer not to say")  # Prefer not to say
    ]
    HOPE_SCALE = [
        (0, "Talina ssuubi nyo"), # Very hopeless
        (1, "Talina ssuubi nyo"), # Hopeless
        (2, "Tewali ssuubi wadde essuubi"), # Neither hopeless nor hopeful
        (3, "Essuubi"), # Hopeful
        (4, "Essuubi nnyo"), # Very hopeful
        (998, "Tamanyi"), # Don't know
        (999, "Nsiima obutayogera") # Prefer not to say
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
        label="9.1. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Okuddiramu/okusonyiwa abalwanyi bonna.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of all previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_2 = models.IntegerField(
        label="9.2. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Okuddiramu/okisonyiwo kya abo bokka abali ku balwanyi b'omutendera gwa wansi bokka.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of only low-rank previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_3 = models.IntegerField(
        label="9.3. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Okuteebwa kwabo bonna abasibwa olwentalo.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Release of prisoners of wars
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_4 = models.IntegerField(
        label="9.4. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Onteseganya wakati we njuuyi ezivuganya.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Reconciliation between both sides
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    justice_provision_5 = models.IntegerField(
        label="9.5. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Okuzaayo ababundabunda bentalo.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Return of refugees of war
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_1 = models.IntegerField(
        label="9.6. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Okugatta awamu abalwanyi bonna mu jje lye ggwanga.",
        # Regarding the conflict, please tell me how much do you support the following initiative: Integration of all fighters in the national army
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_4 = models.IntegerField(
        label="9.7. Ku bikwata ku bukubagano, bambi owagira kyenkana kyi enteekateeka zinno wammanga: Effuga elya Federo."
              "*Fedelo ye ffuga erigata gavumenti eyawakati ku gavumenti ya matwale amatono nga bagabana obuyinza mu bukulembeze.",
        #  Regarding the conflict, please tell me how much do you support the following initiative: Federalism
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    ngo_binary = models.BooleanField(
        label="9.8. Wandiyagadde okuwaayonekitundu ku kasiimo ko akokwetabamu? ",
        # 9.10. Do you want to give part of your participation fee?
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        blank=False
    )
    ngo_amount = models.IntegerField(
        label="9.9. Bwekiba yye, Ssente mmeka?",
        blank=True
    )
    ngo_name = models.IntegerField(
        label="9.10. Eri ekitongole kyi? ",
        choices=C.CHOICE_NGO_NAME,
        widget=widgets.RadioSelect,
        blank=True
    )
    hope_check = models.IntegerField(
        label="9.12. Owulira suubi lyenkana kyi kati ku kusoboka kwokusonyiwagana wakati wa baali abalwanyi ne abantu babulijjo mu bitundu by'omumambuka ga Uganda?",
        # How hopeful do you feel right now about the possibility of a peace process bewteen the central  government and armed groups in the Deep South?
        choices= C.HOPE_SCALE,
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g3 = models.IntegerField(
        label="9.12.1. TRANSLATION",
        choices=C.OTHER_GROUP,
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g1 = models.IntegerField(
        label="9.12.3. TRANSLATION",
        choices=C.OTHER_GROUP_CONTROL,
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
        if participant.treatment_other == 3:
            return [
                'hope_check',
                'treatment_other_check_g3'
            ]
        elif participant.treatment_other == 0 and player.session.config['name'] == "session_C4P_LUGANDA_w2":
            return [
                'hope_check',
                'treatment_other_check_g1'
            ]
        else:
            return ['hope_check']


page_sequence = [
    Page1,
    Page2,
    Page3
]