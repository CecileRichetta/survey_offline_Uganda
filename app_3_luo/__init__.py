from otree.api import *
import random
import csv

doc = """
Questions military service and exposure to violence"""


class C(BaseConstants):
    NAME_IN_URL = 'app_3_LUO'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # EXTERNAL DATA
    DATA_TREATMENT_LOC = '_static/data_external/treatment_balance.csv'
    # CHOICES IN VARIABLES
    UNIT_TIME = [
        (1, "Days"),
        (2, "Weeks"),
        (3, "Months"),
        (4, "Years"),
        (999, "Prefer not to say")
    ]
    BINARY_ANSWER = [
        (1, 'Yes'),  # Yes
        (0, 'No'), # No
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    LRA_CONSCRIPTION = [
        (0, 'Join voluntarily'), # Join voluntarily
        (1, 'Abdudcted '), # Abudcted
        (2, "Born in the bush"), # Born in the bush
        (999, 'Prefer not to say') # Prefer not to say
    ]
    SUBREGION_UGANDA = [
        (1, 'Acholi subregion'),  #
        (2, 'Lango subregion'),  #
        (3, 'West Nile subregion'),  #
        (4, 'Teso subregion'),  #
        (5, 'Karamoja subregion'),  #
        (6, 'Central region'),
        (7, 'South Sudan'),  #
        (8, 'DRC'),  #
        (9, 'Central African Republic'),  #
        (10, 'Sudan'),
        (11, 'Other'),
        (999, 'Prefer not to say') # Prefer not to say
    ]
    MONTH = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say') # Prefer not to say
    ]
    SCALE_EMPHASIS = [
        (0, 'None'), # None
        (1, 'Some'), # Some
        (2, 'A lot'), # A lot
        (998, "Don't know"),  # Don't know
        (999, 'Prefer not to say')  # Prefer not to say
    ]
    SCALE_SUPPORT = [
        (0, "Not at all"),  # Not at all
        (1, "Somewhat"),  # Somewhat
        (2, "Completely"),  # Completely
        (998, "Tamanyi"),  # Don't know
        (999, "Prefer not to say")  # Prefer not to say
    ]
    SCALE_ETV = [
        (0, 'Rarely'), # Rarely
        (1, 'Often'), # Often
        (999, 'Prefer not to say')  # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # MILITARY SERVICE
    military_binary = models.IntegerField(
        label="3.1. Manaka tika ibedo I lweny mony pa LRA in ki komi?",
        # Have you ever been directly involved in the LRA Bush conflict?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    # QUESTIONS MILITARY
    lra_conscription = models.IntegerField(
        label="3.2.1. Iyoo mene ma ibedo kwede ilweny man?",
        # How did you get involved?
        choices=C.LRA_CONSCRIPTION,
        widget=widgets.RadioSelect,
        blank=False
    )
    lra_length = models.IntegerField(
        label="3.2.2. Pi kare ma rom mene ma ibedo ilum ki adwii pa LRA? (If respondent prefers not to say, enter '999')",
        # For how long were you involved in the bush with the LRA? (in years)
        min=0,
        blank=False
    )
    lra_length_unit = models.IntegerField(
        label="3.2.2.1. Unit:",
        choices=C.UNIT_TIME,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    military_province_main = models.IntegerField(
        label="3.2.3. Kabedo mene mapol kare ibedo  iye ikare me lweny pa LRA?",
        # In which subregion were you primarily located during your time in the LRA?
        choices=C.SUBREGION_UGANDA,
        blank=False
    )
    military_province_main_other = models.StringField(
        label="3.2.3.1. If other, please specify:",
        blank=True
    )
    maindeployment_start_year = models.IntegerField(
        label="3.2.4. I mwaka mene ma icako bedo i kabedo meno?",
        # 3.1.5. In which year did you start to be in that subregion?
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    maindeployment_start_month = models.IntegerField(
        label="3.2.5. Ocake idwe mene?",
        #in which starting month?
        choices=C.MONTH,
        blank=False
    )
    maindeployment_length = models.IntegerField(
        label="3.2.6. Pi kare ma rom mene ma ibedo I kabedo meno ki LRA? (If respondent prefers not to say, enter '999')",
        # How long were you in that region with the LRA (number of months)?
        blank=False
    )
    maindeployment_length_unit = models.IntegerField(
        label="3.2.6.1. Unit",
        choices=C.UNIT_TIME,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    deployment_second = models.IntegerField(
        label="3.2.7. Tika ibedo i kabedo mukene mapat ikare ma onongo itye bot LRA?",
        # Were you deployed in any other province?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_province_second = models.IntegerField(
        label="3.2.8. Kabedo mukene mene ma ibedo iye ikare ma itye bot mony pa LRA? (yer kama pol kare ibedo iye mapat ki kabedo ma lakwongi)",
        # If yes, in which province were you deployed?
        choices=C.SUBREGION_UGANDA,
        blank=True
    )
    military_province_second_other = models.StringField(
        label="3.2.8.1. If other, please specify:",
        blank=True
    )
    seconddeployment_start_year = models.IntegerField(
        label="3.2.9. I mwaka mene ma ibedo i kabedo meno?",
        # In which YEAR were you deployed in this province?
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    seconddeployment_start_month = models.IntegerField(
        label="3.2.10. Ocake idwe mene?",
        # 3.1.11. In which starting month:
        choices=C.MONTH,
        blank=True
    )
    seconddeployment_length = models.IntegerField(
        label="3.2.11. Pi kare ma rom mene ma ibedo irii ikabedo meno? (If respondent prefers not to say, enter '999')",
        # How long were you been stationed in that subregion (number of months)?
        min=0,
        blank=True
    )
    seconddeployment_length_unit = models.IntegerField(
        label="3.2.11.1. Unit",
        choices=C.UNIT_TIME,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    military_socialization_1 = models.IntegerField(
        label="3.2.12. I kare ma ibedo i LRA, pi rwom ma rom mene ma onongo mite tutwale me woro loc?",
        # During your service, how much emphasis was placed on respect for authority?
        choices=C.SCALE_EMPHASIS,
        widget = widgets.RadioSelect,
        blank=False
    )
    military_socialization_2 = models.IntegerField(
        label="3.2.13. I kare ma ibedo i LRA, rwom marom mene ma onongo giketo calo gin mapire tek me niang gin maracu me "
              "lobo man ite kare eno ni, labole calo UPDF?",
        # During your service, how much emphasis was placed on understand the domestic security threats of the time?
        choices=C.SCALE_EMPHASIS,
        widget = widgets.RadioSelect,
        blank=False
    )
    military_socialization_3 = models.IntegerField(
        label="3.2.14. I kare ma ibedo I LRA, rwom  marom mene ma onongo ijenge I kom kony  ki bot jo mukene maki mako gi?",
        # During your service, how much could you count on your peers for support?
        choices=C.SCALE_SUPPORT,
        widget = widgets.RadioSelect,
        blank=False
    )
    # QUESTIONS NON-MILITARY
    noncombatant_geography_main = models.IntegerField(
        label="3.3.1. Ikine me mwaka ma kinywali kwede ki 2025, pole imaro bedo kwene?",
        # 3.2.1. Between 'the year you were born' and 2025, in which subregion did you primarily reside?
        choices= C.SUBREGION_UGANDA,
        blank=False
    )
    noncombatant_geography_main_other = models.StringField(
        label="3.3.3.1. If other, please specify:",
        blank=True
    )
    noncombatant_geography_main_start_year = models.IntegerField(
        label="3.3.2. I mwaka mene ma icako bedo i kabedo meno?",
        # In which period did you reside in this province?
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    noncombatant_geography_main_start_month = models.IntegerField(
        label="3.3.3. Ocake idwe mene?", # start month
        choices=C.MONTH,
        blank=False
    )
    noncombatant_geography_main_end_year = models.IntegerField(
        label="3.3.4. Me oo imwaka mene?",
        # 3.2.3. Until what year?:
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    noncombatant_geography_main_end_month = models.IntegerField(
        label="3.3.5. Ogik idwe mene?", # end month
        choices=C.MONTH,
        blank=False
    )
    noncombatant_geography_second_b = models.IntegerField(
        label="3.3.6. Ikine me mwaka ma kinwyali kwede ki 2025, tika ibedo kabedo  kamukene mapat?",
        # During that period, did you also live in another province?
        choices= C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    noncombatant_geography_second = models.IntegerField(
        label="3.3.7. Kace otime, kabedo mene mukene ma ikwo iye bene? (Yer kama pole kare ibedo iye , mapat ki kabedo ma lakwongi)",
        # If yes, in which province did you also reside?
        choices= C.SUBREGION_UGANDA,
        blank=True
    )
    noncombatant_geography_second_other = models.StringField(
        label="3.3.7.1. If other, please specify:",
        blank=True
    )
    noncombatant_geography_second_start_year = models.IntegerField(
        label="3.3.8. I mwaka mene ma icako bedo i kabedo meno? (If respondent prefers not to say, enter '9999')",
        # In which period did you reside in this province? Buddhist era start year:
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    noncombatant_geography_second_start_month = models.IntegerField(
        label="3.3.9. Ocake idwe mene?",
        choices=C.MONTH,
        blank=True
    )
    noncombatant_geography_second_end_year = models.IntegerField(
        label="3.3.10. Me oo imwaka mene? (If respondent prefers not to say, enter '9999')",
        # until what year?
        choices=[
            [999, "Prefer not to say"],
            [998, "Don't know"],
            *[[y, str(y)] for y in range(1950, 2025)]
        ],
        blank=True
    )
    noncombatant_geography_second_end_month = models.IntegerField(
        label="3.3.11. Ogik idwe mene?",
        choices=C.MONTH,
        blank=True
    )
    # QUESTIONS EXPOSURE TO VIOLENCE
    etv_bi_1 = models.IntegerField(
        label="3.4. Manaka tika dul pa mony calo LRA, UPDF onyo dul pa lulweny mukene gu omwonyi?",
        # … were you ever ambushed by combatants of the conflict or forced to hide during the confrontation?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_1 = models.IntegerField(
        label="3.5. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_2 = models.IntegerField(
        label="3.6. Manaka tika dul pa mony calo LRA, UPDF onyo lulweny mukene gu buru kwo ni?",
        # … were you ever threatened by combatants of the conflict?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_2 = models.IntegerField(
        label="3.7. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_3 = models.IntegerField(
        label="3.8. Tye nino mo keken manaka ma ibedo peke ki cam onyo kabedo?",
        # … were you left without food or shelter?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_3 = models.IntegerField(
        label="3.9. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_5_1 = models.IntegerField(
        label="3.10. Manaka tika inongo aun, gojo onyo ret me kom ki bot dul pa lulweny calo LRA, UPDF ki lulweny mukene?",
        # … were you ever physically injured, subject to beating(s) to the body, or tortured by combatants of the conflict?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_5_1 = models.IntegerField(
        label="3.11. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_5_2 = models.IntegerField(
        label="3.12. Manaka tika inongo aun, gojo onyo ret me kom ki bot Komanda pa LRA, onyo la memba pa LRA mukene?",
        # … were you ever physically injured, subject to beating(s) to the body, or tortured by your superiors or other abudctees (LRA)?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_5_2 = models.IntegerField(
        label="3.13. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_6 = models.IntegerField(
        label="3.14. Manaka tika ineno onyo ikato ki te kare me mwoc pa bom?",
        # …have you ever witnessed or experienced a bombing?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_6 = models.IntegerField(
        label="3.15. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_7 = models.IntegerField(
        label="3.16. Manak tika ineno jemo?",
        # … have you ever witnessed or experienced a riot?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_7 = models.IntegerField(
        label="3.17. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_8 = models.IntegerField(
        label="3.18. Manaka tika ineno nek atyee ikin dano onyo cel atyee",
        # … have you ever witnessed or experienced a shooting?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_8 = models.IntegerField(
        label="3.19. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_9 = models.IntegerField(
        label="3.20. Manaka tika ineno lweny ma kityo ki dege?",
        # … have you ever witnessed or experienced an aerial strike?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_9 = models.IntegerField(
        label="3.21. Kace ada, tyen adi?",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_10 = models.IntegerField(
        label="3.22. Manaka tika iringo mony I kam?",
        # … have you ever been internally displaced?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )


# FUNCTIONS
def assign_treatments(p, csv_file):
    participant = p.participant

    # Read all data from CSV
    all_data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            all_data.append(row)

    # Filter by group_participant and etv
    group_player = [
        row for row in all_data
        if int(row['group_participant']) == participant.group
           and int(row['etv']) == participant.etv
    ]

    # Find minimum nb_participant value
    if group_player:
        min_value = min(int(row['nb_participant']) for row in group_player)

        # Filter rows with minimum value
        min_rows = [
            row for row in group_player
            if int(row['nb_participant']) == min_value
        ]

        # Select row (random if multiple, otherwise take the first)
        if len(min_rows) > 1:
            selected_row = random.choice(min_rows)
        else:
            selected_row = min_rows[0]

        # Assign treatments
        participant.treatment_hope = int(selected_row['treatment_hope'])
        participant.side_ultimatum = int(selected_row['side_UG'])
        participant.treatment_other = int(selected_row['treatment_other'])
    else:
        # Handle case where no matching rows found
        # You may want to set defaults or raise an error
        pass



# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'military_binary'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.military_binary = player.military_binary
        if participant.military_binary !=1:
            participant.etv=0
            assign_treatments(player, C.DATA_TREATMENT_LOC)
            print(participant.etv)
            print(participant.treatment_other)
        else:
            pass
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_LUO_w1"


class Page2_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary == 1 and player.session.config['name'] == "session_C4P_LUO_w1":
            return [
                'lra_conscription',
                'lra_length',
                'lra_length_unit',
                'military_province_main',
                'military_province_main_other',
                'maindeployment_start_year',
                'maindeployment_start_month',
                'maindeployment_length',
                'maindeployment_length_unit',
                'deployment_second',
                'military_province_second',
                'military_province_second_other',
                'seconddeployment_start_year',
                'seconddeployment_start_month',
                'seconddeployment_length',
                'seconddeployment_length_unit'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary == 1 and player.session.config['name'] == "session_C4P_LUO_w1"
    def error_message(player, values):
        if values['military_province_main'] == 11:
            if not values.get('military_province_main_other') or str(values['military_province_main_other']).strip() == '':
                return 'Please fill 3.2.3.1.'
        if values['deployment_second'] == 1:
            if values.get('military_province_second') is None:
                return 'Please fill 3.2.8.'
            if values['military_province_second'] == 11 and (
                    not values.get('military_province_second_other') or str(
                    values['military_province_second_other']).strip() == ''):
                return 'Please fill 3.2.8.1.'
            if values.get('seconddeployment_start_year') is None:
                return 'Please fill 3.2.9.'
            if values.get('seconddeployment_start_month') is None:
                return 'Please fill 3.2.10.'
            if values.get('seconddeployment_length') is None:
                return 'Please fill 3.2.11.'
            if values.get('seconddeployment_length_unit') is None:
                return 'Please fill unit of 3.2.11.'
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if participant.military_binary==1 & player.lra_conscription==1 :
            participant.etv = 1
        else:
            participant.etv = 0
        assign_treatments(player, C.DATA_TREATMENT_LOC)
        print(participant.etv)
        print(participant.treatment_other)


class Page2_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary != 1 and player.session.config['name'] == "session_C4P_LUO_w1":
            return [
                'noncombatant_geography_main',
                'noncombatant_geography_main_other',
                'noncombatant_geography_main_start_year',
                'noncombatant_geography_main_start_month',
                'noncombatant_geography_main_end_year',
                'noncombatant_geography_main_end_month',
                'noncombatant_geography_second_b',
                'noncombatant_geography_second',
                'noncombatant_geography_second_other',
                'noncombatant_geography_second_start_year',
                'noncombatant_geography_second_start_month',
                'noncombatant_geography_second_end_year',
                'noncombatant_geography_second_end_month'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary != 1 and player.session.config['name'] == "session_C4P_LUO_w1"
    def error_message(player, values):
        if values['noncombatant_geography_main'] == 11:
            if not values.get('noncombatant_geography_main_other') or str(values['noncombatant_geography_main_other']).strip() == '':
                return 'Please fill 3.3.3.1.'
        if values['noncombatant_geography_second_b'] == 1:
            if values.get('noncombatant_geography_second') is None:
                return 'Please fill 3.3.7.'
            if values['noncombatant_geography_second']==11 and (
                    not values.get('noncombatant_geography_second_other') or str(
                    values['noncombatant_geography_second_other']).strip() == ''):
                return 'Please fill 3.3.7.1.'
            if values.get('noncombatant_geography_second_start_year') is None:
                return 'Please fill 3.3.8.'
            if values.get('noncombatant_geography_second_start_month') is None:
                return 'Please fill 3.3.9.'
            if values.get('noncombatant_geography_second_end_year') is None:
                return 'Please fill 3.3.10.'
            if values.get('noncombatant_geography_second_end_month') is None:
                return 'Please fill unit of 3.3.11.'

class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary == 1 and player.session.config['name'] == "session_C4P_LUO_w1":
            return [
                'military_socialization_1',
                'military_socialization_2',
                'military_socialization_3'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary == 1 and player.session.config['name'] == "session_C4P_LUO_w1"


class Page4(Page):
    # Different text on webpage displayed depending on age and military service status
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        participant = player.participant
        if participant.etv == 1:
            return [
                'etv_bi_1',
                'etv_sc_1',
                'etv_bi_2',
                'etv_sc_2',
                'etv_bi_3',
                'etv_sc_3',
                'etv_bi_5_1',
                'etv_sc_5_1',
                'etv_bi_5_2',
                'etv_sc_5_2',
                'etv_bi_6',
                'etv_sc_6',
                'etv_bi_7',
                'etv_sc_7',
                'etv_bi_8',
                'etv_sc_8',
                'etv_bi_9',
                'etv_sc_9',
                'etv_bi_10'
    ]
        else:
            return [
                'etv_bi_1',
                'etv_sc_1',
                'etv_bi_2',
                'etv_sc_2',
                'etv_bi_3',
                'etv_sc_3',
                'etv_bi_5_1',
                'etv_sc_5_1',
                'etv_bi_6',
                'etv_sc_6',
                'etv_bi_7',
                'etv_sc_7',
                'etv_bi_8',
                'etv_sc_8',
                'etv_bi_9',
                'etv_sc_9',
                'etv_bi_10'
    ]
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_LUO_w1"
    def error_message(player, values):
        pairs = [
            ('etv_bi_1', 'etv_sc_1'),
            ('etv_bi_2', 'etv_sc_2'),
            ('etv_bi_3', 'etv_sc_3'),
            ('etv_bi_5_1', 'etv_sc_5_1'),
            ('etv_bi_5_2', 'etv_sc_5_2'),
            ('etv_bi_6', 'etv_sc_6'),
            ('etv_bi_7', 'etv_sc_7'),
            ('etv_bi_8', 'etv_sc_8'),
            ('etv_bi_9', 'etv_sc_9')
        ]
        for bi_field, sc_field in pairs:
            if bi_field in values and values[bi_field] == 1:
                if sc_field not in values or values[sc_field] is None:
                    return f'Please fill in frequency question'

page_sequence = [
    Page1, # military service filter + treatment assignment
    Page2_1, # questions military service
    Page2_2, # question non-military service
    Page3, # military socialization
    Page4 # exposure to violence
]