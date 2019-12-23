# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Manufacturing_extension',
    'version': '12.0.1.0.0',
    'Author': 'SAM VISITH',
    'website':'',
    'category': 'Manufacturing',
    'sequence': 16,
    'summary': '',
    'depends': ['mrp'],
    'description': """This module provides the following features:
                    1. Not allow negative stock.
                    2. Allow to re-allocate stock reservation to more urgent MOs. 
               """,
    'data': [
        "views/mrp_production_view.xml",
        "views/asset.xml",
    ],
    'installable': True,
    'application': True,
}
