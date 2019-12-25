# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Re-allocate Stock Reservation of Manufacturing Orders',
    'version': '12.0.1.0.0',
    'Author': 'SAM VISITH',
    'website': '',
    'category': 'Manufacturing',
    'summary': 'Allow to re-allocate stock reservation to more urgent MOs',
    'depends': ['mrp'],
    'description': """
This module provides the following features:
1. Not allow negative stock.
2. Allow to re-allocate stock reservation to more urgent MOs. 
""",
    'data': [
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': True,
}
