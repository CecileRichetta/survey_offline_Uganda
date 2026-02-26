from otree.api import *
from random import shuffle


doc = """
Manipulation check and Emotions.
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_7_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # SCALE
    ANSWER_SCALE = [
        (0, "Sikkiriziganya ddala"), # Strongly disagree
        (1, "Sikkiriziganya"), # Disagree
        (2, "Wadde sikkiriziganya oba okukkaanya "), # Neither disagree nor agree
        (3, "Nzikiriza"), # Agree
        (4, "Akkiriziganya ddala"), # Strongly agree
        (998, "Tamanyi"), # Don't know
        (999, "Nsiima obutayogera") # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    empathy_6 = models.IntegerField(
        # dynamic labels in the webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    guilt_1 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    anger_2 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    fear_1 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )


# FUNCTIONS



# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'empathy_6',
        'guilt_1',
        'anger_2',
        'fear_1',
    ]

page_sequence = [
    Page1 # group emotions
]