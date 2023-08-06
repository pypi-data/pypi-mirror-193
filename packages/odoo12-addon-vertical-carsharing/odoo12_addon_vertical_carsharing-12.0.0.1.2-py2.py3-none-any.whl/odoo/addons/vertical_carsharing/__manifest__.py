# -*- coding: utf-8 -*-
{
    'name': "vertical_carsharing",

    'summary': """
    Modules to masnage your carsharing enerprise using TMF reservation app""",

    'author': "Som Mobilitat",
    'website': "https://www.sommobilitat.coop",

    'category': 'vertical-carsharing',
    'version': '12.0.0.1.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base_vat',
        'base',
        'project'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'email_tmpl/notification_email.xml',
        'data/sm_account_journal.xml',
        'views/views.xml',
        'views/views_members.xml',
        'views/views_cs_task.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
