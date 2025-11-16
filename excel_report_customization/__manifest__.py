# -*- coding: utf-8 -*-
{
    'name': 'Excel Report Customization',
    'summary':'Excel Report Customization',
    'description': 'Excel Report Customization',
    'author':'Test User',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'base',
        'clinic_system',

    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/clinic_system_report.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}