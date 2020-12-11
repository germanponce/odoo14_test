# -*- coding: utf-8 -*-
{
    'name': "Sale Order Line Pagination",

    'summary': """
        add a option to filter number of order lines visible on page with pagitination""",

    'description': """
        Display as many row you want. Set a limit on number of rows to be displayed per page. Easy to use.
    """,

    'author': "Linescripts Softwares",
    'website': "http://www.linescripts.com",
    'license': 'LGPL-3',
    'support': "developers@linescripts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/user.png'],
}