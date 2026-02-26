from otree.api import *

doc = """
Demographics questions
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_2_ENG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    VENN_ENGLISH = 'imgs/Venn_english.png'
    # CHOICES IN VARIABLES
    GENDER = [
        (0, 'Man'), # Man
        (1, 'Woman'), # Woman
        (999, 'Prefer not to say') # Prefer not to say
    ]
    EDUCATION = [
        (0, 'No schooling'),  # No schooling
        (1, 'Some primary school'),  # Some primary school
        (2, 'Completed primary school'),  # Completed primary school
        (3, 'Some Secondary _O Level'),  # Some Secondary_O Level
        (4, "Completed Secondary _O level"),  # Completed Secondary O-level
        (5, "Some secondary _A Level"),  # Some secondary _A Level
        (6, 'Completed Secondary _A level'),  # Completted Secondary A-level
        (7, "Some Tertiary"),  # Some Tertairy
        (8, 'Completed Tertiary'),  # Completed tertiary
        (9, 'Other'),  # Other
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    DEPENDENTS_SALARY = [
        (0, "One person"), # one person
        (1, "Two people"), # two people
        (2, "Three people"), # three people
        (3, "Four people"), # four people
        (4, "Five people"), # five people
        (5, "More than five people"), # more than give people
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]
    RELIGION = [
        (0, 'Islam'), # Islam
        (1, 'Christianity'), # Christianity
        (2, "Indigenous/traditionalist Religion"), # Indigenous/traditionalist Religion
        (3, "Other"), # Other
        (4, "I don't believe in any"), # I don't believe in any
        (999, 'Prefer not to say') # Prefer not to say
    ]
    RELIGIOSITY = [
        (0, "Not religious at all"), # Not religious at all
        (1, "Somewhat religious"), # Somewhat religious
        (2, "Religious"), # Religious
        (3, "Very religious"), # Very religious
        (997, 'Not applicable'),  # Not applicable
        (999, 'Prefer not to say') # Prefer not to say
    ]
    INSECURITY = [
        (0, 'Never'), # Never
        (1, 'Just once or twice'), # Just once or twice
        (2, 'Several times'), # Several times
        (3, 'Many times'), # Many times
        (4, 'Always'), # Always
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]
    ETHNIC_GROUP = [
        (0, 'Acholi'), #
        (1, 'Muganda'), #
        (2, 'Alur'), #
        (3, 'Langi'), #
        (4, 'Musoga'), #
        (5, "Munyoro"), #
        (6, "Other"), # Oher
        (999, 'Prefer not to say') # Prefer not to say
    ]
    SCALE_AGREEMENT = [
        (0, 'Completely disagree'), # Completely disagree
        (1, 'Disagree'), # Disagree
        (2, 'Neither disagree or agree'), # Neither disagree or agree
        (3, 'Agree'), # Agree
        (4, 'Completely agree'), # Completely agree
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]
    BINARY_ANSWER = [
        (1, 'Yes'),  # Yes
        (0, 'No'), # No
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    BINARY_ANSWER_NA = [
        (1, 'Yes'),  # Yes
        (0, 'No'), # No
        (997, 'Not applicable'), # Not applicable
        (999, 'Prefer not to say') # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # SOCIO-DEM VARIABLES
    recall = models.StringField(
        label="2.1. What is your name",
        # what is your name
        blank=False
    )
    age = models.IntegerField(
        label="2.2. How old are you (in years)?", # Please indicate how old you are (in years):
        min=18,
        max=75,
        blank=False
    )
    gender = models.IntegerField(
        label="2.3. Gender of the respondent: (Enumerator note: if unclear, pse ask: What is your gender?)", # Which gender do you identify with:
        choices=C.GENDER,
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    education = models.IntegerField(
        label="2.4. What is your highest level of education completed? ", # What is your highest level of education completed?
        choices=C.EDUCATION,
        blank=False,
        widget=widgets.RadioSelect
    )
    education_other = models.StringField(
        label="2.4.1. If other, please specify: ",
        blank=True
    )
    dependents_salary = models.IntegerField(
        label="2.5. How many people live in your household? By Household, we mean people who live together in the same dwelling, share meals and share the same descision making forum. Please exclude any visitors and any temporary occupants.",
        # How many people live in your household? + definition household
        choices=C.DEPENDENTS_SALARY,
        widget=widgets.RadioSelect,
        blank=False
    )
    religion = models.IntegerField(
        label="2.6. What is your religion? ", # what is your religion?
        choices=C.RELIGION,
        widget=widgets.RadioSelect,
        blank=False
    )
    religiosity = models.IntegerField(
        label="2.7. How religious are you?", # how religious are you?
        choices=C.RELIGIOSITY,
        widget=widgets.RadioSelect,
        blank=True
    )
    insecurity = models.IntegerField(
        label="2.8. Over the past year, how often, if ever, have you or anyone in your family felt unsafe in your home or neighborhood?",
        # Over the past year, how often, if ever, have you or anyone in your family felt unsafe in your home or neighborhood?
        choices=C.INSECURITY,
        widget=widgets.RadioSelect,
        blank=False
    )
    ethnic_group = models.IntegerField(
        label="2.9. What is your ethnic group?",
        # What is your ethnic group?
        choices=C.ETHNIC_GROUP,
        widget=widgets.RadioSelect,
        blank=False
    )
    ethnic_other = models.StringField(
        label="2.9.1. If other, please specify: ",
        blank=True
    )
    group_attachment_1 = models.IntegerField(
        choices=C.SCALE_AGREEMENT,
        widget=widgets.RadioSelect,
        blank=False
    )
    group_attachment_2 = models.IntegerField(
        choices=C.SCALE_AGREEMENT,
        widget=widgets.RadioSelect,
        blank=False
    )
    venn_1 = models.IntegerField(
        choices=[
            (0, "(1)"),
            (1, "(2)"),
            (2, "(3)"),
            (3, "(4)"),
            (4, "(5)"),
            (998, "Don't know"),
            (999, "Refuse to answer")
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )

# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'recall',
        'age',
        'gender',
        'education',
        'education_other',
        'dependents_salary',
        'religion',
        'religiosity',
        'insecurity',
        'ethnic_group',
        'ethnic_other'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.age = player.age
        participant.recontact = player.recall
        player.recall = "Anonymous"
        if player.ethnic_group == 0:
            participant.group = 0
            print(participant.group)
        else:
            participant.group = 1
            print(participant.group)
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_ENGLISH_w1"
    def error_message(player, values):
        if values['education'] == 9:
            if not values.get('education_other') or str(values['education_other']).strip() == '':
                return 'Please fill other education field'
        if values['religion'] != 4 and values['religion'] != 999:
            if values.get('religiosity') is None:
                return 'Please fill religiosity field'
        if values['ethnic_group'] == 6:
            if not values.get('ethnic_other') or str(values['ethnic_other']).strip() == '':
                return 'Please fill other ethnicity field'



class Page2(Page):
    form_model = 'player'
    form_fields = [
        'group_attachment_1',
        'group_attachment_2',
        'venn_1'
    ] # dynamic labels coded in html webpage

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_ENGLISH_w1"


page_sequence = [
    Page1, # socio-demographics
    Page2 # group attachment with dynamic labels
]
