# -*- coding: utf-8 -*-
{
    'name': 'Notice Dashboard',
    'summary':'Notice Dashboard Website',
    'description': 'Notice Dashboard Website',
    'author':'Test User',
    'category':'Website',
    'version': '1.0',
    'depends': [
        'website',
        'portal',

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/notice_dashboard_view.xml',
        'data/website_menu.xml',
        'views/website_portal_template.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}