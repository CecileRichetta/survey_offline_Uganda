from otree.api import *
import csv
import os
import shutil
from functools import wraps
from pathlib import Path
from datetime import datetime

doc = """
Final app 
- recall -> if no, debrief
- final thank you
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_12_ENG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TEMPLATE_DEBRIEF_FORM = '_static/texts_ENGLISH/debrief_form.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    recall_phone1 = models.StringField(
        label="12.1. For the payment of the compensation received from the survey and the activities, we will send you mobile money. On which phone number can we send you the money?",
        # phone number for payment
        blank=False
    )
    recall_firstwave = models.BooleanField(
        label="12.2. As mentioned at the beginning of the questionnaire, this is a two-parts study. Would you like to participate in the second wave of this survey?",
        # As mentionned at the beginning of the questionnaire, this is a two-parts study. Would you like to participate in the second wave of this survey?
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        widget=widgets.RadioSelect,
        blank=False
    )
    recall_phone2 = models.StringField(
        label="12.3. If yes, could you please give me the phone number of someone in your household so we can recontact you in case your phone won't be on?",
        # phone number household
        blank=True
    )
    recall_phone3 = models.StringField(
        label="12.4. If yes, could you please give me the phone number of a neighbour so we can recontact you in case your phone won't be on?",
        # phone number neighbor
        blank=True
    )


# DECORATEUR
# VERSION SIMPLE ET ROBUSTE pour tes fonctions
def simple_safe_operation(func):
    """
    Version simple qui protège juste contre les crashes
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erreur dans {func.__name__}: {e}")
            # Log l'erreur mais ne crash pas le participant
            return None
    return wrapper


# FUNCTIONS
@simple_safe_operation
def export_payoffs_headenumerator(player):
    participant = player.participant
    data_folder = Path("_static/data_internal/payoffs")
    timestamp = datetime.now().strftime("%Y_%m_%d_%H:%M")
    csv_file_path = data_folder / "payoffs.csv"
    temp_file = csv_file_path.with_suffix('.tmp')

    data_folder.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        'participant_label', 'date_interview', 'participant_number', 'participation_fee',
        'payoff_games', 'total_compensation'
    ]
    new_row = {
        'participant_label': participant.label,
        'date_interview': timestamp,
        'participant_number': player.recall_phone1,
        'participation_fee': participant.participation_fee,
        'payoff_games': participant.payoff_games,
        'total_compensation': participant.total_compensation
    }

    try:
        if csv_file_path.exists():
            # Copy original to temp, then append new row
            with open(csv_file_path, 'r', newline='') as original:
                with open(temp_file, 'w', newline='') as temp:
                    temp.write(original.read())
            with open(temp_file, 'a', newline='') as temp:
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writerow(new_row)
        else:
            # Create new file with header
            with open(temp_file, 'w', newline='') as temp:
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(new_row)

        # Replace original with temp
        os.replace(temp_file, csv_file_path)

        # Si tout va bien, effacer les données
        player.recall_phone1 = "Anonymous"

    except Exception as e:
        if temp_file.exists():
            os.remove(temp_file)
        print(f"Erreur dans export_payoffs_headenumerator: {e}")
        raise e

@simple_safe_operation
def export_recall(player):
    participant = player.participant
    data_folder = Path("_static/data_internal/for_wave_2")
    csv_file_path = data_folder / "recall.csv"
    temp_file = csv_file_path.with_suffix('.tmp')
    # Create directory if it doesn't exist
    data_folder.mkdir(parents=True, exist_ok=True)
    try:
        new_data = {
            'participant_label': participant.label,
            'participant_name': participant.recontact,
            'participant_phone': player.recall_phone1,
            'participant_phone_family': player.recall_phone2,
            'participant_phone_neighbor': player.recall_phone3
        }

    # PROTECTION: Écrire dans temp d'abord
        if csv_file_path.exists():
            # Copier l'original vers temp
            shutil.copy2(csv_file_path, temp_file)

             # Ajouter la nouvelle ligne au temp
            with open(temp_file, 'a', newline='') as f:
                # Lire le header du fichier original pour l'ordre des colonnes
                with open(csv_file_path, 'r', newline='') as orig:
                    reader = csv.DictReader(orig)
                    fieldnames = reader.fieldnames

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(new_data)
        else:
            # Créer nouveau fichier dans temp
            fieldnames = list(new_data.keys())
            with open(temp_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(new_data)

        # Si tout va bien, remplacer l'original
        shutil.move(temp_file, csv_file_path)

        # Si tout va bien, effacer les données
        participant.recontact = "Anonymous"
        player.recall_phone1 = "Anonymous"
        player.recall_phone2 = "Anonymous"
        player.recall_phone3 = "Anonymous"

    except Exception as e:
         # Nettoyer le fichier temp en cas d'erreur
        if temp_file.exists():
            os.remove(temp_file)
        print(f"Erreur dans export_recall: {e}")
        raise e


# PAGES
class Page1_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        participant = player.participant
        if participant.dropout is False and player.session.config['name'] == "session_C4P_ENGLISH_w1":
            return [
                'recall_phone1',
                'recall_firstwave',
                'recall_phone2',
                'recall_phone3'
            ]
        else:
            pass
    def before_next_page(player, timeout_happened):
        phone_1 = player.recall_phone1
        export_payoffs_headenumerator(player)
        if player.recall_firstwave is True:
            player.recall_phone1 = phone_1
            export_recall(player)
    def is_displayed(player):
        participant = player.participant
        return not participant.dropout and player.session.config['name'] == "session_C4P_ENGLISH_w1"
    def error_message(player, values):
        # Validate recall fields: required if recall_firstwave == True (only in wave 1)
        if 'recall_firstwave' in values and values['recall_firstwave'] == True:
            if not values.get('recall_phone2') or values['recall_phone2'].strip() == '':
                return 'Please indicate a family phone number or "999" if the respondent refuses'
            if not values.get('recall_phone3') or values['recall_phone3'].strip() == '':
                return 'Please indicate a neighbor phone number or "999" if the respondent refuses'


class Page1_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        participant = player.participant
        if participant.dropout is False and player.session.config['name'] == "session_C4P_ENGLISH_w2":
            return [
                'recall_phone1'
            ]
        else:
            pass
    def before_next_page(player, timeout_happened):
        export_payoffs_headenumerator(player)
    def is_displayed(player):
        participant = player.participant
        return not participant.dropout and player.session.config['name'] == "session_C4P_ENGLISH_w2"

class Page2(Page):
    pass
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        return (not participant.dropout) and (
                (player.field_maybe_none('recall_firstwave') is False and participant.treatment_hope == 1) or
                (player.session.config['name'] == "session_C4P_ENGLISH_w2" and participant.treatment_hope == 1)
        )


class Page3(Page):
    pass


page_sequence = [
    Page1_1,
    Page1_2,
    Page2,
    Page3
]
