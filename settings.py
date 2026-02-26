from os import environ

#environ['DATABASE_URL']="postgres://otree_user:OT_spirit12@localhost/otree_second_db"

ROOMS = [
    dict(
        name="C4PTHP_LUG",
        display_name="C4PTHP_LUG",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_luganda_inc.txt", # change when final study to _inc
        use_secure_urls=False
    ),
    dict(
        name="C4PTHP_LUO",
        display_name="C4PTHP_LUO",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_luo_inc.txt",  # change when final study to _inc
        use_secure_urls=False
    ),
    dict(
        name="C4PTHP_ENG",
        display_name="C4PTHP_ENG",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_english.txt",  # change when final study to _inc
        use_secure_urls=False
    ),
    dict(
        name="pilot_UGA_HEAD",
        display_name="C4P_UGA_HEAD"
    )
]

SESSION_CONFIGS = [
    dict(
         name='session_C4P_LUGANDA_w1',
        app_sequence=[
            'app_1_lug', 'app_2_lug', 'app_3_lug', 'app_4_lug', 'app_5_lug', 'app_6_lug',
            'app_7_lug', 'app_8_lug', 'app_9_lug', 'app_10_lug', 'app_11_lug'
        ],
         num_demo_participants=6,
     ),
    dict(
         name='session_C4P_LUGANDA_w2',
        app_sequence=[
            'app_1_lug', 'app_2_lug', 'app_3_lug', 'app_4_lug', 'app_5_lug', 'app_6_lug',
            'app_7_lug', 'app_8_lug', 'app_9_lug', 'app_10_lug', 'app_11_lug'
        ],
         num_demo_participants=6,
     ),
    dict(
        name='session_C4P_ENGLISH_w1',
        app_sequence=[
            'app_1_eng', 'app_2_eng', 'app_3_eng', 'app_4_eng', 'app_5_eng', 'app_6_eng',
            'app_7_eng', 'app_8_eng', 'app_9_eng', 'app_10_eng', 'app_11_eng'
        ],
        num_demo_participants=6
    ),
    dict(
        name='session_C4P_ENGLISH_w2',
        app_sequence=[
            'app_1_eng', 'app_2_eng', 'app_3_eng', 'app_4_eng', 'app_5_eng', 'app_6_eng',
            'app_7_eng', 'app_8_eng', 'app_9_eng', 'app_10_eng', 'app_11_eng'
        ],
        num_demo_participants=6,
    ),
    dict(
        name='session_C4P_LUO_w1',
        app_sequence=[
            'app_1_luo', 'app_2_luo', 'app_3_luo', 'app_4_luo', 'app_5_luo', 'app_6_luo',
            'app_7_luo', 'app_8_luo', 'app_9_luo', 'app_10_luo', 'app_11_luo'
        ],
        num_demo_participants=6,
    ),
    dict(
        name='session_C4P_LUO_w2',
        app_sequence=[
            'app_1_luo', 'app_2_luo', 'app_3_luo', 'app_4_luo', 'app_5_luo', 'app_6_luo',
            'app_7_luo', 'app_8_luo', 'app_9_luo', 'app_10_luo', 'app_11_luo'
        ],
        num_demo_participants=6,
    ),
    dict(
        name='session_C4P_UGA_headenumerator',
        app_sequence=[
            'app_12'
        ],
        num_demo_participants=1,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'dropout', 'participation_fee',
    'group', 'age', 'military_binary', 'etv', 'treatment_hope', 'side_ultimatum', 'treatment_other',
    'decision_UG', 'decision_PG',
    'other_UG_decision', 'other_PG_decision',
    'payoff_UG', 'payoff_PG',
    'total_payoff_token', 'payoff_games', 'total_compensation',
    'recontact'
]

SESSION_FIELDS = []

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'BHT'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = '9805055233605'
