# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Task Followers',
    'version': '12.0.1.0.0',
    'Author': 'SAM VISITH',
    'website': '',
    'category': 'Project',
    'summary': 'Allow users to follow a particular task and get notified',
    'depends': ['project'],
    'description': """
This module provides the following features:
1. to show the followers who are the clients in the task page.
2. hide internal user in the follower list. 
""",
    'data': [
        'views/project_task_view.xml',
    ],
    'installable': True,
    'application': True,
}
