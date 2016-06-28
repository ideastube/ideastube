# -*- coding: utf-8 -*-
"""Ideaxbox for Welcome Point, Dusseldorf"""
from .idb import *  # noqa
from django.utils.translation import ugettext_lazy as _

IDEASCUBE_NAME = u"Welcome Point Dusseldorf"
IDEASCUBE_PLACE_NAME = _("city")
COUNTRIES_FIRST = ['DE']
TIME_ZONE = None
LANGUAGE_CODE = 'de'
LOAN_DURATION = 14
MONITORING_ENTRY_EXPORT_FIELDS = ['serial', 'user_id', 'birth_year', 'gender']
USER_FORM_FIELDS = (
    ('Ideasbox', ['serial', 'box_awareness']),
    (_('Personal informations'), ['short_name', 'full_name', 'birth_year', 'gender', 'id_card_number']),  # noqa
    (_('Family'), ['marital_status', 'family_status', 'children_under_12', 'children_under_18', 'children_above_18']),  # noqa
    (_('In the town'), ['current_occupation', 'school_level']),
    (_('Language skills'), ['en_level']),
)
HOME_CARDS = STAFF_HOME_CARDS + [
    {
        'id': 'blog',
    },
    {
        'id': 'library',
    },
    {
        'id': 'mediacenter',
    },
    {
        'id': 'khanacademy',
    },
    {
        'id': 'wikipedia',
        'languages': ['de', 'ar', 'fa', 'en']
    },
    {
        'id': 'w2eu',
    }
]
