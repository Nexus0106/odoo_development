# -*- coding: utf-8 -*-
{
    'name': 'Clinic System',
    'summary':'Clinic System',
    'description': 'Clinic System',
    'author':'Test User',
    'category':'Customization',
    'version': '1.0',
    'depends': [
        'base',
        'hr',
        'product',
        'resource',
    ],
    'data': [
        'views/customer_booking_view.xml',
        'security/ir.model.access.csv',
    ],
    'license':'LGPL-3',
    'installable':True,
    'auto_install':False,
    'application':False,
}