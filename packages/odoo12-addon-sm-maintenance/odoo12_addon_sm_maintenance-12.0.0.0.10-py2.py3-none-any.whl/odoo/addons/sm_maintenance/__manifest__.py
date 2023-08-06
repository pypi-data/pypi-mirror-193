# -*- coding: utf-8 -*-
{
    'name': "sm_maintenance",

    'summary': """
    Module containing a set of sm_maintenance tasks to be executed periodically
    and keep database entries and sm services healthy""",

    'description': """
    Module containing a set of sm_maintenance tasks to be executed periodically
    and keep database entries and sm services healthy
  """,

    'author': "Som Mobilitat",
    'website': "https://www.sommobilitat.coop",

    'category': 'Mobility',
    'version': '12.0.0.0.10',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sm_connect', 'base_iban'],  # 'account'

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_successful_action_message.xml',
        'views/views_res_config_settings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
