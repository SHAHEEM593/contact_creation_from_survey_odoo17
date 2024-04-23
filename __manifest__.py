# -*- coding: utf-8 -*-
{
    'name': "Contact Creation From Survey",
    'version': '17.0.1.0.0',
    'depends': ['base','survey','contacts'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
    Contact Creation From Survey
    """,
    'summary': 'Contact Creation From Survey',
    'data': [
        'security/ir.model.access.csv',
        'views/survey_survey_view.xml',
        'views/survey_user_input_view.xml',

    ],


    'application': True,
    'installable': True,

}
