from otree.api import *


doc = """
Questions about trust.
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_8_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WVS_SCALE = [
        (0, "You have to be very cautious"), # You have to be very cautious
        (1, "Most people can be trusted"), # Most people can be trusted
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]
    WALLET_SCALE = [
        (0, "Not at all likely"), # Not at all likely
        (1, "Not very likely"), # Not very likely
        (2, "Neither likely nor unlikely"), # Neither likely nor unlikely
        (3, "Quite likely"), # Quite likely
        (4, "Very likely"), # Very likely
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
        ]
    TRUST_SCALE = [
        (0, "Not at all"), # Not at all
        (1, "A little"), # A little
        (2, "Somewhat"), # Somewhat
        (3, "A lot"), # A lot
        (4, 'Completely'), # Completely
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]
    IG_OG_TRUST_SCALE = [
        (0, "Completely disagree"), # Completely disagree
        (1, "Disagree"), # Disagree
        (2, "Neither disagree nor agree"), # Neither disagree nor agree
        (3, "Agree"), # Agree
        (4, "Completely agree"), # Completely agree
        (998, "Don't know"), # Don't know
        (999, "Prefer not to say") # Prefer not to say
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Social trust
    social_trust_wvs = models.IntegerField(
        label="8.1. Mukutwaliza awamu, oyinza okugamba abantu abasiinga besigika oba oyinza okugamba kyetagisa okwegendereza nga tukolaganga nabantu abasiinga?",
        # Generally speaking, would you say that most people can be trusted or would you say it’s necessary to be "
        #               "very cautious when dealing with most people?
        choices=C.WVS_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_wallet = models.IntegerField(
        label="8.2. Singa obuliddwako akasawo mwotereka nga kalimu ebikwata ku ndagiriro yo, nezulibwa ku luguudo lwa mulirwanwa wo. Kisoboka kyenkana kyi nti ejja komezebwawo jooli nga temuli kibulamu?",
        # Suppose you lost your purse/wallet containing your address details, and it was found in the street by "
        #               "someone living in the neighborhood you last lived in, in your home country. How likely is it that it would "
        #               "be returned to you with nothing missing?
        choices= C.WALLET_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_2 = models.IntegerField(
        label="8.3. Bambi mbulira wesiga kyenkana kyi: Famire yo? ",
        # Please tell me how much you trust: Your family.
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_3 = models.IntegerField(
        label="8.4. Bambi mbulira wesiga kyenkana kyi: Balilanwa bo?",
        # Please tell me how much you trust: Your neighbors.
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # Intergroup trust
    intergroup_trust_3 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    intergroup_trust_4 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    intergroup_trust_7 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # Outgroup trust
    outgroup_trust_3 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    outgroup_trust_4 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    outgroup_trust_7 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # institutional trust
    institutional_trust_1 = models.IntegerField(
        label="8.11. Bambi mbulira wesiga kyenkana kyi abantu bano banno wammanga: Omukulembeze we ggwanga",
        # The president
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_2 = models.IntegerField(
        label="8.12. Bambi mbulira wesuga kyenkana kyi abantu bano banno wammanga: Olukiiko oluyisa amateeka/ Palaamenti",
        # The parliament
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_7 = models.IntegerField(
        label="8.13. Bambi mbulira wesuga kyenkana kyi abantu bano banno wammanga: Poliisi",
        # The Police
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_8 = models.IntegerField(
        label="8.14. Bambi mbulira wesuga kyenkana kyi abantu bano banno wammanga: Amajje",
        # The army
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_9 = models.IntegerField(
        label="8.15. Bambi mbulira wesuga kyenkana kyi abantu bano banno wammanga: Essiga Eddamuzi oba Kooti za mateeka",
        # The courts of law
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_10 = models.IntegerField(
        label="8.16. Bambi mbulira wesuga kyenkana kyi abantu bano banno wammanga: Abakulembeze ab'ennono",
        # The traditional leaders
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )



# PAGES

class Page1(Page):
    form_model = 'player'
    form_fields = [
        'social_trust_wvs',
        'social_trust_wallet',
        'social_trust_2',
        'social_trust_3',
    ]


class Page2(Page):
    form_model = 'player'
    form_fields = [
        'intergroup_trust_3',
        'intergroup_trust_4',
        'intergroup_trust_7'
    ]


class Page3(Page):
    form_model = 'player'
    form_fields = [
        'outgroup_trust_3',
        'outgroup_trust_4',
        'outgroup_trust_7'
    ]


class Page4(Page):
    form_model = 'player'
    form_fields = [
        'institutional_trust_2',
        'institutional_trust_7',
        'institutional_trust_1',
        'institutional_trust_8',
        'institutional_trust_9',
        'institutional_trust_10'
    ]

page_sequence = [
    Page1, # social trust
    Page2, # ingroup trust
    Page3, # outgroup trust
    Page4 # institutional trust
]
