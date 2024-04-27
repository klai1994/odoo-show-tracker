# -*- coding: utf-8 -*-

{
    'name': 'Show Tracker',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Keep track of your favorite shows in Odoo!',
    'description': """
This app will help you keep track of and rate the shows you watch.
    """,
    'depends': [
        'base_setup', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/show_tracker_views.xml',
        'views/show_tracker_menuitems.xml',
    ],
    'demo': [
        'data/res_partner_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}