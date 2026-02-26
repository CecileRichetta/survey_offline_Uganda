from otree.api import *
import random

doc = """
Economics questions
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_10_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # CHOICES IN VARIABLES
    BINARY_ANSWER = [
        (1, 'Yee'), # Yes
        (0, 'Nedda'),  # No
        (998, "Tamanyi"), # don't know
        (999, 'Nsiima obutayogera')  # Prefer not to say
    ]
    ETHNIC_COMP = [
        (0, "Eggwanga lye limu nga nze"), # Same ethnic group as me
        (1, "Eggwanga ery'enjawulo okusinga nze"), # A different ethnic group than me
        (2, "Ebitabuddwa: Ebimu biva mu ggwanga lye limu, ebirala si"), # Mixed: Some are from the same ethnic group as me, others not
        (998, "Tamanyi"),  # Don't know
        (999, 'Nsiima obutayogera')  # Prefer not to say
    ]
    ECONOMIC_STATUS_1 = [
        (0, 'Kibbi nnyo'), # Completely disagree
        (1, 'Fairly bad'), # Disagree
        (2, 'Sikibbi sikilungi'), # Neither disagree or agree
        (3, 'Kirungi muko'), # Agree
        (4, 'Kirungi nnyo'), # Completely agree
        (998, "Tamanyi"),  # Don't know
        (999, 'Nsiima obutayogera') # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # SOCIO-DEM VARIABLES
    asset_1 = models.IntegerField(
        label="10.1. Nsaba okumannya oba binno wamanga obiyinna: Pikipiki ekola",
        # Do you have the following at home: motorcycle
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    asset_2 = models.IntegerField(
        label="10.2. Nsaba okumannya oba binno wamanga obiyinna: Eggali ekola",
        # Do you have the following at home: bicycle
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    asset_3 = models.IntegerField(
        label="10.3. Nsaba okumannya oba binno wamanga obiyinna: Ente ne Mbuzi",
        # Do you have the following at home: cows or goats
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    ethnic_composition = models.IntegerField(
        label="10.4. Bantu abasiinga mu kyalo/ku muliraano  ggwo olowooza  ba ggwanga kyi? ",
        #
        choices=C.ETHNIC_COMP,
        widget=widgets.RadioSelect,
        blank=False
    )
    eco_status_1 = models.IntegerField(
        label="10.5. Okutwaliza awamu, osobola kunyonyola otya embeera yo jolimu kati?", # In general, how would you describe your own present living conditions?
        widget=widgets.RadioSelect,
        choices=C.ECONOMIC_STATUS_1,
        blank=False
    )
    eco_status_2 = models.StringField(
        label="10.6. Ngogatta ku makubo gojjamu enyingizaayo, Enyingizaayo nga amaka buli mwezi(nga tonajjako musolo, ezekitta vvu Kya bakozi nensasanya endala)?",
        # Adding up your sources of income, what is your household's gross monthly income (before deducting taxes, social security contributions and other expenses)?
        blank=False
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
        return player.session.config['name'] == "session_C4P_LUGANDA_w1"

page_sequence = [
    Page1 # socio-demographics
]
