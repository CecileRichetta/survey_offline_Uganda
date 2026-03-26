from otree.api import *
import csv
from datetime import datetime


doc = """
Consent form for Pilot Study

Elements
- app_1 form -> end of the study if participant does not app_1 

"""
def district_choices(player):
    participant = player.participant
    label = participant.label or ""
    if label.startswith("AN"):
        return [
            ("Gulu District"),
            ("Gulu City"),
            ("Nwoya"),
            ("Amuru"),
            ("Kitgum"),
            ("Lamwo"),
            ("Omoro"),
        ]
    elif label.startswith("NAN"):
        return [
            ('Gulu District'),
            ('Mityana'),
        ]
    elif label.startswith("NAS"):
        return [
            ("Mityana"),
        ]
    else:
        return [
            ("Gulu District"),
            ("Gulu City"),
            ("Nwoya"),
            ("Amuru"),
            ("Kitgum"),
            ("Lamwo"),
            ("Omoro"),
            ('Mityana')
        ]

class C(BaseConstants):
    NAME_IN_URL = 'module_1_LUG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # PAYMENT INFO VARIABLES
    DATA_TREATMENT_W1_LOC = 'data_internal/for_wave_2/'
    # CONSTANTS
    TOKEN_ENDOWMENT = 4
    ENUMERATORS = [
        "Semirembe Godfrey",
        "Tusiime Timothy",
        "Komakech David",
        "Abwot Sandra",
        "Gum Samuel",
        "Guma Ninah"
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    enumerator = models.StringField(
        label="1.1. Enumerator:", # enter your enumerator identifier
        choices=C.ENUMERATORS,
        blank=False
    )
    district = models.StringField(
        label="1.2. What is the district?", #
        blank=False
    )
    subcounty = models.StringField(
        label="1.3. What is the subcounty?", #
        blank=False
    )
    parish = models.StringField(
        label="1.4. What is the parish?",
        blank=False
    )
    village = models.StringField(
        label="1.5. What is the village?",
        blank=False
    )
    urban_rural = models.IntegerField(
        label="1.6. Is it an urban or rural setting?",
        choices=((0, "Urban"), # urban
                 (1, "Rural")), # rural
        widget=widgets.RadioSelect,
        blank=False
    )
    timestamp = models.StringField()
    consent = models.BooleanField(choices=[[True, 'Yes'],
                                           [False, 'No']],
                                  label='1.7. Okiriza okwetaba mu musomo gunno?',
                                  widget=widgets.RadioSelect)
    p_label = models.StringField()


# FUNCTIONS
def extract_participant_w1(p):
    participant = p.participant
    with open("_static/data_internal/for_wave_2/participant_wave_1.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Participant_label'] == participant.label:
                participant.group = int(row['Participant_group'])
                participant.etv = int(row['Participant_etv'])
                participant.treatment_hope = int(row['Participant_treatment_hope'])
                participant.side_ultimatum = int(row['Participant_side_ultimatum'])
                participant.treatment_other = int(row['Participant_treatment_other'])
                break


# PAGES
class Page0(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = [
        'enumerator',
        'district',
        'subcounty',
        'parish',
        'village',
        'urban_rural'
    ]
    @staticmethod
    def error_message(player, values):
        # Validate name field
        raw_name_subcounty = str(values.get('subcounty', '') or '').strip()
        if raw_name_subcounty != '':
            if not raw_name_subcounty.replace(' ', '').isalpha():
                return 'Subcounty: Please enter alphabetical characters only (no numbers or special characters).'
        raw_name_parish = str(values.get('parish', '') or '').strip()
        if raw_name_parish != '':
            if not raw_name_parish.replace(' ', '').isalpha():
                return 'Parish: Please enter alphabetical characters only (no numbers or special characters).'
        raw_name_village = str(values.get('village', '') or '').strip()
        if raw_name_village != '':
            if not raw_name_village.replace(' ', '').isalpha():
                return 'Village: Please enter alphabetical characters only (no numbers or special characters).'

class Page2(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        label = participant.label or ""

        # Determine which text file to use based on label prefix
        if player.session.config['name'] == "session_C4P_LUGANDA_w1":
            if label.startswith("AN"):
                text_file = "consent_form_w1_AN.html"  # or whatever your file is named
            elif label.startswith("NAN"):
                text_file = "consent_form_w1_NAN.html"
            else:
                text_file = "consent_form_w1_NAS.html"  # default fallback

            # Read the text file
            import os
            file_path = os.path.join('_static', 'texts_LUGANDA', text_file)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text_content = f.read()
            except FileNotFoundError:
                text_content = "Text file not found."

            return dict(
                text_content = text_content.replace('ENUMERATOR_NAME', player.enumerator)
            )
        else:
            if label.startswith("AN"):
                text_file = "consent_form_w2_AN.html"  # or whatever your file is named
            elif label.startswith("NAN"):
                text_file = "consent_form_w2_NAN.html"
            else:
                text_file = "consent_form_w2_NAS.html"  # default fallback

            # Read the text file
            import os
            file_path = os.path.join('_static', 'texts_LUGANDA', text_file)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text_content = f.read()
            except FileNotFoundError:
                text_content = "Text file not found."

            return dict(
                text_content = text_content.replace('ENUMERATOR_NAME', player.enumerator)
            )
    def before_next_page(player: Player, timeout_happened):
        current_datetime = datetime.now()
        player.timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        participant = player.participant
        participant.participation_fee = 10000
        participant.vars['consent'] = player.consent
        participant.dropout = not player.consent
        player.p_label = participant.label
        if player.session.config['name']=="session_C4P_LUGANDA_w2":
            participant.military_binary = 997
            extract_participant_w1(player)
        else:
            pass
    def app_after_this_page(player: Player, upcoming_apps):
        if not player.consent:
            participant = player.participant
            participant.dropout = True  # custom field in Player model
            participant.treatment_hope = 999
            participant.participation_fee = 0
            return upcoming_apps[-1]

page_sequence = [
    Page0,
    Page1, # enumerator identifier
    Page2 # consent form
]
